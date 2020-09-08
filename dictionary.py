import os, json

from difflib import get_close_matches as matches



if not os.path.exists("dictionary.json"):
     print("Dictionary not found")
else:   
     
     dictionary = json.load(open("dictionary.json"))
          
     def print_word(word):
          print(f"\n{word.title()}\n\n", "\n".join(dictionary[word]), "\n")
          
     while True:
          
          word = input("Type a word to see its definition: ").lower()
          
          if word == "\exit": break
          
          if word in dictionary:
               print_word(word)
               continue
          
          close_words = matches(word, dictionary.keys())
          
          if len(close_words) == 0:
               print(f"\"{word}\" couldn't be found, please try another one.")
               continue
          
          for close_word in close_words:
               response = input(f"Did you mean {close_word}? [Yes(n) / No (n) / Exit(\e)] ").lower()
               
               if response == "\e": break
               
               if response == "y" or response == "yes":
                    print_word(close_word)
                    break
               if close_word == close_words[-1]:
                    print(f"\"{word}\" couldn't be found, please try another one.")
          
     print("Thank you! <3")


