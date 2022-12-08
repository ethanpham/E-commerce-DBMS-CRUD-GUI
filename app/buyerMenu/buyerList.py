import pymysql.cursors
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import customtkinter

class BuyerList(customtkinter.CTkFrame):
    TABLE = "BUYER"
    NUMBER_OF_ATTRIBUTE = 3
    ATTRIBUTE1 = "ID"
    ATTRIBUTE2 = "AccountType"
    ATTRIBUTE3 = "TotalMoneySpent"
    ATTRIBUTE4 = ""
    ATTRIBUTE5 = ""
    ATTRIBUTE6 = ""
    ATTRIBUTE7 = ""
    
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
                                                   text = "BUYER TABLE", 
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
        self.entry4 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder4, fg_color="#737373")
        self.entry5 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder5, fg_color="#737373")
        self.entry6 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder6, fg_color="#737373")
        self.entry7 = customtkinter.CTkEntry(self, width=600, text_font=('Segoe Ui', 10), textvariable = self.placeHolder7, fg_color="#737373")

        #, fg_color="#737373"
        
        self.entry1.grid(row=3, column=1, padx=(10,20), pady=0)
        self.entry2.grid(row=4, column=1, padx=(10,20), pady=0)
        self.entry3.grid(row=5, column=1, padx=(10,20), pady=0)
        self.entry4.grid(row=6, column=1, padx=(10,20), pady=0)
        self.entry5.grid(row=7, column=1, padx=(10,20), pady=0)
        self.entry6.grid(row=8, column=1, padx=(10,20), pady=0)
        self.entry7.grid(row=9, column=1, padx=(10,20), pady=0)
        
        self.entry4.configure(state= "disabled")
        self.entry5.configure(state= "disabled")
        self.entry6.configure(state= "disabled")
        self.entry7.configure(state= "disabled")

        self.addButton = customtkinter.CTkButton(self, text = "Add", text_font=('Segoe Ui', 11), command = lambda: controller.add(self))
        self.updateButton = customtkinter.CTkButton(self, text = "Update", text_font=('Segoe Ui', 11), command = lambda: controller.update(self))
        self.deleteButton = customtkinter.CTkButton(self, text = "Delete", text_font=('Segoe Ui', 11), command = lambda: controller.delete(self))
        self.searchButton = customtkinter.CTkButton(self, text = "Search", text_font=('Segoe Ui', 11), command = lambda: controller.search(self))
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

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column(self.ATTRIBUTE1, anchor=W, width=120)
        self.tree.column(self.ATTRIBUTE2, anchor=W, width=160)
        self.tree.column(self.ATTRIBUTE3, anchor=W, width=200)
        self.tree.column(self.ATTRIBUTE4, anchor=W, width=120)
        self.tree.column(self.ATTRIBUTE5, anchor=W, width=150)
        self.tree.column(self.ATTRIBUTE6, anchor=W, width=170)
        self.tree.column(self.ATTRIBUTE7, anchor=W, width=180)

        self.tree.heading(self.ATTRIBUTE1, text = self.ATTRIBUTE1, anchor=W)
        self.tree.heading(self.ATTRIBUTE2, text = self.ATTRIBUTE2, anchor=W)
        self.tree.heading(self.ATTRIBUTE3, text = self.ATTRIBUTE3, anchor=W)
        self.tree.heading(self.ATTRIBUTE4, text = self.ATTRIBUTE4, anchor=W)
        self.tree.heading(self.ATTRIBUTE5, text = self.ATTRIBUTE5, anchor=W)
        self.tree.heading(self.ATTRIBUTE6, text = self.ATTRIBUTE6, anchor=W)
        self.tree.heading(self.ATTRIBUTE7, text = self.ATTRIBUTE7, anchor=W)

        self.rowStyle = ttk.Style()
        self.rowStyle.configure("Treeview", rowheight=30)
        
        self.controller.refreshTable(self)

    def select(self):
        try:
            selectedItem = self.tree.selection()[0]
            attribute1 = str(selectedItem.split( )[0])
            attribute2 = str(self.tree.item(selectedItem)['values'][1])
            attribute3 = str(self.tree.item(selectedItem)['values'][2])

            self.controller.setPlaceHolder(self, attribute1, 1)
            self.controller.setPlaceHolder(self, attribute2, 2)
            self.controller.setPlaceHolder(self, attribute3, 3)
        except:
            messagebox.showinfo("Error!", "Please select a data row.")