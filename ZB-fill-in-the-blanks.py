# IPND Stage 3 Final Project

#Quiz questions and answers, using the same format as example provided by Udacity.
easy_quiz = "Sheldon and ___1___ live in an apartment across the hall from ___2___, who works at The ___3___ Factory. They all live in Pasadena, ___4___."
answers_easy = ["Leonard", "Penny", "Cheesecake", "California"]

medium_quiz = "Sheldon, Raj and Leonard are ___1___ and work at a university called ___2___. Howard also works at the university, and is ridiculed for being an ___3___. Howard has a Master's Degree from ___4___."
answers_medium = ["physicists", "Caltech", "engineer", "MIT"]

hard_quiz = "Howard has a half-brother called ___1___. Leonard's middle name is ___2___. Raj's sister is called ___3___. Sheldon's middle name is ___4___."
answers_hard = ["Josh", "Leakey", "Priya", "Lee"]

blanks = ["___1___", "___2___", "___3___", "___4___"]

def user_guesses():
	'''
		1. Behaviour/functionality: Captures the number of attempts the user would like and stores it for use in the play_game function.
		2. Inputs: The number of guesses the user would like for each incorrect answer.
		3. Outputs: Stores the number of guesses for use in the play_game function, or prompts for a valid selection.
	'''
	guesses = int(raw_input("Please type in the number of guesses you would like: "))
	if guesses <= 0:
		print "Whoops, that isn't a valid selection. Please try again."
		guesses = user_guesses()
	return guesses
		
def replay():
	'''
		1. Behaviour/functionality: Asks the player if they would like to play again, and, if so, restarts the game.
		2. Inputs: Whether or not the player wants to replay (yes or no).
		3. Outputs: Calls set_difficulty to restart the game, or prints a thank you message.
	'''
	replay = raw_input("Would you like to play again? yes or no.")
	if replay == "yes":
		set_difficulty()
	else:
		print "Thanks for playing. See you soon!"


def set_difficulty():
	'''
		1. Behaviour/functionality: Takes in user's level selection and either starts the game with requested level and answers, 
		or gives a warning message and restarts the level selection loop.
		2. Inputs: Chosen difficulty level (easy, medium or hard)
		3. Outputs: Calls the play_game function with the selected question and answer set, or prints warning message and restarts the loop.
	'''
	print "Welcome to the Big Bang Theory Quiz."
	level_selection = raw_input("Please select a difficulty: 'easy', 'medium', or 'hard': ")
	if level_selection == "easy":
		play_game(easy_quiz, blanks, answers_easy)
	elif level_selection == "medium":
		play_game(medium_quiz, blanks, answers_medium)
	elif level_selection == "hard":
		play_game(hard_quiz, blanks, answers_hard)
	else:
		print "Please choose a valid level."
		set_difficulty()


def play_game(quiz_level, blanks, answer_level):
	'''
		1. Behaviour/functionality: Runs game by printing quiz question at selected difficulty, prompting for answer. If correct, returns question with correct answer filled in. 
		Position marker moves along for "blanks" and for "answer_level" to move on to the next question.
		If incorrect and user has guesses left, asks question again. If user has no guesses left, game ends.
		2. Inputs: quiz_level (easy, medium or hard), blanks, answer_level, position (position index in blanks and answer_level, to ensure the answer is going in the correct blank), 
		count (to keep track of number of attempts compared to requested guesses).
		3. Outputs: Congratulatory message and quiz question with correct answers filled in. Increased count number.
		Message if player has run out of guesses.
	'''
	guesses = user_guesses()
	print quiz_level
	position = 0
	count = 1
	while position<len(blanks):
		user_answer = raw_input("What is the answer to: " + blanks[position] + "?")
		if user_answer == answer_level[position]:
			print "Well done, that is correct."
			quiz_level = quiz_level.replace(blanks[position], user_answer)
			print quiz_level
			position += 1
		elif count != guesses:
				count += 1
				print "Please try again."
		else:
			print "Sorry you are out of guesses."
			return position

set_difficulty()
replay()

