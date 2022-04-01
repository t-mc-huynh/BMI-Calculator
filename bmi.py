from tkinter import *
from tkinter import messagebox

def calculateBMI():
    lb = int(weight_tf.get())
    # cm = int(height_tf.get())/100
    feet = float(height_tf.get())
    inch = feet * 12
    bmi = (lb / (inch * inch)) * 703
    bmi = round(bmi, 1)
    indexBMI(bmi)

def indexBMI(bmi):
    if bmi < 16.0:
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is severely underweight')
    elif (bmi > 16.0) and (bmi < 18.4):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is underweight')
    elif (bmi > 18.4) and (bmi < 24.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is overweight')
    elif (bmi > 29.9) and (bmi < 34.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is moderately obese')
    elif (bmi > 34.9) and (bmi < 39.9):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is severly obese')
    elif (bmi > 40.0):
        messagebox.showinfo('bmi-pythonguides', f'BMI = {bmi} is morbidly obese') 
    else:
        messagebox.showerror('bmi-pythonguides', 'something went wrong!') 
        
def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
    padx=10, 
    pady=10
)
frame.pack(expand=True)

frame4 = Frame(
    frame
)

frame2 = Frame(
    frame
)

select_lb = Label(
    frame2,
    text='Select Mode'
)

us_rb = Radiobutton(
    frame2,
    text = 'US',
    variable = var,
    value = 1
)

metric_rb = Radiobutton(
    frame2,
    text = 'Metric',
    variable = var,
    value = 2
)

frame3 = Frame(
    frame
)

age_lb = Label(
    frame3,
    text="Enter Age (2 - 120)     "
)

age_tf = Entry(
    frame3, 
)

frame5 = Frame(
    frame
)

gen_lb = Label(
    frame5,
    text='Select Gender'
)

male_rb = Radiobutton(
    frame5,
    text = 'Male',
    variable = var,
    value = 3
)

female_rb = Radiobutton(
    frame5,
    text = 'Female',
    variable = var,
    value = 4
)

height_lb = Label(
    frame4,
    text="Enter Height (inches)  "
)

weight_lb = Label(
    frame4,
    text="Enter Weight (lbs)  "
)

height_tf = Entry(
    frame4,
)

weight_tf = Entry(
    frame4,
)

cal_btn = Button(
    frame,
    text='Calculate',
    command=calculateBMI
)

reset_btn = Button(
    frame,
    text='Reset',
    command=reset_entry
)

exit_btn = Button(
    frame,
    text='Exit',
    command=lambda:ws.destroy()
)

frame2.grid(row=0, column=2, pady=5)
select_lb.grid(row=1, column=0)
us_rb.grid(row=1, column=1)
metric_rb.grid(row=1, column=2)

frame3.grid(row=1, column=2, pady=3)
age_lb.grid(row=1, column=0)
age_tf.grid(row=1, column=2, pady=5)

gen_lb.grid(row=1, column=0)
male_rb.grid(row=1, column=1)
female_rb.grid(row=1, column=2)

frame4.grid(row=2, column=2)
height_lb.grid(row=1, column=1)
weight_lb.grid(row=2, column=1)
height_tf.grid(row=1, column=2, pady=5)
weight_tf.grid(row=2, column=2, pady=5)

frame5.grid(row=5, columnspan=3, pady=10)

ws.mainloop()