from tkinter import messagebox
from tkinter import *
import tkinter as tk
import script


# Car Rental System GUI

class CarRentalSystem(object):
    def __init__(self):
        # username and password
        self.username = "admin123"
        self.password = "12345678"

    def add_car_to_db(self):
        script.add_cars(car_name.get(), car_type.get(), rent.get())
        messagebox.showinfo('Entry Successful', 'Your response has been recorded successfully')
    def add_car(self):
        screen3 = Toplevel(screen2)
        screen3.title('Add Car')
        screen3.geometry('500x500')
        label = Label(screen3, text='Add New Car', font="Tahoma 18", bg='black', fg='white')
        label.pack()
        global car_name
        global car_type
        global rent
        car_name = StringVar()
        car_type = StringVar()
        rent = StringVar()
        frame = Frame(screen3)
        frame.config(pady=50, bg='black')
        frame.pack()
        Label(frame, text='Car Name', font='Tahoma 12 bold', bg='black', fg='white').pack()

        Entry(frame, textvariable=car_name).pack()

        Label(frame, text='Car Type', font='Tahoma 12 bold', bg='black', fg='white').pack()
        Entry(frame, textvariable=car_type).pack()

        Label(frame, text='Rent', font='Tahoma 12 bold', bg='black', fg='white').pack()
        Entry(frame, textvariable=rent).pack()
        Button(frame, text = "Add Car", command=self.add_car_to_db).pack()
        screen3.config(bg='black')


    def add_customer_to_db(self):
        script.add_customers(name.get(), address.get(), number.get())
        messagebox.showinfo('Successful Entry', 'Your record has been recorded successfully')

    def add_customer(self):
        screen3 = Toplevel(screen2)
        screen3.title('Add Customer')
        screen3.geometry('500x500')
        label = Label(screen3, text='Add New Customer', font="Tahoma 18", bg='black', fg='white')
        label.pack()
        global name
        global address
        global number
        name = StringVar()
        address = StringVar()
        number = StringVar()
        frame = Frame(screen3)
        frame.config(pady=50, bg='black')
        frame.pack()
        Label(frame, text='Name', font='Tahoma 12 bold', bg='black', fg='white').pack()

        Entry(frame, textvariable=name).pack()

        Label(frame, text='Address', font='Tahoma 12 bold', bg='black', fg='white').pack()
        Entry(frame, textvariable=address).pack()

        Label(frame, text='Number', font='Tahoma 12 bold', bg='black', fg='white').pack()
        Entry(frame, textvariable=number).pack()
        Button(frame, text = "Add Customer", command=self.add_customer_to_db).pack()
        screen3.config(bg='black')

    def add_bookings_to_db(self):
        script.add_bookings(customer_name.get(), car_id.get(), from_date.get(), to_date.get(), rent_per_day.get(), total_rent.get())
        messagebox.showinfo('Successful Entry', 'Your record has been recorded successfully')

    def add_bookings(self):
        screen7 = Toplevel(screen2)
        screen7.title('Add Booking')
        screen7.geometry('500x500')
        label = Label(screen7, text='Add New Booking', font="Tahoma 18", bg='black', fg='white')
        label.pack()
        global customer_name
        global car_id
        global from_date
        global to_date
        global rent_per_day
        global total_rent
        customer_name = StringVar()
        car_id = StringVar()
        from_date = StringVar()
        to_date = StringVar()
        rent_per_day = StringVar()
        total_rent = StringVar()
        frame = Frame(screen7)
        frame.config(pady=50, bg='black')
        frame.pack()
        Label(frame, text='Customer Name', font='Tahoma 12 bold', bg='black', fg='white').pack()

        Entry(frame, textvariable=customer_name).pack()

        Label(frame, text='car_id', font='Tahoma 12 bold', bg='black', fg='white').pack()
        Entry(frame, textvariable=car_id).pack()

        Label(frame, text='From Date', font='Tahoma 12 bold', bg='black', fg='white').pack()
        Entry(frame, textvariable=from_date).pack()

        Label(frame, text='To Date', font='Tahoma 12 bold', bg='black', fg='white').pack()
        Entry(frame, textvariable=to_date).pack()

        Label(frame, text='Rent Per Day', font='Tahoma 12 bold', bg='black', fg='white').pack()
        Entry(frame, textvariable=rent_per_day).pack()

        Label(frame, text='Total Rent', font='Tahoma 12 bold', bg='black', fg='white').pack()
        Entry(frame, textvariable=total_rent).pack()

        Button(frame, text="Add Customer", command=self.add_bookings_to_db).pack()
        screen7.config(bg='black')


    def view_sorted_customers(self):
        screen3 = Toplevel(screen2)
        screen3.title('All Customers')
        screen3.geometry('750x500')
        global cus_name
        cus_name = StringVar()
        label = Label(screen3, text='List of All Customers', font="Tahoma 18", bg='black', fg='white')
        label.grid(row=0, column=1, sticky=NSEW, pady=15, padx=15)
        customers_list = script.sorted_customers()
        print(customers_list)
        titles = ['Sr No.', 'Customer Name', 'Address', 'Tel. Number']
        rows = []
        i = 1

        for j in range(len(titles)):
            e = Entry(screen3, relief=GROOVE, font="bold")

            e.grid(row=i, column=j, sticky=NSEW)

            e.insert(END, '%s' % (titles[j]))

        i = 2

        for row in customers_list:

            cols = []

            for j in range(4):
                e = Entry(screen3, relief=GROOVE)

                e.grid(row=i, column=j, sticky=NSEW)

                e.insert(END, '%s' % (row[j]))

                cols.append(e)

            rows.append(cols)
            i += 1

        screen3.config(bg='black')

    def view_customers(self):
        screen3 = Toplevel(screen2)
        screen3.title('All Customers')
        screen3.geometry('750x500')
        global cus_name
        cus_name = StringVar()
        label = Label(screen3, text='List of All Customers', font="Tahoma 18", bg='black', fg='white')
        label.grid(row=0, column=1, sticky=NSEW, pady=15, padx=15)
        customers_list = script.show_customers()
        print(customers_list)
        titles = ['Sr No.', 'Customer Name', 'Address', 'Tel. Number']
        rows = []
        i = 1

        for j in range(len(titles)):
            e = Entry(screen3, relief=GROOVE, font="bold")

            e.grid(row=i, column=j, sticky=NSEW)

            e.insert(END, '%s' % (titles[j]))

        i = 2

        for row in customers_list:

            cols = []

            for j in range(4):
                e = Entry(screen3, relief=GROOVE)

                e.grid(row=i, column=j, sticky=NSEW)

                e.insert(END, '%s' % (row[j]))

                cols.append(e)

            rows.append(cols)
            i += 1

        screen3.config(bg='black')

    def search_booking_results(self):
        screen3 = Toplevel(screen2)
        screen3.title('Search Booking Results')
        screen3.geometry('1080x500')
        label = Label(screen3, text='Searched Booking', font="Tahoma 18", bg='black', fg='white')
        label.grid(row=0, column=1, sticky=NSEW, pady=15, padx=15)

        bookings_list = script.search_bookings(search_customer_name.get())
        titles = ['Sr No.', 'Customer Name', 'Car ID', 'From Date', 'To Date', 'Rent Per Day', 'Total Rent']
        rows = []
        i = 1

        for j in range(len(titles)):
            e = Entry(screen3, relief=GROOVE, font="bold")

            e.grid(row=i, column=j, sticky=NSEW)

            e.insert(END, '%s' % (titles[j]))

        i = 2

        for row in bookings_list:

            cols = []

            for j in range(7):
                e = Entry(screen3, relief=GROOVE)

                e.grid(row=i, column=j, sticky=NSEW)

                e.insert(END, '%s' % (row[j]))

                cols.append(e)

            rows.append(cols)
            i += 1

        screen3.config(bg='black')

    def search_booking(self):
        screen3 = Toplevel(screen2)
        screen3.title("Search Bookings")
        screen3.geometry('650x500')
        global search_customer_name
        search_customer_name = StringVar()

        label = Label(screen3, text='Search Booking', font="Tahoma 18", bg='black', fg='white')
        Label(screen3, text='Customer Name', font='Tahoma 12 bold', bg='black', fg='white').pack()

        Entry(screen3, textvariable=search_customer_name).pack()
        Button(screen3, text="Search Booking", command=self.search_booking_results).pack()
        screen3.config(bg='black')

    def search_customer_results(self):
        screen3 = Toplevel(screen2)
        screen3.title('Search Customer Results')
        screen3.geometry('650x500')
        label = Label(screen3, text='Search Customer', font="Tahoma 18", bg='black', fg='white')
        label.grid(row=0, column=1, sticky=NSEW, pady=15, padx=15)

        customer_list = script.search_customers(search_customer_name.get())
        titles = ['Sr No.', 'Customer Name', 'Address', 'Tel. Number']
        rows = []
        i = 1

        for j in range(len(titles)):
            e = Entry(screen3, relief=GROOVE, font="bold")

            e.grid(row=i, column=j, sticky=NSEW)

            e.insert(END, '%s' % (titles[j]))

        i = 2

        for row in customer_list:

            cols = []

            for j in range(4):
                e = Entry(screen3, relief=GROOVE)

                e.grid(row=i, column=j, sticky=NSEW)

                e.insert(END, '%s' % (row[j]))

                cols.append(e)

            rows.append(cols)
            i += 1
        screen3.config(bg='black')

    def search_customer(self):
        screen3 = Toplevel(screen2)
        screen3.title("Search Customers")
        screen3.geometry('650x500')
        global search_customer_name
        search_customer_name = StringVar()

        label = Label(screen3, text='Search Customer', font="Tahoma 18", bg='black', fg='white')
        Label(screen3, text='Customer Name', font='Tahoma 12 bold', bg='black', fg='white').pack()

        Entry(screen3, textvariable=search_customer_name).pack()
        Button(screen3, text="Search Customer", command=self.search_customer_results).pack()
        screen3.config(bg='black')

    def search_car_results(self):
        screen3 = Toplevel(screen2)
        screen3.title('Search Car Results')
        screen3.geometry('650x500')
        label = Label(screen3, text='Search Car', font="Tahoma 18", bg='black', fg='white')
        label.grid(row=0, column=1, sticky=NSEW, pady=15, padx=15)

        car_list = script.search_cars(search_car_name.get())
        titles = ['Sr No.', 'Car Name', 'Car Type', 'Rent']
        rows = []
        i = 1

        for j in range(len(titles)):
            e = Entry(screen3, relief=GROOVE, font="bold")

            e.grid(row=i, column=j, sticky=NSEW)

            e.insert(END, '%s' % (titles[j]))

        i = 2

        for row in car_list:

            cols = []

            for j in range(4):
                e = Entry(screen3, relief=GROOVE)

                e.grid(row=i, column=j, sticky=NSEW)

                e.insert(END, '%s' % (row[j]))

                cols.append(e)

            rows.append(cols)
            i += 1
        screen3.config(bg='black')


    def search_car(self):
        screen3 = Toplevel(screen2)
        screen3.title("Search Cars")
        screen3.geometry('650x500')
        global search_car_name
        search_car_name = StringVar()

        label = Label(screen3, text='Search Car', font="Tahoma 18", bg='black', fg='white')
        Label(screen3, text='Car Name', font='Tahoma 12 bold', bg='black', fg='white').pack()

        Entry(screen3, textvariable=search_car_name).pack()
        Button(screen3, text="Search", command=self.search_car_results).pack()
        screen3.config(bg='black')

    def view_sorted_cars(self):
        screen3 = Toplevel(screen2)
        screen3.title('All Cars')
        screen3.geometry('650x500')
        label = Label(screen3, text='List of All Cars', font="Tahoma 18", bg='black', fg='white')
        label.grid(row=0, column=1, sticky=NSEW, pady=15, padx=15)
        cars_list = script.sorted_cars()
        titles = ['Sr No.', 'Car Name', 'Car Type', 'Rent']
        rows = []
        i = 1

        for j in range(len(titles)):
            e = Entry(screen3, relief=GROOVE, font="bold")

            e.grid(row=i, column=j, sticky=NSEW)

            e.insert(END, '%s' % (titles[j]))

        i = 2

        for row in cars_list:

            cols = []

            for j in range(4):
                e = Entry(screen3, relief=GROOVE)

                e.grid(row=i, column=j, sticky=NSEW)

                e.insert(END, '%s' % (row[j]))

                cols.append(e)

            rows.append(cols)
            i += 1
        screen3.config(bg='black')

    def view_cars(self):
        screen3 = Toplevel(screen2)
        screen3.title('All Cars')
        screen3.geometry('650x500')
        label = Label(screen3, text='List of All Cars', font="Tahoma 18", bg='black', fg='white')
        label.grid(row=0, column=1, sticky=NSEW, pady=15, padx=15)
        cars_list = script.show_cars()
        titles = ['Sr No.', 'Car Name', 'Car Type', 'Rent']
        rows = []
        i = 1

        for j in range(len(titles)):
            e = Entry(screen3, relief=GROOVE, font="bold")

            e.grid(row=i, column=j, sticky=NSEW)

            e.insert(END, '%s' % (titles[j]))

        i=2

        for row in cars_list:

            cols = []

            for j in range(4):
                e = Entry(screen3, relief=GROOVE)

                e.grid(row=i, column=j, sticky=NSEW)

                e.insert(END, '%s' % (row[j]))

                cols.append(e)

            rows.append(cols)
            i+=1
        screen3.config(bg='black')

    def view_sorted_bookings(self):
        screen6 = Toplevel(screen2)
        screen6.title('All Bookings')
        screen6.geometry('1080x500')
        label = Label(screen6, text='List of All Bookings', font="Tahoma 18", bg='black', fg='white')
        label.grid(row=0, column=1, sticky=NSEW, pady=15, padx=15)
        bookings_list = script.sorted_bookings()
        titles = ['Sr No.', 'Customer Name', 'Car ID', 'From Date', 'To Date', 'Rent Per Day', 'Total Rent']
        rows = []
        i = 1

        for j in range(len(titles)):
            e = Entry(screen6, relief=GROOVE, font="bold")

            e.grid(row=i, column=j, sticky=NSEW)

            e.insert(END, '%s' % (titles[j]))

        i = 2

        for row in bookings_list:

            cols = []

            for j in range(7):
                e = Entry(screen6, relief=GROOVE)

                e.grid(row=i, column=j, sticky=NSEW)

                e.insert(END, '%s' % (row[j]))

                cols.append(e)

            rows.append(cols)
            i += 1
        screen6.config(bg='black')

    def view_bookings(self):
        screen6 = Toplevel(screen2)
        screen6.title('All Cars')
        screen6.geometry('1080x500')
        label = Label(screen6, text='List of All Bookings', font="Tahoma 18", bg='black', fg='white')
        label.grid(row=0, column=1, sticky=NSEW, pady=15, padx=15)
        bookings_list = script.show_bookings()
        titles = ['Sr No.', 'Customer Name', 'Car ID', 'From Date', 'To Date', 'Rent Per Day', 'Total Rent']
        rows = []
        i = 1

        for j in range(len(titles)):
            e = Entry(screen6, relief=GROOVE, font="bold")

            e.grid(row=i, column=j, sticky=NSEW)

            e.insert(END, '%s' % (titles[j]))

        i=2

        for row in bookings_list:

            cols = []

            for j in range(7):
                e = Entry(screen6, relief=GROOVE)

                e.grid(row=i, column=j, sticky=NSEW)

                e.insert(END, '%s' % (row[j]))

                cols.append(e)

            rows.append(cols)
            i+=1
        screen6.config(bg='black')

    def options_panel(self):
        global screen2
        screen2 = Tk()
        screen2.title('Car Rental System Panel')
        screen2.geometry('400x550')
        menubar = Menu(screen2)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="View All Cars", command=self.view_cars)
        filemenu.add_command(label="View All Customers", command=self.view_customers)
        filemenu.add_command(label="View All Bookings", command=self.view_bookings)
        filemenu.add_command(label="Add New Car", command=self.add_car)
        filemenu.add_command(label="Add New Customer", command=self.add_customer)
        filemenu.add_command(label="Add New Booking", command=self.add_bookings)
        filemenu.add_command(label="Search Car", command=self.search_car)
        filemenu.add_command(label="Search Customer", command=self.search_customer)
        filemenu.add_command(label="Search Booking", command=self.search_booking)
        filemenu.add_command(label="View Sorted Cars", command=self.view_sorted_cars)
        filemenu.add_command(label="View Sorted Customers", command=self.view_sorted_customers)
        filemenu.add_command(label="View Sorted Bookings", command=self.view_sorted_bookings)

        filemenu.add_command(label="Sign Out", command=self.signout)

        menubar.add_cascade(label="File", menu=filemenu)

        Label(screen2, text='Car Rental System Panel', font="Tahoma 18", bg='black', fg='white').pack()

        frame = Frame(screen2)
        frame.config(pady=50, bg='black')
        frame.pack()

        btn1 = Button(frame, text='View All Cars', height='1', width='15', command=self.view_cars, bg='white')
        btn1.pack()
        btn2 = Button(frame, text='View All Customers', height='1', width='15', command=self.view_customers, bg='white')
        btn2.pack()
        btn3 = Button(frame, text='View All Bookings', height='1', width='15', command=self.view_bookings, bg='white')
        btn3.pack()
        btn4 = Button(frame, text='Add New Car', height='1', width='15', command=self.add_car, bg='white')
        btn4.pack()
        btn5 = Button(frame, text='Add New Customer', height='1', width='15', command=self.add_customer, bg='white')
        btn5.pack()
        btn13 = Button(frame, text='Add New Booking', height='1', width='15', command=self.add_bookings, bg='white')
        btn13.pack()
        btn6 = Button(frame, text='Search Car', height='1', width='15', command=self.search_car, bg='white')
        btn6.pack()
        btn7 = Button(frame, text='Search Customer', height='1', width='15', command=self.search_customer, bg='white')
        btn7.pack()
        btn8 = Button(frame, text='Search Booking', height='1', width='15', command=self.search_booking, bg='white')
        btn8.pack()
        btn9 = Button(frame, text='View Sorted Cars', height='1', width='15', command=self.view_sorted_cars, bg='white')
        btn9.pack()
        btn10 = Button(frame, text='View Sorted Customers', height='1', width='15', command=self.view_sorted_customers, bg='white')
        btn10.pack()
        btn11 = Button(frame, text='View Sorted Bookings', height='1', width='15', command=self.view_sorted_bookings, bg='white')
        btn11.pack()
        btn12 = Button(frame, text='Logout', height='1', width='15', command=self.signout, bg='white')
        btn12.pack()

        screen2.config(bg='black', menu=menubar)


    def signout(self):

        screen2.destroy()
        self.LoginPanel()

    def validate(self):
        username_info = username.get()
        password_info = password.get()
        if self.username == username_info and self.password == password_info:
            screen.destroy()
            self.options_panel()
        else:
            messagebox.showinfo(title="Invalid input", message="Username or password is incorrect")



    def LoginPanel(self):
        global screen
        screen = Tk()
        screen.title('Car Rental System Login')
        screen.geometry('400x400')

        global username
        global password
        username = StringVar()
        password = StringVar()
        Label(screen, text='Car Rental System Login', font="Tahoma 20 bold", bg='black', fg='white').pack()
        frame = Frame(screen)
        frame.config(pady=50, bg='black')
        frame.pack()
        lbl1 = Label(frame, text='Username', font='Tahoma 12 bold', bg='black', fg='white').pack()

        Entry(frame, textvariable=username).pack()

        Label(frame, text='Password', font='Tahoma 12 bold', bg='black', fg='white').pack()
        Entry(frame, show="*", textvariable=password).pack()

        frame2 = Frame(screen)
        frame2.config(bg='black')
        frame2.pack()

        btn1 = Button(frame2, text='Login', height='1', width='15', command=self.validate, bg='white')
        btn1.pack()
        Label(screen, text='username: admin123, password: 12345678', font="Tahoma 12", bg='black', fg='white').pack()

        screen.config(bg='black')
        screen.mainloop()

obj = CarRentalSystem()
obj.LoginPanel()