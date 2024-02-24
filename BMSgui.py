import tkinter as tk
from datetime import datetime
from openpyxl import Workbook
from tkinter import messagebox

class Bms:
    def __init__(self):
        self.customers = {}
        self.order_id_counter = 1

    def add_order(self, customer_name, order_info, phone_number):
        order_id = self.order_id_counter
        self.order_id_counter += 1

        order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order_details = {
            "Customer name": customer_name,
            "Order Details": order_info,
            "Phone Number": phone_number,
            "Order Date": order_date,
        }
        self.customers[order_id] = order_details
        print(f"Order placed successfully. Order ID: {order_id}")

    def export_to_excel(self, file_name="bakery_orders.xlsx"):
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Bakery Orders"
        sheet.append(["OrderID", "Customer name", "Order Details", "Phone Number"])

        for order_id, order_details in self.customers.items():
            sheet.append([
                order_id,
                order_details["Customer name"],
                order_details["Order Details"],
                order_details["Phone Number"],
                order_details["Order Date"],
            ])
        workbook.save(file_name)
        print(f"Data exported to {file_name} successfully.")

    def get_order_details(self, order_id):
        order_details = self.customers.get(order_id)
        if order_details:
            print(f"Order ID: {order_id}")
            for key, value in order_details.items():
                print(f"{key}: {value}")
        else:
            print(f"Order ID {order_id} not found.")

class BmsGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Bakery Management System")

        self.bakery_system = Bms()

        # Set background color
        self.master.configure(bg="white")

        # Create labels
        self.labels = [
            ("Enter customer name:", 0, 0),
            ("Enter Order info:", 1, 0),
            ("Enter customer phone number:", 2, 0),
        ]

        # Set label background color
        for text, row, col in self.labels:
            label = tk.Label(master, text=text, bg="white")
            label.grid(row=row, column=col, padx=10, pady=10, sticky="w")

        # Create entry widgets
        self.customer_name_entry = tk.Entry(master)
        self.order_info_entry = tk.Entry(master)
        self.phone_number_entry = tk.Entry(master)

        # Create buttons
        button_font = ("Impact", 12)
        self.buttons = [
            ("Add Order", self.add_order, 3, 0),
            ("New Order", self.new_order, 3, 1),
            ("Export to Excel", self.export_to_excel, 4, 0),
            ("Exit", self.exit_program, 4, 1),
        ]

        # Pack or grid widgets
        self.customer_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.order_info_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.phone_number_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        for text, command, row, col in self.buttons:
            button = tk.Button(master, text=text, command=command, bg="blue", fg="white", font=button_font)
            button.grid(row=row, column=col, padx=10, pady=10, sticky="w")

    def add_order(self):
        customer_name = self.customer_name_entry.get()
        order_info = self.order_info_entry.get()
        phone_number = self.phone_number_entry.get()

        if customer_name.lower() == 'exit':
            self.master.withdraw()
            return

        self.bakery_system.add_order(customer_name, order_info, phone_number)

    def new_order(self):
        self.customer_name_entry.delete(0, tk.END)
        self.order_info_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)

    def export_to_excel(self):
        self.bakery_system.export_to_excel()
        tk.messagebox.showinfo("Success", "Data exported to bakery_orders.xlsx successfully.")

    def exit_program(self):
        self.master.destroy()

    def run_input_loop(self):
        self.master.mainloop()

# Create the Tkinter application
root = tk.Tk()
app = BmsGUI(root)

# Run the Tkinter event loop
app.run_input_loop()
