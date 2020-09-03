question = ("how", "why", "what", "could", "should", "can")
text = ""
while True:
     phrase = input("Say something: ").lower()
     if phrase == "\\end":
          print(text)
          break
     if phrase.startswith(question):
          phrase += "?"
     else:
          phrase += "."
     text += f" {phrase.capitalize()}"