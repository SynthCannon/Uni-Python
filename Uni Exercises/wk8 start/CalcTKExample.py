#wk8ex3 -> CalcTKExample.py
#by Nicholas Sumner
from Tkinter import *
"""
We begin by defining convenience functions to make the creation of frame and button widgets
more compact. These functions use the pack geometry manager and use generally useful
values for widget behavior. It is always a good idea to collect common code in compact functions
(or classes, as appropriate) since this makes readability and maintenance much easier.
"""
def frame(root, side):
    w = Frame(root)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w

def button(root, side, text, command=None):
    w = Button(root, text=text, command=command)
    w.pack(side=side, expand=YES, fill=BOTH)
    return w
    
class Calculator(Frame):
    def __init__(self):
        """
        We call the Frame constructor to create the toplevel shell and an enclosing frame. Then, we
        set titles for the window and icon.
        """
        Frame.__init__(self)
        
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Simple Calculator')
        self.master.iconname("calc1")
        """
        Next, we create the display at the top of the calculator and define a Tkinter variable which
        provides access to the widget’s contents:
        """
        #display = StringVar()
        Entry(self, relief=SUNKEN,textvariable=display).pack(side=TOP, expand=YES,fill=BOTH)
        """
        Remember that character strings are sequences of characters in Python, so that each of the
        subsequences is really an array of characters over which we can iterate:
        """
        for key in ("123", "456", "789", "-0."):
            keyF = frame(self, TOP)
            for char in key: # We create a frame for each row of keys.
                """
                We use the convenience function to create a button, passing the frame, pack option, label
                and callback:
                Python supports the creation of anonymous functions (i.e. functions that are not bound to a name)
                at runtime, using a construct called "lambda"
                """
                button(keyF, LEFT, char,lambda w=display, s=' %s '%char: w.set(w.get()+s))
        opsF = frame(self, TOP)
        for char in "+-*/=":
            if char == '=':
                btn = button(opsF, LEFT, char)
                """
                The = key has an alternate binding to the other buttons since it calls the calc method when
                the left mouse button is released:
                """
                btn.bind('<ButtonRelease-1>',lambda e, s=self, w=display: s.calc(w), '+')
            else:
                btn = button(opsF, LEFT, char, lambda w=display, c=char: w.set(w.get()+' '+c+' '))
        clearF = frame(self, BOTTOM)
        button(clearF, LEFT, 'Clr', lambda w=display: w.set(''))
    def calc(self, display):
        """
        The calc method attempts to evaluate the string contained in the display and then it replaces
        the contents with the calculated value or an ERROR message:
        """
        try:
            display.set(`eval(display.get())`)
        except ValueError:
            display.set("ERROR")
if __name__ == '__main__':
    Calculator().mainloop()
    
"""
__WIDGET CLASSES__
Button- A simple button, used to execute a command or other operation
Canvas- Structured graphics. This widget can be used to draw graphs and plots, create graphics editors, and to implement custom widgets.
Checkbutton- Represents a variable that can have two distinct values. Clicking the button toggles between the values.
Entry- A text entry field.
Frame-A container widget. The frame can have a border and a background, and is used to group other widgets when creating an application 
      or dialog layout
Label-Displays a text or an image.
Listbox- Displays a list of alternatives. The listbox can be configured to get radiobutton or checklist behavior.
Menu- A menu pane. Used to implement pulldown and popup menus.
Menubutton- A menu button. Used to implement pulldown menus.
Message- Display a text. Similar to the label widget, but can automatically wrap text to a given width or aspect ratio.
Radiobutton-Represents one value of a variable that can have one of many values. Clicking the button sets 
            the variable to that value, and clears all other radiobuttons associated with the same variable.
Scale- Allows you to set a numerical value by dragging a "slider".
Scrollbar- Standard scrollbars for use with canvas, entry, listbox, and text widgets.
Text- Formatted text display. Allows you to display and edit text with various styles and attributes. Also supports embedded images and windows.
Toplevel- A container widget displayed as a separate, top-level window.
"""