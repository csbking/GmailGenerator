import os

real_pass = os.getenv("GM_PASS")  # সিস্টেম থেকে পাস নেবে
user_pass = input("Enter password: ")

if user_pass != real_pass:
    exit()

print("Access Granted")
