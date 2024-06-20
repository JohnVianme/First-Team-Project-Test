# This is the main file for the calc app
# Authors: John and Man
from tkinter import *
import tkinter as tk

expression = ""
if __name__ == "__main__": 
      gui = Tk() 

      
      
      
      # set the background colour of GUI window 
      gui.configure(background="black") 
      
      # set the title of GUI window 
      gui.title("Calculator") 
      
      # set the configuration of GUI window 
      gui.geometry("400x600")

      equation = StringVar() 
 
      # create the text entry box for 
      # showing the expression . 
      expression_field = Entry(gui, textvariable=equation) 
      
      # grid method is used for placing 
      # the widgets at respective positions 
      # in table like structure . 
      expression_field.grid(columnspan= 90, ipadx=110)

      gui.mainloop() 

# addition fuction, takes in two inputs numbers and adds them
def addition(num1,num2):
	return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def division(num1,num2):
      return num1/num2

def multiplication(num1, num2):
	return num1 * num2

def Nth_Root(num,Nth):
      return num**(1/Nth)
def Sqr_Root(num):
      return num**(1/2)

def exponential (num, power):
    return num**power

#print statement to test function works
#print(addition(5 , 5))
#print(Sqr_Root(4))
#print("buttttttttt")



