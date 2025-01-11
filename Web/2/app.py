from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Hardcoded username, password, and admin parameter
users = {
    'user': ['password123', '123456', 'userpass'],  # user has multiple passwords
    'admin': ['adminpass123', 'myspace123', 'computer123', 'batman', 'joker'],  # admin has multiple passwords
}

# HTML for the login form
login_form = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <script>
        function autoFillAdminParam() {
            var username = document.getElementById("username").value;
            var form = document.getElementById("loginForm");

            // Remove any previously appended 'admin' parameter if it exists
            var existingAdminParam = document.querySelector("input[name='admin']");
            if (existingAdminParam) {
                existingAdminParam.remove();
            }

            // If the username is 'admin', add the hidden 'admin' parameter with value 'true'
            if (username === "admin") {
                var input = document.createElement("input");
                input.type = "hidden";
                input.name = "admin";
                input.value = "true";
                form.appendChild(input);
            }
        }
    </script>
</head>
<body>
    <h2>Login Form</h2>
    <form id="loginForm" action="/login" method="POST" onsubmit="autoFillAdminParam()">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(login_form)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    admin_param = request.form.get('admin')

    # Simple login validation
    if username in users and password in users[username]:
        if admin_param == 'true':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('user_dashboard'))
    return 'Invalid username or password', 403

@app.route('/user_dashboard')
def user_dashboard():
    return 'Welcome to the user dashboard.'

@app.route('/admin_xyzw')
def admin_dashboard():
    # The flag is hidden in a comment within the HTML
    return '''
        <html>
        <body>
            <h1>Welcome to the Admin Dashboard!</h1>
            <!-- CKCTF{admin_dashboard_exploited} -->
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)