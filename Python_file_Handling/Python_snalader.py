# Function to simulate snakes and ladders
def snakes_and_ladders(board_config, dice_sequence):
    # Create a dictionary for board mapping
    board = {}
    for item in board_config.split(","):
        start, end = map(int, item.split(":"))
        board[start] = end

    position = 0  # Player starting position

    # Loop through dice rolls
    for roll in dice_sequence:
        position += roll  # Move forward

        # Check for snake or ladder
        if position in board:
            position = board[position]

        # Check if player reached 100 or beyond
        if position >= 100:
            return "YES"

    return "NO"


# Input
input1 = "6:14,11:28,17:74,22:7,38:59,49:12,57:76,61:54,81:98,88:4"
input2 = "6,3,4,3,5"

# Convert input2 to list of integers
dice_sequence = list(map(int, input2.split(",")))

# Check and print result
result = snakes_and_ladders(input1, dice_sequence)
print(result)
