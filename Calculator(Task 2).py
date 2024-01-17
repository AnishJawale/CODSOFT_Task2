import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

window = tk.Tk()
window.title("Calculator")
window.geometry("400x450")  
window.configure(bg='#E0E0E0')

entry = tk.Entry(window, width=30, borderwidth=5, font=("Arial", 14), bg='#FFFFFF')
entry.grid(row=0, column=0, columnspan=4, pady=10)

button_style = {'padx': 20, 'pady': 10, 'font': ('Arial', 12)}

for i in range(1, 10):
    button = tk.Button(window, text=str(i), command=lambda i=i: button_click(i), bg='#AED6F1', **button_style)
    button.grid(row=(i-1)//3 + 1, column=(i-1)%3)

button_0 = tk.Button(window, text="0", command=lambda: button_click(0), bg='#AED6F1', **button_style)
button_0.grid(row=4, column=1)

operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, command=lambda operator=operator: button_click(operator), bg='#ABEBC6', **button_style)
    button.grid(row=i+1, column=3)

button_clear = tk.Button(window, text="Clear", command=button_clear, bg='#F1948A', **button_style)
button_clear.grid(row=4, column=0)

button_equal = tk.Button(window, text="=", command=button_equal, bg='#58D68D', **button_style)
button_equal.grid(row=4, column=2)

for i in range(4):
    window.grid_columnconfigure(i, weight=1)
window.grid_rowconfigure(5, weight=1)

window.mainloop()
