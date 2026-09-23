# Task 21 String Analyzer:- Create a function that counts vowels, consonants, digits, spaces and special characters in a sentence.

try:
    sen = input("Write Sentence:- ")

    if sen.strip() == "":
        print("Please Enter Some Text!!")

    else:
        def analyze(text):
            vowels = 0
            digits = 0
            spaces = 0
            spechar = 0
            uppercase = 0
            lowercase = 0

            for i in text:
                if i.isupper():
                    uppercase += 1
                elif i.islower():
                    lowercase += 1
                elif i.lower() in "aeiou":
                    vowels += 1
                elif i.isdigit():
                    digits += 1
                elif i.isspace():
                    spaces += 1
                else:
                    spechar +=1

            return vowels, digits, spaces, spechar, uppercase, lowercase

        vowels, digits, spaces, spechar, uppercase, lowercase = analyze(sen)

        print("Vowels:-", vowels)
        print("Digits:-", digits)
        print("Spaces:-", spaces)
        print("Special Characters:-", spechar)
        print("Uppercase:-", uppercase)
        print("Lowercase:-", lowercase)
    
except Exception as e:
    print("Error", e)