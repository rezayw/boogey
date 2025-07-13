import asyncio
from aioquic.quic.configuration import QuicConfiguration
from aioquic.asyncio import connect
from aioquic.quic.events import HandshakeCompleted, ProtocolNegotiated
from aioquic.h3.connection import H3_ALPN, H3Connection
from aioquic.h3.events import HeadersReceived, DataReceived

class Http3Client:
    def __init__(self, domain):
        self.domain = domain
        self.port = 443
        self.path = "/"

    async def run(self):
        config = QuicConfiguration(is_client=True, alpn_protocols=H3_ALPN)
        async with connect(self.domain, self.port, configuration=config, server_name=self.domain) as connection:
            protocol = connection._quic
            stream_id = protocol.get_next_available_stream_id()
            h3_conn = H3Connection(protocol)

            h3_conn.send_headers(
                stream_id,
                [
                    (":method", "GET"),
                    (":scheme", "https"),
                    (":authority", self.domain),
                    (":path", self.path),
                ]
            )
            connection.send(protocol.datagram_send(h3_conn.data_to_send()))

            while True:
                event = await connection.wait_event()
                if isinstance(event, HandshakeCompleted):
                    print("[✓] HTTP/3 handshake completed.")
                elif isinstance(event, ProtocolNegotiated):
                    print(f"[+] ALPN protocol negotiated: {event.alpn_protocol}")
                elif isinstance(event, HeadersReceived):
                    print("[+] Response headers:", event.headers)
                elif isinstance(event, DataReceived):
                    print("[+] Response data:", event.data.decode())
                    break


def run_http3_probe(domain):
    print(f"[+] Running HTTP/3 QUIC probe on {domain}")
    try:
        client = Http3Client(domain)
        asyncio.run(client.run())
    except Exception as e:
        print(f"[!] HTTP/3 probe error: {e}")
