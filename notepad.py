import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter.messagebox import showinfo,showerror
import os
import mysql.connector as sql

def destroy_all_widgets(parent_widget):
    for widget in parent_widget.winfo_children():
        widget.destroy()
def selection():
    global mydb
    def oldfile(File):
        global file
        def NewFile():
            Textarea.delete(1.0,tk.END)
            root.title("Untitled.txt - Notepad")
        def OpenFile():
            global file
            file=askopenfilename(defaultextension=".txt",filetypes=[("all files","*.*"),("text documents","*.txt")])
            if file=="":
                file=None
            else:
                root.title(os.path.basename(file)+"-notepad")
                Textarea.delete(1.0,tk.END)
                f=open(file,"r")
                Textarea.insert(1.0,f.read())
                f.close()
        def SaveFile():
            global file
            global mydb
            mycursor = mydb.cursor()

            if file ==None:
                file=asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("all file","*.*"),("text document","*.txt")])
                if file=="":
                    file=None
                else:
                    f=open(file,"w")
                    f.write(Textarea.get(1.0,tk.END))
                    f.close()
                    root.title(os.path.basename(file)+"- Notepad")
                    print("file saved")
                
                mycursor.execute("INSERT INTO notes (head, path) VALUES (%s, %s)", (os.path.basename(file), file))
                mydb.commit()
            else:        
                f=open(file,"w")
                f.write(Textarea.get(1.0,tk.END))
                f.close()
                root.title(os.path.basename(file)+"- Notepad")

        def saveasfile():
            global file
            global mydb
            mycursor=mydb.cursor()
            file=asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("all file","*.*"),("text document","*.txt")])
            f=open(file,"w")
            f.write(Textarea.get(1.0,tk.END))
            f.close()
            root.title(os.path.basename(file)+"- Notepad")
            mycursor.execute("INSERT INTO notes (head, path) VALUES (%s, %s)", (os.path.basename(file), file))
            mydb.commit()


        def exitapp():
            root.destroy()
        def cut():
            Textarea.event_generate(("<<Cut>>"))
        def copy():
            Textarea.event_generate(("<<Copy>>"))
        def paste():
            Textarea.event_generate(("<<Paste>>"))
            
        def infobox():
            showinfo("info","this is a notepad made by Aksh Gupta")

        destroy_all_widgets(root)
        file=File
        root.title(os.path.basename(file)+"-Notepad") 
        Textarea=tk.Text(root)
        Textarea.pack(fill="both", expand=True)  
        scrollBar=tk.Scrollbar(Textarea)
        scrollBar.pack(side="right",fill="y")
        scrollBar.config(command=Textarea.yview)
        Textarea.config(yscrollcommand=scrollBar.set)
        Menu=tk.Menu(root)
        filemenu=tk.Menu(Menu,tearoff=0)
        filemenu.add_command(label="new",command=NewFile)
        filemenu.add_command(label="open",command=OpenFile)
        filemenu.add_command(label="save",command=SaveFile)
        filemenu.add_command(label="save as",command=saveasfile)
        filemenu.add_command(label="exit",command=exitapp)
        Menu.add_cascade(label="File",menu=filemenu)

        Editmenu=tk.Menu(Menu,tearoff=0)
        Editmenu.add_command(label="cut",command=cut)
        Editmenu.add_command(label="copy",command=copy)
        Editmenu.add_command(label="paste",command=paste)
        Menu.add_cascade(label="Edit",menu=Editmenu)
        
        Menu.add_command(label='info',command=infobox)
        
        root.config(menu=Menu)

        f=open(File,"r")
        Textarea.insert(1.0,f.read())
        f.close()
    
    def create_notepad():
        def NewFile():
            Textarea.delete(1.0,tk.END)
            root.title("Untitled.txt - Notepad")
        def OpenFile():
            global file
            file=askopenfilename(defaultextension=".txt",filetypes=[("all files","*.*"),("text documents","*.txt")])
            if file=="":
                file=None
            else:
                root.title(os.path.basename(file)+"-notepad")
                Textarea.delete(1.0,tk.END)
                f=open(file,"r")
                Textarea.insert(1.0,f.read())
                f.close()
        def SaveFile():
            global file
            global mydb
            mycursor = mydb.cursor()

            if file ==None:
                file=asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("all file","*.*"),("text document","*.txt")])
                if file=="":
                    file=None
                else:
                    f=open(file,"w")
                    f.write(Textarea.get(1.0,tk.END))
                    f.close()
                    root.title(os.path.basename(file)+"- Notepad")
                    print("file saved")
                
                mycursor.execute("INSERT INTO notes VALUE(%s, %s)", (os.path.basename(file), file))
                mydb.commit()
            else:        
                f=open(file,"w")
                f.write(Textarea.get(1.0,tk.END))
                f.close()
                root.title(os.path.basename(file)+"- Notepad")

        def saveasfile():
            global file
            global mydb
            mycursor=mydb.cursor()
            file=asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("all file","*.*"),("text document","*.txt")])
            f=open(file,"w")
            f.write(Textarea.get(1.0,tk.END))
            f.close()
            root.title(os.path.basename(file)+"- Notepad")
            mycursor.execute("INSERT INTO notes VALUE(%s, %s)", (os.path.basename(file), file))
            mydb.commit()


        def exitapp():
            root.destroy()
        def cut():
            Textarea.event_generate(("<<Cut>>"))
        def copy():
            Textarea.event_generate(("<<Copy>>"))
        def paste():
            Textarea.event_generate(("<<Paste>>"))
            
        def infobox():
            showinfo("info","this is a notepad made by Aksh Gupta")

        destroy_all_widgets(root)
        root.title("new note") 
        Textarea=tk.Text(root)
        Textarea.pack(fill="both", expand=True)  
        scrollBar=tk.Scrollbar(Textarea)
        scrollBar.pack(side="right",fill="y")
        scrollBar.config(command=Textarea.yview)
        Textarea.config(yscrollcommand=scrollBar.set)
        Menu=tk.Menu(root)
        filemenu=tk.Menu(Menu,tearoff=0)
        filemenu.add_command(label="new",command=NewFile)
        filemenu.add_command(label="open",command=OpenFile)
        filemenu.add_command(label="save",command=SaveFile)
        filemenu.add_command(label="save as",command=saveasfile)
        filemenu.add_command(label="exit",command=exitapp)
        Menu.add_cascade(label="File",menu=filemenu)

        Editmenu=tk.Menu(Menu,tearoff=0)
        Editmenu.add_command(label="cut",command=cut)
        Editmenu.add_command(label="copy",command=copy)
        Editmenu.add_command(label="paste",command=paste)
        Menu.add_cascade(label="Edit",menu=Editmenu)
        
        Menu.add_command(label='info',command=infobox)
        
        root.config(menu=Menu)

    username_label.destroy()
    username_entry.destroy()
    passw_label.destroy()
    passw_entry.destroy()
    sub_btn.destroy()
    root.title("select notes")
    mycursor=mydb.cursor()
    mycursor.execute("select * from notes")
    r=0
    for i in mycursor:
        b = tk.Button(root, text=i[0], command=lambda path=i[1]: oldfile(path))
        b.grid(row=r, column=0)
        l = tk.Label(root, text=i[1])
        l.grid(row=r, column=1)
        r += 1
    b=tk.Button(root,text="new++",command=create_notepad).grid(row=r,column=0)

