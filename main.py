def main():
    # This part opens the Frankenstein book and stores them in the variable file_contents
    file = "books/Frankenstein.txt"
    with open("books/Frankenstein.txt") as f:
        file_contents = f.read()
    
    # This function splits the words based on whitespace, then counts the lenght (numer of words)
    number_of_words = len(file_contents.split())

    # This function counts the letters in the book, all lower case, and puts them in a dictionary
    letters_dict = {}
    letters = file_contents.lower()
    for char in letters:
        if char.isalpha():
            letters_dict[char] = letters_dict.get(char, 0) + 1

    
    print(f"--- Begin report of {file} ---")
    print(f"{number_of_words} words found in the document")
    print()
    
    letters_list =list(letters_dict.items())
    for char, amount in letters_list:
        print(f"The {char} character was found {amount} times")
    print("--- End report ---")    

    

if __name__ == '__main__':
    main()
