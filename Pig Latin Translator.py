__author__ = 'Josh Bierwiler'

print("Welcome to the Pig Latin Translator!")

pyg = "ay"                                                ## Adds 'ay' to the end of the word

original = input("Enter a word: ")                        ## Original prompt

if len(original) > 0 and original.isalpha():              ## Checks to ensure there are letters present and no numbers.
    print(original)                                       ## Prints the original word.
    word = original.lower()                               ## Converts to lower.
    first = word[0]                                       ## Grabs the first letter of the word.
    new_word = original + first + pyg                     ## Combines into the newly translated word
    new_word = new_word[1:len(new_word)]                  ## Cuts off the first letter from the word.
    print("This is the translated word: %s " % new_word)  ## Prints the newly translated word.
else:
    print("Empty")

