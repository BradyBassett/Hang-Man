#imports 
import random
import time

#Variables
playAgain = True
playAgainInput = ""
correctResponses = ["y", "n"]

#Hangman Function
def Hangman():
	#Importing wordlist and formatting 
	def getWordList():
		#Importing list
		#variables
		convertedWordList = []

		f = open("wordlist.txt", "r")
		wordList = f.readlines()
		f.close()

		#Formating list
		wordList = list(wordList)
		for element in wordList:
			element.lower()
			convertedWordList.append(element.strip())
		return convertedWordList

	#Checks wordlist to find the min word length
	def getMinWord(wordList):
		#variables
		minLength = 2147483648

		#find min length
		for i in range(len(wordList)):
			currentWordLength = len(wordList[i])
			if currentWordLength < minLength:
				minLength = len(wordList[i])
		return minLength

	#Checks wordlist to find the max word length
	def getMaxWord(wordList):
		#variables
		maxLength = -2147483648
		
		#find min length
		for i in range(len(wordList)):
			currentWordLength = len(wordList[i])
			if currentWordLength > maxLength:
				maxLength = len(wordList[i])
		return maxLength
	#=============================================================================================================================
	#=============================================================================================================================
	#Variables
	wordList = getWordList()
	minWordLength = getMinWord(wordList)
	maxWordLength = getMaxWord(wordList)
	#=============================================================================================================================
	#=============================================================================================================================
	#Gets usr input for number of attemtps and checks if is an integer between 1 and 25
	def getNumAttempts():
		while True:
			numAttempts = input("How many incorrect attempts would you like? [1-25]: ")
			try:	
				numAttempts = int(numAttempts)
				if 1 <= numAttempts <= 25:
					return numAttempts
				else:
					print("{0} is not between 1 and 25".format(numAttempts))
			except ValueError:
				print("{0} is not an integer between 1 and 25".format(numAttempts))

	#Gets usr input for minimum length of word and checks if it is an integer between the shortest word and the longest word in the list
	def getMinLength(minWordLength, maxWordLength):
		while True:
			minLength = input("What minimum word length would you like? [{0}-{1}]: ".format(minWordLength, maxWordLength))
			try:
				minLength = int(minLength)
				if minWordLength <= minLength <= maxWordLength:
					return minLength
				else:
					print("{0} is not between {1} and {2}".format(minLength, minWordLength, maxWordLength))
			except ValueError:
				print("{0} is not an integer between {1} and {2}".format(minLength, minWordLength, maxWordLength))

	#Adjusts list to adhere to minLength and randomly selects a word from the adjusted list
	def getRandomWord(wordList, minLength):
		#Variables
		adjWordList = []
		position = 0
		word = ""

		#Adjusting list according to minLength
		for i in range(len(wordList)):
			if len(wordList[i]) >= minLength:
				adjWordList.append(wordList[i])

		#Finding a random word within random list
		position = random.randint(0, len(adjWordList))
		word = adjWordList[position]

		return word
	#=============================================================================================================================
	#=============================================================================================================================
	#Program Start
	print("Starting a game of Hangman...")
	time.sleep(1)

	numAttempts = getNumAttempts()
	minLength = getMinLength(minWordLength, maxWordLength)

	print("Selecting a word...")
	word = getRandomWord(wordList, minLength)
	time.sleep(random.uniform(0.25, 2.0))
	#=============================================================================================================================
	#=============================================================================================================================
	#Guessing Loop
	def guessTheWord(word, numAttempts):
		#Checking guess input and putting it to lowercase if needed
		def inputGuess():
			while True:
					guess = input("What is your guess?: ")
					guess = guess.lower()
					try:
						guess = str(guess)
						if guess.isalpha():
							if len(guess) == 1:
								return guess
							else:
								print("{0} is not a valid guess [a-z]".format(guess))
						else:
							print("{0} is not a valid guess [a-z]".format(guess))
					except ValueError:
						print("{0} is not a valid guess [a-z]".format(guess))		

		#variables
		remainingAttempts = numAttempts
		wordLength = len(word)
		wordArray = list(word)
		uncoveredWord = wordLength * "*"
		uncoveredWordArray = list(uncoveredWord)
		previousGuesses = ""

		#Guessing loop until attempts are out or word is sovled
		while "*" in uncoveredWord and remainingAttempts != 0:
			print("\nWord: {0}".format(uncoveredWord))
			print("Attempts Remaining: {0}".format(remainingAttempts))
			print("Previous Guesses: {0}".format(previousGuesses))
			guess = inputGuess()
			#Checking if the guess is correct, incorrect, or the same
			if guess in previousGuesses:
				print("{0} has been guessed before".format(guess))
			elif guess in wordArray:
				for i in range(len(wordArray)):
					if guess == wordArray[i]:
						uncoveredWordArray[i] = guess
						uncoveredWord = ''.join(uncoveredWordArray)
						if guess not in previousGuesses:	
							previousGuesses += (guess + " ")
							print("{0} is in the word!".format(guess))
			elif guess not in wordArray:
				remainingAttempts -= 1
				if guess not in previousGuesses:
					previousGuesses += (guess + " ")
					print("{0} is NOT in the word!".format(guess))

		if "*" not in uncoveredWord:
			print("\nCongratulations, you have found the word!\nThe word was {0}".format(word))
		elif remainingAttempts == 0:
			print("\nUnfortunately you have run out of attempts...\nThe word was {0}".format(word))

	guessTheWord(word, numAttempts)
#=============================================================================================================================
#=============================================================================================================================
#running main function
while playAgain == True:
	Hangman()
	playAgainInput = input("\nWould you like to play again? [y/n]: ")
	playAgainInput.lower()
	while playAgainInput not in correctResponses:
		playAgainInput = input("Please enter a valid response [y/n]")
	if playAgainInput == "y":
		playAgain = True
	elif playAgainInput == "n":
		playAgain = False

print("\nThanks for playing my Hangman game!")