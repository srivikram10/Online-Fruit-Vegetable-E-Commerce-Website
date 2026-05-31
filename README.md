# Fresh Basket - Online Fruit & Vegetable E-Commerce Website

A modern, responsive, and full-stack e-commerce platform for fresh produce built with Python Flask, MySQL, and Premium UI design.

## Features
- **Premium UI**: Clean, attractive design with green/orange theme and glassmorphism.
- **User Authentication**: Secure Login and Registration system.
- **Product Management**: Browse products by category, search functionality.
- **Shopping Cart**: Dynamic cart system with AJAX "Add to Cart".
- **Admin Dashboard**: Overview of sales, orders, and product management.
- **Responsive Design**: Optimized for mobile, tablet, and desktop.
- **Sample Data**: Easy-to-use seeder script for quick setup.

## Technologies Used
- **Backend**: Python Flask
- **Database**: MySQL
- **Frontend**: HTML5, CSS3 (Vanilla), JavaScript (ES6)
- **Icons**: Font Awesome 6

## Setup Instructions

### 1. Database Setup
1. Open your MySQL client (like XAMPP, MySQL Workbench, etc.).
2. Create a database named `fresh_basket`.
3. Import the `schema.sql` file or copy its content into a SQL editor and run it.

### 2. Configuration
1. Open `config.py`.
2. Update `MYSQL_PASSWORD` with your MySQL root password (default is usually empty in XAMPP).

### 3. Install Dependencies
Run the following command to install required Python libraries:
```bash
pip install flask mysql-connector-python werkzeug
```

### 4. Seed Database
Run the seed script to populate categories, sample products, and an admin user:
```bash
python seed_db.py
```
*Note: Admin login: `admin@freshbasket.com` / `admin123`*

### 5. Run the Application
Start the Flask development server:
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser.

## Folder Structure
- `app.py`: Main application logic and routes.
- `database.py`: Database connection utilities.
- `static/`: Contains CSS, JS, and images.
- `templates/`: Jinja2 HTML templates.
- `schema.sql`: Database structure.
- `seed_db.py`: Initial data population script.
