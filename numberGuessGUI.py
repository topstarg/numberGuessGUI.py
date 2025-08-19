"""
Program: numberGuessGUI.py
case study
8/15/2025

***NOTE: the Python module breezypythongui.py MUST be in the same directory as this file for the app to run properly!

GUI-based version of the number guessing game app from chapter 3
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
import random
# Other imports can go here

# Class Header (class name will change project to project)
class GuessingGames(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		"""Sets up the window and the widgets."""
		# Call to the EasyFrame class constructor
		EasyFrame.__init__(self, title = "Guessing Game 2.0", width = 240, height = 160, background = "ivory3")
		# Create the instance variables for this class
		self.mynumber = random.randint(1, 100)
		self.count = 0
		# Add the widgets to that EasyFrame window
		self.hintLabel = self.addLabel(text = "Guess a number Between 1 and 100", row = 0, column = 0, columnspan = 2, sticky = "NEWS", background = "ivory3")
		self.addLabel(text = "Your Guess: ", row = 1, column = 0, background = "ivory3")
		self.guessField = self.addIntegerField(value = 0, row = 1, column = 1,)
		# Bind additional key to the input that can also trigger nextGuess()
		self.guessField.bind("<Return>", lambda event: self.nextGuess())
		self.guessField.bind("<space>", lambda event: self.nextGuess())		
		self.guessField.focus_set()

		self.nextButton = self.addButton(text = "Guess", row = 2, column = 0, command = self.nextGuess)
		self.newButton = self.addButton(text = "New Game", row = 2, column = 1, state = "disabled", command = self.newGame)
		self.nextButton["background"] = "lightgreen"
		
	# Definition of the nextGuess() method which handles the next button click
	def nextGuess(self):
		self.count += 1
		# Grab the user input from the integer field
		guess = self.guessField.getNumber()
		# Logic that determines the games outcome
		if guess == self.mynumber:
			self.hintLabel["text"] = f"Correct! You guessed it in {self.count} attempt(s)."
			self.nextButton["state"] = "disabled"
			self.newButton["state"] = "normal"
		elif guess < self.mynumber:
			self.hintLabel["text"] = "Sorry! Your guess was too low."
		else:
			self.hintLabel["text"] = "Whoops! Your guess was too high."
            
# Definition of the newGame() method which handles the "new game" button click
	def newGame(self):   
		self.mynumber = random.randint(1, 100)
		self.count = 0
		self.hintLabel["text"] = "Guess a number Between 1 and 100"
		self.guessField.setNumber(0)
		self.nextButton["state"] = "normal"
		self.newButton["state"] = "disabled"

# End of class block

# Global definition of the main() function
def main():
	# Instantiate an object from the class into mainloop()
	GuessingGames().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':

	main()
