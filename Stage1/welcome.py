from sense_hat import SenseHat
from time import sleep

#below are simple print statments. 
#Any code between quotation marks are considered Strings, or text.

print("Welcome to the Raspimon!")

#We can import other Python code to help us. Sleep is like a pause in the code.
#Change the value inside the sleep() function call to change the pause amount.
sleep(2) 

print("Let's get started!")

sleep(1.5)

print("what's your favorite color?")

#input is used to get text input from a keyboard. We store it as a variable called name
#the \n forces a new line.
color = input("my my favorite color is: \n")

sleep(1)

#Use the name in a new print statement. You can combine strings with the + symbol.
print("That's nice, " + color)

sleep(1.5)

print("I think you are ready to meet your Raspimon in Lab 2.")



 
