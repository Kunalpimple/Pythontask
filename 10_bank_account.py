# empty account space
account = {
    "username": "kunal",
    "pin": "1234",
    "balance": 0.0
}

# Function to log in
def login():
    print("🔐 Login to your account")
    entered_username = input("Username: ")
    entered_pin = input("PIN: ")

    if entered_username == account["username"] and entered_pin == account["pin"]:
        print("✅ Login successful!")
        return True
    else:
        print("❌ Invalid username or PIN.")
        return False

# Function to check balance
def check_balance():
    print(f"💰 Your current balance is: ₹{account['balance']:.2f}")

# Function to deposit money
def deposit():
    amount = float(input("Enter amount to deposit: ₹"))
    if amount > 0:
        account["balance"] += amount
        print(f"✅ ₹{amount:.2f} deposited successfully.")
    else:
        print("❌ Invalid amount.")

# Function to withdraw money
def withdraw():
    amount = float(input("Enter amount to withdraw: ₹"))
    if 0 < amount <= account["balance"]:
        account["balance"] -= amount
        print(f"✅ ₹{amount:.2f} withdrawn successfully.")
    else:
        print("❌ Invalid amount or insufficient balance.")

# Main Program
if login():
    while True:
        print("\n🏦 Bank Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("👋 Thank you for banking with us!")
            break
        else:
            print("⚠️ Invalid option. Please choose between 1 and 4.")
