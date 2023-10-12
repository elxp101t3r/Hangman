import hangman_art as art
import hangman_words as word
import random as r
chosen_word = r.choice(word.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(art.logo)
print(f'Pssst, the solution is {chosen_word}')
display = []
for _ in range(word_length):
    display += '_'
while not end_of_game:
    guess = input('Guess a letter: ').lower()
    for i in display:
        if guess == i:
            print(f'You already guess {i}')
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print('The letter is not in the word..')
        lives -= 1
        
        if lives == 0:
            end_of_game = True
            print('You lose.')
    print(f'{" ".join(display)}')
    if '_' not in display:
        end_of_game = True
        print('You win.')
    print(art.stages[lives])