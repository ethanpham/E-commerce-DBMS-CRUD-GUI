import sys
sys.dont_write_bytecode = True

from tkinter import *
from tkinter import messagebox
import customtkinter
import pymysql.cursors
from itertools import chain
from login import Login
from landing import Landing
from userMenu.userList import UserList
from userMenu.creditInformation import CreditInformation
from sellerMenu.sellerList import SellerList; from sellerMenu.personalAccount import PersonalAccount; from sellerMenu.businessAccount import BusinessAccount; from sellerMenu.brandAccount import BrandAccount
from sellerMenu.productList import ProductList; from sellerMenu.couponList import CouponList; from sellerMenu.couponForProduct import CouponForProduct
from buyerMenu.buyerList import BuyerList; from buyerMenu.buyerFavoriteStore import BuyerFavoriteStore; from buyerMenu.couponOwnByBuyer import CouponOwnByBuyer
from orderMenu.orderList import OrderList; from orderMenu.productBoughtInOrder import ProductBoughtInOrder; from orderMenu.couponAppliedInOrder import CouponAppliedInOrder
from shipperMenu.shipperList import ShipperList; from shipperMenu.vehicleList import VehicleList
from shipperMenu.vehicleAssignedForShipper import VehicleAssignedForShipper; from shipperMenu.orderAssignedForShipper import OrderAssignedForShipper; from shipperMenu.route import Route

