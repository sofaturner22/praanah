from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('loginpage'))

@app.route('/loginpage', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Perform authentication logic (e.g., check username and password against database)
        # For simplicity, let's assume username is 'admin' and password is 'password'
        if username== 'admin' and password == 'password':
            # Redirect to the homepage if authentication is successful
            return redirect(url_for('homepage'))
        else:
            # If authentication fails, show an error message or redirect back to login page
            return render_template('loginpage.html', error='Invalid username or password')

    # Render the login page template for GET requests
    return render_template('loginpage.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)
