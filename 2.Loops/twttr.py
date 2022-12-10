#Program that ommits(removes) vowels (A,E,I,O,U) when inputed as upper or lower case.
#Commit check

#Step1: taking input from user as "Input: "
s = input("Input: ")

#Performing actions such as removing the vovels
vowels = ["a", "e", "i","o","u","A","E","I","O","U"]
for vowel in vowels:
    s = s.replace(vowel, "")

#outputting the user with removed vowels as "Output: "
    
print(s,end="")