# 8-Puzzle-Problem-Solver

This is a **Python** implementation of the **8-puzzle** problem solver using the A* search algorithm. The program allows users to input an initial and goal state, select a heuristic function, and find the optimal solution.

## Group Members 
- Parth Patel
- Sai Priyanka Taduri

## Features

- Implements A* Search Algorithm to solve the 8-puzzle problem.
- Supports two heuristic functions:
  - **Manhattan Distance**
  - **Misplaced Tiles**
- Displays step-by-step moves from the initial state to the goal state.
- Shows performance metrics, including:
  - Number of nodes generated
  - Number of nodes expanded
  - Number of steps taken

---

## Getting Started

### Prerequisites

Ensure you have **Python 3.x** installed. You can check your current version by running:

```bash
python3 --version
```
## Installation & Running the Program

### Clone the Repository:

```bash
git clone https://github.com/parth448812/8-Puzzle-Problem-Solver.git
cd 8-Puzzle-Problem-Solver
```
### Run the Solver:

```bash
python3 puzzle_solver.py
```

### Provide Input:

- The program will prompt you to enter the **initial state** (3x3 grid, space as `0`).
- Enter the **goal state** in the same format.
- Choose a heuristic function:
  - Enter `1` for **Manhattan Distance**.
  - Enter `2` for **Misplaced Tiles**.

### View the Output:

- The program will display the **steps taken** to reach the goal.
- It will also print:
  - **Number of nodes generated**.
  - **Number of nodes expanded**.
  - **Total moves required**.

### Example Run

#### Input:

```bash
Enter the INITIAL state (use 0 for blank):
Row 1: 1 2 3
Row 2: 4 0 5
Row 3: 6 7 8

Enter the GOAL state (use 0 for blank):
Row 1: 1 2 3
Row 2: 4 5 6
Row 3: 7 8 0

Choose the heuristic function:
1: Manhattan Distance
2: Misplaced Tiles
Enter your choice (1 or 2): 1
```
#### Output:

```bash
==================================
Solution Found!
==================================
Heuristic Used: Manhattan Distance
Nodes Generated: 23
Nodes Expanded: 14
Steps Taken: 5

Initial State:
1 | 2 | 3
4 |   | 5
6 | 7 | 8
    ↓
Step 1:
1 | 2 | 3
  | 4 | 5
6 | 7 | 8
    ↓
...
Goal State Reached!
