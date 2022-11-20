import pymysql.cursors
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter

class UserList(customtkinter.CTkFrame):
    TABLE = "USER"
    NUMBER_OF_ATTRIBUTE = 7
    ATTRIBUTE1 = "ID"
    ATTRIBUTE2 = "Name"
    ATTRIBUTE3 = "Sex"
    ATTRIBUTE4 = "Birthdate"
    ATTRIBUTE5 = "Phone"
    ATTRIBUTE6 = "Email"
    ATTRIBUTE7 = "Address"
    
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.controller = controller
        
        self.tree = ttk.Treeview(self, height=8)
        
        self.placeHolder1 = tk.StringVar()
        self.placeHolder2 = tk.StringVar()
        self.placeHolder3 = tk.StringVar()
        self.placeHolder4 = tk.StringVar()
        self.placeHolder5 = tk.StringVar()
        self.placeHolder6 = tk.StringVar()
        self.placeHolder7 = tk.StringVar()
        
        self.titleLabel = customtkinter.CTkLabel(self, 
                                                 text = "E-commerce Database Management System CRUD", 
                                                 text_font=('Segoe Ui Bold', 24),
                                                 text_color="#E5E5E5")
        self.titleLabel.grid(row=0, column=0, columnspan=10, padx=150, pady=(20,10))

        self.headingLabel = customtkinter.CTkLabel(self, 
                                                   text = "USER TABLE", 
                                                   text_font=('Segoe Ui Bold', 18),
                                                   text_color="#E5E5E5")
        self.headingLabel.grid(row=1, column=0, columnspan=10, padx=90, pady=(0,25))
        
        self.label1 = customtkinter.CTkLabel(self, text = self.ATTRIBUTE1, text_font=('Segoe Ui', 12))
        self.label2 = customtkinter.CTkLabel(self, text = self.ATTRIBUTE2, text_font=('Segoe Ui', 12))
        self.label3 = customtkinter.CTkLabel(self, text = self.ATTRIBUTE3, text_font=('Segoe Ui', 12))
        self.label4 = customtkinter.CTkLabel(self, text = self.ATTRIBUTE4, text_font=('Segoe Ui', 12))
        self.label5 = customtkinter.CTkLabel(self, text = self.ATTRIBUTE5, text_font=('Segoe Ui', 12))
        self.label6 = customtkinter.CTkLabel(self, text = self.ATTRIBUTE6, text_font=('Segoe Ui', 12))
        self.label7 = customtkinter.CTkLabel(self, text = self.ATTRIBUTE7, text_font=('Segoe Ui', 12))

        self.label1.grid(row=3, column=0, padx=(40,5), pady=5)
        self.label2.grid(row=4, column=0, padx=(40,5), pady=5)
        self.label3.grid(row=5, column=0, padx=(40,5), pady=5)
        self.label4.grid(row=6, column=0, padx=(40,5), pady=5)
        self.label5.grid(row=7, column=0, padx=(40,5), pady=5)
        self.label6.grid(row=8, column=0, padx=(40,5), pady=5)
        self.label7.grid(row=9, column=0, padx=(40,5), pady=5)

        self.entry1 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder1)
        self.entry2 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder2)
        self.entry3 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder3)
        self.entry4 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder4)
        self.entry5 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder5)
        self.entry6 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder6)
        self.entry7 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder7)

        # fg_color="#737373"
        
        self.entry1.grid(row=3, column=1, padx=(10,20), pady=0)
        self.entry2.grid(row=4, column=1, padx=(10,20), pady=0)
        self.entry3.grid(row=5, column=1, padx=(10,20), pady=0)
        self.entry4.grid(row=6, column=1, padx=(10,20), pady=0)
        self.entry5.grid(row=7, column=1, padx=(10,20), pady=0)
        self.entry6.grid(row=8, column=1, padx=(10,20), pady=0)
        self.entry7.grid(row=9, column=1, padx=(10,20), pady=0)
        
        # self.entry6.configure(state= "disabled")
        # self.entry7.configure(state= "disabled")

        self.addButton = customtkinter.CTkButton(self, text = "Add", text_font=('Segoe Ui', 11), command = self.add)
        self.updateButton = customtkinter.CTkButton(self, text = "Update", text_font=('Segoe Ui', 11), command = self.update)
        self.deleteButton = customtkinter.CTkButton(self, text = "Delete", text_font=('Segoe Ui', 11), command = self.delete)
        self.searchButton = customtkinter.CTkButton(self, text = "Search", text_font=('Segoe Ui', 11), command = self.search)
        self.selectButton = customtkinter.CTkButton(self, text = "Select", text_font=('Segoe Ui', 11), command = self.select)
        self.backToLandingButton = customtkinter.CTkButton(self, 
                                                        text = "Back To Landing", 
                                                        text_font=('Segoe Ui', 11),
                                                        fg_color="#1A5C41",
                                                        command=lambda: controller.showFrame("Landing"))

        self.addButton.grid(row=3, column=3, columnspan=1)
        self.updateButton.grid(row=4, column=3, columnspan=1)
        self.deleteButton.grid(row=5, column=3, columnspan=1)
        self.searchButton.grid(row=6, column=3, columnspan=1)
        self.selectButton.grid(row=7, column=3, columnspan=1)
        self.backToLandingButton.grid(row=8, column=3, columnspan=1)

        self.headingStyle = ttk.Style()
        self.headingStyle.configure("Treeview.Heading", font=('Segoe Ui Semibold', 11), rowheight=30)

        self.tree['columns'] = (self.ATTRIBUTE1, 
                                self.ATTRIBUTE2, 
                                self.ATTRIBUTE3, 
                                self.ATTRIBUTE4, 
                                self.ATTRIBUTE5, 
                                self.ATTRIBUTE6,
                                self.ATTRIBUTE7)

        # 1330
        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column(self.ATTRIBUTE1, anchor=W, width=80)
        self.tree.column(self.ATTRIBUTE2, anchor=W, width=220)
        self.tree.column(self.ATTRIBUTE3, anchor=W, width=90)
        self.tree.column(self.ATTRIBUTE4, anchor=W, width=190)
        self.tree.column(self.ATTRIBUTE5, anchor=W, width=120)
        self.tree.column(self.ATTRIBUTE6, anchor=W, width=170)
        self.tree.column(self.ATTRIBUTE7, anchor=W, width=390)

        self.tree.heading(self.ATTRIBUTE1, text = self.ATTRIBUTE1, anchor=W)
        self.tree.heading(self.ATTRIBUTE2, text = self.ATTRIBUTE2, anchor=W)
        self.tree.heading(self.ATTRIBUTE3, text = self.ATTRIBUTE3, anchor=W)
        self.tree.heading(self.ATTRIBUTE4, text = self.ATTRIBUTE4, anchor=W)
        self.tree.heading(self.ATTRIBUTE5, text = self.ATTRIBUTE5, anchor=W)
        self.tree.heading(self.ATTRIBUTE6, text = self.ATTRIBUTE6, anchor=W)
        self.tree.heading(self.ATTRIBUTE7, text = self.ATTRIBUTE7, anchor=W)

        self.rowStyle = ttk.Style()
        self.rowStyle.configure("Treeview", rowheight=30)
        
        self.refreshTable()
        
    def connection(self):
        dbConnection = pymysql.connect(
            host = 'localhost',
            user = 'root', 
            password = '',
            db = 'ecom',
        )
        return dbConnection

    def refreshTable(self):
        for data in self.tree.get_children():
            self.tree.delete(data)

        for array in self.read():
            self.tree.insert(parent = '', index = 'end', iid=array, text = "", values=(array), tag = "oddrow")

        self.tree.tag_configure('oddrow', font=('Segoe Ui', 10))
        self.tree.grid(row=12, column=0, columnspan=7, padx=50, pady=50)

    def setPlaceHolder(self,word,num):
        if num == 1:
            self.placeHolder1.set(word)
        if num == 2:
            self.placeHolder2.set(word)
        if num == 3:
            self.placeHolder3.set(word)
        if num == 4:
            self.placeHolder4.set(word)
        if num == 5:
            self.placeHolder5.set(word)
        if num == 6:
            self.placeHolder6.set(word)
        if num == 7:
            self.placeHolder7.set(word)

    def read(self):
        dbConnection = self.connection()
        cursor = dbConnection.cursor()
        cursor.execute("SELECT * FROM " + self.TABLE)
        results = cursor.fetchall()
        dbConnection.commit()
        dbConnection.close()
        return results

    def add(self):
        attribute1 = str(self.entry1.get())
        attribute2 = str(self.entry2.get())
        attribute3 = str(self.entry3.get())
        attribute4 = str(self.entry4.get())
        attribute5 = str(self.entry5.get())
        attribute6 = str(self.entry6.get())
        attribute7 = str(self.entry7.get())

        if (attribute1 == "" or attribute1 == " ") \
            or (attribute2 == "" or attribute2 == " ") \
            or (attribute3 == "" or attribute3 == " ") \
            or (attribute4 == "" or attribute4 == " ") \
            or (attribute5 == "" or attribute5 == " ") \
            or (attribute6 == "" or attribute6 == " ") \
            or (attribute7 == "" or attribute7 == " ") \
            :
            messagebox.showinfo("Error!", "Please fill up the blank entry.")
            return
        else:
            try:
                dbConnection = self.connection()
                cursor = dbConnection.cursor()
                cursor.execute("INSERT INTO " + self.TABLE + " VALUES ('" + attribute1 +
                               "','" + attribute2 +
                               "','" + attribute3 +
                               "','" + attribute4 +
                               "','" + attribute5 +
                               "','" + attribute6 +
                               "','" + attribute7 +
                               "') ")
                dbConnection.commit()
                dbConnection.close()
            except:
                messagebox.showinfo("Error!", "ID already exist.")
                return

        self.refreshTable()

    def delete(self):
        decision = messagebox.askquestion("Warning!", "This will delete the data directly from the table. Do you want to continue?")
        if decision != "yes":
            return 
        else:
            if not self.tree.selection():
                messagebox.showinfo("Error!", "You have not chosen the data from the table.")
                return 
            else:
                selectedItem = self.tree.selection()[0]
                deleteData = str(selectedItem.split( )[0])
                try:
                    dbConnection = self.connection()
                    cursor = dbConnection.cursor()
                    cursor.execute("DELETE FROM " + self.TABLE + " WHERE " + self.ATTRIBUTE1 + " = '" + str(deleteData) + "'")
                    dbConnection.commit()
                    dbConnection.close()
                except:
                    messagebox.showinfo("Error!", "Sorry an error occurred!")
                    return

                self.refreshTable()

    def select(self):
        try:
            selectedItem = self.tree.selection()[0]
            attribute1 = str(selectedItem.split( )[0])
            attribute2 = str(self.tree.item(selectedItem)['values'][1])
            attribute3 = str(self.tree.item(selectedItem)['values'][2])
            attribute4 = str(self.tree.item(selectedItem)['values'][3])
            attribute5 = str(self.tree.item(selectedItem)['values'][4])
            attribute6 = str(self.tree.item(selectedItem)['values'][5])
            attribute7 = str(self.tree.item(selectedItem)['values'][6])

            self.setPlaceHolder(attribute1,1)
            self.setPlaceHolder(attribute2,2)
            self.setPlaceHolder(attribute3,3)
            self.setPlaceHolder(attribute4,4)
            self.setPlaceHolder(attribute5,5)
            self.setPlaceHolder(attribute6,6)
            self.setPlaceHolder(attribute7,7)
        except:
            messagebox.showinfo("Error!", "Please select a data row.")

    def search(self):
        attribute1 = str(self.entry1.get())
        attribute2 = str(self.entry2.get())
        attribute3 = str(self.entry3.get())
        attribute4 = str(self.entry4.get())
        attribute5 = str(self.entry5.get())
        attribute6 = str(self.entry6.get())
        attribute7 = str(self.entry7.get())

        dbConnection = self.connection()
        cursor = dbConnection.cursor()
        cursor.execute("SELECT * FROM " + self.TABLE + " WHERE " + self.ATTRIBUTE1 + " = '" +  attribute1 +
                       "' or " + self.ATTRIBUTE2 + " = '" + attribute2 +
                       "' or " + self.ATTRIBUTE3 + " = '" + attribute3 +
                       "' or " + self.ATTRIBUTE4 + " = '" + attribute4 +
                       "' or " + self.ATTRIBUTE5 + " = '" + attribute5 +
                       "' or " + self.ATTRIBUTE6 + " = '" + attribute6 +
                       "' or " + self.ATTRIBUTE7 + " = '" + attribute7 +
                       "' ")  
        try:
            result = cursor.fetchall()

            for num in range(0,self.NUMBER_OF_ATTRIBUTE):
                self.setPlaceHolder(result[0][num],(num + 1))

            dbConnection.commit()
            dbConnection.close()
        except:
            messagebox.showinfo("Error!", "No data found.")

    def update(self):
        selectedId = ""
        try:
            selectedItem = self.tree.selection()[0]
            # selectedId = str(self.tree.item(selectedItem)['values'][0])
            selectedId = str(selectedItem.split( )[0])
        except:
            messagebox.showinfo("Error!", "Please select a data row.")

        attribute1 = str(self.entry1.get())
        attribute2 = str(self.entry2.get())
        attribute3 = str(self.entry3.get())
        attribute4 = str(self.entry4.get())
        attribute5 = str(self.entry5.get())
        attribute6 = str(self.entry6.get())
        attribute7 = str(self.entry7.get())

        if (attribute1 == "" or attribute1 == " ") \
            or (attribute2 == "" or attribute2 == " ") \
            or (attribute3 == "" or attribute3 == " ") \
            or (attribute4 == "" or attribute4 == " ") \
            or (attribute5 == "" or attribute5 == " ") \
            or (attribute6 == "" or attribute6 == " ") \
            or (attribute7 == "" or attribute7 == " ") \
            :
            messagebox.showinfo("Error!", "Please fill up the blank entry.")
            return
        else:
            try:
                dbConnection = self.connection()
                cursor = dbConnection.cursor()
                cursor.execute("UPDATE " + self.TABLE + " SET " + self.ATTRIBUTE1 + " = '" + attribute1 +
                               "', " + self.ATTRIBUTE2 + " = '" + attribute2 +
                               "', " + self.ATTRIBUTE3 + " = '" + attribute3 +
                               "', " + self.ATTRIBUTE4 + " = '" + attribute4 +
                               "', " + self.ATTRIBUTE5 + " = '" + attribute5 +
                               "', " + self.ATTRIBUTE6 + " = '" + attribute6 +
                               "', " + self.ATTRIBUTE7 + " = '" + attribute7 +
                               "' WHERE " + self.ATTRIBUTE1 + " = '" + selectedId + "' ")
                dbConnection.commit()
                dbConnection.close()
            except:
                messagebox.showinfo("Error!", "ID already exist.")
                return

        self.refreshTable()