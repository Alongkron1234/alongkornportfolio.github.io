from cgitb import text
from msilib.schema import Font
from tkinter import *
from tkinter import ttk
from tkinter import font
from tokenize import String
from turtle import bgcolor
import requests
from tkinter import messagebox

root=Tk()
root.title('Covid-19')
root.geometry('650x470')

url_A = "https://covid19.ddc.moph.go.th/api/Cases/today-cases-all"
url_P = "https://covid19.ddc.moph.go.th/api/Cases/today-cases-by-provinces"
data_province = requests.get(url_P).json()
data_all = requests.get(url_A).json()

p1 = PhotoImage(file = 'D:\Icon\App-virus-detected-2-icon.png')
p2 = PhotoImage(file = 'D:\Icon\Thailand-Flag-icon.png')
p3 = PhotoImage(file = 'D:\Icon\Search-icon.png')
FONT1=(None, 17)
root.iconphoto(False, p1)
set = {'a','b'}

def show_P(event=None):
    province = V_province.get()
    for index in data_province:
        set.add(index["province"])
    for indexx in data_province:
        if indexx["province"] == province:
            V_show_1.set(f"จังหวัด: {indexx['province']}")
            V_show_2.set("โควิดล่าสุดวันที่: {}".format(indexx['update_date']))
            V_show_3.set("ติดเชื้อเพิ่มวันนี้: {:,} ราย".format(indexx['new_case']))
            V_show_4.set("เสียชีวิตเพิ่มวันนี้: {:,} ราย".format(indexx['new_death']))
            V_show_5.set("เสียชีวิตสะสม: {:,} ราย".format(indexx['total_death']))
            V_show_6.set("ยอดสะสมตั้งแต่เริ่มระบาด: {:,} ราย".format(indexx['total_case']))
            break
        elif province not in set:
            V_show_1.set('')
            V_show_2.set('')
            V_show_3.set('')
            V_show_4.set('')
            V_show_5.set('') 
            V_show_6.set('') 
            messagebox.askretrycancel("ใส่ชื่อจังหวัดไม่ถูกต้อง", "Try again?")
            break
        
            
    V_province.set('')
    E1.focus()

def show_a():
    V_show_1.set(f"โควิดล่าสุดวันที่: {data_all[0]['update_date']}")
    V_show_2.set("หายป่วยวันนี้: {:,}".format(data_all[0]['new_recovered']))
    V_show_3.set("ติดเชื้อเพิ่มวันนี้: {:,} ราย".format(data_all[0]['new_case']))
    V_show_4.set("เสียชีวิตเพิ่ม: {:,} ราย".format(data_all[0]['new_death']))
    V_show_5.set("เสียชีวิตสะสม: {:,} ราย".format(data_all[0]['total_death']))
    V_show_6.set("ยอดสะสมตั้งแต่เริ่มระบาด: {:,} ราย".format(data_all[0]['total_case']))


V_province = StringVar()
V_show_1 = StringVar()
V_show_2 = StringVar()
V_show_3 = StringVar()
V_show_4 = StringVar()
V_show_5 = StringVar()
V_show_6 = StringVar()

L = ttk.Label(root, text="กรอกจังหวัดของคุณ", font=FONT1)
L.pack(pady=5)

E1=ttk.Entry(root, textvariable=V_province, font=FONT1)
E1.pack(pady=10)

B1=ttk.Button(root, text='ค้นหา',image=p3,compound=LEFT ,command=show_P)
B1.pack(pady=10, ipady=5)

B2=ttk.Button(root, text='โควิดประเทศไทย',image=p2,compound=LEFT ,command=show_a)
B2.pack(pady=10, ipadx=10, ipady=5)

L1=ttk.Label(root, textvariable=V_show_1, font=FONT1, foreground='green')
L1.pack(pady=5)

L2=ttk.Label(root, textvariable=V_show_2, font=FONT1, foreground='green')
L2.pack(pady=5)

L3=ttk.Label(root, textvariable=V_show_3, font=FONT1, foreground='green')
L3.pack(pady=5)

L4=ttk.Label(root, textvariable=V_show_4, font=FONT1, foreground='green')
L4.pack(pady=5)

L5=ttk.Label(root, textvariable=V_show_5, font=FONT1, foreground='green')
L5.pack(pady=5)

L6=ttk.Label(root, textvariable=V_show_6, font=FONT1, foreground='green')
L6.pack(pady=5)
E1.bind('<Return>', show_P)
root.mainloop()