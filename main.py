import tkinter as tk

root = tk.Tk()

root.title("NEKEN")
root.geometry("1920x1080")

label = tk.Label(root, text="Welcome to the Neken!", font=("Arial", 20))
label.pack(pady=30)

exit_button = tk.Button(root, text = "Exit", command = root.quit)
exit_button.pack(pady = 30)

root.mainloop()