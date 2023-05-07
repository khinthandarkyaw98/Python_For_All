from Input import Input
from Process import Process


words = ["apple", "orange", "pineapple", "strawberry", "grape"]
process = Process(words)
#generated_word, word_length = process.generate_words()

#print(generated_word, word_length)
guess = Input(process.words)
guess.user_input()
