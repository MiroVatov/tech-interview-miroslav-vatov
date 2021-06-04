from collections import deque


class MarsRover:
    RIGHT_ROTATION_DICT = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }

    LEFT_ROTATION_DICT = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }

    def __init__(self, plateau_width: int, plateau_height: int, x: int, y: int, direction: str):
        self._plateau_width = plateau_width
        self._plateau_height = plateau_height
        self._x = x
        self._y = y
        self._direction = direction
        self.move = ""

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, value):
        if value not in ['N', 'W', 'E', 'S']:
            print(f"{value} is wrong! Chosen direction not correct! Please chose from: N, E, W, S")
        else:
            self._direction = value

    def rover_move(self, move):
        if move == "M":
            if self.direction == "N":
                self._y += 1
            elif self.direction == "E":
                self._x += 1
            elif self._direction == "W":
                self._x -= 1
            elif self._direction == "S":
                self._y -= 1

    def return_rover_to_previous_position(self):
        if self.direction == "N":
            self._y -= 1
        elif self.direction == "S":
            self._y += 1
        elif self.direction == "E":
            self._x -= 1
        elif self.direction == "W":
            self._x += 1

    def left_rotate(self):
        self.direction = self.LEFT_ROTATION_DICT[self._direction]

    def right_rotate(self):
        self.direction = self.RIGHT_ROTATION_DICT[self.direction]

    @staticmethod
    def print_final_output(output):
        return f"{output[0][0]} {output[0][1]} {output[0][2]}"


def main():
    def check_valid_coordinates(x, y, width, height):
        if (0 <= x <= width) and (0 <= y <= height):
            return True
        return False

    plateau_width = int(input("Please insert plateau width:"))
    plateau_height = int(input("Please insert plateau height:"))

    '''
    Please use only one of the moves lists/arrays provided at a time and put a comment on the others, while you are testing the code!

    '''
    # moves = [["LMLMLMLMM"], ["MMRMMRMRRM"]]
    moves = [['RMMMLMMLMM'], ['MMRMMRMRRM']]
    # moves = ["MMRMMRMRRM"]
    # moves = [['MMRMM'], ['MMRMMRMRRM']]
    # moves = ["MMRMMRMRRM"]
    # moves = ["LLLMMMLMMLMLM"]

    moves = deque(moves)
    final_output = []

    while moves:
        x_coordinate = int(input("Please insert the X coordinate:"))
        y_coordinate = int(input("Please insert the Y coordinate:"))

        if not check_valid_coordinates(x_coordinate, y_coordinate, plateau_width, plateau_height):
            print("The chosen coordinates are out of the plateau field." + '\n' f"Please choose X less than or equal to "
                                                                         f"{plateau_width} and Y less than or equal to {plateau_height}")
            continue

        direction = input("Please insert direction from: N, W, E, S")

        if direction not in ["N", "E", "W", "S"]:
            print(f"{direction} is wrong! Chosen direction not correct! Please chose from: N, E, W, S")
            continue

        mars_rover = MarsRover(plateau_width, plateau_height, x_coordinate, y_coordinate, direction)
        move_lines = moves.popleft()

        for move in move_lines[0]:
            if move == "M":
                mars_rover.rover_move(move)
            elif move == "L":
                mars_rover.left_rotate()
            elif move == "R":
                mars_rover.right_rotate()
            if not check_valid_coordinates(mars_rover.x, mars_rover.y, plateau_width, plateau_height):
                mars_rover.return_rover_to_previous_position()

        final_output.append([mars_rover.x, mars_rover.y, mars_rover.direction])
        print(mars_rover.print_final_output(final_output))
        final_output = []


if __name__ == '__main__':
    main()

