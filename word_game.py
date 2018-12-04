import os
import random

class View:

	def ask(self, prompt):
		query = "{}>> ".format(prompt)
		answer = input(query)
		return answer
	
	def say(self, msg):
		print(msg)


class GuessGame:

	def __init__(self):
		self.random_word = self.get_random_word()
		self.current_word_state = self.convert_word_to_symbols(self.random_word)
		
	def get_random_word(self, file = 'words.txt'):
		try:
			contents = open(file)
			word_list = []
			max = len(word_list) -1
			for word in contents:
				word_list.append(word.strip())
			max = len(word_list) -1
			word_num = random.randint(0, max)
			secret_word =  word_list[word_num]
			return secret_word
		except:
			print('Could not open file: {}'.format(file))
			return False

	def convert_word_to_symbols(self, random_word):
		new_word = ''
		for aletter in random_word:
			new_word += '*'
		return new_word
	
	def get_secretword_length(self):
		return len(self.random_word)

	def check_guess(self, guess):
		if len(guess) > 1:
			return self.has_won(guess)
		else:
			word = self.update_word(guess)
			return self.has_won(word)
			

	def update_word(self, letter):
		current_word = self.current_word_state
		secret_word = self.random_word
		new_word = ''
		x = 0
		for a_letter in current_word:
			if secret_word[x] == letter:
				new_word += letter
			else:
				new_word += current_word[x]
			x += 1
		self.current_word_state = new_word
		return new_word
		
	def has_won(self, word = ''):
		if word == '':
			word = self.current_word_state
		if self.random_word == word : 
			self.current_word_state = word
			return True
		else : return False


class Controller:
	
	def do_stuff(self):
		view = View()
		count = 0
		playagain = 'y'
		while playagain == 'y':
			game = GuessGame()
			view.say("The word comprises {} letters".format(game.get_secretword_length()))
			while game.has_won() == False:
				count +=1
				view.say(game.current_word_state)
				guess = view.ask("Guess a letter/word")
				if game.check_guess(guess):
					view.say("Well done, you guessed the secret word '{}' in {} goes!".format(game.random_word, count))
					playagain = view.ask('Do you want to play again (y/n) ') 
					count = 0
		
def main():
	control = Controller()
	control.do_stuff()
	
if __name__ == '__main__' : main()
