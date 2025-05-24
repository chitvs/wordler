# Wordle solver

This project contains a Python program designed to solve the popular word game **Wordle**. The solver uses strategic guessing and feedback processing to efficiently narrow down the list of possible solutions, aiming to solve the puzzle in the fewest possible guesses.

## Features

- **Strategic initial guess**: starts with an optimal guess to cover common letters.
- **Feedback processing**: filters the list of possible words based on feedback from guesses.
- **Best guess selection**: uses letter frequencies to select the next guess that maximizes information gain.
- **Simulation mode**: runs the solver on all possible Wordle solutions to evaluate its performance.

## Optimization

This program can be further optimized by calculating entropy after each guess. By selecting the guess that maximizes the information gain (reduces uncertainty the most), the solver can improve its efficiency. This approach is inspired by the video ["Solving Wordle Using Information Theory"](https://www.youtube.com/watch?v=v68zYyaEmEA) by 3Blue1Brown, which explains the concepts of entropy and information theory in the context of solving Wordle.

## Requirements

- Python
- JSON file containing a frequency map (`data/freq_map.json`)
- Text file containing allowed words (`data/allowed_words.txt`)

## File structure

- `src/wordle_solver.py`: Main program file containing the Wordle solver logic.
- `src/wordle_auto.py`: Script to run simulations and evaluate performance.
- `data/allowed_words.txt`: List of all allowed 5-letter words.
- `data/possible_words.txt`: List of 5-letter words with a higher probability of being the solution.
- `data/nyt_words.txt`: List of NYT Wordle allowed words.
- `data/solutions.txt`: List of all possible solutions.
- `data/freq_map.json`: JSON file with word frequency data used to score guesses.
- Other data files: Additional files can be added to enhance the solver's efficiency by providing more information for guess optimization.

## Usage

### Running the solver

To run the Wordle solver for a single interactive session:

1. **Navigate to the project directory**:
   Change to the root directory of your project where the `src` folder is located:

   ```sh
   cd /path/to/wordle-solver
   ```

2. **Execute the solver script**:
   Run the `wordle.py` script located in the `src` directory:

   ```sh
   python3 src/wordle.py
   ```

3. **Interactive session**:
   The program will prompt you to enter feedback for each guess. Feedback should be in the format of `g` (green), `y` (yellow), and `b` (black), where:
   
   - `g` indicates that a letter is correct and in the correct position.
   - `y` indicates that a letter is correct but in the wrong position.
   - `b` indicates that a letter is not in the solution.

   Provide your guesses and feedback as prompted.

![Example](wordle.gif)

### Running simulations

To run the solver on all possible Wordle solutions and evaluate its performance:

1. **Navigate to the project directory**:
   Change to the root directory of your project:

   ```sh
   cd /path/to/wordle-solver
   ```

2. **Run the simulation script**:
   Execute the `wordle_auto.py` script located in the `src` directory:

   ```sh
   python3 src/wordle_auto.py
   ```

   This will simulate solving the puzzle for each word in `data/allowed_words.txt` and print the number of guesses needed for each solution, as well as the average number of guesses and other performance data.

## Code overview

### Main functions

- `load_word_list(filename)`: Loads a list of 5-letter words from a file.
- `filter_words(input_list, feedback, current_guess)`: Filters words based on feedback for each letter and position.
- `generate_feedback(solution, guess)`: Generates feedback for a guess compared to the solution.
- `find_best_guess(possible, data)`: Finds the best guess based on a frequency map.
- `wordle_solver_auto(solution, allowed_words, data)`: Solves Wordle for a given solution with automatic feedback generation.
- `run_all_solutions_auto()`: Runs the solver for all possible solutions and prints performance statistics.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
