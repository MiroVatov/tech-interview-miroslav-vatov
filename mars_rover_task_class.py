class MarsRover:

    def __init__(self, width, height, *args):
        self.plateau_width = int(width) + 1  # NOTE this is the value for plateau width, increasing the value with 1 in order the plateau indexes to be valid, statring from 0
        self.plateau_height = int(height) + 1  # NOTE this is the value for plateau height, increasing the value with 1 in order the plateau indexes to be valid, starting from 0
        self.rover_details = []  # List where the rover initial position and movement details will be stored
        self.rover_position_x = 0  # variable, will store the current rover position on X coordinate
        self.rover_position_y = 0  # variable, will store the current rover position on Y coordinate

        self.ROTATE_RIGHT_DICT = {  # Dictionary with the direction, which will take the rover after right rotation command appears
            'N': 'E',
            'E': 'S',
            'S': 'W',
            'W': 'N'
        }

        self.ROTATE_LEFT_DICT = {  # Dictionary with the direction, which will take the rover after left rotation command appears
            'N': 'W',
            'W': 'S',
            'S': 'E',
            'E': 'N'
        }

        # filling the rover details list with the rover coordinates (X, Y), rover's direction ('N', 'E', 'S', 'W') and moves that will be taken by the rover.
        for index in range(0, len(args)):
            self.rover_details.append(args[index])

        self.ind = 0  #  variable that indicates the current index, of the below list
        self.rover_moves_to_print = [[] for _ in range(len(self.rover_details))]  #  List that stores the last position and the direction of each rover, after all the moves are taken

        # iterating through the rover details, in order to split the rover details to separate parts
        for rover_detail in self.rover_details:
            try:  # Checking if some of the rover details are missing, if Yes, Exception will be thrown
                self.rover_position_x = rover_detail[0]
                self.rover_position_y = rover_detail[1]
                self.direction = rover_detail[2]
                self.rover_moves = rover_detail[3]

                # after extraction of the rover details we are checking if the initial rover coordinates are not out of the plateau dimensions.
                # if initial rover coordinates are out of the plateau dimensions, we print simple message and proceed with the next rover.
                if not self._check_rover_valid_coordinates(self.plateau_width, self.plateau_height, self.rover_position_x, self.rover_position_y):
                    print("The Input Coordinates are out of the Plateau field")
                    continue

                #iteration through the rover movement commands and directions that rover has to take.
                for action in self.rover_moves:
                    if action == 'L':
                        self.direction = self.rotate_left
                    elif action == 'R':
                        self.direction = self.rotate_right
                    elif action == 'M':
                        self.rover_position_x, self.rover_position_y = self.move_rover

                        #  simple check if the rover position is still valid and if not, the function returns the rover to its previous coordinates
                        if not self._check_rover_valid_coordinates(self.plateau_width, self.plateau_height, self.rover_position_x, self.rover_position_y):
                            self.rover_position_x, self.rover_position_y = self.return_rover_to_previous_position

                # filling the list with the final coordinates and the direction of each rover
                self.rover_moves_to_print[self.ind] = [self.rover_position_x, self.rover_position_y, self.direction]
                self.ind += 1  # incrementing the index in order the list with the rover moves to be filled correctly

            except IndexError:
                print('Not all rover movement details are provided')

    # method, which is used for moving the rover after command 'M' appears according to the current direction.
    @property
    def move_rover(self):
        if self.direction == 'N':
            self.rover_position_y += 1
        elif self.direction == 'E':
            self.rover_position_x += 1
        elif self.direction == 'S':
            self.rover_position_y -= 1
        elif self.direction == 'W':
            self.rover_position_x -= 1
        return self.rover_position_x, self.rover_position_y

    # method, which returns the rover to its previous position, if the current coordinates after command 'M' are not valid (out of the plateau dimensions)
    @property
    def return_rover_to_previous_position(self):
        if self.direction == "N":
            self.rover_position_y -= 1
        elif self.direction == "S":
            self.rover_position_y += 1
        elif self.direction == "E":
            self.rover_position_x -= 1
        elif self.direction == "W":
            self.rover_position_x += 1
        return self.rover_position_x, self.rover_position_y

    # method that checks if the current rover coordinates are valid (Not out of the plateau dimensions)
    @staticmethod
    def _check_rover_valid_coordinates(width, height, x, y):
        if (0 <= x < width) and (0 <= y < height):
            return True
        return False

    @property  # Property for left rotation
    def rotate_right(self):
        self.direction = self.ROTATE_RIGHT_DICT[self.direction]
        return self.direction

    @property  # Property for right rotation
    def rotate_left(self):
        self.direction = self.ROTATE_LEFT_DICT[self.direction]
        return self.direction

    def print_rovers_final_coordinates(self):
        # method for printing the final output after rovers are finished their moves
        for position in range(len(self.rover_moves_to_print)):
            if self.rover_moves_to_print[position]:
                print(f"{self.rover_moves_to_print[position][0]} {self.rover_moves_to_print[position][1]} {self.rover_moves_to_print[position][2]}")


mars_rover = MarsRover(5, 5, [1, 2, 'N', 'LMLMLMLMM'], [3, 3, 'E', 'MMRMMRMRRM'])
mars_rover.print_rovers_final_coordinates()
mars_rover2 = MarsRover(5, 6, [1, 3, 'N', 'LMLMLMLMM'], [1, 3, 'E', 'MMRMMRMRRM'])
mars_rover2.print_rovers_final_coordinates()
mars_rover3 = MarsRover(5, 7, [6, 2, 'W', 'RMMMLMMLMM'], [5, 3, 'W', 'MMRMMRMRRM'])
mars_rover3.print_rovers_final_coordinates()
mars_rover4 = MarsRover(8, 20, [9, 5, 'S', 'LMLMLMLMM'], [6, 19, 'S', 'MMRMMRMRRM'], [8, 3, 'E', 'MMRMMRMRRM'])
mars_rover4.print_rovers_final_coordinates()
mars_rover5 = MarsRover(5, 5, [1, 2, 'N', 'LMLMLMLMM'], [3, 3, 'E',])
mars_rover5.print_rovers_final_coordinates()
mars_rover = MarsRover(5, 5, [6, 4, 'N', 'LMLMLMLMM'])