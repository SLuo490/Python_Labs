#Name: Shi Tao Luo
#Email: Shitao.luo40@myhunter.cuny.edu
#Date: Oct. 23, 2019
#A program that print out the string of the integer
#Modified by: Shi Tao Luo

def num2string(num):
     """
     Takes as input a number, num, and
     returns the corresponding name as a string.
     Examples: num2string(0) returns "zero", num2string(1)returns "one"
     Assumes that input is an integer ranging from 0 to 9
     """
     
     numString = ""
     if num == 1:
         return str("one")
     if num == 2:
         return str("two")
     if num == 3:
         return str("three")
     if num == 4:
         return str("four")
     if num == 5:
         return str("five")
     if num == 6:
         return str("six")
     if num == 7:
         return str("seven")
     if num == 8:
         return str("eight")
     if num == 9:
         return str("nine")
     if num == 0:
         return str("zero")
     
            
     return(numString)



def main():
     nums = input('Enter a multi-digit number: ')
     newStr = ""
     for n in nums:
         word = num2string(int(n))
         newStr = newStr + " " + word
     msg = 'In words, your number is:' + newStr + "."
     print(msg)   


#Allow script to be run directly:
if __name__ == "__main__":
     main()
