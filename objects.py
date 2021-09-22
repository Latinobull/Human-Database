from prompt_toolkit.shortcuts import confirm
from psycopg2 import connect
from db import Database
from PyInquirer import prompt, Separator

# Human needs name, job, age, salary, bills
DB = Database()


class Bills:
    @staticmethod
    def Tax(salary):
        tax = salary * 0.1175
        salary = salary - tax
        return salary

    @staticmethod
    def Groceries(salary):
        salary = salary - 120
        return salary

    @staticmethod
    def House(salary):
        salary = salary - 2500
        return salary


class Activities:
    @staticmethod
    def Gym(salary):
        salary = salary - 100
        return salary

    @staticmethod
    def Club(salary):
        salary = salary - 2000
        return salary

    @staticmethod
    def Subcriptions(salary):
        salary = salary - 200
        return salary


class Human(Bills, Activities):
    livingHumans = 0
    listOfHumans = []

    def __init__(self, name, age, job, salary, bank) -> None:
        self.name = name
        self.age = age
        self.job = job
        self.salary = salary
        self.bank = bank
        Human.addHumans()
        Human.listHuman(self.name)

    @classmethod
    def liveHumans(cls):
        return cls.livingHumans

    @classmethod
    def addHumans(cls):
        cls.livingHumans += 1

    @classmethod
    def listHuman(cls, name):
        cls.listOfHumans.append(name)

    @classmethod
    def list(cls):
        return cls.listOfHumans

    def mySalary(self):
        if self.salary > 0:
            return f"Your salary is {self.salary}"
        else:
            return f"You don`t make any money right now, Look for a job"


# Create a game involving a human spending money and earning money throughout his life
def createHuman():
    name = input("What is your name:")
    age = int(input("What is your age:"))
    choices = {
        "Doctor": 250000,
        "Developer": 140000,
        "Retail Worker": 35000,
        "Plumber": 74000,
        "Teacher": 83000,
        "Unemployed": 0,
    }
    jobQuestion = [
        {
            "type": "list",
            "name": "job",
            "message": "choose your job",
            "choices": choices,
        }
    ]
    answer = prompt(jobQuestion)
    job = answer.get("job")
    salary = choices.get(job)
    print(job, salary)
    DB.insert(name, age, job, salary, 0)


def viewHuman():
    for row in DB.view():
        print(f"{row} \n {Separator()}")


def deleteHuman():
    choices = {}
    for value, key in DB.viewName():
        choices.setdefault(key, []).append(value)

        # choices.append("".join(row))
        print(choices)
    deleteOptions = [
        {
            "type": "list",
            "name": "delete",
            "message": "Who do you want to delete?",
            "choices": choices,
        }
    ]
    answer = prompt(deleteOptions)
    person = answer.get("delete")
    print(person)
    for i in choices.get(person):
        index = i
    print(index)
    confirmation = [
        {
            "type": "confirm",
            "name": "confirm",
            "message": f"Are you sure you want to delete {person}?",
        }
    ]
    answer = prompt(confirmation)
    confirm = answer.get("confirm")
    if confirm:
        DB.delete(index)
        print(f"You have removed {person} for the program")
    else:
        print("You have cancelled your deletion request")


# Add a Jobs, Taxes, Activities, Money
# DJ = Human("DJ", 24, "Software Engineer", 0, 2000)
# print(DJ.Tax(DJ.salary))
# del DJ
# print(Human.liveHumans())
# print(Human.list())
deleteHuman()
