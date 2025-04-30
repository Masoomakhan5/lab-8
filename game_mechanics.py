#---------------------------------------

#---------------------------------------
#  Game Mechanics
#    Student A (team lead) MASOOMA KHAN
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    print(" ============ ")
    print(" hello player" )
    print(" your game begins now" )
    print(" solve mazes and win game ")
    print(" ============ ")
    
    
    #------------------------
#---------------------------------------
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    print("Choose a category:")

    for i in range (len(categories)):
        print(str(i + 1) + ". " + categories[i])

    while True:
        choice_str = input("enter a name ")
        if choice_str.isdigit():
            choice_num = int(choice_str)
            if 1 <= choice_num <= len(categories):
                return categories[choice_num - 1]
            else:
                print("the nummber is not in list, try again")
        else:
            print("enter a number")
    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    print("----------")
    print("round", round_number)
    print("score", score)
    print("----------")
    #------------------------
    
    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    print("==========")
    print(" Game Over ")
    print("thanks for playing")
    print("Your final score is:", final_score)
    print("==============================")
    #------------------------

    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    score = 0

    for round_number in range(1, 6):
        print("Round", round_number)
        
        category = choose_category(categories)
        print("You chose:", category)

        answer = input("Did you answer the question correctly? (yes/no): ")

        if answer.lower() == "yes":
            score = score + 1
            print("Correct! You get 1 point.")
        else:
            print("Wrong answer. No points this time.")

        display_score(score, round_number)

    game_over_message(score)
    #------------------------
    r
    #------------------------

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    if player_answer.lower() == correct_answer.lower():
        return True
    else:
        return False
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    if correct:
        score += 1  
    return score

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    if incorrect_answers >= 3:
        return True  
    else:
        return False
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    player_choice = input("Would you like to play again? (yes/no): ").lower()

    if player_choice == "yes":
        print("start a new game")
        
    elif player_choice == "no":
        print("goodbye! go to hell")
        
    else:
        print("pleasse enter 'yes' or 'no'")
        restart_or_exit() 

