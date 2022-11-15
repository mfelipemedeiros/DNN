from tkinter import Button
from gui_buttons import Buttons

button = Buttons()
button.add_button("person", 20, 20)
button.add_button("cell phone", 20, 100)
button.add_button("keyboard", 20,180)
button.add_button("remote",20, 260)
button.add_button("scissors", 20, 340)
button.add_button()

colors = button.colors