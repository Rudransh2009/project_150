# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:08:23 2021

@author: pc
"""

from tkinter import*
import random
root=Tk()
root.title('City And Name')
root.geometry('500x500')


contry=Entry(root)
city=Entry(root)

conty_list=Label(root)
city_list=Label(root)
conty_show=Label(root)
city_show=Label(root)

contry_list=[]
capital_list=[]

def addNames():
    contry_name=contry.get()
    city_name=city.get()
    contry_list.append(contry_name)
    capital_list.append(city_name)
    conty_list['text']='Contry List :'+str(contry_list)
    city_list['text']='Capital List :'+str(capital_list)

def random_no():
    length1=len(contry_list)
    random_no_1=random.randint(0,length1-1)
    random_contry=contry_list[random_no_1]
    conty_show['text']='YOUR CONTRY  IS :'+str(random_contry)
    
    length2=len(city_list)
    random_no_2=random.randint(0,length2-1)
    random_captil=capital_list[random_no_2]
    city_show['text']='YOUR Captil  IS :'+str(random_captil)
    
contry.place(relx=0.5,rely=0.2,anchor=CENTER)
city.place(relx=0.5,rely=0.3,anchor=CENTER)

btn=Button(root,text='show contry list :',command=addNames)
bt=Button(root,text='show your contry:',command=random_no)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

conty_list.place(relx=0.5,rely=0.5,anchor=CENTER)
city_list.place(relx=0.5,rely=0.6,anchor=CENTER)

bt.place(relx=0.5,rely=0.7,anchor=CENTER)

conty_show.place(relx=0.5,rely=0.8,anchor=CENTER)
city_show.place(relx=0.5,rely=0.9,anchor=CENTER)

root.mainloop()
