from Process import Process

class Input(Process):
    def __init__(self, words) -> None:
        super().__init__(words)
    
    def user_input(self):
        yes_or_no = "y"
        while yes_or_no == "y":
            guess_index = []
            word, word_length, num_unique_chars = self.generate_words()
            random_word = word
            hint = "*" * word_length
            guess_history = []
            missed_count = 0
            while num_unique_chars > 0: # count is number of unique characters in random_word
                while True: # keep asking for non-empty input, otherwise, it is hard to calculate missed_count for empty input
                    try:
                        guess = input(f"(Guess) Enter a letter in word {hint} > ") 
                        if guess == "":
                            raise ValueError("Empty input is not allowed!")
                        break
                    except ValueError as ve:
                        print(ve)
                if guess in guess_history:
                    print(f"{guess} is already in the word")
                if guess != "": # skip empty input being appended
                    guess_history.append(guess)
                if guess in word:
                    # we must loop according to word.count(guess)
                    # otherwise, -1 will be included in guess_index[]
                    # we only want the position of found 
                    # we do not want the position of unfound
                    for _ in range(word.count(guess)):
                        guess_idx= word.find(guess)
                        guess_index.append(guess_idx)
                        # let'say word = "aba", guess is "a", so we have 2 "a"s
                        # the first "a" is found by find()
                        # to find the second "a", we need to ignore the first "a"
                        # so we take it out by doing the followings
                        word = word[:guess_idx] + " " + word[guess_idx+1:]
                    # string is immutable in python
                    # to convert the element of the string 
                    # convert it to list
                    hint = list(hint)
                    # guess_index = [0, 2] for "aba"
                    for j in guess_index:
                        hint[j] = guess
                    # what we want is string
                    # reconvert it to the string again
                    hint = "".join(hint)
                    # clean the guess_idx
                    guess_index = []
                    # convert to the original word version
                    word = random_word
                else:
                    print(f"{guess} is not in the word")
                    missed_count +=1
                num_unique_chars -=1
            print("The word is {}. You missed {}{}.".format(word, missed_count, " times" if missed_count > 1 else " time"))
            yes_or_no = input("Do you want to guess another word? Enter y or n > ")