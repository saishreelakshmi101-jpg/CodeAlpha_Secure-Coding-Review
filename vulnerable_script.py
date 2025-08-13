import os

password = "1234"  # Hardcoded password (vulnerability)

def login():
    if password == "1234":
        print("Access granted")
    else:
        print("Access denied")

login()