class App(customtkinter.CTk):
    
    APP_NAME = "E-commerce Database Management System CRUD"
    WIDTH = 1400
    HEIGHT = 800
    
    def __init__(self):
        super().__init__()
        
        self.title(self.APP_NAME)
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.minsize(self.WIDTH, self.HEIGHT)
        self.maxsize(self.WIDTH, self.HEIGHT)
        self.resizable(False, False)
        
        self.tk.call("source", "azure.tcl")
        self.tk.call("set_theme", "dark")

        entityMenu = Menu(self)
        self.config(menu=entityMenu)
        
        self.loggedIn = "logout"
        
        # User Menu
        userMenu = Menu(entityMenu)
        entityMenu.add_cascade(label="User", menu=userMenu)
        
        userMenu.add_command(label="User List", command=lambda: self.showFrame("UserList"))
        userMenu.add_separator()
        userMenu.add_command(label="Credit Information", command=lambda: self.showFrame("CreditInformation"))
        
        # Seller Menu
        sellerMenu = Menu(entityMenu)
        entityMenu.add_cascade(label="Seller", menu=sellerMenu)
        
        sellerMenu.add_command(label="Seller List", command=lambda: self.showFrame("SellerList"))
        sellerMenu.add_separator()
        sellerMenu.add_command(label="Personal Account", command=lambda: self.showFrame("PersonalAccount"))
        sellerMenu.add_command(label="Business Account", command=lambda: self.showFrame("BusinessAccount"))
        sellerMenu.add_command(label="Brand Account", command=lambda: self.showFrame("BrandAccount"))
        sellerMenu.add_separator()
        sellerMenu.add_command(label="Product List", command=lambda: self.showFrame("ProductList"))
        sellerMenu.add_command(label="Coupon List", command=lambda: self.showFrame("CouponList"))
        sellerMenu.add_command(label="Coupon For Product", command=lambda: self.showFrame("CouponForProduct"))
        
        # Buyer Menu
        buyerMenu = Menu(entityMenu)
        entityMenu.add_cascade(label="Buyer", menu=buyerMenu)
        
        buyerMenu.add_command(label="Buyer List", command=lambda: self.showFrame("BuyerList")) 
        buyerMenu.add_separator()
        buyerMenu.add_command(label="Buyer Favorite Store", command=lambda: self.showFrame("BuyerFavoriteStore"))
        buyerMenu.add_command(label="Coupon Own By Buyer", command=lambda: self.showFrame("CouponOwnByBuyer"))
        
        # Order Menu
        orderMenu = Menu(entityMenu)
        entityMenu.add_cascade(label="Order", menu=orderMenu)
        
        orderMenu.add_command(label="Order List", command=lambda: self.showFrame("OrderList"))
        orderMenu.add_separator()
        orderMenu.add_command(label="Product Bought In Order", command=lambda: self.showFrame("ProductBoughtInOrder"))
        orderMenu.add_command(label="Coupon Applied In Order", command=lambda: self.showFrame("CouponAppliedInOrder"))
        
        # Shipper Menu
        shipperMenu = Menu(entityMenu)
        entityMenu.add_cascade(label="Shipper", menu=shipperMenu)
        
        shipperMenu.add_command(label="Shipper List", command=lambda: self.showFrame("ShipperList"))
        shipperMenu.add_command(label="Vehicle List", command=lambda: self.showFrame("VehicleList"))
        shipperMenu.add_separator()
        shipperMenu.add_command(label="Vehicle Assigned For Shipper", command=lambda: self.showFrame("VehicleAssignedForShipper"))
        shipperMenu.add_command(label="Order Assigned For Shipper", command=lambda: self.showFrame("OrderAssignedForShipper"))
        shipperMenu.add_command(label="Route", command=lambda: self.showFrame("Route"))

        container = customtkinter.CTkFrame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.buyerFrames = {}
        self.sellerFrames ={}

        for tableFrame in (Login,
                           Landing, 
                           UserList, CreditInformation,
                           SellerList, PersonalAccount, BusinessAccount, BrandAccount,
                           ProductList, CouponList, CouponForProduct,
                           BuyerList, BuyerFavoriteStore, CouponOwnByBuyer,
                           OrderList, ProductBoughtInOrder, CouponAppliedInOrder,
                           ShipperList, VehicleList,
                           VehicleAssignedForShipper, OrderAssignedForShipper, Route
                           ):

            if tableFrame in (Login,
                            Landing, 
                            BuyerList, BuyerFavoriteStore, CouponOwnByBuyer,
                            OrderList, ProductBoughtInOrder, CouponAppliedInOrder):
                page_name = tableFrame.__name__
                frame = tableFrame(parent=container, controller=self)
                self.buyerFrames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")
            if tableFrame in (Login,
                            Landing, 
                            SellerList, PersonalAccount, BusinessAccount, BrandAccount,
                            ProductList, CouponList, CouponForProduct,
                            OrderList, ProductBoughtInOrder, CouponAppliedInOrder,
                            ShipperList, VehicleList,
                            VehicleAssignedForShipper, OrderAssignedForShipper, Route):
                page_name = tableFrame.__name__
                frame = tableFrame(parent=container, controller=self)
                self.sellerFrames[page_name] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            page_name = tableFrame.__name__
            frame = tableFrame(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("Login")

    def pressed(self):
        self.pressLabel = customtkinter.CTkLabel(self, text="Switch to this Page").pack()

    def showFrame(self, page_name):
        if self.loggedIn != "logout" or page_name == "Login":
            if page_name == "Login":
                frame = self.frames[page_name]
                frame.tkraise()
            elif self.loggedIn == "admin":
                frame = self.frames[page_name]
                frame.tkraise()
            elif self.loggedIn == "buyer" and page_name in self.buyerFrames:
                frame = self.buyerFrames[page_name]
                frame.tkraise()
            elif self.loggedIn == "seller" and page_name in self.sellerFrames: 
                frame = self.sellerFrames[page_name]
                frame.tkraise() 
            else:
                messagebox.showinfo("Error!", "You do not have the privilege to access other tables!")
                return
        else:
            messagebox.showinfo("Error!", "You have to log in first!")
            return
        
    def connection(self):
        dbConnection = pymysql.connect(
            host = 'localhost',
            user = 'root', 
            password = '190802',
            db = 'ecom',
        )
        return dbConnection

    def refreshTable(self, child):
        for data in child.tree.get_children():
            child.tree.delete(data)

        for array in self.read(child):
            child.tree.insert(parent = '', index = 'end', iid=array, text = "", values=(array), tag = "oddrow")

        child.tree.tag_configure('oddrow', font=('Segoe Ui', 10))
        child.tree.grid(row=12, column=0, columnspan=7, padx=50, pady=50)
        
    def setPlaceHolder(self, child, word, num):
        if num == 1:
            child.placeHolder1.set(word)
        if num == 2:
            child.placeHolder2.set(word)
        if num == 3:
            child.placeHolder3.set(word)
        if num == 4:
            child.placeHolder4.set(word)
        if num == 5:
            child.placeHolder5.set(word)
        if num == 6:
            child.placeHolder6.set(word)
        if num == 7:
            child.placeHolder7.set(word)
    
    def read(self, child):
        dbConnection = self.connection()
        cursor = dbConnection.cursor()
        cursor.callproc('READTABLE', (child.TABLE,))
        results = cursor.fetchall()
        dbConnection.commit()
        dbConnection.close()
        return results

    def add(self, child):
        attribute1 = str(child.entry1.get())
        attribute2 = str(child.entry2.get())
        attribute3 = str(child.entry3.get())
        attribute4 = str(child.entry4.get())
        attribute5 = str(child.entry5.get())
        attribute6 = str(child.entry6.get())
        attribute7 = str(child.entry7.get())
        
        attributes = list(chain(attribute1, attribute2, attribute3, attribute4, attribute5, attribute6, attribute7))
        
        for num in range(0, child.NUMBER_OF_ATTRIBUTE):
            if (len(attributes[num]) == 0 or attributes[num].isspace() == 1): 
                messagebox.showinfo("Error!", "Please fill up the blank entry.")
                return
        else:
            try:
                dbConnection = self.connection()
                cursor = dbConnection.cursor()
                cursor.callproc('ADDVALUE', (child.TABLE, attribute1, attribute2, attribute3, attribute4, attribute5, attribute6, attribute7,))
                dbConnection.commit()
                dbConnection.close()
            except Exception as e:
                messagebox.showinfo(f"Error!", {e})
                return

        self.refreshTable(child)

    def delete(self, child):
        decision = messagebox.askquestion("Warning!", "This will delete the data directly from the table. Do you want to continue?")
        if decision != "yes":
            return 
        else:
            if not child.tree.selection():
                messagebox.showinfo("Error!", "You have not chosen the data from the table.")
                return 
            else:
                selectedItem = child.tree.selection()[0]
                deleteData = str(selectedItem.split( )[0])
                try:
                    dbConnection = self.connection()
                    cursor = dbConnection.cursor()
                    cursor.callproc('DELETEVALUE', (child.TABLE, deleteData, "", "",))
                    dbConnection.commit()
                    dbConnection.close()
                except Exception as e:
                    messagebox.showinfo(f"Error!", {e})
                    return

                self.refreshTable(child)
                
    def search(self, child):
        attribute1 = str(child.entry1.get())
        attribute2 = str(child.entry2.get())
        attribute3 = str(child.entry3.get())
        
        dbConnection = self.connection()
        cursor = dbConnection.cursor()
        cursor.callproc('SEARCHVALUE', (child.TABLE, attribute1, attribute2, attribute3,))
        try:
            result = cursor.fetchall()
            
            for num in range(0, child.NUMBER_OF_ATTRIBUTE):
                self.setPlaceHolder(child, result[0][num], (num + 1))

            dbConnection.commit()
            dbConnection.close()
        except:
            messagebox.showinfo("No data found.")

    def update(self, child):
        selectedId = ""
        try:
            selectedItem = child.tree.selection()[0]
            selectedId = str(selectedItem.split( )[0])
        except:
            messagebox.showinfo("Error!", "Please select a data row.")

        attribute1 = str(child.entry1.get())
        attribute2 = str(child.entry2.get())
        attribute3 = str(child.entry3.get())
        attribute4 = str(child.entry4.get())
        attribute5 = str(child.entry5.get())
        attribute6 = str(child.entry6.get())
        attribute7 = str(child.entry7.get())

        attributes = list(chain(attribute1, attribute2, attribute3, attribute4, attribute5, attribute6, attribute7))
        
        for num in range(0, child.NUMBER_OF_ATTRIBUTE):
            if (len(attributes[num]) == 0 or attributes[num].isspace() == 1): 
                messagebox.showinfo("Error!", "Please fill up the blank entry.")
                return
        else:
            try:
                dbConnection = self.connection()
                cursor = dbConnection.cursor()
                cursor.callproc('UPDATEVALUE', (child.TABLE, attribute1, attribute2, attribute3, attribute4, attribute5, attribute6, attribute7,))
                dbConnection.commit()
                dbConnection.close()
            except Exception as e:
                messagebox.showinfo(f"Error!", {e})
                return

        self.refreshTable(child)
        
    def exit(self):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()