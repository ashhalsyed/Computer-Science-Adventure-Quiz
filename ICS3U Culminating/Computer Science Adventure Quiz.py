import easygui
import sys
import random
#Imports all necessary libraries

def Introduction():
    """ Function used to introduce the user to the game"""
    print "Welcome to my Computer Science Adventure Quiz\n"
    print "To win this game you must navigate to the end of the maze without losing all of your lives\n"
    print "The X's represent blocks you can not walk on, the 'C' Represents your character, and the 'E' represents the end of the maze\n"
    print "Enemies are hidden throughout your path. When encountered, you must answer a computer science related multiple choice question\n"
    print "Good luck!"
    #Prints the user's goal and explains how the game works

def PresetVariables():
    """Function used to reset variables"""

    characterlocation=91
    #Sets the character location to the starting block

    enemylocation=[15,84,66,89]
    #Sets the locations of the enemies to the hidden locations

    lives=3
    #Sets the player's lives to 3

    questions={"Which of the following is an interpreted programming language":["Python"
                                                                                ,"C"
                                                                                ,"C++"
                                                                                ,"Visual Basic"],

               "Which of the following is not a data type":                    ["Variable"
                                                                                ,"String"
                                                                                ,"Integer"
                                                                                ,"Float"],

               "What is not a requirement when defining a function":           ["Doc String"
                                                                                ,"Parameter Brackets"
                                                                                ,"Function Name"
                                                                                ,"Body"],

               "Which of the following libraries does Python have built in":   ["Random Library"
                                                                                ,"GObject Library"
                                                                                ,"EasyGui Library"
                                                                                ,"Sys Library"]}
    #Sets a dictionary with questions as the keys and the answers in a list as the values

    return characterlocation,enemylocation,lives,questions
    #Returns all the variables needed to begin the program

def FormatGrid():
    """Format the grid the user navigates on"""

    grid={}
    #Creates a dictionary called grid

    for block in range(100):
        block+=1
        grid[block]="x"
    #Creates 100 keys of 1-100 all with the value "x". Each number in the grid represents a block. The value associated with the key is type of block

    for key in grid:
        if key>=12 and key<=20:
            grid[key]="o"
        if str(key)[-1]=="2" and key>=22 and key<=52:
            grid[key]="o"
        if str(key)[-1]=="8" and key>=28 and key<=58:
            grid[key]="o"
        if str(key)[-1]=="0" and key>=30 and key<=80:
            grid[key]="o"
        if key>=61 and key<=63:
            grid[key]="o"
        if key>=66 and key<=68:
            grid[key]="o"
        if str(key)[-1]=="1" and key>=71 and key<=91:
            grid[key]="o"
        if str(key)[-1]=="3" and key>=73 and key<=83:
            grid[key]="o"
        if str(key)[-1]=="6" and key>=76 and key<=96:
            grid[key]="o"
        if key>=88 and key<=90:
            grid[key]="o"
        if str(key)[-1]=="4" and key>=84 and key<=94:
            grid[key]="o"
    #For all the necessary locations, the program changes the values of each block to "o". "o" will mean an open block while "x" will mean a wall block

        if key==98:
            grid[key]="END"
    #sets the value of the block representing the end to "END"

    return grid
    #Return the grid with the correctly formatted values for each key

def DrawGrid(characterlocation,grid):
    """Prints the grid the user navigates on"""

    for key in grid:
        if str(key)=="1":
            print " _"*11
        #Prints  the top border of the maze.

        if str(key)[-1]=="1":
            print "|",
        #Prints the left border before every line of the maze

        if key==characterlocation:
            print "C",
        #Prints "C" in the place of the block representing the player's current location

        elif grid[key]=="o":
            print " ",
        #Prints a space for the keys with a value of "o"

        elif grid[key]=="END" and key!=characterlocation:
            print "E",
        #Prints "E" for the key that represents the end of the maze

        else:
            print "X",
        #Prints "X" for each value representing a block the user can not walk on

        if str(key)[-1]=="0":
            print "|"
        #Prints the right border after every line of the maze

        if str(key)=="100":
            print " -"*11
        #Prints the bottom border of the maze.


def DisplayStats(enemylocation,lives):
    enemiesFound=4
    for enemy in enemylocation:
        enemiesFound-=1
    #Determines the amount of enemies the user has found

    print
    print "%s / 4 Enemies found" %(enemiesFound)
    print "lives: %s" %(lives)
    #Prints the enemies found and the user's current lives

def PlayerInput(grid,characterlocation):
    """Moves the user in the direction they choose"""

    while True:
        playermove=easygui.buttonbox(msg="What direction would you like to move in. Select quit to exit the game?",choices=["UP","DOWN","LEFT","RIGHT","QUIT"])
        #Displays an easygui buttonbox that asks the user which direction they would like to move in

        if playermove=="UP" and characterlocation-10>0 and grid[characterlocation-10]!="x":
            characterlocation-=10
            break
        #If the player chose to go up and there is not a border or wall above the character, the character's location is decreased by 10.

        elif playermove=="DOWN" and characterlocation+10<100 and grid[characterlocation+10]!="x":
            characterlocation+=10
            break
        #If the player chose to go down and there is not a border or wall below the character, the character's location is increased by 10.

        elif playermove=="LEFT" and str(characterlocation)[-1]!="1" and grid[characterlocation-1]!="x":
            characterlocation-=1
            break
        #If the player chose to go left and there is not a border or wall to the left of the character, the character's location is decreased by 1.

        elif playermove=="RIGHT" and str(characterlocation)[-1]!="0" and grid[characterlocation+1]!="x":
            characterlocation+=1
            break
        #If the player chose to go right and there is not a border or wall to the right of the character, the character's location is increased by 1.

        elif playermove=="QUIT":
            print "You have quit the game"
            sys.exit()
        #If the player chose to quit, the program ends

        else:
            print "You can't move in that direction"
        #If the character tries to move into a wall or border they will be told that they cant move in that direction

    return characterlocation
    #Returns the character's new location

