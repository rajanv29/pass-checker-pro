import tkinter as tk
import re
def checkpassword():
    password = entry.get()
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("At least 8 characters is must")
    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append("Use a uppercase letter")
    if re.search("[a-z]", password):
        score += 1
    else:
        suggestions.append("Use a lowercase letter")
    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append("Use a number")
    if re.search("[@#$%^&*!]", password):
        score += 1
    else:
        suggestions.append("Use a special character")
    if score <= 2:
        result = "Weak Password"
    elif score <= 4:
        result = "Medium Password"
    else:
        result = "Strong Password"

    output = result + "\n" + "\n".join(suggestions)
    result_label.config(text=output)
    
##Adding gui to the program
root = tk.Tk()
root.title("SmartPass Analyzer")
root.geometry("400x250")
title = tk.Label(root, text="SmartPass Analyzer", font=("Georgia", 14))
title.pack(pady=10)
entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=5)
check_btn = tk.Button(root, text="Check", command=check_password)
check_btn.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
