from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#makeover time! Here is a Python list. It holds  collection of string values.

names = ["Codey" , "Galbert" , "Freedy", "Voltria" , "Kat-Kat", "dudey"]

names.append("Lizardia")

sense.show_message(names[5])

#Colors:

r = (255, 0, 0 ) # RED color, stored in an another data structure called a tuple.
k = (0, 0, 0) # black means zero amounts of red, green and blue
g = (0,255,0)
b = (0, 0, 255)
w = (255, 255, 255)
p = (255, 100, 100)
d = (0, 50, 0)
#define another color. Use one letter variable names to make it easy later

raspimon = [
k, k, k, k, k, k, k, k,
k, k, r, r, r, r, k, k,
k, r, k, k, k, k, r, k,
k, r, r, k, r, k, r, k,
k, r, k, k, k, k, r, k,
k, k, r, r, r, r, k, k,
k, k, r, k, r, k, k, k,
k, k, r, k, r, k, k, k
]
 
sense.set_pixels(raspimon)

#add a one-pixel mouth

sense.set_pixel(3,4, [200, 150, 200])


new = [k,k,k,k,k,k,k,k,
       k,g,g,g,g,g,g,k,
       k,g,g,g,g,g,g,k,
       k,g,k,g,g,k,g,k,
       k,g,w,g,g,w,g,k,
       k,p,p,g,g,p,p,k,
       k,g,g,g,g,g,g,k,
       k,g,k,k,k,k,g,k ]

sleep = [k,k,k,k,k,w,w,k,
         k,k,w,w,k,k,w,w,
         k,k,k,w,w,k,k,k,
         k,k,g,g,g,g,k,k,
         k,g,g,g,g,g,g,k,
         g,d,d,g,g,d,d,g,
         g,p,p,g,g,p,p,g,
         g,g,d,d,d,d,g,g ]
 
sense.set_pixels(new)

sense.set_pixels(sleep)

 


