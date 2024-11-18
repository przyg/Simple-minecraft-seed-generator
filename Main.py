import os
import random
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox


root = tk.Tk()
root.title("Simple seed generator")
label = tk.Label(root, text="Please enter a number of seeds that will be generated", font=("Arial", 9))
label.pack()


entry = tk.Entry(root, font=("Arial",10))
entry.pack()

progress = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=280)
progress.pack(pady=10)
def onButtonClick():
    print("button clicked")
    nos = entry.get()

    try:
        nos = int(nos)
        seeds = [random.randint(1, 1000000000000) for _ in range(nos)]
        progress["maximum"] = nos
        progress["value"] = 0


        print(seeds)
        filename = "Seeds " + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
        if nos == 144:
            messagebox.showwarning("yay", "You found my favorite number! Code: 144")
        if nos > 0:
            with open(filename, "w") as file:
                for i, seed in enumerate(seeds):
                    progress["value"] = i + 1
                    root.update_idletasks()
                    file.write(f"Seed number #{i + 1}: {seed}\n")
            print(f"Seeds saved to {filename}")
        else:
            messagebox.showerror("Value Error", f"{nos} is not a valid number! Code: 2")
        if nos == 1:
            if messagebox.showinfo("Success", f"Seed generated and saved to: {filename}, Seed: {seeds} Code: -1"):
                progress["value"] = 0
            if messagebox.askyesno("Open file", f"Do you want to open file with your seed?"):
                os.startfile(filename)

        elif nos > 1:
            if messagebox.showinfo("Success", f"Generated {nos} seeds and saved them to {filename} Code: -2"):
                progress["value"] = 0
            if messagebox.askyesno("Open file", f"Do you want to open file with your seeds?"):
                os.startfile(filename)

    except ValueError:
        print("enter a valid number")
        messagebox.showerror("Value Error", f"Please enter a valid number! {nos} is not a valid number! Code: 1")


button = tk.Button(root, text="Generate", command=onButtonClick)
button.pack()
root.geometry("300x130")

root.resizable(False, False)
root.mainloop()