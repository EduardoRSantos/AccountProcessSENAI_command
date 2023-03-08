from action import Action
from command import Command


class Account:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def process(self, command: Command):
        if(command.action == Action.DEPOSIT):
            self.balance += command.amount
            command.success = True
        elif(command.action == Action.WITHDRAW and command.amount <= self.balance):
            self.balance -= command.amount
            command.success = True
        else:
            command.success = False