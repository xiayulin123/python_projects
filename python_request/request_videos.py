import tkinter as tk
from PIL import Image, ImageTk
import requests
import re
import webbrowser
# create a window
root = tk.Tk()
# set the window properties
root.geometry('800x300+200+200')

# the title
root.title('Yulin_Online_video')


# function start
def show():
    # choose which one
    number = num_int_var.get()
    word = input_va.get()
    test = 1
    if number == 1:
        link = "https://jiexi.pengdouw.com/jiexi1/?url=" + word
        html_data = requests.get(url=link).text
        video_url = re.findall(
            '<iframe id = "baiyug" scrolling="no" src="(.*?)"', html_data)
        webbrowser.open(video_url)

    elif number == 2:
        link = "https://jiexi.pengdouw.com/jiexi2/?url=" + word
        html_data = requests.get(url=link).text
        video_url = re.findall(
            '<iframe id = "baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)

    elif number == 3:
        print('picked 3')
        print('Enter the URL:', word)
        link = "https://jiexi.pengdouw.com/jiexi3/?url=" + word
        html_data = requests.get(url=link).text
        video_url = re.findall(
            '<iframe id = "baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)


image = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\xiayu\\OneDrive\\Desktop\\code\\python_projects\\python_request\\photo.png"))
# set the photo for it
l = tk.Label(image=image)
l.pack()

# set port
choose_frame = tk.LabelFrame(root)
choose_frame.pack(pady=10, fill='both')


tk.Label(choose_frame, text="Choose Port: ",
         font=("黑体", 20)).pack(side=tk.LEFT)

num_int_var = tk.IntVar()
# initialize the number of int
num_int_var.set(1)

# set choices
tk.Radiobutton(choose_frame, text="1:vip system(very stable connection)",
               variable=num_int_var, value=1).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(choose_frame, text="2:vip system(very stable connection)",
               variable=num_int_var, value=2).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(choose_frame, text="3:vip system(very stable)",
               variable=num_int_var, value=3).pack(side=tk.LEFT, padx=5)

# input the url
input_frame = tk.LabelFrame(root)
input_frame.pack(pady=10, fill='both')

# set a variable to hold link
input_va = tk.StringVar()


tk.Label(input_frame, text="Enter URL: ", font=("黑体", 20)).pack(side=tk.LEFT)
tk.Entry(input_frame, width=100, relief='flat',
         textvariable=input_va).pack(side=tk.LEFT, fill='both')

# click for analyze
tk.Button(root, text="Go Analyze Right Now", font=(
    '黑体', 15), relief='flat', bg='#449d44', command=show).pack(fill='both')


# keep window
root.mainloop()
