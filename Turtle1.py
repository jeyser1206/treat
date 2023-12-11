import turtle
import time
turtle.shape("turtle")
turtle.color("green")

#creates a list which contains value 0 or 1 for each element, each element represents if there is a treat inside of a house written by michael holmes
def trickortreat():
        import random
        treats=["","","",""]
        for index in range (0,3):
            x=random.randint(0,1)
            treats[index]=x
        return treats

'''
turtle builds a house takes a parameter which is used to decide how many times to build houses second parameter decides if it clears the screen at the end set it to 1 for the
animation of the turtle building the 4 houses and set it to 0 for the checkhouses() function written by michael holmes
'''
def build_houses(number_of_houses,clear_screen):
        for x in range (0,number_of_houses):
              
             #drawing the house written by michael holmes
              turtle.penup()
              turtle.speed(1)
              turtle.goto(0,0)
              turtle.speed(3)
              turtle.pendown()
              turtle.forward(100)
              turtle.left(90)
              turtle.forward(100)
              turtle.left(45)
              turtle.forward(50)
              turtle.left(90)
              turtle.forward(50)
              turtle.left(45)
              turtle.forward(100)
              turtle.bgcolor("white")
              turtle.penup()
              turtle.goto(-300,0)
              turtle.showturtle()
              time.sleep(3)
              #functionality to clear screen needed to be able to clear screen at different points written by michael holmes
              if clear_screen==1:
                turtle.clearscreen()
                turtle.shape("turtle")
                turtle.color("green")


              

#this is inside of the check houses function put here for readability written by michael holmes               
def setup():  
        turtle.clearscreen()
        turtle.shape("turtle")
        turtle.color("green")
        turtle.speed(10)
        turtle.bgcolor("black")
        turtle.pencolor("black")
        turtle.hideturtle()        


#uses input boxes to allow the user to say if they liked out animation or not written by michael holmes
def enjoy():
                turtle.clearscreen()
                turtle.shape("turtle")
                turtle.color("green")
                answer=turtle.textinput("did you enjoy the animation?","did you enjoy the animation?")
                if answer == "yes":
                        turtle.penup()
                        turtle.circle(200)
                        turtle.write("    Thank you")
                        turtle.exitonclick()
                else:
                        turtle.write("    TOO BAD")
                        turtle.exitonclick()


   

#takes the list from trickortreat() as a parameter and uses an if statement decide if there is a treat inside each house written by michael holmes
def check_houses(treats):
       
        #checks the list from trickortreat() to see if there was a treat or not written by michael holmes
       for index in range (0,3):
        if treats[index] == 0:
                setup()
                build_houses(1,0)
                turtle.speed(2)
                #negative reaction written by michael holmes
                child=turtle.clone()
                child.left(90)
                child.forward(300)
                turtle.write("there was no treat here")
                time.sleep(3)
        elif treats[index]== 1:
                setup()
                build_houses(1,0)
                turtle.speed(3)      
                #positive reaction written by michael holmes
                child=turtle.clone()
                child.left(90)
                child.forward(300)
                turtle.write("there was a treat here")
                turtle.penup()
                child.circle(200)
                time.sleep(3)
              
        
          

       
        
        
        
        
        


  


treats=trickortreat()
check_houses(treats)
enjoy()