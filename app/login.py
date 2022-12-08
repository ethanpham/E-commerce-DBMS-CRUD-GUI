import tkinter as tk
from tkinter import messagebox
import customtkinter

class Login(customtkinter.CTkFrame):
    
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.controller = controller
        
        self.placeHolder1 = tk.StringVar()
        self.placeHolder2 = tk.StringVar()
        
        self.titleLabel = customtkinter.CTkLabel(self, 
                                            text="E-commerce Database Management System CRUD", 
                                            text_font=('Segoe Ui Bold', 24),
                                            text_color="#E5E5E5")
        self.titleLabel.grid(row=0, column=0, columnspan=10, padx=250, pady=(100,0))
        
        self.loginFrame = customtkinter.CTkFrame(self, width=1200, height=600, corner_radius=28, fg_color=("#E5E5E5"))
        self.loginFrame.grid(row=2, column=0, columnspan=10, sticky="nwe", padx=265, pady=(60, 30))
        
        self.info = customtkinter.CTkLabel(self.loginFrame, text="Login", text_font=('Segoe Ui Bold', 18), text_color="#1F6AA5")
        self.info.grid(row=0, column=0, columnspan=4, sticky="nwe", padx=360, pady=(20, 30))

        self.label1 = customtkinter.CTkLabel(self.loginFrame, text = "Username", text_font=('Segoe Ui Bold', 14), text_color="#1F6AA5")
        self.label2 = customtkinter.CTkLabel(self.loginFrame, text = "Password", text_font=('Segoe Ui Bold', 14), text_color="#1F6AA5")
        
        self.label1.grid(row=1, column=0, padx=(20,0), pady=5)
        self.label2.grid(row=2, column=0, padx=(20,0), pady=5)

        self.entry1 = customtkinter.CTkEntry(self.loginFrame, width=480, height=40, text_font=('Segoe Ui', 10), textvariable = self.placeHolder1)
        self.entry2 = customtkinter.CTkEntry(self.loginFrame, width=480, height=40, text_font=('Segoe Ui', 10), textvariable = self.placeHolder2)

        self.entry1.grid(row=1, column=1, pady=(10,20))
        self.entry2.grid(row=2, column=1, pady=(10,10))
        
        self.button = customtkinter.CTkButton(self.loginFrame, 
                                          text="Login", 
                                          text_font=('Segoe Ui Bold', 12), 
                                          width=140, 
                                          height=40, 
                                          corner_radius=8, 
                                          command=self.login)
        
        self.button.grid(row=3, column=0, columnspan=4, padx=200, pady=(20,30))
        
    def login(self):
        self.username = str(self.entry1.get())
        self.password = str(self.entry2.get())
        if self.username == "admin" and self.password == "123":
            self.controller.loggedIn = "admin"
            return self.controller.showFrame("Landing")
        elif self.username == "buyer" and self.password == "123":
            self.controller.loggedIn = "buyer"
            return self.controller.showFrame("Landing")
        elif self.username == "seller" and self.password == "123":
            self.controller.loggedIn = "seller"
            return self.controller.showFrame("Landing")
        else:
            messagebox.showinfo("Error!", "Username not exists or the password is wrong!")
            return