import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USER = {
  'first-name': 'Louise',
  'last-name': 'Belcher',
  'email': 'louisebelcher@bobsburgers.com'
}

MENU = {'name': 'Lunch Menu'}

ITEMS = [{
  'item-name': 'New Bacon-ings',
  'description':
  'New Beginnings; The New Bacon-ings is a delicious sandwich that features a juicy beef patty topped with crispy bacon and melted cheese, all served on a soft bun.',
  'price': 10.99,
  'image': 'static/bacon-strips.png'
}, {
  'item-name': 'Tunami',
  'description':
  "Tsunami; The Tunami is a savory sandwich made with a flavorful tuna patty,  with ingredients such as breadcrumbs, onions, and spices. Served on a bun with lettuce, tomato, and other toppings of your choice, it's a healthy and satisfying alternative to a traditional beef burger.",
  'price': 11.99,
  'image': 'static/tuna.png'
}, {
  'item-name': 'Fig-eta Bout It Burger',
  'description':
  "Forget-About-It; The Fig-eta Bout It Burger is a unique and flavorful sandwich that combines a juicy beef patty with sweet and savory toppings such as caramelized onions, fig jam, and goat cheese. Served on a soft bun, it's a delicious and sophisticated take on a classic burger.",
  'price': 12.99,
  'image': 'static/figs.png'
}, {
  'item-name': "Thank God It's Fried Egg Burger",
  'description':
  "Thank God It's Friday; The Thank God It's Fried Egg Burger is a delicious sandwich that features a juicy beef patty topped with a freshly fried egg, which adds an extra layer of richness and flavor to the burger. Served on a bun with other classic toppings like lettuce, tomato, and mayo, it's a hearty and satisfying meal that's perfect for breakfast, lunch, or dinner",
  'price': 11.99,
  'image': 'static/frying-pan.png'
}]

CURRENT_ORDERS = [{
  'order-id': 1235324,
  'status': 'Processing'
}, {
  'order-id': 3478590,
  'status': 'Order in Progress'
}, {
  'order-id': 8905659,
  'status': 'Ready for Pickup'
}]

PAST_ORDERS = [{
  'order-id': 4834789,
  'status': 'Picked Up'
}, {
  'order-id': 3493458,
  'status': 'Picked Up'
}, {
  'order-id': 2364105,
  'status': 'Picked Up'
}]

CART_ITEMS = [{
  'item-name': 'New Bacon-ings',
  'description':
  'New Beginnings; The New Bacon-ings is a delicious sandwich that features a juicy beef patty topped with crispy bacon and melted cheese, all served on a soft bun.',
  'price': 10.99,
  'image': 'static/bacon-strips.png'
}, {
  'item-name': 'New Bacon-ings',
  'description':
  'New Beginnings; The New Bacon-ings is a delicious sandwich that features a juicy beef patty topped with crispy bacon and melted cheese, all served on a soft bun.',
  'price': 10.99,
  'image': 'static/bacon-strips.png'
}, {
  'item-name': 'Fig-eta Bout It Burger',
  'description':
  "Forget-About-It; The Fig-eta Bout It Burger is a unique and flavorful sandwich that combines a juicy beef patty with sweet and savory toppings such as caramelized onions, fig jam, and goat cheese. Served on a soft bun, it's a delicious and sophisticated take on a classic burger.",
  'price': 12.99,
  'image': 'static/figs.png'
}, {
  'item-name': "Thank God It's Fried Egg Burger",
  'description':
  "Thank God It's Friday; The Thank God It's Fried Egg Burger is a delicious sandwich that features a juicy beef patty topped with a freshly fried egg, which adds an extra layer of richness and flavor to the burger. Served on a bun with other classic toppings like lettuce, tomato, and mayo, it's a hearty and satisfying meal that's perfect for breakfast, lunch, or dinner",
  'price': 11.99,
  'image': 'static/frying-pan.png'
}]
CART_INFO = {'total': 46.98}

