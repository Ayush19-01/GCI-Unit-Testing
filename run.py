# Made for the sole purpose of GCI 2019

import random
import numpy as np
import os
import time


os.system("clear")




def prRed(skk): return str("\033[91m{}\033[00m" .format(skk)) 
def prGreen(skk): return str("\033[92m{}\033[00m" .format(skk)) 
def prYellow(skk): return str("\033[93m{}\033[00m" .format(skk)) 
def prPurple(skk): return str("\033[95m{}\033[00m" .format(skk)) 
def prCyan(skk): return str("\033[96m{}\033[00m" .format(skk)) 

print(prRed("Welcome to Unit testing of matrices, in this test we will check if a matrix is a singular matrix or not.\nOutput should return True if it is a singular matrix, else False would be the output.\n"))


time.sleep(5)

def unit_test(matrix):
	time.sleep(1)
	if np.linalg.det(matrix) == 0:
		print(prCyan("\nTrue"))
	if not np.linalg.det(matrix) == 0:                                                 
		print(prRed("\nFalse"))
	time.sleep(2)	
	print(prPurple("\nMatrix used for Unit test :\n"))
	print(prPurple(str(np.matrix(matrix))))
	print()
	time.sleep(5)
	os.system("clear")                                             
	return None
	
def own_matrix():
	order = int(input(prYellow("\nEnter the order of your matrix : ")))
	m1 = []
	for i in range(1,order+1):
		tmpl = []
		for j in range(1,order+1):
			xtmp = int(input(prYellow("\nEnter the value to be inserted at the address {},{} of the matrix : ".format(i,j))))
			tmpl.append(xtmp)
		m1.append(tmpl)
	choice=input(prCyan("\n[Optional] Do you want to Unit test the inverse of the given matrix [y/N] : "))
	print(prCyan("\nOnly the inverse or the original matrix will be tested!"))
	if choice == "Y" or choice == "y":
		final = np.linalg.inv(m1)
	else:
		final = m1
	unit_test(final)


def dot_matrix():
	order = int(input(prYellow("\nEnter the order of the matrices : ")))
	m1 = []
	m2 = []
	for i in range(order):
		tmpl1 = []
		tmpl2 = []
		for j in range(order):
			tmpl1.append(random.randint(0,9))
			tmpl2.append(random.randint(0,9))
		m1.append(tmpl1)
		m2.append(tmpl2)
	final = np.dot(m1,m2)
	unit_test(final)
	
def inverse_matrix():
	order = int(input(prYellow("\nEnter the order of matrix : ")))
	m1 = []
	for i in range(order):
		tmpl = []
		for j in range(order):
			tmpl.append(random.randint(0,9))
		m1.append(tmpl)
	final = np.linalg.inv(m1)
	unit_test(final)


def form_matrix():   
    order = int(input(prYellow("\nEnter the order of the matrix : ")))
    m1 = []
    for i in range(order):
        tmpl = []
        for j in range(order):
            tmpl.append(random.randint(0,9))
        m1.append(tmpl)
    final=m1
    unit_test(final)




while True:
	print(prYellow("Choose from the following options to compute matrices and Unit Test them : \n"))
	print(prCyan("1. Unit Test the product of two randomly generated matrices\n\n2. Unit Test the inverse of a randomly generated matrix\n"))
	print(prCyan("3. Unit test a randomly generated matrix\n\n4. Unit test a matrix entered by the User\n\n5. Exit the program\n"))
	userchoice=int(input(prYellow("Enter your choice (For example : 1,2,3,4 or 5) :  ")))
	if userchoice == 1:
		dot_matrix()
	if userchoice == 2:
		inverse_matrix()
	if userchoice ==  3:
		form_matrix()
	if userchoice == 4:
		own_matrix()
	if userchoice == 5:
		print(prRed("\nExiting..."))
		break

    
    
    