def Progress(characterlocation,enemylocation,lives,questions):
    """Keeps track of the user's lives and tells him if he's won or lost"""

    if characterlocation==98 or lives==0:
        if characterlocation==98:
            print "You have won the game"
    #If the character in on the end block, the player is told they have won the game

        else:
            print "You have lost the game"
    #If the user lost all of their lives, they are told they have lost

        characterlocation,enemylocation,lives,questions=PlayAgain(characterlocation,enemylocation,lives,questions)
    #If the user has won or lost, a function is called that asks the user if they want to play again

    return characterlocation,enemylocation,lives,questions
    #Returns all of the variables that may be reset if the user chooses to play again

def EnemyEncounter(characterlocation,enemylocation,lives,questions):
    """Does what needs to be done if the user encounters an enemy"""

    for location in enemylocation:
        if characterlocation==location:
            easygui.msgbox(msg="ENEMY SPOTTED",image="Enemy.gif")
            #If the character is on an enemy block, they are told they have encountered an enemy

            questions,result=Questions(questions)
            #A function that asks the user multiple choice questions is called

            if result=="CORRECT":
                easygui.msgbox("Correct",image="EnemyLose.gif")
                enemylocation.remove(location)
            #If the result from the multiple choice question is correct, the enemy's location is removed

            elif result=="INCORRECT":
                easygui.msgbox("Incorrrect",image="EnemyWin.gif")
                lives-=1
                enemylocation.remove(location)
            #If the result from the multiple choice question is incorrect, the enemy's location is removed and the character loses one life

    return enemylocation,lives,questions
    #Returns the new enemy locations, the character's updated lives, and the dictionary with the updated questions

def Questions(questions):
    """Asks the user multiple choice questions"""

    questionlist=[]
    #Sets a question list that will hold all of the questions in the dictionary

    answers=["Python","Variable","Doc String","Random Library"]
    #Sets a list with all of the answers to the multiple choice questions

    for question in questions:
        questionlist.append(question)
    #Adds all of the keys in the questions dictionary to the questions list

    randomquestion=random.choice(questionlist)
    #Generates a random question from the questions list

    choicelist=questions[randomquestion]
    #creats a list with the values for the random question chosen

    random.shuffle(choicelist)
    #Shuffles the answers list

    guess=easygui.buttonbox(msg=randomquestion,choices=choicelist)
    #Displays the questions and answers in an easygui button box

    del(questions[randomquestion])
    #deletes the question from the question dictionary after the user has picked an answer

    for answer in answers:
        if guess==answer:
            result="CORRECT"
            break
        #If the answer the user inputted is equal to any of the answers in the answer list, a variable called "result" is set to "CORRECT"

        else:
            result="INCORRECT"
        #If the answer does not match the answers in the list, a varible called "result" is set to "INCORRECT"

    return questions,result
    #Returns the updated questions dictionary and the outcome of the player's guess

def PlayAgain(characterlocation,enemylocation,lives,questions):
    """Allows user to play again"""

    choice=easygui.buttonbox(msg="Would you like to play again?",choices=["YES","NO"])
    #Displays an easygui button box that asks the player if they want to play again

    if choice=="NO":
        sys.exit()
    #If the player chose to not play again, the program ends

    characterlocation,enemylocation,lives,questions=PresetVariables()
    #Calls the function that resets the variables, if the user chooses to play again

    return characterlocation,enemylocation,lives,questions
    #returns the reset variables for the character's location, the enemy locations, the lives and the questions dictionary

Introduction()
#Calls the function that introduces the user to the Adventure Quiz

characterlocation,enemylocation,lives,questions=PresetVariables()
#Calls the function that sets the variables needed for the program to run

while True:
    grid=FormatGrid()
    #Calls the function that formats the grid

    DisplayStats(enemylocation,lives)
    #Calls the function that displays the character's stats.

    DrawGrid(characterlocation,grid)
    #Calls the function that draws the grid. Recievs the character's current location and the formatted grid

    characterlocation=PlayerInput(grid,characterlocation)
    #Calls the function that asks the player which direction they would like to move in and updates the character location variable.

    enemylocation,lives,questions=EnemyEncounter(characterlocation,enemylocation,lives,questions)
    #Calls the function that checks if the character is on an enemy block. The function may also update the enemy locations, the player's lives, and the questions dictionary.

    characterlocation,enemylocation,lives,questions=Progress(characterlocation,enemylocation,lives,questions)
    #Calls the function that checks if the user has won or lost the game. The function may also reset the variables to allow the player to play again

#Calls functions in proper order with proper parameters.