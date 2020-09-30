#Name: Shi Tao Luo
#Email: shitao.luo40@myhunter.cuny.edu
#Date: September 3, 2019
#This program: let you enter a DNA string and the program return its length
#and its GC-content



DNAstring = input("Enter a DNA squence: ")
length = len(DNAstring)
print ("The length is", length)

numC = DNAstring.count('C')
numG = DNAstring.count('G')
numA = DNAstring.count('A')
numT = DNAstring.count('T')

gc = (numC + numG) / (numC + numG + numA + numT)
gcPercent = gc / 1
print(' GC-content is', gcPercent) 
