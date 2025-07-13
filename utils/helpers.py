import os
import datetime


def ensure_report_dir():
    os.makedirs("reports", exist_ok=True)

def write_report(domain, mode, content):
    ensure_report_dir()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/{domain}_{mode}_{timestamp}.log"
    with open(filename, "w") as f:
        f.write(content)
    return filename

def log_result(domain, mode, result):
    report = f"[REPORT] Domain: {domain}\nMode: {mode}\nTime: {datetime.datetime.now()}\nResult:\n{result}\n"
    return write_report(domain, mode, report)