import requests
import os
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

# -------------------------
# STEP 1: Scrape headlines
# -------------------------

url = "https://www.thehindu.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headings = soup.find_all("h3")

news = ""

i = 0
for h in headings[:20]:
    i += 1
    news += f"{i}. {h.get_text(strip=True)}\n\n"

print(news)

# -------------------------
# STEP 2: Email settings
# -------------------------

sender_email = os.environ["SENDER_EMAIL"]
receiver_email = os.environ["RECEIVER_EMAIL"]
password = os.environ["EMAIL_PASSWORD"]

# Create email
msg = MIMEText(news)

msg["Subject"] = "Today's Hindu Headlines"
msg["From"] = sender_email
msg["To"] = receiver_email

# -------------------------
# STEP 3: Send email
# -------------------------

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(sender_email, password)

server.send_message(msg)

server.quit()

print("Email sent successfully!")