
from tkinter import *
from tkinter import ttk


# Performing the Calculation
# -- Speaking of which, here we define our calculate procedure.
# -- It's called when a user presses Calculate button or hits the Return key. It performs the feet-meters calculation.


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


# Setting up the Main Application Window
# the following code sets up the main application window, giving it the title "Feet to Meters."
root = Tk()
root.title("Feet to Meters")


#
# Creating a Content Frame
#
# Next, we create a frame widget, which will hold the contents of our user interface.
# #####################################################################################################################
#
# After the frame is created, grid places it directly inside our main application window.
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#
# Why do we put a frame inside the main window?
# * Strictly speaking, we could just put the other widgets in our interface directly into the main application window,
# * without the intervening content frame. That's what you'll see in older Tk programs.
#
# However, the main window isn't itself part of the newer "themed" widgets.
# Its background color doesn't match the themed widgets we will put inside it.
# Using a "themed" frame widget to hold the content ensures that the background is correct.
#
# #####################################################################################################################
#
# columnconfigure/rowconfigure tell Tk that the frame should expand to fill any extra space if the window is resized
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Creating the Entry Widget
#
# The first widget we'll create is the entry where we can input the number of feet that we want to convert.
# We need to do two things: create the widget itself, and then place it onscreen.
#
feet = StringVar()
#
# When we create a widget, we need to specify its parent, which is the widget that this widget will be placed inside.
# In this case, we want our entry placed inside the content frame.
# Our entry, and other widgets we'll create shortly, are said to be children of the content frame.
# In Tcl and Perl, the widget name is used to specify the parent-child relationship, i.e. .c.feet is a child of .c.
# In Python and Ruby, the parent is passed as the first parameter when instantiating a widget object.
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# When we create a widget, we can optionally provide it with certain configuration options.
# Here, we want the entry to appear, 7 chars. We also assign it a mysterious textvariable; we'll see this shortly.
#
# Widgets aren`t automatically on the screen - Tk doesn't know how you want them to be placed relative to other widgets.
# That's what the grid part does. Remember the layout grid when we sketched out our application?
# Widgets are placed in the appropriate column (1, 2, or 3), and row (also 1, 2, or 3).
feet_entry.grid(column=2, row=1, sticky=(W, E))
# The sticky option to grid describes how the widget should line up within the grid cell, using compass directions.
# 'W' means to anchor the widget to left side of the cell, 'W,E' means to attach it to both left/right sides, and so on.
# Python also defines constants for these directional strings, which you can provide as a list, e.g. W or (W, E).


#
# Creating the Remaining Widgets
# 1.
# then do exactly the same thing for remaining widgets. We have 1 label displaying the number meters that we calculate.
# 2.
# We have a "Calculate" button that is pressed to perform the calculation.
# 3.
# Finally, we have three static text labels to make it clear how to use the application.
#
# For each of these widgets, we first create it and then place it onscreen in the appropriate cell in the grid.

# Ad1
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
# Ad2
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
# Ad3
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#
# Adding Some Polish
# -- We then put a few finishing touches on our user interface.
#
# 1.
# The first part walks through all of the widgets that are contained within our content frame,
# and adds a little bit of padding around each, so they aren't so scrunched together.
# We could have added these options to each grid call when we 1st put the widgets onscreen, but this is a nice shortcut.
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
#
# 2.
# The second part tells Tk to put the focus on our entry widget.
# That way, the cursor will start in that field, so users don't have to click in it before starting to type.
feet_entry.focus()
#
# 3.
# The third line tells Tk that if a user presses the Return key (Enter on Windows) it should call our calculate routine,
# the same as if they pressed the Calculate button.
root.bind("<Return>", calculate)


root.mainloop()
