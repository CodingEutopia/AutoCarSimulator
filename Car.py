from Command import Command
from Direction import Direction
from typing import Optional

class Car:
    carName: str
    xCoordinate: int
    yCoordinate: int
    facingDirection: Direction
    commands: list[Command]
    commandPointer: int
    crashed: bool
    collidedWith: Optional["Car"]

    def __init__(self, carName: str, xCoordinate: int, yCoordinate: int, facingDirection: Direction, commands: list[Command]):
        self.carName = carName
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.facingDirection = facingDirection
        self.commands = commands
        self.commandPointer = 0
        self.crashed = False
        self.collidedWith = None


    
    def getCarName(self):
        return self.carName
    
    def getX(self):
        return self.xCoordinate
    
    def getY(self):
        return self.yCoordinate
    
    def setX(self, x):
        self.xCoordinate = x

    def setY(self, y):
        self.yCoordinate = y
    
    def getFacingDirection(self):
        return self.facingDirection
    
    def setFacingDirection(self, direction: Direction):
        self.facingDirection = direction
    
    def getCommands(self):
        return self.commands
    
    def setCommands(self, newCommandsList):
        self.commands = newCommandsList
    
    def getCommandPointer(self):
        return self.commandPointer

    def incrementPointer(self):
        self.commandPointer += 1

    def getCrashed(self):
        return self.crashed

    def setCrashed(self):
        self.crashed =  not self.crashed

    def getCollidedWith(self):
        return self.collidedWith
    
    def setCollidedWith(self, car: Optional["Car"]):
        self.collidedWith = car

    def move(self, X, Y):
        if self.crashed == False:
            if self.commandPointer < len(self.commands):
                command = self.commands[self.commandPointer]
                if self.facingDirection == Direction.NORTH.value:
                    if command == Command.FORWARD.value:
                        if self.getY() + 1 <= Y:
                            self.setY(self.getY() + 1)
                    elif command == Command.LEFT.value:
                        self.setFacingDirection(Direction.WEST.value)
                    elif command == Command.RIGHT.value:
                        self.setFacingDirection(Direction.EAST.value)
                elif self.facingDirection == Direction.SOUTH.value:
                    if command == Command.FORWARD.value:
                        if self.getY() - 1 >= 0:
                            self.setY(self.getY() - 1)
                    elif command == Command.LEFT.value:
                        self.setFacingDirection(Direction.EAST.value)
                    elif command == Command.RIGHT.value:
                        self.setFacingDirection(Direction.WEST.value)
                elif self.facingDirection == Direction.EAST.value:
                    if command == Command.FORWARD.value:
                        if self.getX() + 1 <= X:
                            self.setX(self.getX() + 1)
                    elif command == Command.LEFT.value:
                        self.setFacingDirection(Direction.NORTH.value)
                    elif command == Command.RIGHT.value:
                        self.setFacingDirection(Direction.SOUTH.value)
                elif self.facingDirection == Direction.WEST.value:
                    if command == Command.FORWARD.value:
                        if self.getX() -1 >= 0:
                            self.setX(self.getX() - 1)
                    elif command == Command.LEFT.value:
                        self.setFacingDirection(Direction.SOUTH.value)
                    elif command == Command.RIGHT.value:
                        self.setFacingDirection(Direction.NORTH.value)
                
                self.incrementPointer()
        return [self.getX(), self.getY(), self.getFacingDirection()]