# E-commerce DBMS CRUD GUI

A simple CRUD to perform basic database SQL on a conceptual database of an E-commerce system.

## Interface

 - [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
 - [Azure Theme](https://github.com/rdbende/Azure-ttk-theme)

## Run Locally

- Clone the project

- Setup MySQL Databse by Ecom.sql then run
```bash
  USE ecom
```

- Install Packages

```bash
  pip install pymysql
  pip install tkinter
  pip install customtkinter==4.6.3
```


- To deploy this project run

```bash
  python App.py
```

## Use App

Enter the app with one of these three usernames: admin, seller, buyer and password: 123

- Admin: Can view all tables.

- Seller: Can view all tables related to them, orders, and shippers.

- Buyer: Can view all tables related to them and orders.
