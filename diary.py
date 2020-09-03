question = ("how", "why", "what", "could", "should", "can")
text = []
while True:
     phrase = input("Say something: ").lower()
     if phrase == "\end":
          break
     if phrase.startswith(question):
          phrase += "?"
     else:
          phrase += "."
     text.append(phrase.capitalize())

print(" ".join(text))