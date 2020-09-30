#Name: Shi Tao Luo
#Email: shitao.luo40@myhunter.cuny.edu
#Date: September 3, 2019
#This program makes a codedword with the message you enter



word = input("Enter a word: ")
codedword = ""
for ch in word:
    offset = ord(ch) - ord('a') + 13
    wrap = offset % 26
    newChar = chr(ord('a') + wrap)
    codedword = codedword + newChar

print("The coded word is", codedword)
