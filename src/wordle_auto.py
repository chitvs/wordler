# Wordler -- A Python Wordle solver
#
# MIT License
#
# Copyright (c) 2024 Alessandro Chitarrini
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json

def load_word_list(filename):
    # Load a list of 5-letter words from a file.
    with open(filename, 'r') as file:
        words = [line.strip().lower() for line in file if len(line.strip()) == 5]
    return words

def filter_words(input_list, feedback, current_guess):
    # Filter words based on feedback for each letter and position.
    output = input_list
    for i, f in enumerate(feedback):
        if f == 'g':
            output = [word for word in output if word[i] == current_guess[i]]
        elif f == 'y':
            output = [word for word in output if current_guess[i] in word and word[i] != current_guess[i]]
        elif f == 'b':
            output = [word for word in output if current_guess[i] not in word or current_guess.count(current_guess[i]) > word.count(current_guess[i])]
    return output
    
def solutions():
    # Load all solutions from 'solutions.txt'
    with open('data/solutions.txt', 'r') as file:
        solutions = [line.strip().split()[0].lower() for line in file]
    return solutions

def generate_feedback(solution, guess):
    # Generate feedback based on the comparison between solution and guess.
    feedback = []
    for s, g in zip(solution, guess):
        if s == g:
            feedback.append('g')
        elif g in solution:
            feedback.append('y')
        else:
            feedback.append('b')
    return ''.join(feedback)

def find_best_guess(possible, data):
    # Find the best guess based on frequency map.
    max_value = float('-inf')
    best_guess = None
    for word in possible:
        if data.get(word, 0) > max_value:
            max_value = data[word]
            best_guess = word
    return best_guess

def wordle_solver_auto(solution, allowed_words, data):
    # Solve Wordle for a single solution with automatic feedback generation.
    possible = allowed_words[:]
    guess = []  # Initialize an empty list for guesses
    result = False
    guess_number = 0
    total_guesses = 0
    
    while not result:
        if guess_number == 0:
            current_guess = "crane"  # Initial guess
        else:
            current_guess = guess[-1]  # Use the last guess
        
        guess.append(current_guess)  # Add the current guess to the list
        print(f"Guess {guess_number + 1} for '{solution}': {current_guess}")
        
        feedback = generate_feedback(solution, current_guess)
        print("Automatically generated feedback:", feedback)
        
        if feedback == "ggggg":
            print(f"Solution '{solution}' solved in {guess_number + 1} guesses.")
            result = True
        else:
            possible = filter_words(possible, feedback, current_guess)
        
        next_guess = find_best_guess(possible, data)
        guess.append(next_guess)
        guess_number += 1
    
    return guess_number + 1

def run_all_solutions_auto():
    # Run the solver for all possible solutions with automatic feedback generation.
    solutions_list = solutions()
    allowed_words = load_word_list('data/allowed_words.txt')
    words_guessed = 0
    with open('data/freq_map.json', 'r') as file:
        data = json.load(file)
    
    total_guesses = 0
    num_solutions = len(solutions_list)
    
    for solution in solutions_list:
        guesses = wordle_solver_auto(solution, allowed_words, data)
        total_guesses += guesses
        if guesses <= 6:
        	words_guessed += 1
    
    average_guesses = total_guesses / num_solutions
    print(f"Average number of guesses: {average_guesses:.2f}")
    print(f"words guessed: {words_guessed}/{num_solutions}")

if __name__ == "__main__":
    run_all_solutions_auto()

