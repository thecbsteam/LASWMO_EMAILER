import smtplib

try:
    # Test with TLS (Port 587)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Upgrade connection to secure
    server.quit()
    print("Connection on port 587 successful!")
except Exception as e:
    print(f"Port 587 failed: {e}")

try:
    # Test with SSL (Port 465)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.quit()
    print("Connection on port 465 successful!")
except Exception as e:
    print(f"Port 465 failed: {e}")
