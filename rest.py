
#import libraries

import random
import time
from tkinter import*

#creating gui environment
root = Tk()
root.geometry("1600x800")
root.title("Restaurant Management System")
# creating frames
Tops =  Frame(root,width=800,height=50)
Tops.pack(side=TOP)

f1= Frame(root,width=800,height=700)
f1.pack(side=LEFT)

f2= Frame(root,width=300,height=700)
f2.pack(side=RIGHT)

localtime= time.asctime(time.localtime(time.time()))

lbl= Label(Tops,font=('arial',50,'bold'),text=" Restaurant Management System",fg="Black")
lbl.grid(row=0,column=0)


lb2= Label(Tops,font=('arial',20),text=localtime,fg="Black")
lb2.grid(row=1,column=0)

#functionn to calculate cost
def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    rand.set(randomRef)

    cof =float(Fries.get())
    colfries= float(Largefries.get())
    cob= float(Burger.get())
    cofi= float(pizza.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflargefries = colfries*40
    costofburger = cob*35
    costofpizza = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflargefries + costofburger + costofpizza + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflargefries + costofburger + costofpizza +  costofcheeseburger + costofdrinks)*0.33)
    Totalcost=(costoffries +  costoflargefries + costofburger + costofpizza  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflargefries + costofburger + costofpizza + costofcheeseburger + costofdrinks)*0.033)
    Service="Rs.",str('%.2f'% Ser_Charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge)


    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PayTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)
#function to exit upon pressing exit button
def qexit():
    root.destroy()

#declaration of variables
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
pizza = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Cheese_burger = StringVar()


lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="steel blue")
lblfries.grid(row=1,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries ,insertwidth=4,bg="powder blue" ,justify='right')
txtfries.grid(row=1,column=1)

lblLargefries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="steel blue")
lblLargefries.grid(row=2,column=0)
txtLargefries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Largefries ,insertwidth=4,bg="powder blue" ,justify='right')
txtLargefries.grid(row=2,column=1)


lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="steel blue")
lblburger.grid(row=3,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger ,insertwidth=4,bg="powder blue" ,justify='right')
txtburger.grid(row=3,column=1)

lblpizza = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="steel blue")
lblpizza.grid(row=4,column=0)
txtpizza = Entry(f1,font=('ariel' ,16,'bold'), textvariable=pizza ,insertwidth=4,bg="powder blue" ,justify='right')
txtpizza.grid(row=4,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="steel blue")
lblCheese_burger.grid(row=5,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger,insertwidth=4,bg="powder blue" ,justify='right')
txtCheese_burger.grid(row=5,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue")
lblDrinks.grid(row=1,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks ,insertwidth=4,bg="powder blue" ,justify='right')
txtDrinks.grid(row=1,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="steel blue")
lblcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost ,insertwidth=4,bg="powder blue" ,justify='right')
txtcost.grid(row=2,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="steel blue")
lblService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable =Service_Charge,insertwidth=4,bg="powder blue" ,justify='right')
txtService_Charge.grid(row=3,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue")
lblTax.grid(row=4,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable= Tax,insertwidth=4,bg="powder blue" ,justify='right')
txtTax.grid(row=4,column=3)


lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue")
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total ,insertwidth=4,bg="powder blue" ,justify='right')
txtTotal.grid(row=5,column=3)


btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
btnTotal.grid(row=7, column=1)



btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=qexit)
btnexit.grid(row=7, column=3)


lblinfo = Label(f2, font=('aria', 15, 'bold'), text="ITEM", fg="black")
lblinfo.grid(row=0, column=0)
lblinfo = Label(f2, font=('aria', 15,'bold'), text="_____________", fg="white")
lblinfo.grid(row=0, column=2)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="PRICE(RS)", fg="black")
lblinfo.grid(row=0, column=3)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue")
lblinfo.grid(row=1, column=0)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="25", fg="steel blue")
lblinfo.grid(row=1, column=3)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue")
lblinfo.grid(row=2, column=0)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="40", fg="steel blue")
lblinfo.grid(row=2, column=3)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue")
lblinfo.grid(row=3, column=0)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="35", fg="steel blue")
lblinfo.grid(row=3, column=3)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue")
lblinfo.grid(row=4, column=0)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="50", fg="steel blue")
lblinfo.grid(row=4, column=3)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue")
lblinfo.grid(row=5, column=0)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="30", fg="steel blue")
lblinfo.grid(row=5, column=3)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue")
lblinfo.grid(row=6, column=0)
lblinfo = Label(f2, font=('aria', 15, 'bold'), text="35", fg="steel blue")
lblinfo.grid(row=6, column=3)
root.mainloop()