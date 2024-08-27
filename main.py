from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

#Initialize the main window
root = Tk()
root.title("Advanced BMI Calculator")
root.geometry("500x620+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")

#function to calculate BMI
def calculate_bmi():
    try:
        h = float(Height.get())
        w = float(Weight.get())

#Convert height into meter
        m = h/100
        bmi = round(w / m**2, 1)
        label1.config(text=bmi)

#Display appropriate message based on BMI
#you can change vale, because different countries have different bmi index
        if bmi<=18.5:
            label1.config(fg="blue")
            label2.config(text="UnderWeight!", fg="blue", wraplength=300)
            label3.config(text="You have lower weight than normal!", fg="blue", wraplength=300)

        elif 18.5 < bmi <=24.9:
            label1.config(fg="green")
            label2.config(text="Normal!", fg="green", wraplength=300)
            label3.config(text="You have a healthy body weight.", fg="green", wraplength=300)

        elif 25 <= bmi <=29.9:
            label1.config(fg="orange")
            label2.config(text="OverWeight!", fg="orange", wraplength=300)
            label3.config(text="You are slightly overweight! Consider lifestyle changes.", fg="orange", wraplength=300)

        else:
            label1.config(fg="red")
            label2.config(text="Obese!", fg="red", wraplength=300)
            label3.config(text="Your health may be at risk. Please consider consulting a healthcare provider.", fg="red", wraplength=300)
    except ValueError:
        label1.config(text="Error", fg="red")
        label2.config(text="Invalid input", fg="red", wraplength=300)
        label3.config(text="Please enter valid nnumbers for height and weight.", fg="red", wraplength=300)

#function to update height and adjust the image
def update_height(event):
    Height.set(get_current_value(current_value))

    size =int(float(get_current_value(current_value)))
    img = Image.open("C:/Users/hp/VS/Python/BMI CALCULATOR/man.png")
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70,y=550 - size)
    secondimage.image = photo2

#function to update weight
def update_weight(event):
    Weight.set(get_current_value(current_value2))

#Utility function to get the current value of a slider
def get_current_value(var):
    return '{: .1f}'.format(var.get())

#Setting up the window icon
image_icon = PhotoImage(file="C:/Users/hp/VS/Python/BMI CALCULATOR/icon.png")
root.iconphoto(False, image_icon)

#Top image setup
top_img = PhotoImage(file="C:/Users/hp/VS/Python/BMI CALCULATOR/top.png")
top_image=Label(root, image=top_img, background="#f0f1f5")
top_image.place(x=-10, y=-10)

#Bottom background label
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

#Two boxes for input
box_img = PhotoImage(file="C:/Users/hp/VS/Python/BMI CALCULATOR/box.png")
Label(root, image=box_img).place(x=20, y=100)
Label(root, image=box_img).place(x=240, y=100)

#scale image
scale_img = PhotoImage(file="C:/Users/hp/VS/Python/BMI CALCULATOR/scale.png")
Label(root, image=scale_img, bg="lightblue").place(x=20,y=310)

#Slider 1 for Height
current_value = tk.DoubleVar()
slider = ttk.Scale(root, from_=0, to=220, orient='horizontal', style="TScale", command=update_height, variable=current_value)
slider.place(x=80, y=250)

#Slider 2 for Weight
current_value2 = tk.DoubleVar()
slider2 = ttk.Scale(root, from_=0, to=200, orient='horizontal', style="TScale", command=update_weight, variable=current_value2)
slider2.place(x=300, y=250)

#Entry Box
Height=StringVar()
Weight=StringVar()

height = Entry(root, textvariable=Height, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER) 
height.place(x=35,y=160)
Height.set(get_current_value(current_value))

weight = Entry(root, textvariable=Weight, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER) 
weight.place(x=225,y=160)
Weight.set(get_current_value(current_value2))

#Man image
secondimage = Label(root, bg="lightblue")
secondimage.place(x=70, y=530)

#View Report Button
Button(root, text="View Report", width=15, height=2, font="arial 10 bold", bg="#1f6e68", fg="white", command=calculate_bmi).place(x=280,y=340)

#Labels for BMI Results
label1 = Label(root, font="arial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=125,y=305)

label2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=280,y=430)

label3 = Label(root, font="arial 10", bg="lightblue")
label3.place(x=200,y=500)

root.mainloop()
