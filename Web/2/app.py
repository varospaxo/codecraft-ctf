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
        function base64Encode(str) {
            return btoa(unescape(encodeURIComponent(str)));
        }

        function base64Decode(str) {
            return decodeURIComponent(escape(atob(str)));
        }

        function autoFillUserParam() {
            var username = document.getElementById("username").value;
            var form = document.getElementById("loginForm");

            // Decrypting the encoded strings at runtime
            var encryptedUser = "YWRtaW4=";
            var encryptedValue = "dHJ1ZQ==";

            var decryptedUser = base64Decode(encryptedUser);
            var decryptedValue = base64Decode(encryptedValue);

            var existingUserParam = document.querySelector("input[name='" + decryptedUser + "']");
            if (existingUserParam) {
                existingUserParam.remove();
            }

            if (username === decryptedUser) {
                var input = document.createElement("input");
                input.type = "hidden";
                input.name = decryptedUser;
                input.value = decryptedValue;
                form.appendChild(input);
            }
        }
    </script>
</head>
<body>
    <h2>Login Form</h2>
    <form id="loginForm" action="/login" method="POST" onsubmit="autoFillUserParam()">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br><br>

        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br><br>

        <button type="submit">Login</button>
    </form>
</body>
</html>

'''

@app.route('/loginform')
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