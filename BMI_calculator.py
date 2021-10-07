from tkinter import *
from tkinter import messagebox


def get_height():
    height = float(entry2.get())
    return height


def get_weight():
    weight = float(entry1.get())
    return weight


def calculate_bmi(a=""):
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo('Result', 'Please enter positive height!!')
    except ValueError:
        messagebox.showinfo('Result', 'Please enter valid data!')
    else:
        if bmi <= 15.0:
            res = 'Your BMI is ' + \
                str(bmi) + '\nRemarks: Very severely underweight!!'
            messagebox.showinfo('Result', res)
        elif 15.0 < bmi <= 16.0:
            res = 'Your BMI is ' + \
                str(bmi) + '\nRemarks: Severely underweight!'
            messagebox.showinfo('Result', res)
        elif 16.0 < bmi < 18.5:
            res = 'Your BMI is ' + str(bmi) + '\nRemarks: Underweight!'
            messagebox.showinfo('Result', res)
        elif 18.5 <= bmi <= 25.0:
            res = 'Your BMI is ' + str(bmi) + '\nRemarks: Normal.'
            messagebox.showinfo('Result', res)
        elif 25.0 < bmi <= 30:
            res = 'Your BMI is ' + str(bmi) + '\nRemarks: Overweight.'
            messagebox.showinfo('Result', res)
        elif 30.0 < bmi <= 35.0:
            res = 'Your BMI is ' + str(bmi) + '\nRemarks: Moderately obese!'
            messagebox.showinfo('Result', res)
        elif 35.0 < bmi <= 40.0:
            res = 'Your BMI is ' + str(bmi) + '\nRemarks: Severely obese!'
            messagebox.showinfo('Result', res)
        else:
            res = 'Your BMI is ' + str(bmi) + '\nRemarks: Super obese!!'
            messagebox.showinfo('Result', res)


if __name__ == '__main__':
    root = Tk()
    root.bind("<Return>", calculate_bmi)
    root.geometry('400x400')
    root.config(bg='sky blue')
    root.title("BMI Calculator (made by S.M.H Naghavi)")
    root.resizable(width=False, height=False)
    lbl1 = Label(root, bg='sky blue', text='Welcome to BMI Calculator',
                 font=('Helvetica', 15, 'bold'), pady=10)
    lbl1.place(x=60, y=20)
    lbl2 = Label(root, bg='sky blue', text='Enter Weight (in kg):', bd=6,
                 font=("Helvetica", 10, "bold"), pady=5)
    lbl2.place(x=60, y=80)
    entry1 = Entry(root, bd=8, width=6, font='Roboto 11')
    entry1.place(x=240, y=80)
    lbl3 = Label(root, bg='sky blue', text='Enter Height (in cm):', bd=6,
                 font=('Helvetica', 10, 'bold'), pady=5)
    lbl3.place(x=60, y=141)
    entry2 = Entry(root, bd=8, width=6, font="Roboto 11")
    entry2.place(x=240, y=141)
    bmi_btn = Button(bg='blue', bd=12, text='BMI', padx=20, pady=10, command=calculate_bmi,
                     font=('Helvetica', 20, 'bold'))
    bmi_btn.place(x=140, y=250)
    root.mainloop()
