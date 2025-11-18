#Ashley Maxam       11/28/2024      A7-Strings(part 2)
#This program prompts user to enter a sentence then converts that
#sentence from English to Pig Latin.

import string

def main():

    #Prompt user to enter a sentence and convert to lower case so there
    #is not a capital letter in the middle of a word.
    englishSentence = input("Enter a sentence: ").lower()

    # Remove punctuation from the sentence
    englishSentence = ''.join(char for char in englishSentence if char not in string.punctuation)

    #Convert sentence string to list of words.
    englishWords = englishSentence.split()

    #Create empty list to store Pig Latin words.
    pLatinWords = []

    #List of vowels.
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    #Outer loop iterates through list of words.
    for word in englishWords:
        hasVowel = False
        #Inner loop iterates through letters in each word.
        for i in range(len(word)):
            #If firt letter of word is vowel append 'yay' at the end of
            #the word (that's how I learned it as a kid), add to list of 
            #Pig Latin words and break inner loop.
            if word[0] in vowels:
                pLatinWords.append(word + 'yay')
                break
            else:
                #Moves consonants before the first vowel to the end and
                #add 'ay', add to list of Pig Latin words and break inner loop.
                if word[i] in vowels:
                    pLatinWords.append(word[i:] + word[:i] + 'ay')
                    hasVowel = True
                    break
                
                #If word has no vowels just add 'ay' to the end of the
                #word, add to list of Pig Latin words and break inner loop.
                if(hasVowel == False and i == len(word)-1):
                    pLatinWords.append(word + 'ay')
                    break

    #Join list of Pig Latin words to make sentence.
    pLatinSentence = ' '.join(pLatinWords)

    #Print the Pig Latin sentence.
    print(f'Your sentence in Pig Latin is: {pLatinSentence}')
    
main()