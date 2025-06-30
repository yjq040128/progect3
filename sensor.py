# Program: Plant Moisture Sensor with Email Notification
# Modified for new configuration: GPIO7, sender 2271427187@qq.com, receiver 13091133576@163.com
# Based on original code from Project 2 Report

import smtplib
from email.message import EmailMessage
from gpiozero import Button
from datetime import datetime
import schedule
import time

# ==== Email Configuration ====
FROM_EMAIL = "2271427187@qq.com"
FROM_PASSWORD = "hofolssvejywdjba"  # QQ Mail app password
TO_EMAIL = "13091133576@163.com"
SMTP_SERVER = "smtp.qq.com"
SMTP_PORT = 587

# ==== Moisture Sensor Configuration ====
# Using physical pin 7 (BCM GPIO4) and GND on physical pin 6
MOISTURE_PIN = 4  # BCM numbering (physical pin 7)
sensor = Button(MOISTURE_PIN, pull_up=True, bounce_time=0.2)

# ==== Water Status (updated in real-time) ====
# True = Dry (no water detected): watering needed
# False = Wet (water detected): no watering needed
water_needed = not sensor.is_pressed  # Initial status on startup

# Callback when water is detected (button pressed)
def on_water_detected():
    global water_needed
    water_needed = False
    # print("Water detected: Plant does NOT need watering.")

# Callback when no water is detected (button released)
def on_no_water():
    global water_needed
    water_needed = True
    # print("No water detected: Plant NEEDS watering.")

# Attach sensor callbacks
sensor.when_pressed = on_water_detected
sensor.when_released = on_no_water

# ==== Email Sending Function ====
def send_email():
    now = datetime.now()
    status = "Plant NEEDS watering" if water_needed else "Plant does NOT need watering"
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

    body = f"""Plant Status Report

Timestamp: {timestamp}
Current Condition: {status}
"""

    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = f"Plant Daily {status} - {now.strftime('%H:%M')}"
    
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    try:
        server.starttls()
        server.login(FROM_EMAIL, FROM_PASSWORD)
        server.send_message(msg)
        print(f"[{timestamp}] Email sent successfully: {status}")
    except Exception as e:
        print(f"[{timestamp}] Error during email send: {e}")
    finally:
        server.quit()

# ==== Schedule Email Times ====
send_times = ["07:00", "10:00", "14:04", "16:00"]
for t in send_times:
    schedule.every().day.at(t).do(send_email)
    print(f"Scheduled email at {t} every day.")

# ==== Main Loop ====
print("Plant Moisture Monitoring System is running...")
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
print("Program manually terminated.")
