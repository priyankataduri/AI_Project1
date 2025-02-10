import queue

# Global variables
INITIAL_STATE = None
GOAL_STATE = None
NODES_GENERATED = 0
NODES_EXPANDED = 0
STEPS_TAKEN = 0


# Print the puzzle state in a nice format
def print_state(state):
    for row in state:
        print(" | ".join(str(cell) if cell != 0 else " " for cell in row))
    print("-" * 10)


# Find the position of the blank tile (0)
def find_blank_tile(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 0:
                return i, j
    raise ValueError("No blank tile found.")


# Generate valid moves for the blank tile
def generate_moves(x, y):
    moves = []
    if x > 0:
        moves.append((-1, 0))  # Move up
    if x < 2:
        moves.append((1, 0))  # Move down
    if y > 0:
        moves.append((0, -1))  # Move left
    if y < 2:
        moves.append((0, 1))  # Move right
    return moves


# Apply a move to the state to create a new state
def apply_move(state, x, y, dx, dy):
    new_state = [row[:] for row in state]  # Make a copy of the state
    new_state[x][y], new_state[x + dx][y + dy] = new_state[x + dx][y + dy], new_state[x][y]
    return new_state


# Heuristic function 1: Manhattan distance
def manhattan_distance(state, goal_state):
    distance = 0
    goal_positions = {}

    for i in range(len(goal_state)):
        for j in range(len(goal_state[i])):
            goal_positions[goal_state[i][j]] = (i, j)

    for i in range(len(state)):
        for j in range(len(state[i])):
            value = state[i][j]
            if value != 0:
                target_x, target_y = goal_positions[value]
                distance += abs(target_x - i) + abs(target_y - j)

    return distance


# Heuristic function 1: Misplaced Tiles
def misplaced_tiles(state, goal_state):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count


# A* search algorithm
def a_star_search(initial_state, goal_state, heuristic_function):
    global NODES_GENERATED, NODES_EXPANDED

    open_list = queue.PriorityQueue()
    open_list.put((0, initial_state, [], 0))
    closed_set = set()

    NODES_GENERATED = 0
    NODES_EXPANDED = 0

    while not open_list.empty():
        f, current_state, path, g = open_list.get()

        if current_state == goal_state:
            return path + [(current_state, g)], NODES_GENERATED, NODES_EXPANDED

        state_tuple = tuple(tuple(row) for row in current_state)
        if state_tuple in closed_set:
            continue

        closed_set.add(state_tuple)
        NODES_EXPANDED += 1

        try:
            x, y = find_blank_tile(current_state)
        except ValueError as e:
            print(e)
            continue

        for dx, dy in generate_moves(x, y):
            new_state = apply_move(current_state, x, y, dx, dy)
            new_state_tuple = tuple(tuple(row) for row in new_state)
            if new_state_tuple not in closed_set:
                new_path = path + [(current_state, g)]
                new_g = g + 1
                h = heuristic_function(new_state, goal_state)
                new_f = new_g + h
                open_list.put((new_f, new_state, new_path, new_g))
                NODES_GENERATED += 1

    return None, NODES_GENERATED, NODES_EXPANDED


# Validate and parse user input
def get_puzzle_input(prompt):
    while True:
        try:
            print(prompt)
            rows = []
            all_numbers = set()
            for i in range(3):
                row = input(f"Row {i + 1}: ").split()
                if len(row) != 3:
                    raise ValueError(
                        "Each row must have exactly 3 numbers separated by spaces."
                    )
                parsed_row = list(map(int, row))
                for num in parsed_row:
                    if num in all_numbers:
                        raise ValueError(
                            "Duplicate numbers found. Use each number 0-8 exactly once."
                        )
                    all_numbers.add(num)
                rows.append(parsed_row)
            if all_numbers != set(range(9)):
                raise ValueError(
                    "You must include all numbers from 0 to 8 exactly once.")
            return rows
        except ValueError as e:
            print(f"Error: {e}\nPlease try again.\n")


# Main function
def main():

    global INITIAL_STATE, GOAL_STATE, STEPS_TAKEN

    INITIAL_STATE = get_puzzle_input(
        "Enter the INITIAL state (use 0 for blank):")
    print("\nInitial State:")
    print_state(INITIAL_STATE)

    GOAL_STATE = get_puzzle_input("Enter the GOAL state (use 0 for blank):")
    print("\nGoal State:")
    print_state(GOAL_STATE)

    while True:
        try:
            print("\nChoose the heuristic function:")
            print("1: Manhattan Distance")
            print("2: Misplaced Tiles")
            choice = int(input("Enter your choice (1 or 2): "))
            if choice == 1:
                heuristic_function = manhattan_distance
                heuristic_name = "Manhattan Distance"
            elif choice == 2:
                heuristic_function = misplaced_tiles
                heuristic_name = "Misplaced Tiles"
            else:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please enter 1 or 2.")

    print(f"\nSelected Heuristic: {heuristic_name}\n")
    print("Solving the puzzle...\n")

    solution_path, nodes_generated, nodes_expanded = a_star_search(
        INITIAL_STATE, GOAL_STATE, heuristic_function)

    if solution_path is None:
        print("No solution found.")
    else:
        STEPS_TAKEN = len(solution_path) - 1
        print("=" * 30)
        print("Solution Found!")
        print("=" * 30)
        print(f"Heuristic Used: {heuristic_name}")
        print(f"Nodes Generated: {nodes_generated}")
        print(f"Nodes Expanded:  {nodes_expanded}")
        print(f"Steps Taken:     {STEPS_TAKEN}\n")

        print("Initial State:")
        print_state(solution_path[0][0])
        print("    ↓\n")

        for idx, (state, _) in enumerate(solution_path[1:], start=1):
            print(f"Step {idx}:")
            print_state(state)
            if idx != STEPS_TAKEN:
                print("    ↓\n")

        print("Goal State Reached!")


if __name__ == "__main__":
    main()
