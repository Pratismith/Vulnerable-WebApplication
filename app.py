from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vulnerable_secret_key'  # Intentionally weak secret key

# Initialize SQLite database
def init_db():
    # Create data directory if it doesn't exist
    import os
    os.makedirs('data', exist_ok=True)
    
    conn = sqlite3.connect('data/vulnerable.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Vulnerability 1: SQL Injection
        # DO NOT USE THIS IN PRODUCTION - This is intentionally vulnerable
        conn = sqlite3.connect('data/vulnerable.db')
        cur = conn.cursor()
        query = f"SELECT * FROM user WHERE username='{username}' AND password='{password}'"
        user = cur.execute(query).fetchone()
        
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Vulnerability 2: No password hashing
        conn = sqlite3.connect('data/vulnerable.db')
        cur = conn.cursor()
        try:
            cur.execute('INSERT INTO user (username, password) VALUES (?, ?)', (username, password))
            conn.commit()
            flash('Registration successful!')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists!')
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # Vulnerability 3: XSS vulnerability
    username = request.args.get('username', '')
    return render_template('dashboard.html', username=username)

@app.route('/search')
def search():
    # Vulnerability 4: Command Injection
    query = request.args.get('q', '')
    # DO NOT USE THIS IN PRODUCTION - This is intentionally vulnerable
    import os
    result = os.popen(f'find . -name "*{query}*"').read()
    return render_template('search.html', result=result)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)