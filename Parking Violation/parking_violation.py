#Name: Shi Tao Luo
#Date: Oct. 23, 2019
#Email: Shitao.luo40@myhunter.cuny.edu
#This program modify the program in Lab 7 which ask the user for the input file
#and its attribute.




import pandas as pd


csvFile = input("Enter a file name: ")  #Name of the CSV file

attribute = input("Enter attribute: ")

tickets = pd.read_csv(csvFile)		#Read in the file to a dataframe

print ("The 10 worst offenders are: ")
print(tickets [attribute].value_counts()[:10])     #Print out the dataframe
