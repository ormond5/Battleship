###Presentation
import sys
import random
import time

user_board = []
for z in range(10):
    user_board.append(["O"]*10)#add something to the pre-existing list.

def print_user_board(user_board): #made a function called print_board with the argument board.
   
    for i in range(10):
        #print the vertical line number
        if i != 9:
            print str(i+1) + "",
        else:
            print str(i+1) + " ";

    for i in range(10):
        #print the vertical line number
        if i != 9:
            print str(i-1) + "",
        else:
            print str(i-1) + " ";
        
    for row in user_board: #for loop
        print(" ").join(row) #sepearion/spacing




##Computer board
computer_board = []
for z in range(10):
    computer_board.append(["O"]*10)#add something to the pre-existing list.

def print_computer_board(computer_board): #made a function called print_board with the argument board.
    for i in range(10):
        #print the vertical line number
        if i != 9:
            print str(i+1) + "",
        else:
            print str(i+1) + " ";
    for row in computer_board: #for loop
        print(" ").join(row) #sepearion/spacing


def get_user_input():
    while(True):
        try:
            #x,y =[int(i) for i in input("Please enter coordinates(x,y): ")]
            x = int(input("Please select a row: "))
            y = int(input("Please select a column: "))
            x = x-1;
            y = y-1;
            if (x >9 or y >9 or x < 0 or y < 0):
                print "Please enter numbers from 1-10"
            else:
                return x,y
        except NameError:
            print "You did not enter a  number, try again"
        except TypeError :
            print "Something went wrong,let's try again"
        except SyntaxError:
            print "Something went wrong,let's try again"
            

def get_ori():
    while(True):
        ori = raw_input("Would you like your ship vertical or horizonatal, (v,h) ").lower()
        if ori == "v" or ori == "h":
            return ori
        else:
            print "Wrong letter, try again"





def place_destroyer():
    while(True):
        print("Let's place your Destroyer")
        i = 1;
        ship = "A";
        print ("It will appear as an 'A' on your board")
        print("Your ship length will be 2")
        origlength = 1 ###Think like a code not a normal person. numbers start at 0
        user_row,user_col = get_user_input()
        user_orientation = get_ori()
        if (orienation_check(user_orientation,user_row,user_col,origlength,ship,i) == True):
            break;
        print "dD"
    
    
    
def place_battleship():
    
    while (True):
        print("Let's place your Battleship")
        i = 2;
        ship = "B";
        print("Your ship length will be 4")
        origlength = 3; #numbers in computer sciece start at 0
        user_row,user_col = get_user_input()
        user_orientation = get_ori()
        if (orienation_check(user_orientation,user_row,user_col,origlength,ship,i) == True):
            break;
        else:
            print"Uh oh, That coordinate overlaps other ships or does not fit on the board\nLet's try again! "
            print_user_board(user_board)



##def place_carrier():
##    while(True):
##        print("Let's place your Carrier")
##        i = 3;
##        ship = "E";
##        print("Your ship length will be 5")
##        origlength = 4;
##        user_row,user_col = get_user_input()
##        user_orientation = get_ori()
##        if(orienation_check(user_orientation,user_row,user_col,origlength,ship,i) == True):
##            break;
##        print"Uh oh, That coordinate overlaps other ships or does not fit on the board\nLet's try again! "
##        print_user_board(user_board)



def orienation_check(user_orientation,user_row,user_col,origlength,ship,i): 
    if i == 1:#Destroyer
        if (user_row < 0  or user_row >=7 or user_col < 0 or user_col >=7):
            print "You are placing the Destroyer ship,\nSo your ship size will be two"
            print "The spot you picked will not fit on your board"
            print "Try and enter some numbers between 1-8 "
            print_user_board(user_board)
            return False;
        else:
            if (ship_placement(user_row,user_col,user_orientation,origlength,ship,i) == True):
                return True;
            
            
    elif i == 2:#Battleship
        if (user_row < 0  or user_row >= 7 or user_col < 0 or user_col >= 7 ):
            print "You are placing the Battlehip\nSo your ship size will be four"
            print "The spot you picked will not fit on your board"
            print "Try and enter some numbers between 1-7 "
            print_user_board(user_board)
            return False;
            
        else:
        
            if (ship_placement(user_row,user_col,user_orientation,origlength,ship,i) == True):
                return True;



