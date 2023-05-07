import random 

class Process:
    def __init__(self, words) -> None:
        self.words = words
        
    def generate_words(self) -> tuple[str,int,int]:
        random_word = random.choice(self.words)
        word_length = len(random_word)
        # count non-repeated characters
        num_unique_chars = len(set(random_word))
        return random_word, word_length, num_unique_chars
        
