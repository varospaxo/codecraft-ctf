1. Find/Bruteforce password for user, intercept the request, add parameter admin=true. Flag is in source comment of admin dashboard.
2. Find/Bruteforce password for admin. Flag is in source comment of admin dashboard.

https://codecraftctf.pythonanywhere.com/loginform
https://codecraftctf.pythonanywhere.com/admin_xyzw
https://codecraftctf.pythonanywhere.com/user_dashboard_z
users = {
    'user': ['password123', '123456', 'userpass'],  # user has multiple passwords
    'admin': ['adminpass123', 'myspace123', 'computer123', 'batman', 'joker'],  # admin has multiple passwords
}

CKCTF{admin_dashboard_exploited}
