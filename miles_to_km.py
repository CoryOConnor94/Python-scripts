from tkinter import *


def miles_to_km():
    """Converts user inputted miles to KM"""
    miles = float(user_input.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}")


result = 0
# Window setup
window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

# Entry Setup
user_input = Entry(width=17)
user_input.grid(column=1, row=0)

# Label setup
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text=result)
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button setup
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()
