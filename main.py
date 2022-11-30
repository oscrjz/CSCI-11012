
import re 
import random 

# Get the answer.
pool_file = open("hangman-sample-answer-pool.txt")

pool_answers = []

pool_answer_line = pool_file.readline()

while pool_answer_line:
    pool_answers.append(pool_answer_line)
    
    pool_answer_line = pool_file.readline()

answer = random.choice(pool_answers)

answer = answer.upper()

# Pre-game setup.
answer_guessed = []

for current_answer_character in answer: 
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

# Game logic.
num_of_incorrect_guesses = 5 

current_incorrect_guesses = 0 

letters_guessed = []

# let user play the game.
while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guessed: 
    # Display game status.
    print(f"Number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}")

    print("Letters guessed: ", end="")

    for current_letter_guessed in letters_guessed:
        print(current_letter_guessed, end=" ")

    print()

    # Display puzzle board.
    for current_answer_index in range(len(answer)):
        if answer_guessed[current_answer_index]:
            print(answer[current_answer_index], end="")
        else:
            print("_", end="")
    
    print()

    # Let the user guess a letter.
    letter = input("Enter a letter: ")
    
letter = letter.upper()
    
    # Check is user entered a valid letter.
if re.search("^[A-Z]$", letter) and len(letter) == 1 and letter not in letters_guessed:
    # Insert letter guessed (insertion sort)
    current_letter_index = 0

    for current_letter_guessed in letters_guessed:
        if letter < current_letter_guessed:
            break

        current_letter_index += 1
    
    letters_guessed.insert(current_letter_index, letter)

    # Check if letter is in the puzzle.
    if letter in answer:
        for current_answer_index in range(len(answer)):
            if letter == answer[current_answer_index]:
                answer_guessed[current_answer_index] = True
    else:
        current_incorrect_guesses += 1
    
# Post-game summary.
if current_incorrect_guesses < num_of_incorrect_guesses:
    print("Congrats, you won!")
else:
    print(f"Sorry, you lost. The answer was {answer}")



=======
import pygame

pygame.init()

#Game settings. 
monitor_display = (800, 600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank Domination")

system_clock = pygame.time.Clock()

game_characteristics = {
    "sky":{
        "color": (135, 206, 235)
    }, 
    "grass":{
        "color": (0,255,0),
        "position": {
            "y": 0.8 * monitor_display[1]
        }
    }
}

game_running_flag = True 

while game_running_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            game_running_flag = False

    if not game_running_flag: 
        pygame.quit()

        break 

    # Running the game. 
    game_display.fill(game_characteristics["sky"]["color"])

    # Create grass.
    pygame.draw.rect(game_display, game_characteristics["grass"]["color"], pygame.Rect(0, game_characteristics["grass"]["position"]["y"], monitor_display[0], monitor_display[1] - game_characteristics["grass"]["position"]["y"]))

    pygame.display.update()

    system_clock.tick(30)

