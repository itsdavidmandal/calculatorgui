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
Defines a class named Calculator that represents the calculator functionality.<br>
__init__(self, master): Initializes the calculator object.<br>
master: Represents the main application window.<br>
Sets the window title, geometry (size and position), background color, and disables resizing.<br>
Creates a StringVar object (equation) to store the user's expression.<br>
Initializes an empty string (entry_value) for the current display value.<br>
Creates an Entry widget to display the expression and binds it to the equation variable.<br>
Creates multiple Button widgets with configurations for various functions:<br>
Number buttons (0-9) call the show method to append the digit.<br>
Operator buttons (+, -, *, /, %) call the show method to append the operator.<br>
Parenthesis buttons call the show method to append the parenthesis.<br>
C (Clear) button calls the clear method to clear the display.<br>
= (Equals) button calls the solve method to evaluate the expression.<br>
show(self, value): Appends the provided value (digit or operator) to the expression and updates the display.<br>
clear(self): Clears the expression and display.<br>
solve(self): Attempts to evaluate the expression using eval and updates the display with the result.<br>

### Main Program:

root = Tk(): Creates the main application window.
Calculator = Calculator(root): Creates a Calculator object, passing the main window as reference.
root.mainloop(): Starts the Tkinter event loop, keeping the application running until the window is closed.
