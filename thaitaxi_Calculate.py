from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title('Thai Taxi Calculate Dev. by Oat')
root.geometry('500x750')


label_01 = Label(root,text='Thai Taxi Cost Calculate',fg='red',font=('Tahoma',20,'bold')).place(x=130,y=20)

logo = PhotoImage(file='taxi.png')
logo_image = Label(root,image=logo).place(x=150,y=70)

label_02 = Label(root,text='Please fill the distance in number for calculate the price',font=(None,16)).place(x=55,y=170)

distance = StringVar()
entry_1 = ttk.Entry(root,textvariable=distance,font=(None,20)).place(x=120,y=200)


def taxiCal():
      try:
            dis_cal = float(distance.get())
            price = 0
            if dis_cal <= 1:
                  price += 35
                  messagebox.showinfo(f'The distance is {dis_cal} km.',f'You have to pay {price} to Taxi')
                  distance.set('1')
            elif dis_cal > 1 and dis_cal <= 10:
                  price = (dis_cal * 5.5) + 35
                  messagebox.showinfo(f'The distance is {dis_cal} km.',f'You have to pay {price} to Taxi')
                  distance.set('1')
            elif dis_cal > 10 and dis_cal <= 20:
                  price = (dis_cal * 6.5) + 35
                  messagebox.showinfo(f'The distance is {dis_cal} km.',f'You have to pay {price} to Taxi')
                  distance.set('1')
            elif dis_cal > 20 and dis_cal <= 40:
                  price = (dis_cal * 7.5) + 35
                  messagebox.showinfo(f'The distance is {dis_cal} km.',f'You have to pay {price} to Taxi')
                  distance.set('1')
            elif dis_cal > 40 and dis_cal <= 60:
                  price = (dis_cal * 8) + 35
                  messagebox.showinfo(f'The distance is {dis_cal} km.',f'You have to pay {price} to Taxi')
                  distance.set('1')
            elif dis_cal > 60 and dis_cal <= 80:
                  price = (dis_cal * 9) + 35
                  messagebox.showinfo(f'The distance is {dis_cal} km.',f'You have to pay {price} to Taxi')
                  distance.set('1')
            elif dis_cal > 80:
                  price = (dis_cal * 10.5) + 35
                  messagebox.showinfo(f'The distance is {dis_cal} km.',f'You have to pay {price} to Taxi')
                  distance.set('1')
      except:
            messagebox.showwarning('Invalid fill','Please try again with number')
            distance.set('1')

button_1 = ttk.Button(root,text='Calculate',command=taxiCal).place(x=200,y=250)


label_03 = Label(root,text='''
                 อัตราค่าโดยสายแท็กซี่
                 
                 ระยะทาง 1 กิโลเมตรแรก 35.00 บาท
                 
                 ระยะทางเกินกว่า 1 กิโลเมตร ถึง กิโลเมตรที่ 10
                 กิโลเมตรละ 5.50 บาท
                 
                 ระยะทางเกินกว่า 10 กิโลเมตร ถึง กิโลเมตรที่ 20
                 กิโลเมตรละ 6.50 บาท
                 
                 ระยะทางเกินกว่า 20 กิโลเมตร ถึง กิโลเมตรที่ 40
                 กิโลเมตรละ 7.50 บาท
                 
                 ระยะทางเกินกว่า 40 กิโลเมตร ถึง กิโลเมตรที่ 60
                 กิโลเมตรละ 8.00 บาท
                 
                 ระยะทางเกินกว่า 60 กิโลเมตร ถึง กิโลเมตรที่ 80
                 กิโลเมตรละ 9.00 บาท
                 
                 ระยะทางเกินกว่า 80 กิโลเมตร ขึ้นไป
                 กิโลเมตรละ 10.50 บาท''',font=(None,14)).place(x=50,y=290)


root.mainloop()