#!/usr/bin/env python3
import smtplib
from email.message import EmailMessage
import getpass
import time


RED = "\033[1;31m"
GREEN = "\033[1;32m"
RESET = "\033[0m"


skull_lines = [
    r"         _.--''''''''--._         ",
    r"       .'                '.       ",
    r"      /                    \      ",
    r"     |                      |     ",
    r"     |   ___          ___   |     ",
    r"     |  /   \        /   \  |     ",
    f"     | |  {GREEN}O{RED}  |      |  {GREEN}O{RED}  | |     ", 
    r"      \ \___/        \___/ /      ",
    r"       \                  /       ",
    r"        \      .---.     /        ",
    r"         \     \___/    /         ",
    r"          \            /          ",
    r"           |==========|           ",
    r"           | || || || |           ",
    r"            `--------`            "
]


print(f"\n{RED}", end="")
for i, line in enumerate(skull_lines):
   
    if i == 1:
        print(f"{line}   {RESET}Gmail Fliker By Zawar Baig.{RED}")
    else:
        print(line)


print(f"\n{GREEN}--- Python Email & SMS Automation Tool ---")

sender_email = input("Enter your Gmail address: ")
app_password = getpass.getpass("Enter your 16-character App Password (hidden): ")
recipient = input("Enter the recipient email : ")
subject = input("Enter the message subject: ")
body = input("Enter the message text: ")

while True:
    try:
        count = int(input("How many times do you want to send this message? "))
        if count > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")


print(RESET, end="")


msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient


try:
    print("\nConnecting to Gmail server...")
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls() 
        server.login(sender_email, app_password)
        print(f"{GREEN}Login successful! Starting delivery...\n{RESET}")
        
        for i in range(count):
            server.send_message(msg)
        
            print(f"{GREEN}[{i + 1}/{count}] Message delivered successfully!{RESET}")
            
            if count > 1 and i < count - 1:
                time.sleep(1)
                
    print(f"\n{GREEN}Task Complete! All messages sent.{RESET}")

except smtplib.SMTPAuthenticationError:
    
    print(f"\n{RED}[!] Error: Login failed. Please check your App Password and try again.{RESET}")
except Exception as e:
    
    print(f"\n{RED}[!] An error occurred: {e}{RESET}")