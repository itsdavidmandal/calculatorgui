from tkinter import Tk, Entry, Button, StringVar
'''
from tkinter import Tk, Entry, Button, StringVar: This line imports the necessary classes from the Tkinter library for creating graphical user interfaces (GUIs).
Tk: Represents the main application window.
Entry: Creates a single-line text input field for user input.
Button: Creates a clickable button widget.
StringVar: Used for managing text displayed in widgets like Entry.
'''


class Calculator:
    def __init__(self, master): # ????
        master.title("Calculator") # the title of the frame 
        master.geometry('357x420+0+0') 
        '''
        Sets the geometry (size and position) of the window. Here, it's set to 357 pixels wide, 420 pixels high, positioned at coordinates (0, 0) on the screen.
        '''
        master.config(bg='gray') #Sets the background color of the window to gray.
        master.resizable(False, False) # Disables resizing of the window. 

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)
        
        Button(width = 11,height = 4, text = '(' ,relief='flat' , bg ='white' , command = lambda:self.show('(')).place(x=0 , y=50)
        '''
        Button(...): This constructs a Button widget, which represents a clickable button on the screen.
Button Configurations:

width = 11: Sets the width of the button in characters (approximately).
height = 4: Sets the height of the button in terms of the number of character rows.
text = '(': Defines the text displayed on the button, which in this case is an opening parenthesis "(".
relief='flat': Sets the relief style of the button. Here, 'flat' creates a button with a flat appearance without any raised or sunken borders.
bg ='white': Sets the background color of the button to white.
Command and Positioning:

command = lambda:self.show('('): This part assigns a command to be executed when the button is clicked.
lambda: This is a shorthand way to define an anonymous function in Python. Here, the lambda function takes no arguments and simply calls the self.show('(') method.
self.show('('): This refers to a method defined within the Calculator class (likely where this code resides). The show method presumably takes a character or string as input, and in this case, it's passing an opening parenthesis "(". You can check the show method definition to understand how it handles the input and updates the calculator display.
.place(x=0, y=50): This method positions the button within the main window. Here, it places the top-left corner of the button at coordinates (0, 50) relative to the window's top-left corner.
        '''

        Button(width = 11,height = 4, text = ')' ,relief='flat' , bg ='white' , command = lambda:self.show(')')).place(x=90 , y=50)
        Button(width = 11,height = 4, text = '%' ,relief='flat' , bg ='white' , command = lambda:self.show('%')).place(x=180 , y=50)
        Button(width = 11,height = 4, text = '1' ,relief='flat' , bg ='white' , command = lambda:self.show(1)).place(x=0 , y=125)
        Button(width = 11,height = 4, text = '2' ,relief='flat' , bg ='white' , command = lambda:self.show(2)).place(x=90 , y=125)
        Button(width = 11,height = 4, text = '3' ,relief='flat' , bg ='white' , command = lambda:self.show(3)).place(x=180 , y=125)
        Button(width = 11,height = 4, text = '4' ,relief='flat' , bg ='white' , command = lambda:self.show(4)).place(x=0 , y=200)
        Button(width = 11,height = 4, text = '5' ,relief='flat' , bg ='white' , command = lambda:self.show(5)).place(x=90 , y=200)
        Button(width = 11,height = 4, text = '6' ,relief='flat' , bg ='white' , command = lambda:self.show(6)).place(x=180 , y=200)
        Button(width = 11,height = 4, text = '7' ,relief='flat' , bg ='white' , command = lambda:self.show(7)).place(x=0 , y=275)
        Button(width = 11,height = 4, text = '8' ,relief='flat' , bg ='white' , command = lambda:self.show(8)).place(x=90 , y=275)
        Button(width = 11,height = 4, text = '9' ,relief='flat' , bg ='white' , command = lambda:self.show(9)) .place(x=180 , y=275)
        Button(width = 11,height = 4, text = '0' ,relief='flat' , bg ='white' , command = lambda:self.show(0)).place(x=90 , y=350)
        Button(width = 11,height = 4, text = '.' ,relief='flat' , bg ='white' , command = lambda:self.show('.')).place(x=180 , y=350)
        Button(width = 11,height = 4, text = '+' ,relief='flat' , bg ='white' , command = lambda:self.show('+')).place(x=270 , y=275)
        Button(width = 11,height = 4, text = '-' ,relief='flat' , bg ='white' , command = lambda:self.show('-')).place(x=270 , y=200)
        Button(width = 11,height = 4, text = '/' ,relief='flat' , bg ='white' , command = lambda:self.show('/')).place(x=270 , y=50)
        Button(width = 11,height = 4, text = 'x' ,relief='flat' , bg ='white' , command = lambda:self.show('*')).place(x=270, y=125)
        Button(width = 11,height = 4, text = '=' ,relief='flat' , bg ='white' , command = self.solve).place(x=270 , y=350)
        Button(width = 11,height = 4, text = 'C' ,relief='flat' , bg ='white' , command = self.clear).place(x=0, y=350)


    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)


root = Tk()
Calculator = Calculator(root)
root.mainloop()
