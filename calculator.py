from tkinter import *
from functools import partial
import math
import operator

class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calculator")
        self.addWidgets()
        self.history = []
        self.root.mainloop()

    def addWidgets(self):
        # Add Entry widgets
        self.e = Entry(self.root, width=35, borderwidth=5)
        self.e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create Button widgets
        self.numButtons = [Button(self.root, text=str(i), padx=40, pady=20, command=partial(self.onClick, i)) for i in range(10)]

        # Defining for number grid coords
        self.gridHeight = int(math.ceil(len(self.numButtons)/3))
        self.gridWidth = 3

        # Adding the number buttons to grid
        for i in range(1, self.gridHeight+1):
            for j in range(self.gridWidth):
                buttonNum = len(self.numButtons) - (self.gridWidth*i - j)
                self.numButtons[max(0,buttonNum)].grid(row=i, column=j)
                if buttonNum < 0:
                    break

        self.addButton = Button(self.root, text="+", padx=39, pady=20, command=partial(self.onClick, 10, operator.add))
        self.equalButton = Button(self.root, text="=", padx=86, pady=20, command=partial(self.onClick, 11))
        self.clearButton = Button(self.root, text="Clear", padx=77, pady=20, command=partial(self.onClick, 12))
        self.subtractButton = Button(self.root, text="-", padx=39, pady=20, command=partial(self.onClick, 10, operator.sub))
        self.multiplyButton = Button(self.root, text="×", padx=39, pady=20, command=partial(self.onClick, 10, operator.mul))
        self.divideButton = Button(self.root, text="÷", padx=39, pady=20, command=partial(self.onClick, 10, operator.truediv))

        self.clearButton.grid(row=4, column=1, columnspan=2)
        self.addButton.grid(row=5, column=0)
        self.equalButton.grid(row=5, column=1, columnspan=2)
        self.subtractButton.grid(row=6, column=0)
        self.multiplyButton.grid(row=6, column=1)
        self.divideButton.grid(row=6, column=2)

    def onClick(self, number, calcOperator=None):
        if number <= 9:
            # Key entry command
            current = self.e.get()
            self.e.delete(0, END)
            self.e.insert(0, str(current) + str(number))

        elif number == 10:
            # Math operator
            self.memory = self.e.get()
            self.operation = calcOperator
            self.e.delete(0, END)

        elif number == 11:
            # Equal command
            current = self.e.get() 
            result = self.operation(float(self.memory), float(current))
            if result % 1 == 0:
                result =  int(result)
            self.e.delete(0, END)
            self.e.insert(0, result)
            self.history.append(result)

        elif number == 12:
            # Clear command
            self.memory = None
            self.e.delete(0, END)


calc1 = Calculator()
