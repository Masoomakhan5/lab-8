#---------------------------------------
#  Question Bank
#    Student b MASOOMA KHAN 
#---------------------------------------
import random
# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        # Add more questions as tuples (question, answer)
    ],
    "Math": [
        ("What is 2 + 2?", "4"),
        ("What is 3 + 5?", "8"),
    ],
    "History": [
        ("Who was the first U.S. president?", "George Washington"),
        ("When did World War II end?", "1945"),
    ],
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    if category in questions:
        question, answer = random.choice(questions[category])
        return question,answer
    else:
        return "Category not found, "

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    if player_answer.lower() == correct_answer.lower():
        return True
    else:
        return False
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    if category in question: 
        for q, a in questions[category]:  
            if q == question:  
                questions[category].remove((q, a))  
                print(f"The question '{question}' has been removed.")
                return  
        print("Question not found.")
    else:
        print("Category not found.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    print(question)
    player_answer = input("your answer")
    return player_answer

   
#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    if category == "science" and question == "what is water made of?":
        return "hint: it is made of hydrogen and oxygen"
    
    if category == "maths" and question == "what is 1 + 1?":
        return "Hint: it is additon of two numbers"

    if category == "history" and question == "who was prime minister os pakistan?":
        return "Hint: he is in jail now"
    
    return "no hints avaliable"
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    print("the correct answer is:", correct_answer)




