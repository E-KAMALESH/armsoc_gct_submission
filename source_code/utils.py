import datetime
import calendar
import subprocess

def speak_and_print(text: str):
    print("ASSISTANT:", text)
    subprocess.run(["espeak-ng", "-v", "hi", text])

def get_time():
    now = datetime.datetime.now()
    return f"समय {now.hour} बजकर {now.minute} मिनट है"

def get_date():
    now = datetime.datetime.now()
    return now.strftime("आज %A, %d %B है")

def days_in_month():
    now = datetime.datetime.now()
    _, days = calendar.monthrange(now.year, now.month)
    return f"इस महीने में {days} दिन हैं"
