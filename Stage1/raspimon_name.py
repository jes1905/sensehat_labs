from sense_hat import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep

#this is how you load the sense object so you can use it in this script.
sense = SenseHat()

#creating variables to store RGB colors
p = (128, 0, 128) #pink
w = (255, 255, 255) #white
k = (0,0,0) #blank
r = (255, 0, 0)
g = (0, 255, 0)

egg = [p,p,p,p,p,p,p,p,
       p,p,p,w,w,p,p,p,
       p,p,w,w,w,w,p,p,
       p,p,w,w,w,w,p,p,
       p,p,w,w,w,w,p,p,
       p,p,w,w,w,w,p,p,
       p,p,p,w,w,p,p,p,
       p,p,p,p,p,p,p,p]
       
hatched = [k,k,k,k,k,k,k,k,
           k,k,k,p,p,p,k,k,
           k,k,p,p,p,p,p,k,
           k,k,p,k,p,k,p,k,
           k,k,p,w,p,w,p,k,
           k,k,k,p,p,p,k,k,
           k,k,k,p,p,p,k,k,
           k,k,p,p,k,p,p,k ]

apple = [w,w,w,w,w,g,w,w,
         w,w,w,w,g,w,w,w,
         w,w,r,r,r,r,w,w,
         w,r,r,r,r,r,r,w,
         w,r,r,r,r,r,r,w,
         w,r,r,r,r,r,r,w,
         w,w,r,r,r,r,w,w,
         w,w,w,w,w,w,w,w ]

empty = [k,k,k,k,k,k,k,k,
         k,k,k,k,k,k,k,k,
         k,k,k,k,k,k,k,k,
         k,k,k,k,k,k,k,k,
         k,k,k,k,k,k,k,k,
         k,k,k,k,k,k,k,k,
         k,k,k,k,k,k,k,k,
         k,k,k,k,k,k,k,k ]



#this is how you scroll a message
sense.show_message("I'm hatching!")

#add more messages below. 


#the sense object has functions we can use: set_pixels. The value in the parentheses should be the egg.
sense.set_pixels(hatched)

#sense.set_pixels(empty)

#sense.show_message("i love apples", text_colour=[255, 0, 0])


#sense.set_pixels(apple)

