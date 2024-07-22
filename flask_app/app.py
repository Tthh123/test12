from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

home_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="post" action="/login">
        <input type="password" name="password" placeholder="Enter password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

welcome_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome</h1>
    <p>Your password: {{ password }}</p>
    <form method="post" action="/logout">
        <button type="submit">Logout</button>
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(home_page)

@app.route('/login', methods=['POST'])
def login():
    password = request.form['password']
    if verify_password(password) and not is_common_password(password):
        return render_template_string(welcome_page, password=password)
    return redirect(url_for('index'))

@app.route('/logout', methods=['POST'])
def logout():
    return redirect(url_for('index'))

def verify_password(password):
    import re
    # OWASP recommended checks
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[#@!$%^&*(),.?\":{}|<>]", password):
        return False
    return True

def is_common_password(password):
    with open('10-million-password-list-top-1000.txt', 'r') as file:
        common_passwords = file.read().splitlines()
        if password in common_passwords:
            return True
    return False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
