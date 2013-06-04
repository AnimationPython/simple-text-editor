# editor.py
# Simple Text Editor
# Written by James Wang, 4 Jun 2013

from Tkinter import * 
import tkFileDialog, tkMessageBox

class EditorWindow(Frame):
    """Displays the text editor window."""
    
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # Create text area
        textentry = EditorEntryArea(master)
        
        # Create toolbar
        toolbar = EditorToolBar(master, textentry)

        # Pack these down
        toolbar.pack(side=TOP, fill=X)
        textentry.pack(side=TOP, fill=BOTH, expand=TRUE)

        # Create menu
        menu = EditorMenu(master, textentry)
        master.config(menu=menu)

        textentry.focus_set()
        
class EditorMenu(Menu):
    """Creates the menu bar for the text editor"""

    def __init__(self, master, textarea):
        Menu.__init__(self, master)

        # defines and adds filemenu
        filemenu = Menu(self)
        filemenu.add_command(label="New", command=lambda: new_file(textarea))
        filemenu.add_command(label="Open...", command=lambda: open_file(master,
                                                                        textarea))
        filemenu.add_command(label="Save as...", command=lambda:
                             save_file(master, textarea))
        filemenu.add_separator()
        filemenu.add_command(label="Quit", command=exit)
        self.add_cascade(label="File", menu=filemenu)

        # defines and adds helpmenu
        helpmenu = Menu(self)
        helpmenu.add_command(label="Help", command=lambda: help_dialog(master))
        helpmenu.add_command(label="About", command=lambda:
                             about_dialog(master))
        self.add_cascade(label="Help", menu=helpmenu)
        
class EditorToolBar(Frame):
    """Creates the editor's toolbar"""

    def __init__(self, master, textarea):
        Frame.__init__(self, master, bd=1, relief=RAISED, background="gray")
        
        # new graphical button
        b_new = GraphicalButton(self, "newfile.gif", lambda:new_file(textarea))
        b_new.pack(side=LEFT, padx=2, pady=2)

        # open graphical button
        b_open = GraphicalButton(self, "openicon.gif", lambda:open_file(master,
                                                                        textarea))
        b_open.pack(side=LEFT, padx=2, pady=2)

        # save graphical button
        b_save = GraphicalButton(self, "saveicon.gif", lambda:save_file(master,
                                                                        textarea))
        b_save.pack(side=LEFT, padx=2, pady=2)

        # quit graphical button
        b_quit = GraphicalButton(self, "quit.gif", exit)
        b_quit.pack(side=LEFT, padx=2, pady=2)

class EditorEntryArea(Text):
    """Creates the editor's text entry area"""

    def __init__(self, master):
        Text.__init__(self, master)

class GraphicalButton(Button):
    """Creates a graphical button using the filename for the image, and the
    command as the bound function/method. Filename must include extension.

    """
    def __init__(self, master, filename, command):
        img = PhotoImage(file=filename)
        Button.__init__(self, master, image=img, command=command,
                        borderwidth=.001)
        self.image = img # so Tkinter doesn't GC the image
        
def new_file(textarea):
    """Initializes a new file. Takes the text area (to clear it if needed)"""
    textarea.delete(1.0, END)
        
def open_file(parent_window, textarea):
    """Dialog that asks user to select a file to open. Takes a parent window to
    anchor to and textarea to input file to be opened. Returns True if user
    selects a file, else returns False if user cancels the dialog.

    """
    the_file = tkFileDialog.askopenfile(defaultextension='.py', 
                                        filetypes=[('text files', '.txt'), 
                                                   ('python files', '.py')],
                                        parent=parent_window)
    if the_file:
        textarea.delete(1.0, END)
        textarea.insert(1.0, the_file.read())
        the_file.close()
        return True
    else:
        return None
    
def save_file(parent_window, textarea):
    """Dialog that asks user to save a file as. Takes a parent window to anchor
    to. Returns True if user selects a file, else returns False if user
    cancels the dialog.

    """
    the_file = tkFileDialog.asksaveasfile(defaultextension='.py', 
                                          filetypes=[('text files', '.txt'), 
                                                     ('python files', '.py')],
                                          parent=parent_window)
    if the_file:
        the_file.write(str(textarea.get(1.0, END)))
        the_file.close()
        return True
    else:
        return False

def help_dialog(parent_window):
    """Dialog that shows user the help file. Takes a parent window as anchor"""
    tkMessageBox.showinfo("Help", "Not implemented, check back later.")
    
def about_dialog(parent_window):
    """Dialog that shows user information about the program."""
    tkMessageBox.showinfo("About", "Made by James Wang, 4 Jun 2013")

def main():
    root = Tk()
    root.title("Simple Text Editor")
    EditorWindow(root)
    mainloop()
    exit()

if __name__ == "__main__":
    main()
