from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/client')
def client():
    return render_template('client.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/order-confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/product-detail')
def product_detail():
    return render_template('product_detail.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/search-results')
def search_results():
    return render_template('search_results.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/view')
def view():
    return render_template('view.html')

if __name__ == '__main__':
    app.run(debug=True)
