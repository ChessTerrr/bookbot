def main():
    print("Welcome to my character counting program!")
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(word_count)
        character_count = count_characters(file_contents)
        print(character_count)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

main()