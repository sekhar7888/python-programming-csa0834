def reverse_word(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word

word = input("Enter a word: ")
print("Reversed word:", reverse_word(word))
