start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
# Loop through from start to end (inclusive)
for num in range(start, end + 1):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
