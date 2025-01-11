"""
Add Students List Page
"""


import tkinter as tk
from Conn import Conn
from tkinter import messagebox

class PageOne(tk.Frame):

    last_list = None


    # Constructor
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.display_page(controller)


    # Load data from database
    def load(self):

        conn = Conn.connect()

        try:

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            results = cursor.fetchall()

            last_list = ""
            for row in results:
                first_name = row[1]
                last_name = row[2]
                email_address = row[3]
                last_list = last_list + first_name + last_name + email_address
            
            # Only rebuild list box if the data has changed in the database
            rebuild = False
            if(self.last_list is None):
                rebuild = True

            elif(last_list != self.last_list):
                rebuild = True

            if(rebuild):
                self.name_listbox.delete(0, tk.END)

                for row in results:
                    first_name = row[1]
                    last_name = row[2]
                    email_address = row[3]
                    self.name_listbox.insert(tk.END, f"{first_name} {last_name}   {email_address}")

                # Store last list
                self.last_list = last_list

        except Exception as e:
            print("Error: ", e)
        finally:
            cursor.close()
            conn.close()



    # Update data
    def update(self):
        self.load()
        self.after(1000, self.update)


    # Add a new student
    def add_student(self):

        # Get the fields 
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email_address = self.email_address_entry.get()

        if (first_name and last_name and email_address):

            conn = Conn.connect()

            try:

                cursor = conn.cursor()
                sql = "INSERT INTO students (`first_name`, `last_name`, `email_address`) VALUES ('" + first_name + "', '" + last_name + "', '" + email_address + "');"
                cursor.execute(sql)
                conn.commit()

            except Exception as e:
                print("Error: ", e)
                messagebox.showinfo("Error: ", e)
            finally:
                cursor.close()
                conn.close()

            self.first_name_entry.delete(0, tk.END)
            self.last_name_entry.delete(0, tk.END)
            self.email_address_entry.delete(0, tk.END)

            self.load()


    def display_page(self, controller):
        label = tk.Label(self, text="Students")
        label.pack(pady=10, padx=10)


        # Scrollbar for the listbox
        scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox to display names
        self.name_listbox = tk.Listbox(self, width=50, height=10, yscrollcommand=scrollbar.set)
        self.name_listbox.pack(padx=20)
        scrollbar.config(command=self.name_listbox.yview)
        
        # Frame for the name entry and submission
        entry_frame = tk.Frame(self)
        entry_frame.pack(pady=10)

        # Entry widgets for first and last names
        self.first_name_entry = tk.Entry(entry_frame, width=25)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)
        self.last_name_entry = tk.Entry(entry_frame, width=25)
        self.last_name_entry.grid(row=1, column=1, padx=5, pady=5)
        self.email_address_entry = tk.Entry(entry_frame, width=25)
        self.email_address_entry.grid(row=2, column=1, padx=5, pady=5)


        # Labels for the entry widgets
        self.first_name_label = tk.Label(entry_frame, text="First Name:")
        self.first_name_label.grid(row=0, column=0)
        self.last_name_label = tk.Label(entry_frame, text="Last Name:")
        self.last_name_label.grid(row=1, column=0)
        self.email_address_label = tk.Label(entry_frame, text="Email Address:")
        self.email_address_label.grid(row=2, column=0)

        # Button to add new name to the list
        add_button = tk.Button(entry_frame, text="Add Name", command=self.add_student)
        add_button.grid(row=3, columnspan=4, pady=5)

        button = tk.Button(self, text="Back to Start",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        # Load data when page is created and start update process
        self.update()