ORDER = {'order-id': 1235324, 'status': 'Processing'}


def get_db_connection():
  conn = psycopg2.connect(
    "postgres://tsdbadmin:hm6pwjytcgkj55kj@xys2b1iso0.oo73ftqreo.tsdb.cloud.timescale.com:37843/tsdb?sslmode=require",
    database="tsdb",
    user="tsdbadmin",
    password="hm6pwjytcgkj55kj")
  # open a cursor to perform database operations
  return conn


@app.route("/")
def home():
  return render_template('sign-in.html')


@app.route("/setupDB")
def setup_DB():

  conn = get_db_connection()
  cur = conn.cursor()

  # execute a command: this creates a new table
  cur.execute('DROP TABLE IF EXISTS customer;')
  cur.execute('CREATE TABLE customer ('
              'customer_id SERIAL PRIMARY KEY,'
              'password varchar(128) DEFAULT NULL,'
              'customerName text,'
              'address text,'
              'phoneNumber VARCHAR,'
              'email text);')

  conn.commit()
  cur.close()
  conn.close()
  return render_template("sign-in.html")


@app.route("/login", methods=['POST'])
def login_confirm():
  USER = {
    'first-name': 'something',
    'last-name': 'else',
    'email': 'something@something'
  }
  return render_template('welcome.html', user=USER)


@app.route("/new_account", methods=['POST'])
def create_new_account():

  firstname = request.form['fname']
  lastname = request.form['lname']
  email = request.form['email']
  password = request.form['password']

  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute(
    'INSERT INTO customer (customer_id,password, customerName, email)'
    'VALUES (1,%s, %s, %s)', ("test", "test", "email"))
  conn.commit()
  cur.close()
  conn.close()

  USER = {'customerName': firstname, 'last-name': lastname, 'email': email}
  return render_template('welcome.html', user=USER)


@app.route('/getallcustomer')
def index():
  conn = get_db_connection()
  cur = conn.cursor()
  cur.execute('SELECT * FROM customer where customer_id=0;')
  books = cur.fetchall()
  cur.close()
  conn.close()
  return render_template('welcome.html', user=books)


@app.route("/send_checkout", methods=['POST'])
def send_checkout_info():
  billing_info = {
    'first-name': request.form['fname'],
    'last-name': request.form['lname'],
    'email': request.form['email'],
    'address': request.form['address'],
    'country': request.form['country'],
    'state': request.form['state'],
    'zip': request.form['zip']
  }
  payment_info = {
    'name-on-card': request.form['ncard'],
    'cc-number': request.form['cc-number'],
    'cc-expiration': request.form['cc-expiration'],
    'cc-ccv': request.form['cc-ccv'],
  }
  return render_template('welcome.html', user=USER)


@app.route("/welcome")
def welcome():
  return render_template('welcome.html', user=USER)


@app.route("/checkout")
def checkout():
  return render_template('checkout.html')


@app.route("/confirm_checkout")
def confirm_checkout():
  return render_template('confirm-checkout.html', order=ORDER)


@app.route("/create_account")
def create_account():
  return render_template('create-account.html')


@app.route("/edit_account")
def edit_account():
  return render_template('edit-account.html', user=USER)


@app.route("/menu")
def menu():
  return render_template("menu.html", menu=MENU, items=ITEMS)


@app.route("/orders")
def orders():
  return render_template("orders.html",
                         current_orders=CURRENT_ORDERS,
                         past_orders=PAST_ORDERS)


@app.route("/view_account")
def view_account():
  return render_template("view-account.html", user=USER)


@app.route("/view_cart")
def view_cart():
  return render_template("view-cart.html",
                         cart_items=CART_ITEMS,
                         cart_info=CART_INFO)


@app.route("/view_order")
def view_order():
  return render_template("view-order.html",
                         order_items=CART_ITEMS,
                         order_info=CART_INFO)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
