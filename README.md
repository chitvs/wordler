# Wordle Solver

This project contains a Python program to solve the popular word game Wordle. The solver uses strategic guessing and feedback processing to efficiently narrow down the list of possible solutions, aiming to solve the puzzle in the fewest possible guesses. 

## Features

- **Strategic Initial Guess**: Starts with an optimal guess to cover common letters.
- **Feedback Processing**: Filters the list of possible words based on feedback from guesses.
- **Best Guess Selection**: Uses letter frequencies to select the next guess that maximizes information gain.
- **Simulation Mode**: Runs the solver on all possible Wordle solutions to evaluate its performance.

## Optimization

This program can be further optimized based on the input data by calculating the entropy after each guess. By selecting the guess that maximizes the information gain (reduces uncertainty the most), the solver can improve its efficiency. This approach is inspired by the video ["Solving Wordle Using Information Theory"](https://www.youtube.com/watch?v=v68zYyaEmEA) by 3Blue1Brown, which explains the concepts of entropy and information theory in the context of solving Wordle.

## Requirements

- Python 3.6+
- JSON file containing a frequency map (`freq_map.json`)
- Text file containing allowed words (`allowed_words.txt`).

## Files

- `wordle.py`: The main program file containing the Wordle solver logic.
- `wordle_auto.py`: The main program where you can run tests on past games.
- `allowed_words.txt`: List of all allowed 5-letter words.
- `possible_words.txt`: List of 5-letter words with more probability to be the solution.
- `nyt_words.txt`: List of NYT wordle allowed words.
- `solutions.txt`: List of all possible solutions.
- `freq_map.json`: JSON file with word frequency data used to score guesses.
- Other data files: Additional files can be added to enhance the solver's efficiency by providing more information for guess optimization.

## Usage

### Running the Solver

To run the solver for a single interactive session:

```sh
python3 wordle.py
```

The program will prompt you to enter feedback for each guess in the form of `g` (green), `y` (yellow), and `b` (black).

![Example:](wordle.gif)

### Running Simulations

To run the solver on all possible Wordle solutions and evaluate performance:

```sh
python3 wordle_auto.py
```

This will simulate solving the puzzle for each word in `allowed_words.txt` and print the number of guesses needed for each solution, as well as the average number of guesses and othere data.

## Code Overview

### Main Functions

- `load_word_list(filename)`: Loads a list of 5-letter words from a file.
- `filter_words(input_list, feedback, current_guess)`: Filters words based on feedback for each letter and position.
- `generate_feedback(guess, solution)`: Generates feedback for a guess compared to the solution.
- `find_best_guess(possible, data)`: Finds the best guess based on a frequency map.
- `wordle_solver(solution, possible, data)`: Solves Wordle for a given solution.
- `run_all_solutions()`: Runs the solver for all possible solutions and prints performance statistics.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
