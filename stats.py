from collections import defaultdict

def number_of_words(text:str) -> int:
    # Count the number of words in the text
    return len(text.split())

def number_of_characters(text:str) -> dict:
    letter_count = defaultdict(int)

    for char in text:
        letter_count[char.lower()] += 1

    if not letter_count:
        return 0
    
    return letter_count

def print_letter_count(letter_count:dict,filename:str,total_words:int) -> None:
    # Print the letter count in a formatted way
    o_dict = dict(sorted(letter_count.items(),  key=lambda item: item[1],reverse=True))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{filename}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    for letter, count in o_dict.items():
        if letter.isalpha():
            print(f"{letter}: {count}")
    print("============= END ===============")

