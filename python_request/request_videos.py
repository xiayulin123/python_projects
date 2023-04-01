import tkinter as tk

# create a window
root = tk.Tk()
# set the window properties
root.geometry('800x300+200+200')

# the title
root.title('Yulin_Online_video')

# set the photo for it
img = tk.PhotoImage(
    file=r"C:\Users\xiayu\OneDrive\Desktop\code\python_projects\python_request\photo.jpg")

tk.Label(root, image=img).pack()
# keep window
root.mainloop()
