import tkinter as tk
from Conn import Conn

class PageOne(tk.Frame):

    last_list = None

    def load(self):

        print("LOAD")
        conn = Conn.connect()

        try:

            print("Connection established")

            '''
            SELECT UPDATE_TIME
            FROM information_schema.tables
            WHERE table_schema = 'your_database' AND table_name = 'example';
            '''

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            results = cursor.fetchall()

            last_list = ""
            for row in results:
                first_name = row[1]
                last_name = row[2]
                email_address = row[3]
                last_list = last_list + first_name + last_name + email_address
            
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


    def update(self):
        self.load()
        self.after(1000, self.update)



    def add_name(self):

        # Get the first and last name from the entry widgets
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email_address = self.email_address_entry.get()

        if (first_name and last_name and email_address):

            conn = Conn.connect()

            try:

                cursor = conn.cursor()
                sql = "INSERT INTO students (`first_name`, `last_name`, `email_address`) VALUES ('" + first_name + "', '" + last_name + "', '" + email_address + "');"
                print(sql)
                cursor.execute(sql)
                conn.commit()

            except Exception as e:
                print("Error: ", e)
            finally:
                cursor.close()
                conn.close()

            self.first_name_entry.delete(0, tk.END)
            self.last_name_entry.delete(0, tk.END)
            self.email_address_entry.delete(0, tk.END)

            self.load()


    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
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
        add_button = tk.Button(entry_frame, text="Add Name", command=self.add_name)
        add_button.grid(row=3, columnspan=4, pady=5)

        button = tk.Button(self, text="Back to Start",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        # Load data when page is created and start update process
        self.update()

