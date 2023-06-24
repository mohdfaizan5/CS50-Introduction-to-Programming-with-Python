#program that convert names to emojis
import pdb
def convert():
    face = input("") #.lower() #.split()
    face2 = face.replace(":)", "🙂").replace(":(", "🙁")
    print(face2)
convert()

"""
replace function definition:
<string_variable>.replace("<source substring>", "<target substring>")
source substring: any substring we would like to replace in the given string variable 
target substring: any substring we would like to replace with in the given string variable
e.g.:
  inp = "Hello :)"
  inp.replace(":)", "🙂")
  'Hello 🙂'
"""