""""
User Login System
Gaven Huynh
This program will simulate a user login system using a dictionary to store
usernames and passwords.
It will validate the user's credentials and assign a security level as well
as limit password attempts to three.
Febuary 19, 2026
"""

users: dict[str, str] = {
    "ghuynh": "T0tally_5trong_P@ssword!",
    "gwalters": "S3curePass!",
    "admin": "password123!",
    "guest": "guest"

}

username: str = input("Please enter a username: ")

if username not in users:
    print("User not found. Exiting.")

else:
    attempts: int = 0
    max_attempts: int = 3

    while attempts < max_attempts:
        password: str = input("Please enter a password: ")

        if password == users[username]:
            security_level: str
            if username == "guest":
                security_level = "Guest Access"
            else:
                security_level = "Security Level 1"

                print(f"Welcome, {username}! You have {security_level}.")
                break