def ship_placement(user_row,user_col,user_orientation,origlength,ship,i):
    count = 0;
    if (user_orientation == "v" ):
        while (origlength >= 0):
            if (user_board[user_row][user_col] != "O" ):##if there is NOT an open spot or it overlaps
                while( count > 0): ##Erase whatever letter was put on the board earlier     
                    user_board[user_row-1][user_col] = "O"
                    user_row = user_row -1;
                    count = count -1;
                return False;

            else: # If open spot then continue
                user_board[user_row][user_col] = ship; ##The letter previously assigned in parent fucntion
                user_row = user_row +1;
                count = count +1
                origlength = origlength - 1;
        return True;
    
    if (user_orientation == "h" ):
        while (origlength >= 0):
            if (user_board[user_row][user_col] != "O" ):
                while( count > 0): 
                    user_board[user_row][user_col-1] = "O"
                    user_col = user_col -1;
                    count = count -1;
                return False;

            else: 
                user_board[user_row][user_col] = ship;
                user_col = user_col +1;
                count = count +1
                origlength = origlength - 1;
        return True;





comp_x = 4;
comp_y = 4;                        
print comp_x, comp_y
################# USER GUESSING ##################################

##EQUAL OPPONENTS SHIPS

def user_guess(computer_board,comp_x,comp_y):
    hits = 0
    print_computer_board(computer_board)
    
    while(True):
        if hits <17:
            user_x,user_y = get_user_input()
            if ( user_x == comp_x and user_y == comp_y):
                computer_board[user_x][user_y] = "X"
                
                print_computer_board(computer_board)
                print "You hit your oppenents ship!"
                print "Guess again!"
                raw_input("Press Enter to continue...")
                hits = hits +1;              
                                                                 
            else:
                computer_board[user_x][user_y] = "M"
                print_computer_board(computer_board)
                print "You missed your opponent's ship"
                print "Now it's your opponent's turn"
                raw_input("Press Enter to continue...")
                break;
                
                
         
        else:
            print "Congratulations! You sunk all of your opponents ships "
            print "YOU WIN"
            print_computer_board(computer_board)
            sys.exit(0)

ships = {'E':5,'B':4, "A":3,"F":3,"D":2}

def computer_place_ships(computer_board, ships):
    for i, j in ships.items():
        ship_not_place = True
        x = random.randint(0,9)
        y = random.randint(0,9)
        print x,y
        ori = 0
        
        while( ship_not_place):
            
            if ori == 0: #"v"
                if computer_board[x][y] == "O":
                    for k in range(j):
                        computer_board[x][y] = i
                        computer_board[x+k][y] = i
                    ship_not_place = False
                    break;
                        
                else:
                    print "same spot", x,y
                    x = random.randint(0,6)
                    y = random.randint(0,6)
                    ship_not_place = True
        return x,y



def computer_place_ships(computer_board, ships):
    for i,j in ships.items():
        ship_not_place = 0
        x = random.randint(0,9)
        y = random.randint(0,9)
        ori = random.randint(0,1) 
        while(ship_not_place < 5 ): 
            try:
                if ori == 0:
                    if computer_board[x][y] =="O": #if the spot is open
                        for k in range(j):  # range through the dictionary j
                            computer_board[x][y] = i #place the ship
                            computer_board[x+k][y] = i #add one to x j-times
                        ship_not_place = ship_not_place + 1
                        print "placed", i
                        break;

                        
                    elif computer_board[x][y] != "O":
                        print "overlapping",x,y,ori,i
                        print_computer_board(computer_board)
                        sys.exit(0)
                    
                    
            except IndexError:
                print "ran into a problem", x,y,ori,i
                #computer_board[x][y] = "WW"
                if ori == 0:
                    for k in range(j):
                     computer_board[x][y] = "O"
                     computer_board[x-k][y] = "O"
                else:
                    for k in range(j):
                        computer_board[x][y] = "O"
                        computer_board[x][y-k] = "O"
                break;

def comp_guess(user_board):
    hits = 0;
    while (True):
        if hits <17:
            print"The computer is guessing....."
            comp_guess_x = random.randint(0,9);
            comp_guess_y = random.randint(0,9);
            
            time.sleep(1)
            if (user_board[comp_guess_x][comp_guess_y] !="O" ):
               
                user_board[comp_guess_x][comp_guess_y] = "X"
                
                print_user_board(user_board)
                comp_guess_y = comp_guess_y +1;
                omp_guess_x = comp_guess_x +1;
                print "The computer guessed" , comp_guess_x , "," ,comp_guess_y
                print "The computer hit your ship!! "
                print "The computer will guess again"
                raw_input("Press Enter to continue...")
                hits = hits + 1;
                
                #nextguess(user_board,comp_guess_x,comp_guess_y,hits)
                
                break;
                
            else:
                
                user_board[comp_guess_x][comp_guess_y] = "H"
                
                print_user_board(user_board)
                print "The computer missed your ship"
                print "The computer guessed" , comp_guess_x+1 , "," ,comp_guess_y+1
                print "Now it is your turn"
                raw_input("Press Enter to continue...")
                break;
                    
        else:
            print "Your opponent hit all of your ships "
            print "YOU LOSE"
            print_user_board(user_board)
            sys.exit(0)

