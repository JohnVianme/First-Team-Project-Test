# This is the main file for the calc app
# Authors: John and Man
from tkinter import *

main = Tk()

main.geometry("250x300")
a = Label(main, text="Hello")
a.pack()
def change_text():
      global a
      a.config(text="New text")

button = Button(main, text = "Enter", command= change_text)
button.pack()
main.mainloop()


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
print("buttttttttt")



