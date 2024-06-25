import sys

# Function to take user input and process it
# Function to take user input and process it
def process_input():
    # Read the number of words
    try:
        num_words = int(input("Enter the number of words: "))
        if num_words <= 0:
            raise ValueError("Number of words must be a positive integer.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)
    
    # Initialize arrays to store words and their frequencies
    wordarray = []
    frequencyarray = []

    # Take words as input from the user
    print("Enter the words:")
    for _ in range(num_words):
        # word = input().strip()
        # wordarray.append(word)
        while True:
            word = input()
            if word:  # Check if word is not empty
                wordarray.append(word)
                break
            else:
                print("Invalid input: Word cannot be empty. Please enter a valid word.")


    # Calculate frequency of each word
    for i in range(len(wordarray)):
        count = 1
        for j in range(i + 1, len(wordarray)):
            word1 = wordarray[i]
            word2 = wordarray[j]
            if word1 == word2:
                count += 1
                # Mark duplicate word as 'null'
                wordarray[j] = 'null'
        if wordarray[i] != 'null':
            frequencyarray.append(count)

    # Print the number of unique words and their frequencies
    print(len(frequencyarray))
    for i in frequencyarray:
        print(i, " ")

if __name__ == "__main__":
    process_input()
