from flask import Flask, render_template, request
from BMSgui import Bms  # Import your BMSgui module

app = Flask(__name__)
bakery_system = Bms()  # Create an instance of your BMS class

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        order_info = request.form['order_info']
        phone_number = request.form['phone_number']

        bakery_system.add_order(customer_name, order_info, phone_number)

    return render_template('order.html')

if __name__ == '__main__':
    app.run(debug=True)
