from tkinter import *


class MilesToKmConverter:
    def __init__(self):
        """Initialize GUI and set up the window"""
        self.window = Tk()
        self.window.title('Miles to KM Converter')
        self.window.config(padx=20, pady=20)
        self.result = 0
        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        """Create and place widgets in window"""

        # Entry Setup
        self.user_input = Entry(width=17)
        self.user_input.grid(column=1, row=0)

        # Label setup
        self.miles_label = Label(text="Miles")
        self.miles_label.grid(column=2, row=0)

        self.equal_label = Label(text="is equal to")
        self.equal_label.grid(column=0, row=1)

        self.result_label = Label(text=self.result)
        self.result_label.grid(column=1, row=1)

        self.km_label = Label(text="Km")
        self.km_label.grid(column=2, row=1)

        # Button setup
        self.button = Button(text="Calculate", command=self.miles_to_km)
        self.button.grid(column=1, row=2)

    def miles_to_km(self):
        """Converts user inputted miles to KM"""
        miles = float(self.user_input.get())
        km = round(miles * 1.609, 2)
        self.result_label.config(text=f"{km}")


if __name__ == '__main__':
    MilesToKmConverter()
