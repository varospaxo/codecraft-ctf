#This is an AI generated script. It is for demonstration purposes only. Your solution might use different approach.

import itertools
import zipfile

# Function to generate all combinations of words from the list
def generate_passwords(word_list, combination_length):
    """
    Generate all possible combinations of words of a given length from the word list.
    
    :param word_list: List of words to combine
    :param combination_length: Number of words in each combination
    :return: List of password combinations
    """
    print("".join(combination) for combination in itertools.permutations(word_list, combination_length))
    return ["".join(combination) for combination in itertools.permutations(word_list, combination_length)]

# Function to try passwords on a ZIP file
def crack_zip(zip_file_path, passwords):
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            for password in passwords:
                try:
                    zf.extractall(pwd=password.encode())
                    print(f"Password found: {password}")
                    return password
                except RuntimeError as e:
                    # Handle incorrect password errors
                    if "Bad password" in str(e):
                        continue
                    else:
                        print(f"Error: {e}")
                except Exception as e:
                    # Handle other exceptions like decompression errors
                    print(f"Unexpected error for password '{password}': {e}")
                    continue
        print("Password not found.")
        return None
    except FileNotFoundError:
        print("ZIP file not found.")
        return None

# User input for the word list and ZIP file
if __name__ == "__main__":
    # Example word list
    words = ["Stellar", "Quantum", "Photon", "Gravity", "Elemental", "Nebular", "Orbital", "Pulsar", "Dark", "Subspace"]
    
    # ZIP file path
    zip_path = "cosmic_breach.zip"  # Replace with your ZIP file path

    # Generate all combinations of words
    passwords_word_length=4
    print("Generating passwords...")
    passwords = generate_passwords(words,  passwords_word_length)
    
    # Attempt to crack the ZIP file
    print("Attempting to crack the ZIP file...")
    result = crack_zip(zip_path, passwords)

    if result:
        print(f"Success! The password is: {result}")
    else:
        print("Failed to find the password.")
