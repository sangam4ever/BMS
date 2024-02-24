
import openpyxl
from datetime import datetime
from openpyxl import Workbook


class Bms:   #class for Bakery management system
    def __init__(self):     #init method to store customer orders
        self.customers = {}
        self.order_id_counter = 1

    def add_order(self, customer_name, order_info, phone_number):    #add order method to take parameters form customer
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
        
    def get_order_details(self, order_id):  # retieve and print  details
        order_details = self.customers.get(order_id)
        if order_details:
            print(f"Order ID: {order_id}")
            for key, value in order_details.items():
                print(f"{key}: {value}")
        else:
            print(f"Order ID {order_id} not found.")

# Usage
bakery_system = Bms()

while True:
    # For user input
    customer_name = input("Enter customer name (type 'exit' to end): ")
    
    if customer_name.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'

    order_info = input("Enter Order info:")
    phone_number = input("Enter customer phone number:")

    bakery_system.add_order(customer_name, order_info, phone_number)

bakery_system.export_to_excel()
