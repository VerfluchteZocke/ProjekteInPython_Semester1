'''
Created on 04.04.2023

@author: VerfluchteZocke

TASK:
Develop a program in Python in which you ask the user to enter his name, gender, degree program and matriculation number. Then output this data formatted.

a. As far as possible, check the user input for plausibility.

b. Extend the program to allow repeated input of the data and its output.
'''
#Variables to check for correct data type
correctDataTypeSex = False
correctDataTypeStudiefield = False
correctDataTypeMatriculationNumber = False


#Get valid user input for sex, studyfield and matriculationnumber (check for correct data type,
#if it is not the correct data type, ask for input again
while(correctDataTypeSex == False):
    sex = input("Enter your sex:")
    if not sex.strip().isdigit():
        correctDataTypeSex = True
    else:
        print("You entered the wrong data type.")
        
while(correctDataTypeStudiefield == False):
    studyfield = input("Enter your study field:")
    if not studyfield.strip().isdigit():
        correctDataTypeStudiefield = True
    else:
        print("You entered the wrong data type.")
             
while(correctDataTypeMatriculationNumber == False):
    matriculationNumber = input("Enter your matriculation number:")
    if matriculationNumber.strip().isdigit() and len(matriculationNumber)>=5:
        correctDataTypeMatriculationNumber = True
    else:
        print("You entered the wrong data type. You need to enter a number which contains at least 5 digits.")

print("Your sex is: " + sex)
print("Your studyfield is: " + studyfield)
print("Your matriculation number is: " + matriculationNumber)