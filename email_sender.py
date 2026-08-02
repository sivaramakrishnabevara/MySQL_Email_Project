import smtplib
from email.message import EmailMessage
import os

# -----------------------------
# Email Configuration
# -----------------------------
sender_email = "sivaram54599@gmail.com"
receiver_email = "sivaramakrishnabevara@gmail.com"

# Gmail App Password (16 characters)
app_password = "bomppjfndravabjb"

# Excel file name
file_name = "Employee_Report.xlsx"

try:
    # Check if file exists
    if not os.path.exists(file_name):
        print(f"❌ {file_name} not found!")
        exit()

    # Create Email
    msg = EmailMessage()
    msg["Subject"] = "Employee Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        """Hello,

Please find the attached Employee Report.

Thank You.
"""
    )

    # Attach Excel file
    with open(file_name, "rb") as file:
        msg.add_attachment(
            file.read(),
            maintype="application",
            subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=file_name
        )

    # Send Email
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("✅ Email Sent Successfully!")

except Exception as e:
    print("❌ Error:", e)