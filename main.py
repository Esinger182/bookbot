
def output_book(book_location):
    with open(book_location) as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents

def count_words(text_input):
    words = text_input.split()
    words_total = len(words)
    #print(words_total)
    return words_total


def count_letters(text_input):
    text_input_lower = text_input.lower()

    letters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for i in text_input_lower:
        if i in letters:
            letters[i] +=1
    return letters
    
def print_report(word_count,counted_letters):
    print(str(word_count) + " words found in the document\n")
    for i in counted_letters:
        print("The letter " + i + " was found " + str(counted_letters[i]) + " times")


def main():
    book_location = "books/frankenstein.txt"
    counted_words = count_words(output_book(book_location))
    counted_letters = count_letters(output_book(book_location))
    #print(letter_count)
    report = print_report(counted_words,counted_letters)

if __name__ == '__main__':
    main()
