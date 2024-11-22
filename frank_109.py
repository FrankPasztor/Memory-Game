# Importing the necessary libraries in order to track time and randomize the hidden grid
import time  
import random
# Function to print the game grid
def print_tile(tile):
    
    # Display grid with column numbers (coordinate system)
    print('  ', end='')
    for i in range(1, len(tile[0]) + 1):
        print(str(i) + ' ', end=' ')

    print()
    
    # Display grid with row letters (coordinate system)
    for i in range(len(tile)):
        print(chr(ord('a') + i), end=' ')

        for j in range(len(tile[0])):
            print(tile[i][j], end=' ')

        print()
        
def austins_face():
    print("                                                 .....                                              ")
    print("                                    ... ......*+...........                                     ")
    print("                                       .....:#%%%%%%%%%%%%%%#=..                                    ")
    print("                                      ...:+#%%%##%%%%%%%%%%@%@%.. .....     .                       ")
    print("                              .........+####%%%%%%%%%%@%%%%@@@@%................                    ")
    print("                             ....:+*#%%%%##%%%%%#%%%%%%%@%@@@@@@%%###%%###**....                    ")
    print("                          ....:##*#%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@%%%%%%%###=.........           ")
    print("                         ....=###%%%%%%%%%%%%@@@%%%%%%%@@@@@@@@@@@@@@@%%%%%%%%%%##-.... .           ")
    print("                         ...*#%%%%%%%%%%%%@@@%@%@%%%%%%@@%%@@%@@@@@@@@@%%%%%%%%%%%##*-....          ")
    print("                      ....:#%%%@%%%%%%%%@%@@%%%%%%%%%%%%@@%@@@@@@@@%@@@@%%%%%%%%%%%%##*=...         ")
    print("                    ....=%%%%%%%%%%@@@%%%%@%%%%#%%%%%%%%%%%@%@%%%%@%%%%%%%%%%%%%%%%%%###+..         ")
    print("                  ....*%%%@%%%%%%%%%%%@%%%%%%%#%%#%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%%%%%%###%-...      ")
    print("                 ...-%%%%%%@@%%%%%%%%%@%%%%%%#%%###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%####*....    ")
    print("                 ..-%%##%@@%%@%%%%%%%%%%%#%%%%%%%###%%%%%%%#***##%%%%%%%%%%%%%%%%%%%%########..     ")
    print("                  .#%%%@@@@%@%%%#%%%###%##%%%%%%%%%%%%%%%##*****########%%%%%%%%%#%%#######%#:..    ")
    print("                 ..%%%@@@@%%@%%%%#%#####%%%%%%%%%%%%%#%####*+*+*#######%%%%%%%%%##%##%%###%%#=..    ")
    print("                ..=%@@@@@%%%@%%%%#%#####%%%%%%%%%%%%%%####*+++**#######%%####%%%#####%%%%%#%%-..    ")
    print("                  #@%@@%%%%%@@%%@%%%%##%%%%%%%%%%%%%%####*+*##*####%#########%%%%#%%%%%%%%%%%-..    ")
    print("                 .%@%@%%%%%%@@%@@%%%#%%%%%%@%%%%%%%%%####*++**#%%%%%##########%%%#%%%%%%%%%%%%....  ")
    print("                 .%@%%%%%%#%%@%@%%%%##%%%%%%%%%##%%%####*****#%%%%%####*######%%#%%%%%%@%%%%%%-...  ")
    print("               ...*%%%%%%%%%%%%@@%%%#%####%%%%##%%%%**#**++*#%%%%%#*****##*#*#%%%%%@%%%%@%%%%%=...  ")
    print("               ...*%%%%%%%%%%%%%%%%%###***#%%#*#%##**++=====+***+++*#%%%%@%#*#%%%%@%%%%#%%%%%%-...  ")
    print("               ...#%@%%%%%%%%%%%%%%#*++++=++++===========--=====+*##%%#***#%#%%%%@@%%%###%#%%*....  ")
    print("             ....*#%%%@%%%%%%%%####***#####**+++===--=========++*###*++++++*#%%%%%%%%%%%%%%%%-..... ")
    print("             ...-*%%%@@@@%%%%%####*#%%%%%%%####**++========++++*#*#%%%%%@@@@@@@@@@@@%%%%%%%%@#....  ")
    print("             ...-%%%%@@%%%%%%%####%#***#%%%%*#%##*+++++==++*%@@@@%%%%%%%%%**%@@%@@@@@%%%%%%%%%....  ")
    print("             ..:%@%%%%%@%%%@@@@@@@@@@%####%%%%%%%@@@%@@%@@@@@%#%%%%%##%%%%%%%#@@%#@@@%%%%%%%%%:...  ")
    print("             ..+%%%@%%%@%%@@@@@%@@##%%%%%@@@@@%%%%%@@@@@@@@@#***#*+##**%#**%%%@@#%@@@%%%%%@%%:....  ")
    print("             ..#%%%%@%%%@@%@@%@@@%%%%%%%%+%%%#=#+**%@@+===@@++=*=+%%%%++##***%@@%%%%@@@%%%%%*..  .  ")
    print("             ..#%%%%@@%%@@%@@@%%@%%#**##**%@@%++*++*@+===++@#+=++********++++*@%%%%%%%%%%%%%....    ")
    print("             ..+%%%@@@@%@@@@@@%%%@*+++*#*****++++++@#+====+*@#+++*******+++++@%#*#%##%%%%%%=..      ")
    print("             ..:%@%@@@@@@@@@@@%%%@%++++*******+++=%%*+====+**%@+=+++++++=++%@%#***#%%#%%%%:.        ")
    print("             ...-%%@@%@@@@@@@%%#%#%%++++++++++==#@#**+===++****%@@@@@@@@@@##%%+***%%##%%%+....      ")
    print("              ...:%%@%@@@@@@@%#*#%#*##%%%%%@@@@%*++**+===++***++====++++++*++++**#%%#####-.         ")
    print("               ....#@@@%@@%%%%#****#####***+====+++**+===+++*++++====++++++++++**#%%%###:..         ")
    print("                  ...%#%@@%%%%##***++++++++==+++++**+++===++**++*+++++++++++++**###%%%*...          ")
    print("                    ....*%#%%%##*****++++++++*++**********######*++**+++++++****#####%-..           ")
    print("                      ...#*#%%##******++++++**++*#%%%@%###%%##*+++++***++++*****##%%%+...           ")
    print("                     .....#######*******++****++++++**#%%#++*++++++************###%%:...            ")
    print("                     ... ..%%%%##**************++++++++++++++++++++************####:.               ")
    print("                     ... ...#%###***************+++++++++++++++++*************##**#..               ")
    print("                          ....=%##***************######****##*******#*******######*..               ")
    print("                             ..=##***********##%%#+#==+=+*-=++*%%%%%#******##*####-..               ")
    print("                             ..-%##*********#%@@@%+#+++==+==+++%%@@###****##*#####...               ")
    print("                               ..###***********#%@@@@@@@@@@@@@@#%##*++*+**#**####*..                ")
    print("                              ...-###******+++**##**===+===++==*###*+*+**#***###*....               ")
    print("                               ...=###******+++*****=+=+=+=++****##**++*#***#%%#:..                 ")
    print("                               .....###***#**++****************###***+**#**#%%#+.                   ")
    print("                                   ..%##**********#####**#####%%#***++*#**#%%%=.                    ")
    print("                                   ...:##************########****++++*##*#%@=...                    ")
    print("                                    ....-##******++++*++*++++++++++**####%@*..                      ")
    print("                                       ...#####**+*++++++++++++*****%%%%%:....                      ")
    print("                                        ...*####******************#@%@*.....                        ")
    print("                                         ....+####*************##%@@+..      ")

