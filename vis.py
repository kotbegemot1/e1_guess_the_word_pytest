def random_word():
	from random import choice
	return choice(['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage'])

def secret_word(word):
    return " ".join("_" * len(word))

def open_secret_word(msg, word):
	return " ".join(w if w==msg else "_" for w in word )

def merger(x_word, x_word_new):
	finale_word = ""
	for i in range(len(x_word)):
		if x_word[i] == x_word_new[i]:
			finale_word += x_word_new[i]
		elif x_word[i] != '_':
			finale_word += x_word[i]
		else:
			finale_word += x_word_new[i]
	return finale_word


if __name__ == '__main__':
	word = random_word()
	x_word = secret_word(word)
	print(f"Здравствуйте, вы на игре Угадай слово. Загаданное слово состоит из {len(word)} букв.")
	print("У вас есть право 4 раза ошибиться") 
	i = 0 
	while i!=4:
		print(f"\n\nОшибок - {i}")
		msg = input("Введите букву: ")
		msg = msg.lower()
		if msg in word:
			x_word_new = open_secret_word(msg, word)
			finale_word = merger(x_word,x_word_new)
			print(f"\nТакая буква есть в слове!\n{finale_word}")
			x_word = finale_word
			if '_' not in x_word:
				print("\nВы победили!")
				break
		else:
			print("Вы ошиблись!")
			i += 1
			if i == 4:
				print("\nИгра окончена")

	
