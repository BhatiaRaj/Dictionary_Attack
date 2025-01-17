import itertools
import string

def generate_dictionary(keywords, min_length, max_length, include_numbers, include_special_chars):
    """
    Generate a dictionary of possible password combinations.

    Args:
        keywords (list): List of keywords related to the target.
        min_length (int): Minimum length of generated passwords.
        max_length (int): Maximum length of generated passwords.
        include_numbers (bool): Include numbers in the combinations.
        include_special_chars (bool): Include special characters in the combinations.

    Returns:
        generator: A generator that yields password combinations.
    """
    base_chars = set()

    # Add keywords to base characters
    for keyword in keywords:
        base_chars.update(keyword)

    # Add letters (case insensitive)
    base_chars.update(string.ascii_letters)

    # Optionally include numbers and special characters
    if include_numbers:
        base_chars.update(string.digits)
    if include_special_chars:
        base_chars.update(string.punctuation)

    base_chars = list(base_chars)

    # Generate combinations
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(base_chars, repeat=length):
            yield ''.join(combination)

def main():
    print("\nDictionary Attack Wordlist Generator")

    # Gather target-related information
    keywords = input("Enter keywords (comma-separated, e.g., name,birthdate,pet): ").split(',')
    min_length = int(input("Enter minimum password length: "))
    max_length = int(input("Enter maximum password length: "))
    include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    # Generate dictionary and save to file
    print("\nGenerating combinations, please wait...")
    output_file = "dictionary_attack_wordlist.txt"
    with open(output_file, "w") as file:
        for word in generate_dictionary(keywords, min_length, max_length, include_numbers, include_special_chars):
            file.write(word + "\n")

    print(f"Wordlist generated successfully! Saved to {output_file}")

if __name__ == "__main__":
    main()