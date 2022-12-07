import tkinter as tk
import customtkinter

class Landing(customtkinter.CTkFrame):
    
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        
        self.controller = controller
        
        self.titleLabel = customtkinter.CTkLabel(self, 
                                            text="E-commerce Database Management System CRUD", 
                                            text_font=('Segoe Ui Bold', 24),
                                            text_color="#E5E5E5")
        self.titleLabel.grid(row=0, column=0, columnspan=10, padx=220, pady=(100,0))
        self.info = customtkinter.CTkLabel(self, 
                                                   text="Welcome to E-commerce Database Management System CRUD\n\n" +
                                                        "See every entity and relationship table\n" +
                                                        "by choosing the table you want from the menu",
                                                   text_font=('Segoe Ui Bold', 16),
                                                   text_color="#1F6AA5",
                                                   width=950,
                                                   height=250,
                                                   corner_radius=28,
                                                   fg_color=("#E5E5E5")
                                                   )
        self.info.grid(row=2, column=0, columnspan=10, sticky="nwe", padx=220, pady=(60, 30))

        self.logoutButton = customtkinter.CTkButton(self, 
                                          text="Logout", 
                                          text_font=('Segoe Ui Bold', 12), 
                                          width=140, 
                                          height=40, 
                                          corner_radius=8, 
                                          command=self.logout)
        self.exitButton = customtkinter.CTkButton(self, 
                                          text="Exit App", 
                                          text_font=('Segoe Ui Bold', 12), 
                                          width=140, 
                                          height=40, 
                                          corner_radius=8, 
                                          command=lambda: controller.exit())
        self.logoutButton.grid(row=3, column=0, columnspan=10, padx=200, pady=(0,10))
        self.exitButton.grid(row=4, column=0, columnspan=10, padx=200, pady=(0,10))
        
    def logout(self):
        self.controller.logedIn = False
        return self.controller.showFrame("Login")
        