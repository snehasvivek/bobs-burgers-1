from flask import Flask, render_template

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


@app.route("/")
def hello_world():
  return render_template('sign-in.html')


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


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
