'''
Created on Jan 26, 2015

@author: Jerry Li
'''
import turtle               # allows us to use the turtles library                                         
wn = turtle.Screen()        # creates a graphics window                                                    
wn.bgcolor("lightblue")     # creates a light blue background                                      
                                                                                   

        
def flowerCenter(turt):
    #creates the center of the flower
    turt.hideturtle()
    turt.dot(70,"yellow")
        
def spiral(turt):
    #creates one set of the petals of the flower
    turt.shape("turtle")
    turt.color("green")
    print(range(7,48,2))
    turt.up()
    for size in range(7,120,2):
        turt.stamp()
        turt.forward(size)
        turt.right(45)

def spiral2(turt):
    #creates another set of the petals of the flower
    turt.shape("turtle")
    turt.color("pink")
    turt.right(90)
    print(range(7,48,2))
    turt.up()
    for size in range(7,120,2):
        turt.stamp()
        turt.forward(size)
        turt.right(45)
        

def cloud(turt):
    #creates one cloud
    turt.hideturtle()
    turt.penup()
    turt.setx(200)
    turt.sety(200)
    turt.pendown()
    turt.shape("circle")
    turt.color("white")
    print(range(7,75,4))
    turt.up()
    for size in range(6,75,1):
        turt.stamp()
        turt.forward(size)
        turt.right(20)
        
def cloud2(turt):
    #creates second cloud
    turt.hideturtle()
    turt.penup()
    turt.goto(-200,200)
    turt.pendown()
    turt.shape("circle")
    turt.color("white")
    print(range(7,75,4))
    turt.up()
    for size in range(6,75,1):
        turt.stamp()
        turt.forward(size)
        turt.right(20)
    

def stem(turt):
    #creates the stem of the flower
    turt.right(90)
    turt.shape("turtle")
    turt.color("green")
    for size in range (5,400,2):
        turt.stamp()
        turt.forward(size)

def leaf(turt):
    #creates the leaf of the stem
    turt.hideturtle()
    turt.penup()
    turt.goto(20,-200)
    turt.pendown()
    turt.begin_fill()
    turt.color("lightgreen")
    turt.forward(30)
    turt.left(60)
    turt.forward(30)
    turt.left(60)
    turt.forward(30)
    turt.left(60)
    turt.forward(30)
    turt.left(60)
    turt.forward(30)
    turt.left(60)
    turt.forward(30)
    turt.left(60)
    turt.forward(30)
    turt.left(60)
    turt.forward(30)
    turt.left(60)
    turt.forward(30)
    turt.end_fill()
    
       
def draw():
    # calls upon all the functions defined above and draws them in the order specified below
    
    daniel = turtle.Turtle()
    cloud(daniel)
    
    grant = turtle.Turtle()
    cloud2(grant)
    
    jerry = turtle.Turtle()    
    spiral(jerry) 
    
    nikhil = turtle.Turtle()
    stem(nikhil)
    
 
    
    dylan = turtle.Turtle()
    leaf(dylan)
    
    ben = turtle.Turtle()
    spiral2(ben)
    
    aly = turtle.Turtle()
    flowerCenter(aly) 
 
if __name__ == '__main__':
    # main function to have a turtle draw a picture 
    draw() 


    wn.exitonclick()        # Must be last line in file
