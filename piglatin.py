import string
import os
def pig_latin_word(word):
    vowels = 'aeiou'
    prefix_punct = ''
    suffix_punct = ''
    while word and word[0] in string.punctuation:
        prefix_punct += word[0]
        word = word[1:]
    while word and word[-1] in string.punctuation:
        suffix_punct = word[-1] + suffix_punct
        word = word[:-1]
    if not word:
        return prefix_punct + suffix_punct
    is_cap = word[0].isupper()
    word = word.lower()
    if word[0] in vowels:
        pig_word = word + "way"
    else:
        pig_word = word[1:] + word[0] + "ay"
    if is_cap:
        pig_word = pig_word.capitalize()
    return prefix_punct + pig_word + suffix_punct
def pig_latin_sentence(sentence):
    words = sentence.split()
    translated_words = [pig_latin_word(word) for word in words]
    return " ".join(translated_words)
print("1. Enter the text manually")
print("2. Enter the file name")
ch = int(input("Enter your choice: "))
match ch:
    case 1:
        text = input("Enter a sentence to translate to Pig Latin: ")
        output = pig_latin_sentence(text)
    case 2:
        file_name = input("Enter the file name: ")
        if os.path.exists(file_name):
            print("File exists")
            with open(file_name, "+r") as fil1:
                text = fil1.read()
                output = pig_latin_sentence(text)
        else:
            print("File does not exist.")
            output = ""
    case _:
        print("Invalid choice.")
        output = ""
if output:
    print("\nPig Latin Output:\n" + output)
