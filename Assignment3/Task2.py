import bcrypt
import time
from nltk.corpus import words
import nltk


# Ensure the NLTK word corpus is available
nltk.download('words')

# Filter the word corpus to get words of length 6 to 10
word_list = [word for word in words.words() if 6 <= len(word) <= 10]


def crack_password(hash_line):
    # Parse the hash line to extract user and bcrypt hash
    user, hash_part = hash_line.split(":", 1)
    
    # Start timer
    start_time = time.time()
    
    # Attempt each word in the word list as the potential password
    for i, word in enumerate(word_list, start=1):
        # Convert word to bytes, as bcrypt expects byte input
        password_attempt = word.encode('utf-8')
        
        # Print heartbeat message every 100 attempts
        # if i % 10000 == 0:
            # print(f"Heartbeat: {i} attempts made for {user}...")

        # Check if the password attempt matches the bcrypt hash
        if bcrypt.checkpw(password_attempt, hash_part.encode('utf-8')):
            # Stop timer and calculate elapsed time
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Password for {user} found: '{word}' in {time_taken:.2f} seconds")
            return word, time_taken
    
    # If no password is found, return None
    print(f"Password for {user} not found.")
    return None, None


def main(): 
    hashes = []

    with open("shadow.txt", "r") as file:
        for line in file:
            hashes.append(line.strip())

    # Run the password cracking for each hash entry
    for hash_line in hashes:
        crack_password(hash_line)


if __name__ == '__main__':
    main() 
    
