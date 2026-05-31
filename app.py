from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
import database as db
import os

app = Flask(__name__)
app.config.from_object(Config)

# Initialize DB teardown
db.init_app(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Context processor to make categories available in all templates
@app.context_processor
def inject_categories():
    categories = db.query_db("SELECT * FROM categories")
    return dict(all_categories=categories)

# Routes
@app.route('/')
def index():
    featured_products = db.query_db("SELECT * FROM products WHERE is_featured = 1 LIMIT 8")
    new_arrivals = db.query_db("SELECT * FROM products ORDER BY id DESC LIMIT 8")
    return render_template('index.html', featured=featured_products, new_arrivals=new_arrivals)

@app.route('/shop')
def shop():
    category_id = request.args.get('category')
    search_query = request.args.get('q')
    
    query = "SELECT * FROM products"
    params = []
    
    if category_id:
        query += " WHERE category_id = %s"
        params.append(category_id)
    elif search_query:
        query += " WHERE name LIKE %s"
        params.append(f"%{search_query}%")
        
    products = db.query_db(query, tuple(params))
    return render_template('shop.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = db.query_db("SELECT * FROM users WHERE email = %s", (email,), one=True)
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'danger')
            
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_pw = generate_password_hash(password)
        
        try:
            db.execute_db("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                         (username, email, hashed_pw))
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Username or Email already exists.', 'danger')
            
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/cart')
def view_cart():
    if 'user_id' not in session:
        flash('Please login to view your cart', 'info')
        return redirect(url_for('login'))
    
    cart_items = db.query_db("""
        SELECT c.*, p.name, p.price, p.image_url 
        FROM cart c 
        JOIN products p ON c.product_id = p.id 
        WHERE c.user_id = %s
    """, (session['user_id'],))
    
    total = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', items=cart_items, total=total)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'Please login first'})
    
    # Check if item already in cart
    item = db.query_db("SELECT * FROM cart WHERE user_id = %s AND product_id = %s", 
                      (session['user_id'], product_id), one=True)
    
    if item:
        db.execute_db("UPDATE cart SET quantity = quantity + 1 WHERE id = %s", (item['id'],))
    else:
        db.execute_db("INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, 1)", 
                     (session['user_id'], product_id))
    
    return jsonify({'status': 'success', 'message': 'Product added to cart'})

@app.route('/update_cart/<int:cart_id>/<string:action>')
def update_cart(cart_id, action):
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'Please login first'})
    
    item = db.query_db("SELECT * FROM cart WHERE id = %s AND user_id = %s", (cart_id, session['user_id']), one=True)
    if not item:
        return jsonify({'status': 'error', 'message': 'Item not found'})
    
    if action == 'increase':
        db.execute_db("UPDATE cart SET quantity = quantity + 1 WHERE id = %s", (cart_id,))
    elif action == 'decrease':
        if item['quantity'] > 1:
            db.execute_db("UPDATE cart SET quantity = quantity - 1 WHERE id = %s", (cart_id,))
        else:
            db.execute_db("DELETE FROM cart WHERE id = %s", (cart_id,))
            return jsonify({'status': 'success', 'removed': True})
            
    # Calculate new totals
    new_item = db.query_db("SELECT quantity FROM cart WHERE id = %s", (cart_id,), one=True)
    cart_items = db.query_db("""
        SELECT c.quantity, p.price 
        FROM cart c 
        JOIN products p ON c.product_id = p.id 
        WHERE c.user_id = %s
    """, (session['user_id'],))
    
    total = sum(i['price'] * i['quantity'] for i in cart_items)
    
    return jsonify({
        'status': 'success', 
        'new_quantity': new_item['quantity'] if new_item else 0,
        'new_total': float(total)
    })

@app.route('/remove_from_cart/<int:cart_id>')
def remove_from_cart(cart_id):
    if 'user_id' not in session:
        return jsonify({'status': 'error', 'message': 'Please login first'})
    
    db.execute_db("DELETE FROM cart WHERE id = %s AND user_id = %s", (cart_id, session['user_id']))
    return jsonify({'status': 'success'})

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def admin_dashboard():
    if session.get('role') != 'admin':
        flash('Unauthorized access', 'danger')
        return redirect(url_for('index'))
    return render_template('admin/dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
