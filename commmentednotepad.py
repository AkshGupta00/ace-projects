import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo, showerror
import os
import mysql.connector as sql

# Define a class for the application window


class screen:
    def __init__(self):
        self.root = tk.Tk()  # Create the main application window
        self.root.geometry("600x400")  # Set the window size
        # Set the window title
        self.root.title("Enter mysql username and password")
        self.username_var = tk.StringVar()
        self.passw_var = tk.StringVar()
        username_label = tk.Label(
            self.root, text='Username', font=('calibre', 10, 'bold'))
        username_entry = tk.Entry(
            self.root, textvariable=self.username_var, font=('calibre', 10, 'normal'))
        passw_label = tk.Label(self.root, text='Password',
                               font=('calibre', 10, 'bold'))
        passw_entry = tk.Entry(self.root, textvariable=self.passw_var, font=(
            'calibre', 10, 'normal'), show='*')
        sub_btn = tk.Button(self.root, text='Submit', command=self.connect)
        # Bind the Enter key to the 'connect' method
        self.root.bind('<Return>', self.connect)
        username_label.grid(row=0, column=0)
        username_entry.grid(row=0, column=1)
        passw_label.grid(row=1, column=0)
        passw_entry.grid(row=1, column=1)
        sub_btn.grid(row=2, column=1)
        self.root.mainloop()  # Start the main GUI event loop

    def destroy_all_widgets(self):
        # Remove all widgets from the current window
        for widget in self.root.winfo_children():
            widget.destroy()

    def notepad(self, userpath=None):
        # creating and editing notes
        def NewFile(event=None):
            # deletes all data from textarea and changes the title to make it look like a unused screen is created
            Textarea.delete(1.0, tk.END)
            self.root.title("Untitled.txt - Notepad")

        def OpenFile(event=None):
            # opens new file
            nonlocal userpath
            userpath = askopenfilename(defaultextension=".txt", filetypes=[
                                       ("all files", "*.*"), ("text documents", "*.txt")])  # reads file path form user
            if userpath == "":
                userpath = None
            else:
                self.root.title(os.path.basename(userpath)+"-notepad")
                # deletes every thing from textarea
                Textarea.delete(1.0, tk.END)
                f = open(userpath, "r")
                # inserts data from file to textarea
                Textarea.insert(1.0, f.read())
                f.close()

        def SaveFile(event=None):
            # saves file
            nonlocal userpath
            mycursor = self.mydb.cursor()

            if userpath == None:
                # if file is new then ask for name of this new file and path for this file
                userpath = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes=[
                                             ("all file", "*.*"), ("text document", "*.txt")])
                if userpath == "":
                    userpath = None
                else:
                    f = open(userpath, "w")  # open file in write mode
                    # write all data from textarea to file
                    f.write(Textarea.get(1.0, tk.END))
                    f.close()  # close file
                    self.root.title(os.path.basename(userpath)+"- Notepad")

                mycursor.execute("INSERT INTO notes (head, path) VALUES (%s, %s)",
                                 (os.path.basename(userpath), userpath))
                self.mydb.commit()  # insert file name and file path into database
            else:
                f = open(userpath, "w")  # open file in write mode
                # write all data from textarea to file
                f.write(Textarea.get(1.0, tk.END))
                f.close()  # close file
                self.root.title(os.path.basename(userpath)+"- Notepad")

        def saveasfile():
            # saving this file as a new one
            nonlocal userpath
            mycursor = self.mydb.cursor()
            userpath = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes=[
                                         ("all file", "*.*"), ("text document", "*.txt")])  # asking name and path for this file
            # creating and opning this file in write mode
            f = open(userpath, "w")
            # write data from text area to file
            f.write(Textarea.get(1.0, tk.END))
            f.close()  # close file
            # change title of the screen
            self.root.title(os.path.basename(userpath)+"- Notepad")
            mycursor.execute("INSERT INTO notes (head, path) VALUES (%s, %s)",
                             (os.path.basename(userpath), userpath))
            self.mydb.commit()  # insert file name and file path into database

        def exitapp(event=None):
            # function to exit the program
            self.root.destroy()

        def cut(event=None):
            # function to cut data
            Textarea.event_generate(("<<Cut>>"))

        def copy(event=None):
            # function to copy data
            Textarea.event_generate(("<<Copy>>"))

        def paste(event=None):
            # function to paste data
            Textarea.event_generate(("<<Paste>>"))

        def infobox():
            # function to tell information about this program
            showinfo("info", "this is a notepad made by Aksh Gupta")

        self.destroy_all_widgets()  # distroys all widgets to get a clean screen
        self.root.title("new note")  # changes title
        Textarea = tk.Text(self.root)  # create a textarea for the notepad
        Textarea.pack(fill="both", expand=True)
        scrollBar = tk.Scrollbar(Textarea)  # creates scrollbar for the notepad
        scrollBar.pack(side="right", fill="y")
        scrollBar.config(command=Textarea.yview)
        Textarea.config(yscrollcommand=scrollBar.set)
        Menu = tk.Menu(self.root)  # create menubar for the notepad

        # create submenu(filemenu) for the notepad
        filemenu = tk.Menu(Menu, tearoff=0)
        filemenu.add_command(label="new", command=NewFile)
        filemenu.add_command(label="open", command=OpenFile)
        filemenu.add_command(label="save", command=SaveFile)
        filemenu.add_command(label="save as", command=saveasfile)
        filemenu.add_command(label="exit", command=exitapp)
        Menu.add_cascade(label="File", menu=filemenu)

        # create submenu(Editmenu) for the notepad
        Editmenu = tk.Menu(Menu, tearoff=0)
        Editmenu.add_command(label="cut", command=cut)
        Editmenu.add_command(label="copy", command=copy)
        Editmenu.add_command(label="paste", command=paste)

        Menu.add_cascade(label="Edit", menu=Editmenu)
        # create a command option info on menubar
        Menu.add_command(label='info', command=infobox)
        self.root.config(menu=Menu)
        self.root.bind("<Control-s>", SaveFile)  # shortcut for save
        self.root.bind("<Control-n>", NewFile)  # shortcut for new
        self.root.bind("<Control-o>", OpenFile)  # shortcut for open
        self.root.bind("<Control-c>", copy)  # shortcut for copy
        self.root.bind("<Control-x>", cut)  # shortcut for cut
        self.root.bind("<Control-v>", paste)  # shortcut for paste
        self.root.bind("<Alt-Key-F4>", exitapp)  # shortcut for exit

        if (userpath != None):
            # checks if this is opning a already existing file if yes then do the same as openfile function
            self.root.title(os.path.basename(userpath)+"-notepad")
            Textarea.delete(1.0, tk.END)
            f = open(userpath, "r")
            Textarea.insert(1.0, f.read())
            f.close()

    def connect(self, event=None):
        # Method for establishing a MySQL database connection
        try:
            self.mydb = sql.connect(
                host="localhost", user=self.username_var.get(), password=self.passw_var.get())
            if self.mydb.is_connected():
                showinfo(
                    "Connected", "Successfully connected to the MySQL database.")

                mycursor = self.mydb.cursor()
                # Check and create the 'notepad' database and 'notes' table
                mycursor.execute("SHOW DATABASES")
                databases = [i[0] for i in mycursor]

                if "notepad" not in databases:
                    mycursor.execute("CREATE DATABASE notepad")

                mycursor.execute("USE notepad")
                mycursor.execute("SHOW TABLES")
                tables = [i[0] for i in mycursor]

                if "notes" not in tables:
                    mycursor.execute(
                        "CREATE TABLE notes (head VARCHAR(30), path VARCHAR(255))")
                    showinfo("Table Created",
                             "The 'notes' table has been created.")
                self.selection()  # Display the list of notes
        except sql.Error as e:
            showerror("Error", "Connection error: " + str(e))

    def selection(self):
        # Display a list of notes from the 'notes' table in the database
        self.root.title("select notes")
        self.destroy_all_widgets()
        mycursor = self.mydb.cursor()
        mycursor.execute("select * from notes")
        r = 0
        for i in mycursor:
            b = tk.Button(
                self.root, text=i[0], command=lambda path=i[1]: self.notepad(path))
            b.grid(row=r, column=0)
            l = tk.Label(self.root, text=i[1])
            l.grid(row=r, column=1)
            r += 1
        b = tk.Button(self.root, text="new++",
                      command=self.notepad).grid(row=r, column=0)


# Create an instance of the 'screen' class to start the application
a = screen()