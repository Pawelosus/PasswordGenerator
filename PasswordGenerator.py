import random
import string
import tkinter as tk


class App:
    def __init__(self, parent):
        # Variables used for generating the password
        self.password = ""
        self.password_length = 10
        self.uppercase = True
        self.uppercase_min = 0
        self.lowercase = True
        self.lowercase_min = 0
        self.digits = True
        self.digits_min = 0
        self.special_char = False
        self.special_char_min = 0
        # GUI basic settings
        self.parent = parent
        self.window = tk.Toplevel()
        # self.window.geometry("600x600")
        self.window.title("Password Generator")
        self.window.protocol("WM_DELETE_WINDOW", self.parent.quit)
        # Creating elements
        self.generate_password_button = tk.Button(self.window, text="Generate", font=("Arial", 24),
                                                  command=self.generate_password)
        self.password_label = tk.Label(self.window, text="Length:", font=("Arial", 20))
        self.password_button_subtract = tk.Button(self.window, text="-",
                                                  command=lambda: self.button_event("password_length", "subtract"))
        self.password_label_length = tk.Label(self.window, text="10", font=("Arial", 20))
        self.password_button_add = tk.Button(self.window, text="+",
                                             command=lambda: self.button_event("password_length", "add"))
        self.password_box_value = tk.StringVar()
        self.password_box = tk.Entry(self.window, textvariable=self.password_box_value)
        # Uppercase row
        self.uppercase_label_info = tk.Label(self.window, text="A-Z: ", font=("Arial", 24))
        self.uppercase_label_is_on = tk.Label(self.window, text="Yes", font=("Arial", 24))
        self.uppercase_checkbox_value = tk.BooleanVar()
        self.uppercase_checkbox_is_on = tk.Checkbutton(
            self.window, variable=self.uppercase_checkbox_value, onvalue=True, offvalue=False,
            command=lambda: self.checkbox_event("uppercase"))
        self.uppercase_label_minimum = tk.Label(self.window, text="Minimum:", font=("Arial", 20))
        self.uppercase_button_subtract = tk.Button(self.window, text="-",
                                                   command=lambda: self.button_event("uppercase", "subtract"))
        self.uppercase_label_value = tk.Label(self.window, text="0", font=("Arial", 24))
        self.uppercase_button_add = tk.Button(self.window, text="+",
                                              command=lambda: self.button_event("uppercase", "add"))
        # Lowercase row
        self.lowercase_label_info = tk.Label(self.window, text="a-z: ", font=("Arial", 24))
        self.lowercase_label_is_on = tk.Label(self.window, text="Yes", font=("Arial", 24))
        self.lowercase_checkbox_value = tk.BooleanVar()
        self.lowercase_checkbox_is_on = tk.Checkbutton(
            self.window, variable=self.lowercase_checkbox_value, onvalue=True, offvalue=False,
            command=lambda: self.checkbox_event("lowercase"))
        self.lowercase_label_minimum = tk.Label(self.window, text="Minimum:", font=("Arial", 20))
        self.lowercase_button_subtract = tk.Button(self.window, text="-",
                                                   command=lambda: self.button_event("lowercase", "subtract"))
        self.lowercase_label_value = tk.Label(self.window, text="0", font=("Arial", 24))
        self.lowercase_button_add = tk.Button(self.window, text="+",
                                              command=lambda: self.button_event("lowercase", "add"))
        # Digit row
        self.digits_label_info = tk.Label(self.window, text="0-9: ", font=("Arial", 24))
        self.digits_label_is_on = tk.Label(self.window, text="Yes", font=("Arial", 24))
        self.digits_checkbox_value = tk.BooleanVar()
        self.digits_checkbox_is_on = tk.Checkbutton(
            self.window, variable=self.digits_checkbox_value, onvalue=True, offvalue=False,
            command=lambda: self.checkbox_event("digits"))
        self.digits_label_minimum = tk.Label(self.window, text="Minimum:", font=("Arial", 20))
        self.digits_button_subtract = tk.Button(self.window, text="-",
                                                command=lambda: self.button_event("digits", "subtract"))
        self.digits_label_value = tk.Label(self.window, text="0", font=("Arial", 24))
        self.digits_button_add = tk.Button(self.window, text="+",
                                           command=lambda: self.button_event("digits", "add"))
        # Special char row
        self.special_char_label_info = tk.Label(self.window, text="!-&: ", font=("Arial", 24))
        self.special_char_label_is_on = tk.Label(self.window, text="Yes", font=("Arial", 24))
        self.special_char_checkbox_value = tk.BooleanVar()
        self.special_char_checkbox_is_on = tk.Checkbutton(
            self.window, variable=self.special_char_checkbox_value, onvalue=True, offvalue=False,
            command=lambda: self.checkbox_event("special_char"))
        self.special_char_label_minimum = tk.Label(self.window, text="Minimum:", font=("Arial", 20))
        self.special_char_button_subtract = tk.Button(self.window, text="-",
                                                      command=lambda: self.button_event("special_char", "subtract"))
        self.special_char_label_value = tk.Label(self.window, text="0", font=("Arial", 24))
        self.special_char_button_add = tk.Button(self.window, text="+",
                                                 command=lambda: self.button_event("special_char", "add"))

    def checkbox_event(self, category):
        if category == "uppercase":
            self.uppercase = self.uppercase_checkbox_value.get()
            self.update_gui_uppercase()
        elif category == "lowercase":
            self.lowercase = self.lowercase_checkbox_value.get()
            self.update_gui_lowercase()
        elif category == "digits":
            self.digits = self.digits_checkbox_value.get()
            self.update_gui_digits()
        elif category == "special_char":
            self.special_char = self.special_char_checkbox_value.get()
            self.update_gui_special_char()

    def button_event(self, category, mode):
        if category == "password_length":
            if mode == "add":
                self.password_length += 1
                self.password_label_length["text"] = str(self.password_length)
            elif mode == "subtract" and self.password_length > 1:
                self.password_length -= 1
                self.password_label_length["text"] = str(self.password_length)
        if category == "uppercase":
            if mode == "add" and self.uppercase_min + self.lowercase_min + self.digits_min + self.special_char_min < self.password_length:
                self.uppercase_min += 1
                self.uppercase_label_value["text"] = str(self.uppercase_min)
            elif mode == "subtract" and self.uppercase_min > 0:
                self.uppercase_min -= 1
                self.uppercase_label_value["text"] = str(self.uppercase_min)
        elif category == "lowercase":
            if mode == "add" and self.uppercase_min + self.lowercase_min + self.digits_min + self.special_char_min < self.password_length:
                self.lowercase_min += 1
                self.lowercase_label_value["text"] = str(self.lowercase_min)
            elif mode == "subtract" and self.lowercase_min > 0:
                self.lowercase_min -= 1
                self.lowercase_label_value["text"] = str(self.lowercase_min)
        elif category == "digits":
            if mode == "add" and self.uppercase_min + self.lowercase_min + self.digits_min + self.special_char_min < self.password_length:
                self.digits_min += 1
                self.digits_label_value["text"] = str(self.digits_min)
            elif mode == "subtract" and self.digits_min > 0:
                self.digits_min -= 1
                self.digits_label_value["text"] = str(self.digits_min)
        elif category == "special_char":
            if mode == "add" and self.uppercase_min + self.lowercase_min + self.digits_min + self.special_char_min < self.password_length:
                self.special_char_min += 1
                self.special_char_label_value["text"] = str(self.special_char_min)
            elif mode == "subtract" and self.special_char_min > 0:
                self.special_char_min -= 1
                self.special_char_label_value["text"] = str(self.special_char_min)

    def update_gui(self):
        self.update_gui_uppercase()
        self.update_gui_lowercase()
        self.update_gui_digits()
        self.update_gui_special_char()

    def add_characters(self, char_type):
        count = 0
        char_set = ""
        if char_type == "uppercase":
            count = self.uppercase_min
            char_set = string.ascii_uppercase
        elif char_type == "lowercase":
            count = self.lowercase_min
            char_set = string.ascii_lowercase
        elif char_type == "digit":
            count = self.digits_min
            char_set = string.digits
        elif char_type == "special_char":
            count = self.special_char_min
            char_set = string.punctuation

        result = ""
        for _ in range(count):
            letter = random.choice(char_set)
            result += letter

        return result

    def display_gui_password(self):
        self.generate_password_button.grid(row=0, column=0)
        self.password_label.grid(row=0, column=1)
        self.password_button_subtract.grid(row=0, column=2)
        self.password_label_length.grid(row=0, column=3)
        self.password_button_add.grid(row=0, column=4)
        self.password_box.grid(row=0, column=6)

    def display_gui_uppercase(self):
        self.uppercase_label_info.grid(row=1, column=0)
        self.uppercase_label_is_on.grid(row=1, column=1)
        self.uppercase_checkbox_is_on.grid(row=1, column=2)
        self.uppercase_label_minimum.grid(row=1, column=3)
        self.uppercase_button_subtract.grid(row=1, column=4)
        self.uppercase_label_value.grid(row=1, column=5)
        self.uppercase_button_add.grid(row=1, column=6)

    def display_gui_lowercase(self):
        self.lowercase_label_info.grid(row=2, column=0)
        self.lowercase_label_is_on.grid(row=2, column=1)
        self.lowercase_checkbox_is_on.grid(row=2, column=2)
        self.lowercase_label_minimum.grid(row=2, column=3)
        self.lowercase_button_subtract.grid(row=2, column=4)
        self.lowercase_label_value.grid(row=2, column=5)
        self.lowercase_button_add.grid(row=2, column=6)

    def display_gui_digits(self):
        self.digits_label_info.grid(row=3, column=0)
        self.digits_label_is_on.grid(row=3, column=1)
        self.digits_checkbox_is_on.grid(row=3, column=2)
        self.digits_label_minimum.grid(row=3, column=3)
        self.digits_button_subtract.grid(row=3, column=4)
        self.digits_label_value.grid(row=3, column=5)
        self.digits_button_add.grid(row=3, column=6)

    def display_gui_special_char(self):
        self.special_char_label_info.grid(row=4, column=0)
        self.special_char_label_is_on.grid(row=4, column=1)
        self.special_char_checkbox_is_on.grid(row=4, column=2)
        self.special_char_label_minimum.grid(row=4, column=3)
        self.special_char_button_subtract.grid(row=4, column=4)
        self.special_char_label_value.grid(row=4, column=5)
        self.special_char_button_add.grid(row=4, column=6)

    def update_gui_uppercase(self):
        if self.uppercase:
            self.uppercase_label_is_on["text"] = "Yes"
            self.uppercase_checkbox_value.set(True)
            self.uppercase_label_value["text"] = self.uppercase_min
            self.uppercase_label_minimum.grid(row=1, column=3)
            self.uppercase_button_subtract.grid(row=1, column=4)
            self.uppercase_label_value.grid(row=1, column=5)
            self.uppercase_button_add.grid(row=1, column=6)
        else:
            self.uppercase_label_is_on["text"] = "No"
            self.uppercase_checkbox_value.set(False)
            self.uppercase_min = 0
            self.uppercase_label_minimum.grid_forget()
            self.uppercase_button_subtract.grid_forget()
            self.uppercase_label_value.grid_forget()
            self.uppercase_button_add.grid_forget()

    def update_gui_lowercase(self):
        if self.lowercase:
            self.lowercase_label_is_on["text"] = "Yes"
            self.lowercase_checkbox_value.set(True)
            self.lowercase_label_value["text"] = self.lowercase_min
            self.lowercase_label_minimum.grid(row=2, column=3)
            self.lowercase_button_subtract.grid(row=2, column=4)
            self.lowercase_label_value.grid(row=2, column=5)
            self.lowercase_button_add.grid(row=2, column=6)
        else:
            self.lowercase_label_is_on["text"] = "No"
            self.lowercase_checkbox_value.set(False)
            self.lowercase_min = 0
            self.lowercase_label_minimum.grid_forget()
            self.lowercase_button_subtract.grid_forget()
            self.lowercase_label_value.grid_forget()
            self.lowercase_button_add.grid_forget()

    def update_gui_digits(self):
        if self.digits:
            self.digits_label_is_on["text"] = "Yes"
            self.digits_checkbox_value.set(True)
            self.digits_label_value["text"] = self.digits_min
            self.digits_label_minimum.grid(row=3, column=3)
            self.digits_button_subtract.grid(row=3, column=4)
            self.digits_label_value.grid(row=3, column=5)
            self.digits_button_add.grid(row=3, column=6)
        else:
            self.digits_label_is_on["text"] = "No"
            self.digits_checkbox_value.set(False)
            self.digits_min = 0
            self.digits_label_minimum.grid_forget()
            self.digits_button_subtract.grid_forget()
            self.digits_label_value.grid_forget()
            self.digits_button_add.grid_forget()

    def update_gui_special_char(self):
        if self.special_char:
            self.special_char_label_is_on["text"] = "Yes"
            self.special_char_checkbox_value.set(True)
            self.special_char_label_value["text"] = self.special_char_min
            self.special_char_label_minimum.grid(row=4, column=3)
            self.special_char_button_subtract.grid(row=4, column=4)
            self.special_char_label_value.grid(row=4, column=5)
            self.special_char_button_add.grid(row=4, column=6)
        else:
            self.special_char_label_is_on["text"] = "No"
            self.special_char_checkbox_value.set(False)
            self.special_char_min = 0
            self.special_char_label_minimum.grid_forget()
            self.special_char_button_subtract.grid_forget()
            self.special_char_label_value.grid_forget()
            self.special_char_button_add.grid_forget()

    def generate_password(self):
        self.password = ""
        if not self.uppercase and not self.lowercase and not self.digits and not self.special_char:
            self.password_box_value.set("Error!")
            return 0
        elif self.uppercase_min + self.lowercase_min + self.digits_min + self.special_char_min \
                > self.password_length:
            self.password_box_value.set("Length too short!")
            return 0
        else:
            inserted_uppercase = False
            inserted_lowercase = False
            inserted_digits = False
            inserted_special_char = False
            char_set = ""

            # Used for instances when user asks for a certain amount of characters of each type.
            if self.uppercase_min > 0 and self.uppercase:
                self.password += self.add_characters("uppercase")
                inserted_uppercase = True
            if self.lowercase_min > 0 and self.lowercase:
                self.password += self.add_characters("lowercase")
                inserted_lowercase = True
            if self.digits_min > 0 and self.digits:
                self.password += self.add_characters("digit")
                inserted_digits = True
            if self.special_char_min > 0 and self.special_char:
                self.password += self.add_characters("special_char")
                inserted_special_char = True

            # No specific characters added
            if not inserted_uppercase and not inserted_lowercase and not inserted_digits and not inserted_special_char:
                if self.uppercase:
                    char_set += string.ascii_uppercase
                if self.lowercase:
                    char_set += string.ascii_lowercase
                if self.digits:
                    char_set += string.digits
                if self.special_char:
                    char_set += string.punctuation

                for _ in range(self.password_length):
                    self.password += random.choice(char_set)
            else:  # Specific characters have been added
                count = self.uppercase_min + self.lowercase_min + self.digits_min + self.special_char_min
                if self.uppercase:
                    char_set += string.ascii_uppercase
                if self.lowercase:
                    char_set += string.ascii_lowercase
                if self.digits:
                    char_set += string.digits
                if self.special_char:
                    char_set += string.punctuation

                for _ in range(self.password_length - count):
                    self.password += random.choice(char_set)

            temp_list = list(self.password)
            random.shuffle(temp_list)
            self.password = ''.join(temp_list)
            self.password_box_value.set(self.password)
            return 1


if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()
    app = App(root)
    app.display_gui_password()
    app.display_gui_uppercase()
    app.display_gui_lowercase()
    app.display_gui_digits()
    app.display_gui_special_char()
    app.update_gui()

    root.mainloop()
