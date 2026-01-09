from turtle import Turtle, Screen

timmy = Turtle() # timmy is an object of class Turtle 
print(timmy)
timmy.shape("turtle")
timmy.color("chartreuse")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight) #my_screen is an object of class Screen and canvheight is attribute to the object
my_screen.exitonclick() #exitonclick() is an method for the object