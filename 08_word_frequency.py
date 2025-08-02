import re
# Ask the user to input a paragraph
text = input("Enter a paragraph:\n")

# Convert text to lowercase to ignore case sensitivity
text = text.lower()

# Remove punctuation using regex (only keep letters and spaces)
text = re.sub(r'[^\w\s]', '', text)

# Split the text into words
words = text.split()

# Create a dictionary to store word frequencies
word_count = {}

# Loop through each word and count its frequency
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the word frequency results
print("\n📊 Word Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")
