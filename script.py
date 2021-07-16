import sqlite3 as sql
from tkinter import *
from operator import itemgetter

conn = sql.connect('crs.db')
cur = conn.cursor()

def show_cars():
    cur.execute("SELECT * from Cars")
    row = cur.fetchall()
    num = 1
    for x in row:
        print(str(num) + ": " + str(x[1]) + " - Rent " + str(x[3]))
        num = num + 1
    return row

def sorted_cars():
    cur.execute("SELECT * from Cars order by Car_Name")
    row = cur.fetchall()
    num = 1
    for x in row:
        print(str(num) + ": " + str(x[1]) + " - Rent " + str(x[3]))
        num = num + 1
    return row

def search_cars(name):
    cur.execute("SELECT * from Cars where Car_Name LIKE '"+ name +"'")
    row = cur.fetchall()
    num = 1
    for x in row:
        print(str(num) + ": " + str(x[1]) + " - Rent " + str(x[3]))
        num = num + 1
    return row

def show_customers():
    cur.execute("SELECT * from Customers")
    row = cur.fetchall()
    num = 1
    if not row:
        print("Empty List")
        return None
    else:
        for x in row:
            print(str(num) + " Customer Name :  " + str(x[1]))
            num = num + 1
        return row

def sorted_customers():
    cur.execute("SELECT * from Customers order by Customer_Name")
    row = cur.fetchall()
    num = 1
    if not row:
        print("Empty List")
        return None
    else:
        for x in row:
            print(str(num) + " Customer Name :  " + str(x[1]))
            num = num + 1
        return row

def search_customers(name):
    cur.execute("SELECT * from Customers where Customer_Name LIKE '"+name+"'")
    row = cur.fetchall()
    num = 1
    if not row:
        print("Empty List")
        return None
    else:
        for x in row:
            print(str(num) + " Customer Name :  " + str(x[1]))
            num = num + 1
        return row

def show_bookings():
    cur.execute("SELECT * from Booking")
    row = cur.fetchall()
    num = 1
    if not row:
        print("Empty List")
        return None
    else:
        for x in row:
            print(x)
            num = num + 1
        return row

def sorted_bookings():
    cur.execute("SELECT * from Booking order by Customer_Name")
    row = cur.fetchall()
    num = 1
    if not row:
        print("Empty List")
        return None
    else:
        for x in row:
            print(x)
            num = num + 1
        return row

def search_bookings(name):
    cur.execute("SELECT * from Booking where Customer_Name LIKE '"+name+"'")
    row = cur.fetchall()
    num = 1
    if not row:
        print("Empty List")
        return None
    else:
        for x in row:
            print(x)
            num = num + 1
        return row

def add_cars(car_name, car_type, car_rent):


    cur.execute(
        "Insert into Cars (Car_Name, Car_Type_ID, Car_Rent) Values ('" + car_name + "', '" + car_type + "', '" + car_rent + "')")
    conn.commit()

def add_customers(customer_name, customer_Address, Customer_phone):

    cur.execute(
        "Insert into Customers (Customer_Name, Customer_Address, Customer_Phone_Number) Values ('" + customer_name + "', '" + customer_Address + "', '" + Customer_phone + "')")
    conn.commit()

def add_bookings(customer_name, car_id, from_date, to_date, rent_per_day, total_rent):

    cur.execute(
        "Insert into Booking (Customer_Name, Car_ID, From_Date, To_Dat    conn.commit()
e, Rent_Per_Day, Total_Rent) Values ('" + customer_name + "', '" + car_id + "', '" +  from_date + "', '" + to_date + "', '" + rent_per_day + "', '" + total_rent + "')")

