import argparse
import time
from tqdm import tqdm
from modules.https_storm import run_https_storm
from modules.browser_js_stress import run_browser_js_stress
from modules.tls_cookie_hold import run_tls_cookie_hold
from modules.http2_rst import run_http2_rst
from modules.cache_bypass_storm import run_cache_bypass_storm
from modules.origin_down_push import run_origin_down_push
from modules.http3_quic_probe import run_http3_probe
from colorama import init, Fore, Style

init(autoreset=True)

def display_menu():
    logo = [
        (Fore.RED,"                                                                                                  :  d  cKl"),
        (Fore.YELLOW,"                                                                                                     .       "),
        (Fore.YELLOW,"                                                                                            .....'.........."),
        (Fore.YELLOW,"                                                                                    .....   .''.  .,,   ....."),
        (Fore.RED,"                                                                               ...  .                    ...."),
        (Fore.RED,"                                                                          ... .                          ...."),
        (Fore.YELLOW,"                                                                     ... .                              ...."),
        (Fore.YELLOW,"                                                                 ...                                   ..."),
        (Fore.YELLOW,"                                                             ... .                                    '.."),
        (Fore.RED,"                                                         ...                                        ..."),
        (Fore.RED,"                  ........           .,,,.          .,;:.          ',,,.    .................    .,;,,,."),
        (Fore.WHITE,"                 XMKKKKKKKXNKk:  .dXNK00KXNOc   .xXNK00KXNOc   'xXNK000KN0o'MWKKKKKKKKKKNKKKXM; oMKKKKWM."),
        (Fore.CYAN,"                 KWccccccccclkW0OWOocccccccxXN:OWOlcccccclxXX:OWklcccccccoKMMKcccccccccc0xccc0WOWkcccOMx''."),
        (Fore.CYAN,"                 KWcccoNNXkccckMWdc:cOXXXxc:cKMWdcccOXXXdcccKMMd:cc0NXNxcccNMKccckNNNNNNWWxcccXM0cccOWd.."),
        (Fore.CYAN,"                 KWcccoXXXkcccKMKccckMl.XWlccoM0ccckMl.XNcccoMXcccxMXOWWXXXWMKcccxKKKKKWMOMkccl0cccOWo..."),
        (Fore.CYAN,"                 KWcccccccccckWMOccc0M;.kMocclMOccc0M;.OWccclM0cccOMMxdddddKMKcccccccccXM,kMkcccccOMd..."),
        (Fore.CYAN,"                 KWcccoNNNKcccoMKcc:kMo'XWl:cdMKccckMo'XNcccdMXcccxMM0Oxccc0MKccckNWWWNMM;.OMxcccOMd.."),
        (Fore.CYAN,"                 XWcccoXXX0c:clMMxccckXXKdcccKMMxcccOXXKo:ccXMMdcccONWNOc:c0MKcccxXXXXXXWW.xMOcccXM,.."),
        (Fore.CYAN,"                 XWcc:cccccclxXXOWOocccccccxXXcOWOocccccclxXXcOWOoccccccccdNMKccccccccccKW.cMOcccXM,."),
        (Fore.WHITE,"                 dK0KKKKKKXXXOo'.; xNKK0KXXOo'..  xNKK0KXXOo...  kXKK0KKXXOxMWKKKKKKKKKKWW.:MXKKKWM,."),
        (Fore.RED,"                    ,,,,,,,'...       ,:;,...        ,:;,...        ;:;,'...  ',,,,,,,,,,,... ,,,,,..."),
        (Fore.RED,"                      '..                                             ..."),
        (Fore.YELLOW,"                    ...                                            .."),
        (Fore.YELLOW,"                  ...                                          ..."),
        (Fore.YELLOW,"                ....                                        ..  ."),
        (Fore.RED,"               ...                                      ..  ."),
        (Fore.RED,"             ....  .                                ..   ."),
        (Fore.YELLOW,"            ....                               ...   ."),
        (Fore.YELLOW,"           ....   .. ,l'                   ..     ."),
        (Fore.YELLOW,"           ....                       ..     ."),
        (Fore.RED,"           ....'               ....     ."),
        (Fore.RED,"             ..............       ."),
        (Fore.YELLOW,"        .:.              '.")
    ]
    for color, line in logo:
        print(color + line)
        time.sleep(0.05)
    
    print(Fore.GREEN + Style.DIM + "\n<<<< WELLCOME TO BOOGEY >>>" + Style.RESET_ALL)
    print("\nBOOGEY Chance is easier than PAR\nbecause it allows for a mistake while PAR demands near-perfect execution.")
    print("\nChoose a Penetration mode:")
    print("1. HTTPS-STORM")
    print("2. BROWSER-JS-STRESS")
    print("3. TLS-COOKIE-HOLD")
    print("4. SPOOFED-HTTP2-RST")
    print("5. CACHE-BYPASS-STORM")
    print("6. ORIGIN-DOWN-PUSH")
    print("7. Run all tests")
    print("8. HTTP/3 QUIC Probe")
    print("0. Exit")

def get_duration():
    print("\nChoose wait time:")
    print("1. 3 minutes")
    print("2. 30 minutes")
    print("3. 1 hour")
    choice = input("Enter choice (1-3): ")
    if choice == '1':
        return 180
    elif choice == '2':
        return 1800
    elif choice == '3':
        return 3600
    else:
        print("Invalid choice. Defaulting to 3 minutes.")
        return 180

def simulate_processing(duration):
    print("\n[+] Processing test...")
    for _ in tqdm(range(duration), desc="Testing", unit="s"):
        time.sleep(1)

def generate_report(domain, mode):
    print(f"\n[+] Generating report for {domain} using {mode.upper()}...")
    time.sleep(1)
    print(f"[✓] Report complete: reports/{domain}_{mode}.log")

def main():
    while True:
        display_menu()
        choice = input("\nSelect test mode (0-8): ")

        if choice == '0':
            print("Exiting.")
            break

        domain = input("\nEnter domain (without http/https): ").strip().lower()
        duration = get_duration()

        if choice == '1':
            run_https_storm(domain)
            simulate_processing(duration)
            generate_report(domain, "https-storm")
        elif choice == '2':
            run_browser_js_stress(domain)
            simulate_processing(duration)
            generate_report(domain, "browser-js-stress")
        elif choice == '3':
            run_tls_cookie_hold(domain)
            simulate_processing(duration)
            generate_report(domain, "tls-cookie-hold")
        elif choice == '4':
            run_http2_rst(domain)
            simulate_processing(duration)
            generate_report(domain, "http2-rst")
        elif choice == '5':
            run_cache_bypass_storm(domain)
            simulate_processing(duration)
            generate_report(domain, "cache-bypass-storm")
        elif choice == '6':
            run_origin_down_push(domain)
            simulate_processing(duration)
            generate_report(domain, "origin-down-push")
        elif choice == '7':
            run_https_storm(domain)
            run_browser_js_stress(domain)
            run_tls_cookie_hold(domain)
            run_http2_rst(domain)
            run_cache_bypass_storm(domain)
            run_origin_down_push(domain)
            simulate_processing(duration)
            generate_report(domain, "all")
        elif choice == '8':
            run_http3_probe(domain)
            simulate_processing(duration)
            generate_report(domain, "http3-quic-probe")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