def nextguess(user_board,comp_guess_x,comp_guess_y,hits):
    smartguess =-1;


    while (smartguess < 0):
        
            
        if (user_board[comp_guess_x]<9 and user_board[comp_guess_x][comp_guess_y]!="O"): ## x+1,y
            hits = hit +1;
            user_board[comp_guess_x+1][comp_guess_y] = "X"
            print_user_board(user_board)
            print "The computer hit your ship!!"
            print "The computer guessed" , comp_guess_x+1 , "," ,comp_guess_y
            print "The computer will guess again"           
            raw_input("Press Enter to continue...")
            

        else:
           
            user_board[comp_guess_x][comp_guess_y] = "M"
            print_user_board(user_board)
            print "The computer missed your ship" 
            print "Now it is your turn"
            smartguess = 1;
            raw_input("Press Enter to continue...")
            break;
                        
################# MAIN ##################################
while (True):
    try:     
        print("Welcome to the game Battleship")
        print("First here is your board. Lets place some ships")
        print("Keep in mind you have a 10 by 10 grid. With numbers from 1-10")
        print_user_board(user_board)
        place_destroyer();
        print("Awesome here is your Destroyer")
        print_user_board(user_board)
        place_battleship();
        print("Awesome here is your Battleship")
        print_user_board(user_board)
    ##place_carrier();
    ##print("Awesome here is your Carrier")
    ##print_user_board(user_board)
        print "Okay you have placed your ships, now lets start finding the enimies ships. "

        while(1):
            user_guess(computer_board,comp_x,comp_y)
            comp_guess(user_board)

    except KeyboardInterrupt:
        decision = raw_input("I see you are not happy! Would you like to quit or restart? (Q or R) ").upper()
        if (decision == "Q"):
            print"Thanks for playing, Goodbye!"
            sys.exit(0)
        elif(decision == "R"):
            print "Restarting now..."
            time.sleep(1)
                              
                   
#     More code for smart guessing Not tested yet

##            elif(user_board[comp_guess_y+1]<9 and user_board[comp_guess_y+1] != "O"):## x,y+1
##                if (user_board[comp_guess_x][comp_guess_y]!="O"):
##                    hits = hit +1
##                    print "The computer hit your ship!!"
##                    print "The computer will guess again"
##                    user_board[comp_guess_x][comp_guess_y] = "X"
##                    print_user_board(user_board)
##                    raw_input("Press Enter to continue...")
##        
##                else:
##                     print "The computer missed your ship" 
##                     user_board[comp_guess_x][comp_guess_y] = "M"
##                     print_user_board(user_board)
##                     print "Now it is your turn"
##                     smartguess = 0;
##                     raw_input("Press Enter to continue...")
##                    
##        
##    
##            elif(user_board[comp_guess_x-1]>=0 and user_board[comp_guess_x-1] != "O"): ##x-1,y
##                if (user_board[comp_guess_x][comp_guess_y] == "O"):
##                    hits = hit +1;
##                    print "The computer hit your ship!!"
##                    print "The computer will guess again"
##                    user_board[comp_guess_x][comp_guess_y] = "X"
##                    print_user_board(user_board)
##                    raw_input("Press Enter to continue...")
##                else:
##                    print "The computer missed your ship" 
##                    user_board[comp_guess_x][comp_guess_y] = "M"
##                    print_user_board(user_board)
##                    print "Now it is your turn"
##                    smartguess = 0;
##                    raw_input("Press Enter to continue...")
##                
##
##        
##            elif(user_board[comp_guess_y-1]>=0 and user_board[comp_guess_y-1] != "O"): ##x,y-1
##                if (user_board[comp_guess_x][comp_guess_y] != "O"):
##                    hits = hit +1;
##                    print "The computer hit your ship!!"
##                    print "The computer will guess again"
##                    user_board[comp_guess_x][comp_guess_y] = "X"
##                    print_user_board(user_board)
##                    raw_input("Press Enter to continue...")
##        
##                else:
##                    print "The computer missed your ship" 
##                    user_board[comp_guess_x][comp_guess_y] = "M"
##                    print_user_board(user_board)
##                    print "Now it is your turn"
##                    smartguess = 0;
##                    raw_input("Press Enter to continue...")


                    


