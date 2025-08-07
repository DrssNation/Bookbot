from stats import number_of_words, number_of_characters,print_letter_count
import os
import sys

def get_book_text(file_path):
    # Use os functions to construct the path relative to the script's location
    try:
        with open(file_path) as file:
            file_content = file.read()
            return file_content  
    except Exception as e:
        print(f"Error dsfsffdf: {e}.")
        sys.exit(1)

def main():
    # Build the file path relative to the script's location
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1] 

    try:
        book_content = get_book_text(file_path)
        word_count = number_of_words(book_content)
        letter_count = number_of_characters(book_content)
        print_letter_count(letter_count, file_path, word_count)
    except Exception as e:
        print(f"Error: {e}.")
        sys.exit(1)

main()