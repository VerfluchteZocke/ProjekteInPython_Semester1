'''
Created on 29.03.2023

@author: VerfluchteZocke
'''
for tab_amount in range(4):
    #loop which creates with every iteration one tab more
    for i in range(tab_amount):
        print("\t", end='')
    print("Hello World")
    
    
#Option2
for tab_amount in range(4):
    #loop which creates with every iteration one tab more
    print("\t" * tab_amount, end='Hello World\n')


#Option3
for tab_amount in range(4):
    #loop which creates with every iteration one tab more
    print("\t" * tab_amount +'Hello World\n', end='')