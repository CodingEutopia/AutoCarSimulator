import logging
from Car import Car
from Grid import Grid
from Direction import Direction
from Command import Command

logging.basicConfig(format='%(message)s', level=logging.INFO)

class AutoCarSimulator:
    grid: Grid
    carPool: list[Car]

    def __init__(self):
        self.carPool = []
        self.grid = None

    def run(self):
        print("```")
        logging.info("Welcome to Auto Driving Car Simulation!")
        try:
            x, y = map(int, input("Please enter the width and height of the simulation field in x y format: \n```\n").split())
            if x <= 0 or y <= 0:
                    raise ValueError(f"x: {x} y: {y}")
        except ValueError as e:
            logging.error(f"Invalid input: {e}. Please Enter 2 positive integers.")
            return

        self.grid = Grid(x, y)
        logging.info("You have created a field of " + str(self.grid.getXDimension()) + " x " + str(self.grid.getYDimension()))
        print("```\n")

        print("```")
        
        main_menu = True
        while main_menu:
            userResponse = input("Please choose from the following options:\n[1] Add a car to field\n[2] Run simulation\n```\n")

            if userResponse == "1":
                self.addCar()
                logging.info("Your current list of cars are:")
                for car in self.carPool:
                    carName = car.getCarName()
                    xPos = car.getX()
                    yPos = car.getY()
                    direction = car.getFacingDirection()
                    commands = "".join(car.getCommands())
                    string = "- " + carName + ", (" + str(xPos) + ", " + str(yPos) + "), " + direction + ", " + commands
                    logging.info(string)
            elif userResponse == "2":
                self.startSim()
                userResponse2 = input("Please choose from the following options:\n[1] Start Over\n[2] Exit\n")
                if userResponse2 == "2":
                    main_menu = False
                    logging.info("Thank you for running this simulation. Goodbye!")
            else:
                logging.error("Invalid option chosen! Please choose again")
    

    def addCar(self):
        print("```")
        carName = input("Please enter the name of the car: \n```\n")

        logging.info("Valid directions are N S E W representing North, South, East, West\n")
        try:
            carXpos, carYpos, direction = input("Please enter the initial position of car " + carName + " in x y Direction format:\n```\n").split()
            
            carXpos = int(carXpos)
            carYpos = int(carYpos)
            direction = direction.upper()

            if self.validateInitialPosition(carXpos, carYpos) == False:
                raise ValueError("Invalid position! Car must be within grid boundaries!")

            if self.validateDirection(direction) == False:
                raise ValueError("Invalid Direction!")
        except ValueError as e:
            logging.error(f"Invalid input: {e}")
            return

        print("Valid Commands that can be issued to car are:")
        print("L: rotates the car by 90 degrees to the left")
        print("R: rotates the car by 90 degrees to the right")
        print("F: moves forward by 1 grid point")

        commands = input("Please enter the commands for Car " + carName + ":\n")

        try:
            commandList = list(commands)

            if self.validateCommands(commandList) == False:
                raise ValueError("Invalid Command Error")
        except ValueError as e:
            logging.error("Invalid command detected!")
            return

        car = Car(carName, carXpos, carYpos, direction, commandList)
        self.carPool.append(car)
        

    def validateInitialPosition(self, x, y):
        if x > self.grid.getXDimension() or x < 0 or y > self.grid.getYDimension() or y < 0:
            return False
        else:
            return True
    
    def validateDirection(self, direction):
            valid_directions = {d.value for d in Direction}
            if direction not in valid_directions:
                return False
            else:
                return True
    
    def validateCommands(self, commands):
        valid_commands = {c.value for c in Command}
        for i in range(len(commands)):
            if commands[i] not in valid_commands:
                return False
        return True
            
    
    def startSim(self):
        positions = {}
        longestCommand = max(len(car.commands) for car in self.carPool)
        iteration = 0
        while iteration < longestCommand:
            positions = {}
            for car in self.carPool:
                if car.getCrashed() == False:
                    newPos = car.move(self.grid.getXDimension(),self.grid.getYDimension())
                    if positions.get((newPos[0], newPos[1])) is None:
                        positions[(newPos[0], newPos[1])] = [car, newPos[2]]
                    else:
                        crashedCar1 = car
                        crashedCar2 = positions.get((newPos[0], newPos[1]))[0]
                        crashedCar1.setCrashed()
                        crashedCar1.setCollidedWith(crashedCar2)
                        crashedCar2.setCrashed()
                        crashedCar2.setCollidedWith(crashedCar1)
            iteration += 1
        
        logging.info("After simulation, the result(s) are:")
        for car in self.carPool:
            carName = car.getCarName()
            carXpos = car.getX()
            carYpos = car.getY()
            direction = car.getFacingDirection()
            collidedWith = car.getCollidedWith()
            if car.getCrashed() == True:
                string = "- " + carName + ", collides with " + collidedWith.getCarName() + " at (" + str(carXpos) + ", " + str(carYpos) + ") at step " + str(car.getCommandPointer())
            else:
                string = "- " + carName + ", (" + str(carXpos) + "," + str(carYpos) + "), " + direction
            logging.info(string)