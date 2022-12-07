import sys
sys.dont_write_bytecode = True

from tkinter import *
from tkinter import messagebox
import customtkinter
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
        
        self.logedIn = False
        
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
            page_name = tableFrame.__name__
            frame = tableFrame(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("Login")

    def pressed(self):
        self.pressLabel = customtkinter.CTkLabel(self, text="Switch to this Page").pack()

    def showFrame(self, page_name):
        if self.logedIn or page_name == "Login":
            frame = self.frames[page_name]
            frame.tkraise()
        else:
            messagebox.showinfo("Error!", "You have to log in first!")
            return
        
    def exit(self):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()