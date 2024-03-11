# Simple Calculator
This code implements a basic calculator application using Python's Tkinter library.

## Functionality:<br><br>
Users can enter numbers, operators (+, -, *, /, %), and parentheses.<br>
The calculator displays the current expression in an entry field.<br>
Clicking the equal sign (=) button evaluates the expression and displays the result.<br>
A clear button (C) clears the expression.<br><br>
## Code Breakdown:

### Importing Tkinter:<br>

from tkinter import Tk, Entry, Button, StringVar: Imports necessary classes for creating the graphical user interface (GUI).<br>
### Calculator Class:
<br>
Defines a class named Calculator that represents the calculator functionality.
__init__(self, master): Initializes the calculator object.
master: Represents the main application window.
Sets the window title, geometry (size and position), background color, and disables resizing.
Creates a StringVar object (equation) to store the user's expression.
Initializes an empty string (entry_value) for the current display value.
Creates an Entry widget to display the expression and binds it to the equation variable.
Creates multiple Button widgets with configurations for various functions:
Number buttons (0-9) call the show method to append the digit.
Operator buttons (+, -, *, /, %) call the show method to append the operator.
Parenthesis buttons call the show method to append the parenthesis.
C (Clear) button calls the clear method to clear the display.
= (Equals) button calls the solve method to evaluate the expression.
show(self, value): Appends the provided value (digit or operator) to the expression and updates the display.
clear(self): Clears the expression and display.
solve(self): Attempts to evaluate the expression using eval and updates the display with the result.

### Main Program:

root = Tk(): Creates the main application window.
Calculator = Calculator(root): Creates a Calculator object, passing the main window as reference.
root.mainloop(): Starts the Tkinter event loop, keeping the application running until the window is closed.
