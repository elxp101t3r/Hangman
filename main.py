import hangman_art as art
import hangman_words as word
import random as r
chosen_word = r.choice(word.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(art.logo)
print(f'Pssst, the solution is {chosen_word}')