from pyscript import display, document
import js

def verify_account():
    username = document.getElementById("username").value
    password = document.getElementById("password").value

    if len(username) < 7:
        return False, f"Username too short. Add {7 - len(username)} more character(s)."

    if len(password) < 10:
        return False, f"Password too short. Add {10 - len(password)} more character(s)."
    if not any(char.isalpha() for char in password):
        return False, "Password must contain at least one letter."
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number."

    return True, "Account created successfully!"

def account_creation(e):
    document.getElementById("output").innerHTML = ""
    valid, message = verify_account()

    if valid:
        js.alert(message)
        js.location.reload()
    else:
        display(message, target="output")