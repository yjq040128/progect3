import smtplib
from email.message import EmailMessage

FROM_EMAIL = "2271427187@qq.com"
FROM_PASSWORD = "hofolssvejywdjba"
TO_EMAIL = "13091133576@163.com"

msg = EmailMessage()
msg.set_content("这是一封来自树莓派的测试邮件")
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = "GPIO4测试"

try:
    with smtplib.SMTP("smtp.qq.com", 587) as server:
        server.starttls()
        server.login(FROM_EMAIL, FROM_PASSWORD)
        server.send_message(msg)
    print("测试邮件发送成功！")
except Exception as e:
    print(f"发送失败: {e}")
