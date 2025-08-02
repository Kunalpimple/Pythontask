import random
import string

# Ask user for length of password
length = int(input("Enter the length of the password: "))

# Define character pools
letters = string.ascii_letters    # a-z + A-Z
digits = string.digits            # 0-9
symbols = string.punctuation      # !@#$%^&* etc.

# Combine all in one list
all_chars = letters + digits + symbols

# Generate password using random.choice
password = ''.join(random.choice(all_chars) for _ in range(length))

# Show the password
print("🔐 Your generated password is:", password)
