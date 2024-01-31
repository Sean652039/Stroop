# Stroop Experiment

![image-20240130193625956](https://cdn.jsdelivr.net/gh/Sean652039/pic_bed@main/uPic/image-20240130193625956.png)

![image-20240130193612656](https://cdn.jsdelivr.net/gh/Sean652039/pic_bed@main/uPic/image-20240130193612656.png)

## Introduction

This project implements a Stroop test experiment using the Pygame library in Python. The Stroop test is a psychological task used to measure participants' reaction time when asked to ignore the meaning of words and focus only on the printed color of the words.

## Dependencies

- Python 3.x
- Pygame library (install using `pip install pygame`)

## Files and Modules

### `Stroop.py`

This script contains the core functionality of the Stroop test experiment. It includes the following:

1. **Initialization:**
   - Import necessary modules (`pygame`, `sys`).
   - Import the `settings` class from the `Settings` module.
   - Import utility functions from the `Functions` module.

2. **Execution of Stroop Test:**
   - Define the `run_exper` function, set up the Pygame window, display the introduction screen, and start the Stroop test using the `run1` function from the `Functions` module.

3. **Pygame Window Setup:**
   - Initialize Pygame and configure the window.

4. **Introduction Screen:**
   - Display an introduction screen with the Stroop test title and instructions.

5. **Event Handling and Start of Test:**
   - Wait for a key press to trigger the start of the Stroop test.
   - Call the `run1` function to execute the Stroop test.

6. **Dependencies:**
   - Requires Python 3.x and the Pygame library.

### `Settings.py`

This module defines a `settings` class containing parameters for the Pygame window, such as screen width and height.

### `Functions.py`

This module contains functions used in the Stroop test, including:

   - `run1`: Implements the main logic of the Stroop test.
   - `textshow`: Displays text on the Pygame window.

## Usage

1. Install Python 3.x.
2. Install the Pygame library using `pip install pygame`.
3. Run the `Stroop.py` script.

## Stroop Test Procedure

1. Participants are instructed to press any key to start the Stroop test.
2. In the first phase, words with colored backgrounds are presented as a reference. Participants press the spacebar after each word.
3. After completing the first phase, the average time is recorded, and instructions for the second phase are displayed.
4. In the second phase, words with text color as a reference are presented. Participants again press the spacebar after each word.
5. After completion, the average time for the second phase is recorded.
6. Results are displayed, and the experiment concludes.