# Function to get the row letter from the user
def get_row_letter(choice):
    while True:
        letter = str(input(f'(Choice {choice}) Which row letter would you like to select: '))
        # Check the user input for incorrect character type 
        L1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        L2 = L1[:tile_size]
        lastLetter = L1[tile_size-1]
        if letter.isalpha() and len(letter) == 1 and letter.islower() and letter in L2:
            return letter
        else:
            print("Throw Me A Frickin' Bone Here! - Austin")
            print(f'Please enter a single lowercase letter in the alphabet from a to {lastLetter}.\n')
            
# Function to create a random grid of characters
def create_random_grid(tile_size):
    characters = ['^ ','% ','$ ','@ ','? ','! ','Z ','Y ','X ','W ','V ','U ','T ','S ','R ','Q ','P ','O ','N ','M ','L ','K ','J ','I ','H ','G ','F ','E ','D ','C ','B ','A ']
    random.shuffle(characters)
    tile_characters = []
    
# Populate grid with shuffled characters
    for q in range(tile_size**2 // 2):
        character = characters.pop()
        tile_characters.extend([character, character])
    random.shuffle(tile_characters)
    grid = [[tile_characters.pop() for u in range(tile_size)] for l in range(tile_size)]
    return grid

# Function to get the column number from the user
def get_column_number(choice):
    while True:
        try:
            number = int(input(f'(Choice {choice}) Which column number would you like to select: '))
            # Check the user input for error and incorrect character type
            if 1 <= number <= tile_size:
                return number
            else:
                print("I've lost my mojo - Austin")
                print(f'Please enter a valid number from 1-{tile_size}.\n')
        except ValueError:
            print("I've lost my mojo - Austin")
            print(f'Please enter a valid number from 1-{tile_size}.\n')
            
# Welcome message and instructions for the game
austins_face()
print("Welcome to Austin Powers' (UNOFFICIAL) Groovy Memory Game!\nEmbark on a shagadelic journey to master the art of concentration and memory skills in this swinging matching game, designed to train future International Men of Mystery.")
print("\nObjective:\nIn Austin's Groovy Memory Game, your goal is to uncover pairs of characters within a hip grid. Match these pairs while sharpening your mojo-filled memory.")
print("\nGameplay:\nIdentify two cells by specifying their row letter and column number (e.g., Select cell A2).\nIf the cells match (i.e., they have the same mojo), keep the pair and take another turn.")
print("If the cells don't match, concentrate, remember the characters' placements, and choose another set of cells to continue your groovy training.")
print("The game progresses until all pairs of characters are successfully matched.\n")
# Section for the user to choose the level of difficulty
while True:
    try:
        tile_size = str(input('Choose a level of difficulty (difficulties: easy, medium, hard, groovy): '))
        # Setup the grid size based on the difficulty the user inputs
        start_time = time.time()  
        if tile_size == 'easy':
            tile_size = 2
            print("I won’t bite… hard - Austin")
            print('\n')
            break
        elif tile_size == 'medium':
            tile_size = 4
            print("Shagadelic, Baby - Austin")
            print('\n')
            break
        elif tile_size == 'hard':
            tile_size = 6
            print("That's a man, Baby - Austin")
            print('\n')
            break
        elif tile_size == 'groovy':
            tile_size = 8
            print("Groovy Baby! - Austin")
            print('\n')
            break
        else: 
            print("If you have an issue, here's a tissue - Austin")
            print('Please enter a valid level of difficulty (difficulties: easy, medium, hard, gamer).\n')
    except ValueError:
        print("If you have an issue, here's a tissue - Austin")
        print('Please enter a valid level of difficulty (difficulties: easy, medium, hard, gamer).\n')
        
# Creation of the game grid and variables
ogTile = [['# ' for x in range(tile_size)] for y in range(tile_size)]
changingTile = [['# ' for j in range(tile_size)] for k in range(tile_size)]
random_tile = create_random_grid(tile_size)
usedCoords = []
print_tile(ogTile)
blanks = 0

# This is the main game loop 
# The program stops once it is broken out of
while True:
    # Section to check for the end of the game and to record the users time.
    if blanks >= (tile_size**2):
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('\n')
        print_tile(changingTile)
        print('\n')
        

        try:
            bestSave = open("save.txt", "r")
            """
            bestEasy = open("easy.txt", "r")
            bestMedium = open("medium.txt", "r")
            bestHard = open("hard.txt", "r")
            bestGroovy = open("groovy.txt", "r")
            """
            best_save = bestSave.read().split(",")
            if best_save[0] == "":
                raise FileNotFoundError
            best_easy_content = best_save[0]
            best_medium_content = best_save[1]
            best_hard_content = best_save[2]
            best_groovy_content = best_save[3]
            """
            best_easy_content = bestEasy.read().split(",")
            best_medium_content = bestMedium.read()
            best_hard_content = bestHard.read()
            best_groovy_content = bestGroovy.read()
            """

        except FileNotFoundError:
            bestSave = open("save.txt", "a+")
            """
            bestEasy = open("easy.txt", "a+")
            bestMedium = open("medium.txt", "a+")
            bestHard = open("hard.txt", "a+")
            bestGroovy = open("groovy.txt", "a+")
            """
            
            bestSave.close()
            best_save = [3.6195948123931885,99,99,99]
            
            best_easy_content = best_save[0]
            best_medium_content = best_save[1]
            best_hard_content = best_save[2]
            best_groovy_content = best_save[3]
            
            """
            bestEasy.close()
            bestMedium.close()
            bestHard.close()
            bestGroovy.close()
            """

        """
        bestEasy.close()
        bestMedium.close()
        bestHard.close()
        bestGroovy.close()
        """
        bestSave.close()
        
        """
        bestEasy = open("easy.txt", "w")
        bestMedium = open("medium.txt", "w")
        bestHard = open("hard.txt", "w")
        bestGroovy = open("groovy.txt", "w")
        """
        bestSave = open("save.txt","w")

        if tile_size == 2 and (elapsed_time < float(best_easy_content)):
            best_easy_content = elapsed_time  
        if tile_size == 4 and (elapsed_time < float(best_medium_content)):
            best_medium_content = elapsed_time
        if tile_size == 6 and (elapsed_time < float(best_hard_content)):
            best_hard_content = elapsed_time
        if tile_size == 8 and (elapsed_time < float(best_groovy_content)):
            best_groovy_content = elapsed_time

        
        if tile_size == 2:
            print(f"Groovy Baby! THE END | Final Time: {elapsed_time} | Fastest Time: {best_easy_content} secs")
        if tile_size == 4:
            print(f"Groovy Baby! THE END | Final Time: {elapsed_time} | Fastest Time: {best_medium_content} secs")
        if tile_size == 6:
            print(f"Groovy Baby! THE END | Final Time: {elapsed_time} | Fastest Time: {best_hard_content} secs")
        if tile_size == 8:
            print(f"Groovy Baby! THE END | Final Time: {elapsed_time} | Fastest Time: {best_groovy_content} secs")
        
        """
        bestEasy.close()
        bestMedium.close()
        bestHard.close()
        bestGroovy.close()
        """
        bestSave.write(f"{best_easy_content},{best_medium_content},{best_hard_content},{best_groovy_content}")
        bestSave.close()
        
        break
    
# User input section to select coords of the grid and reveal characters
    letter1 = get_row_letter(1)
    number1 = get_column_number(1)
    
    letter2 = get_row_letter(2)
    number2 = get_column_number(2)
    
    firstCoord = letter1 + str(number1)
    secondCoord = letter2 + str(number2)

# Section to check if selected pairs match and update the game grid
    if letter1 == letter2 and number1 == number2:
        print("Ouch! That stings - Austin")
        print(f'You have selected the same tile ({letter1}{number1}) already. Please try again.\n')

    else:  

        if number1 == 1 and number2 == 1:
            if changingTile[ord(letter1)-97][(number1-1)*2] == '  ' or changingTile[ord(letter2)-97][(number2-1)*2] == '  ':
                print("Ouch! That stings - Austin")
                print("Unable to select coords, as you have already matched at least one of these two.")
                print_tile(changingTile)

            else:
                changingTile[ord(letter1)-97][(number1-1)*2] = random_tile[ord(letter1)-97][(number1-1)*2]
                changingTile[ord(letter2)-97][(number2-1)*2] = random_tile[ord(letter2)-97][(number2-1)*2]
                
                if changingTile[ord(letter1)-97][(number1-1)*2] == changingTile[ord(letter2)-97][(number2-1)*2]:
                    print('\n'*20)
                    print("MATCH!!!")
                    print('\n')
                    print_tile(changingTile)
                    changingTile[ord(letter1)-97][(number1-1)*2] = '  '
                    changingTile[ord(letter2)-97][(number2-1)*2] = '  '
                    blanks += 2

                else:   
                    print('\n'*20)
                    print("NO MATCH")
                    print('\n')
                    print_tile(changingTile)
                    changingTile[ord(letter1)-97][(number1-1)*2] = ogTile[ord(letter1)-97][(number1-1)*2]
                    changingTile[ord(letter2)-97][(number2-1)*2] = ogTile[ord(letter2)-97][(number2-1)*2]

        else:
            if changingTile[ord(letter1)-97][(number1-1)] == '  ' or changingTile[ord(letter2)-97][(number2-1)] == '  ':
                print("Ouch! That stings - Austin")
                print("Unable to select coords, as you have already matched at least one of these two.")
                print_tile(changingTile)

            else:
                changingTile[ord(letter1)-97][(number1-1)] = random_tile[ord(letter1)-97][(number1-1)]
                changingTile[ord(letter2)-97][(number2-1)] = random_tile[ord(letter2)-97][(number2-1)]
                
                if changingTile[ord(letter1)-97][(number1-1)] == changingTile[ord(letter2)-97][(number2-1)]:
                    print('\n'*20)
                    print("MATCH!!!")
                    print('\n')
                    print_tile(changingTile)
                    changingTile[ord(letter1)-97][(number1-1)] = '  '
                    changingTile[ord(letter2)-97][(number2-1)] = '  '
                    blanks += 2

                else:
                    print('\n'*20)
                    print("NO MATCH")
                    print('\n')
                    print_tile(changingTile)
                    changingTile[ord(letter1)-97][(number1-1)] = ogTile[ord(letter1)-97][(number1-1)]
                    changingTile[ord(letter2)-97][(number2-1)] = ogTile[ord(letter2)-97][(number2-1)]
        

        usedCoords.append(firstCoord)
        usedCoords.append(secondCoord)
        
        





