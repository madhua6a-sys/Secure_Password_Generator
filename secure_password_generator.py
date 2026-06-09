import secrets
import string


def generate_secure_password(length=12):

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    password = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    password += [secrets.choice(all_chars) for _ in range(length - 3)]

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def check_strength(password):

    strength = "Weak"

    if len(password) >= 8:
        strength = "Medium"

    if (
        len(password) >= 12
        and any(char.isdigit() for char in password)
        and any(char in string.punctuation for char in password)
    ):
        strength = "Strong"

    return strength


password_length = int(input("Enter desired password length: "))

if password_length < 3:
    print("Password length must be at least 3.")
    exit()


password = generate_secure_password(password_length)

print("Generated secure password:", password)

strength = check_strength(password)

print("Password Strength:", strength)