def connect():
    global mydb
    try:
        mydb = sql.connect(host="localhost", user=username_var.get(), password=passw_var.get())
        if mydb.is_connected():
            showinfo("Connected", "Successfully connected to the MySQL database.")
            
            mycursor = mydb.cursor()
            mycursor.execute("SHOW DATABASES")
            databases = [i[0] for i in mycursor]

            if "notepad" not in databases:
                mycursor.execute("CREATE DATABASE notepad")

            mycursor.execute("USE notepad")
            mycursor.execute("SHOW TABLES")
            tables = [i[0] for i in mycursor]

            if "notes" not in tables:
                mycursor.execute("CREATE TABLE notes (head VARCHAR(30), path VARCHAR(255))")
                showinfo("Table Created", "The 'notes' table has been created.")
            selection()
    except sql.Error as e:
        showerror("Error", "Connection error: " + str(e))

        

if __name__=='__main__':
    file=None
    mydb=None
    root=tk.Tk()
    root.geometry("600x400")

    root.title("Enter mysql username and password") 


    username_var=tk.StringVar()
    passw_var=tk.StringVar()
    username_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
    username_entry = tk.Entry(root,textvariable = username_var, font=('calibre',10,'normal'))
    passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    sub_btn=tk.Button(root,text = 'Submit', command = connect)
    username_label.grid(row=0,column=0)
    username_entry.grid(row=0,column=1)
    passw_label.grid(row=1,column=0)
    passw_entry.grid(row=1,column=1)
    sub_btn.grid(row=2,column=1)
    root.mainloop()
    