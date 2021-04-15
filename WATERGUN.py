from random import choice
print("Lets Play Snake Water Gun Game \n GAME RULES...")

def am():
    """S(1)nake vs.Water: Snake drinks the water hence wins.
       (2)Water vs.Gun: The gun will drown in water, hence a point for water.
       (3)Gun vs.Snake: Gun will kill the snake and win"""
print(am.__doc__)

p = 0
snake = 2
water = 3
Gun = 4
You = 0
com = 0
q = 0

print("SNAKE WATER GUN GAME")
print("Use Character in Capital Format")
while p < 10:
    i= input("Entered any of one S/W/G/....")
    if(i == "S"):
        j = choice([water, Gun])
        if snake*j == 6:
            print("You won!!!")
            You = You + 1
            print("Your Score is",You)
        else:
            print("You lose!! Computer won!!")
            com = com+1
            print("Computer Score", com)
    if(i == "W"):
        j = choice([Gun,snake])
        if water*j == 6:
            print("You Won!!!")
            You = You + 1
            print("Your Score is..", You)
        else:
            print("You Lose... ComputerWon!!!")
            com = com+1
            print("Computer Score is", com)
    if(i == "G"):
        j = choice([water,snake])
        if Gun*j == 8:
            print("You  won!!")
            You = You+1
            print("Your Score is..", You)
        else:
            print("You lose  Com Won!!!")
            com = com +1
            print("Computer Score", com)
    p = p +1
    
    
print("Your Score is..", You)
print("Computer Score", com)



