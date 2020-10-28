#                                   Restaurant Management System
# user name: root
# password:  123
from tkinter import *
from functools import partial
from tkinter import messagebox
import tkinter.ttk as ttk
import random
import time
import sqlite3

def app():                                            # main funtion
    
    logWin.destroy()                                  # destroying login window
    root = Tk()                                       # creating main root window
    root.geometry("1600x750+0+0")
    root.title("Lovely Restaurant")

    Heading = Frame(root,bg="#7D1B7E",width = 1600,height=50,relief=SUNKEN)            #creating frame for headers
    Heading.pack(side=TOP)

    Menu = LabelFrame(root,width = 900,height=640,relief=SUNKEN, text="Menu")          #creating label frame for menus
    Menu.pack(fill= "both", expand="yes", padx=20, pady=20)


    Controls = LabelFrame(root,width = 900,height=300,relief=SUNKEN, text="Controls")  #creatinf label fram for controls
    Controls.pack(fill= "both", expand="yes", padx=20, pady=10)



    localtime=time.asctime(time.localtime(time.time()))             # storing local time in variable


    # setting hearders
    lblhead = Label(Heading, font=( 'aria' ,30, 'bold' ),text="Lovely Restaurant",fg="Black",bd=10,anchor='w')
    lblhead.grid(row=0,column=0)
    lblhead = Label(Heading, font=( 'aria' ,19, ),text=localtime,fg="black",anchor=W)
    lblhead.grid(row=1,column=0)



    def Cost():                                              # funtion to calculate cost of meal and return those values
        x = random.randint(10000, 1000000)                  # storing random number in variable
        randomRef = str(x)
        rand.set(randomRef)
        
        #extracting values from boxes and type-casting it to float
        
        quantity_chai         = float(Chai.get())
        quantity_coffee       = float(Coffee.get())
        quantity_lassi        = float(Lassi.get())
        quantity_chas         = float(Chas.get())
        quantity_samosa       = float(Samosa.get())
        quantity_vada_pav     = float(Vada_Pav.get())

        quantity_chana_masala = float(Chana_Masala.get())
        quantity_tikka_masala = float(Tikka_Masala.get())
        quantity_veg_korma    = float(Veg_Korma.get())
        quantity_matar_paneer = float(Matar_Paneer.get())
        quantity_shahi_paneer = float(Shahi_Paneer.get())

        quantity_veg_biryani  = float(Veg_Biryani.get())
        quantity_daal_tadka   = float(Daal_Tadka.get())
        quantity_daal_makhni  = float(Daal_Makhni.get())
        quantity_paratha      = float(Paratha.get())
        quantity_roti         = float(Roti.get())
        quantity_naan         = float(Naan.get())

        quantity_mung_halwa   = float(Mung_Halwa.get())
        quantity_gulab_jamun  = float(Gulab_Jamun.get())
        quantity_rabbdi       = float(Rabbdi.get())
        quantity_jalebi       = float(Jalebi.get())


        # calculating cost of items ordered
        
        costofChai            = quantity_chai     * 20
        costofCoffee          = quantity_coffee   * 40
        costofLassi           = quantity_lassi    * 60
        costofChas            = quantity_chas     * 30
        costofsamosa          = quantity_samosa   * 20
        costofVadaPav         = quantity_vada_pav * 30


        costofChanaMasala     = quantity_chana_masala * 100
        costofTikkaMasala     = quantity_tikka_masala * 120
        costofVegKorma        = quantity_veg_korma    * 120
        costofMatarPaneer     = quantity_matar_paneer * 140
        costofShahiPaneer     = quantity_shahi_paneer * 200


        costofVegBiryani      = quantity_veg_biryani * 350
        costofDaalTadka       = quantity_daal_tadka  * 70
        costofDaalMakhni      = quantity_daal_makhni * 80
        costofParatha         = quantity_paratha     * 30
        costofRoti            = quantity_roti        * 10
        costofNaan            = quantity_naan        * 40


        costofMungHalwa       = quantity_mung_halwa  * 60
        costofGulabJamun      = quantity_gulab_jamun * 50
        costofRabbdi          = quantity_rabbdi      * 50
        costofJalebi          = quantity_jalebi      * 40



        # performing various calculations and storing there values in variables 

        costofmeal = ("Rs.",str('%.2f'% (costofChai + costofCoffee + costofLassi + costofChas + costofsamosa + costofVadaPav + costofChanaMasala + costofTikkaMasala + costofVegKorma + costofMatarPaneer + costofShahiPaneer + costofVegBiryani + costofDaalTadka + costofDaalMakhni + costofParatha + costofRoti + costofNaan + costofMungHalwa + costofGulabJamun + costofRabbdi + costofJalebi)))
        PayTax=((costofChai + costofCoffee + costofLassi + costofChas + costofsamosa + costofVadaPav + costofChanaMasala + costofTikkaMasala + costofVegKorma + costofMatarPaneer + costofShahiPaneer + costofVegBiryani + costofDaalTadka + costofDaalMakhni + costofParatha + costofRoti + costofNaan + costofMungHalwa + costofGulabJamun + costofRabbdi + costofJalebi)*0.2)
        Totalcost=(costofChai + costofCoffee + costofLassi + costofChas + costofsamosa + costofVadaPav + costofChanaMasala + costofTikkaMasala + costofVegKorma + costofMatarPaneer + costofShahiPaneer + costofVegBiryani + costofDaalTadka + costofDaalMakhni + costofParatha + costofRoti + costofNaan + costofMungHalwa + costofGulabJamun + costofRabbdi + costofJalebi)
        Ser_Charge=((costofChai + costofCoffee + costofLassi + costofChas + costofsamosa + costofVadaPav + costofChanaMasala + costofTikkaMasala + costofVegKorma + costofMatarPaneer + costofShahiPaneer + costofVegBiryani + costofDaalTadka + costofDaalMakhni + costofParatha + costofRoti + costofNaan + costofMungHalwa + costofGulabJamun + costofRabbdi + costofJalebi)/99.2)
        Service="Rs.",str('%.2f'% Ser_Charge)
        OverAllCost="Rs.",str(round((PayTax + Totalcost + Ser_Charge),2))
        PaidTax="Rs.",str('%.2f'% PayTax)

        Service_Charge.set(Service)
        cost.set(costofmeal)
        Tax.set(PaidTax)
        Subtotal.set(costofmeal)
        Total.set(OverAllCost)
        lst = [costofmeal, PaidTax, Service, OverAllCost, randomRef]

        return lst      # returning values for future use


    def exit():                       # funtion to destroy main root window
        root.destroy()



    def reset():                     # funtion to reset the different values specified in boxes

        Chai.set(0)
        Coffee.set(0)
        Lassi.set(0)
        Chas.set(0)
        Samosa.set(0)
        Vada_Pav.set(0)
        Chana_Masala.set(0)
        Tikka_Masala.set(0)
        Veg_Korma.set(0)
        Matar_Paneer.set(0)
        Shahi_Paneer.set(0)
        Veg_Biryani.set(0)
        Daal_Tadka.set(0)
        Daal_Makhni.set(0)
        Paratha.set(0)
        Roti.set(0)
        Naan.set(0)
        Mung_Halwa.set(0)
        Gulab_Jamun.set(0)
        Rabbdi.set(0)
        Jalebi.set(0)
        rand.set("")
        Subtotal.set("")
        Total.set("")
        Service_Charge.set("")
        Tax.set("")
        cost.set("")
        CusName.set("")
        CusPhone.set("")



    # declaring various String Variables for future use
    
    Chai = StringVar()
    Coffee = StringVar()
    Lassi = StringVar()
    Chas = StringVar()
    Samosa = StringVar()
    Vada_Pav = StringVar()
    Chana_Masala = StringVar()
    Tikka_Masala = StringVar()
    Veg_Korma = StringVar()
    Matar_Paneer = StringVar()
    Shahi_Paneer = StringVar()
    Veg_Biryani = StringVar()
    Daal_Tadka = StringVar()
    Daal_Makhni = StringVar()
    Paratha = StringVar()
    Roti = StringVar()
    Naan = StringVar()
    Mung_Halwa = StringVar()
    Gulab_Jamun = StringVar()
    Rabbdi = StringVar()
    Jalebi = StringVar()

    rand = StringVar()
    Subtotal = StringVar()
    Total = StringVar()
    Service_Charge = StringVar()
    Tax = StringVar()
    cost = StringVar()
    
    CusName = StringVar()
    CusPhone = StringVar()



    # creating various menus on main interface
    
    lblorder = Label(Menu, font=( 'aria' ,15, 'bold' ),text="Order No.",fg="Black",bd=10,anchor='w')
    lblorder.grid(row=0,column=0)
    txtorder = Entry(Menu,font=('ariel' ,15,'bold'), textvariable=rand , bd=2 ,justify='right')
    txtorder.grid(row=0,column=1)


    lblChai = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Chai ",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblChai.grid(row=2,column=0)
    txtChai = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Chai , bd=2,justify='right')
    txtChai.grid(row=2,column=1)

    lblCoffee = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Coffee ",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblCoffee.grid(row=3,column=0)
    txtCoffee = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Coffee , bd=2,justify='right')
    txtCoffee.grid(row=3,column=1)

    lblLassi = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Lassi ",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblLassi.grid(row=4,column=0)
    txtLassi = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Lassi , bd=2,justify='right')
    txtLassi.grid(row=4,column=1)

    lblChas = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Chas ",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblChas.grid(row=5,column=0)
    txtChas = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Chas , bd=2,justify='right')
    txtChas.grid(row=5,column=1)

    lblSamosa = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Samosa",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblSamosa.grid(row=6,column=0)
    txtSamosa = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Samosa , bd=2,justify='right')
    txtSamosa.grid(row=6,column=1)

    lblVada_Pav = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Vada Pav",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblVada_Pav.grid(row=7,column=0)
    txtVada_Pav = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Vada_Pav , bd=2,justify='right')
    txtVada_Pav.grid(row=7,column=1)



    lblChana_Masala = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Chana Masala",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblChana_Masala.grid(row=2,column=3,padx=10)
    txtChana_Masala = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Chana_Masala , bd=2,justify='right')
    txtChana_Masala.grid(row=2,column=4)

    lblTikka_Masala = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Tikka Masala",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblTikka_Masala.grid(row=3,column=3,padx=10)
    txtTikka_Masala = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Tikka_Masala , bd=2,justify='right')
    txtTikka_Masala.grid(row=3,column=4)

    lblVeg_Korma = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Veg Korma",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblVeg_Korma.grid(row=4,column=3,padx=10)
    txtVeg_Korma = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Veg_Korma , bd=2,justify='right')
    txtVeg_Korma.grid(row=4,column=4)

    lblMatar_Paneer = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Matar Paneer",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblMatar_Paneer.grid(row=5,column=3,padx=10)
    txtMatar_Paneer = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Matar_Paneer , bd=2,justify='right')
    txtMatar_Paneer.grid(row=5,column=4,padx=10)

    lblShahi_Paneer = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Shahi Paneer",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblShahi_Paneer.grid(row=6,column=3,padx=10)
    txtShahi_Paneer = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Shahi_Paneer , bd=2,justify='right')
    txtShahi_Paneer.grid(row=6,column=4,padx=10)

    lblVeg_Biryani = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Veg Biryani",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblVeg_Biryani.grid(row=7,column=3,padx=10)
    txtVeg_Biryani = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Veg_Biryani , bd=2,justify='right')
    txtVeg_Biryani.grid(row=7,column=4,padx=10)



    lblDaal_Tadka = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Daal Tadka",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblDaal_Tadka.grid(row=2,column=5,padx=10)
    txtDaal_Tadka = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Daal_Tadka , bd=2,justify='right')
    txtDaal_Tadka.grid(row=2,column=6,padx=10)

    lblDaal_Makhni = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Daal Makhni",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblDaal_Makhni.grid(row=3,column=5,padx=10)
    txtDaal_Makhni = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Daal_Makhni , bd=2,justify='right')
    txtDaal_Makhni.grid(row=3,column=6,padx=10)

    lblParatha = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Paratha",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblParatha.grid(row=4,column=5,padx=10)
    txtParatha = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Paratha , bd=2,justify='right')
    txtParatha.grid(row=4,column=6,padx=10)

    lblRoti = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Chapati",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblRoti.grid(row=5,column=5,padx=10)
    txtRoti = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Roti , bd=2,justify='right')
    txtRoti.grid(row=5,column=6,padx=10)

    lblNaan = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Naan",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblNaan.grid(row=6,column=5,padx=10)
    txtNaan = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Naan , bd=2,justify='right')
    txtNaan.grid(row=6,column=6,padx=10)



    lblMung_Halwa = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Mung Halwa",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblMung_Halwa.grid(row=7,column=5,padx=10)
    txtMung_Halwa = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Mung_Halwa , bd=2,justify='right')
    txtMung_Halwa.grid(row=7,column=6,padx=10)


    lblRabbdi = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Rabbdi",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblRabbdi.grid(row=2,column=7,padx=10)
    txtRabbdi = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Rabbdi , bd=2,justify='right')
    txtRabbdi.grid(row=2,column=8,padx=10)

    lblJalebi = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Jalebi",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblJalebi.grid(row=3,column=7,padx=10)
    txtJalebi = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Jalebi , bd=2,justify='right')
    txtJalebi.grid(row=3,column=8,padx=10)

    lblGulab_Jamun = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Gulab Jamun",fg="#7D1B7E",bd=10,anchor='w',justify='right')
    lblGulab_Jamun.grid(row=4,column=7,padx=10)
    txtGulab_Jamun = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Gulab_Jamun , bd=2,justify='right')
    txtGulab_Jamun.grid(row=4,column=8,padx=10)


    lblTotal = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Total Cost",fg="Black",bd=10,anchor='w',justify='right')
    lblTotal.grid(row=7,column=7,padx=10)
    txtTotal = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=Total , bd=2,justify='right')
    txtTotal.grid(row=7,column=8,padx=10)

    lblCond = Label(Menu, font=( 'aria' ,10 ),text="*Including all taxes",fg="Black",bd=10,anchor='w',justify='right')
    lblCond.grid(row=8,column=8)
    
    lblTotal = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Customer Name:",fg="Black",bd=10,anchor='w',justify='right')
    lblTotal.grid(row=9,column=5,padx=10,pady=15)
    txtTotal = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=CusName , bd=2,justify='right')
    txtTotal.grid(row=9,column=6,padx=10, pady=15)
    
    lblTotal = Label(Menu, font=( 'aria' ,12, 'bold' ),text="Customer Phone:",fg="Black",bd=10,anchor='w',justify='right')
    lblTotal.grid(row=9,column=7,padx=10,pady=15)
    txtTotal = Entry(Menu,font=('ariel' ,12,'bold'), textvariable=CusPhone , bd=2,justify='right')
    txtTotal.grid(row=9,column=8,padx=10,pady=15)
    
     
    
    # function to pop-up message box, when user tries to generate bill without specifing name and phone number
    
    def customer():
        Name = CusName.get()
        Phone = CusPhone.get()
        
        if (Name == "" or Phone == ""):
            messagebox.showinfo("Alert", "Please fill Customer Name and Phone Number!")
        else:
            bill(Name, Phone)
            
    
    
    
    # function to create database if it's not created earlier
    
    def Database():
        global conn, cursor
        conn = sqlite3.connect('db_saleReports.db')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `SalesRepo` (sales_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name TEXT, Phone TEXT, Sales TEXT)")
            
    
    
    # funtion to insert values into the database
    
    def insert(cname, cphone, csales):
        Database()
        sql="INSERT INTO SalesRepo(Name, Phone, Sales) VALUES(?,?,?)"
        val=cname,cphone,csales
        cursor.execute(sql, val)
        conn.commit()

    
    
    # function to display rate card on different window
    
    def Rate():
        rateWin = Tk()
        rateWin.geometry("500x820+0+0")
        rateWin.title("Rate Card")

        RateCard = LabelFrame(rateWin,width = 400,height=800,relief=SUNKEN, text="Rate Card", bg="white")
        RateCard.pack(fill= "both", expand="yes", padx=20, pady=10)

        lblinfo = Label(RateCard, font=('aria', 12, 'bold'), text="ITEM", fg="Black", bd=2, anchor ='w',justify='left')
        lblinfo.grid(row=0, column=0,padx=25, pady=10)

        lblinfo = Label(RateCard, font=('aria', 12, 'bold'), text="RATE", fg="Black", anchor='w',justify='left')
        lblinfo.grid(row=0, column=3,padx=25, pady=10)

        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Chai", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=1, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 20/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=1, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Coffee", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=2, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 40/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=2, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Lassi", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=3, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 60/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=3, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Chas", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=4, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 30/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=4, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Samosa", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=5, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 20/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=5, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Vada Pav", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=6, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 30/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=6, column=3,padx=25, pady=5)

        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Channa Masala", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=7, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 100/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=7, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Tikka Masala", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=8, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 120/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=8, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Veg Korma", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=9, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 120/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=9, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Matar Paneer", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=10, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 140/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=10, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Shahi Paneer", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=11, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 200/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=11, column=3,padx=25, pady=5)

        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Veg Biryani", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=12, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 350/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=12, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Daal Tadka", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=13, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 70/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=13, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Daal Makhni", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=14, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 80/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=14, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Paratha", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=15, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 30/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=15, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Chapati", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=16, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 10/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=16, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Naan", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=17, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 40/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=17, column=3,padx=25, pady=5)

        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Mung Halwa", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=18, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 60/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=18, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Gulab Jamun", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=19, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 50/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=19, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rabbdi", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=20, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 50/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=20, column=3,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Jalebi", fg="#7D1B7E", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=21, column=0,padx=25, pady=5)
        lblinfo = Label(RateCard, font=('aria', 10, 'bold'), text="Rs. 40/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=21, column=3,padx=25, pady=5)

        RateCard.mainloop()
    
    
    
    # funtion to generate bill and display it on diffent window
    
    def bill(nam, phn):
        
        billWin = Tk()
        billWin.geometry("600x520+550+50")
        billWin.title("Bill")

        billFrame = LabelFrame(billWin,width = 580,height=500,relief=SUNKEN, text="Bill", bg="white")
        billFrame.pack(fill= "both", expand="yes", padx=20, pady=10)

        
        rtn = Cost()       # calling cost function to retrive values

        
        lbinfo = Label(billFrame, font=( 'aria' ,19, 'bold' ),text="Lovely Restaurant",fg="Black",bd=10,anchor='w',bg="white")
        lbinfo.grid(row=0,column=0,padx=10, pady=15)
        lbinfo = Label(billFrame, font=( 'aria' ,10, ),text=localtime,fg="black",anchor=W,bg="white")
        lbinfo.grid(row=0,column=1,padx=10, pady=5)

        lbinfo = Label(billFrame, font=( 'aria' ,10, ),text="------------------------------------------",fg="black",anchor=W,bg="white")
        lbinfo.grid(row=2,column=0)
        lbinfo = Label(billFrame, font=( 'aria' ,10, ),text="------------------------------------------",fg="black",anchor=W,bg="white")
        lbinfo.grid(row=2,column=1)

        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="Order no.       - ", fg="Black", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=3, column=0,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text=rtn[4], fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=3, column=1,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="Name             - ", fg="Black", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=4, column=0,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text=nam, fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=4, column=1,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="Phone no.      - ", fg="Black", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=5, column=0,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text=phn, fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=5, column=1,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="Cost of Meal   - ", fg="Black", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=6, column=0,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="Rs. "+ rtn[0][1] + "/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=6, column=1,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="GST / TAX       -", fg="Black", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=7, column=0,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="Rs. "+ rtn[1][1] + "/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=7, column=1,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="Service Charges -", fg="Black", anchor='w',justify='left', bg="white")
        lblinfo.grid(row=8, column=0,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="Rs. "+ rtn[2][1] + "/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=8, column=1,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="Total Bill       - ", fg="Black", anchor='w',justify='left', bg="white")

        lbinfo = Label(billFrame, font=( 'aria' ,10, ),text="------------------------------------------",fg="black",anchor=W,bg="white")
        lbinfo.grid(row=9,column=0)
        lbinfo = Label(billFrame, font=( 'aria' ,10, ),text="------------------------------------------",fg="black",anchor=W,bg="white")
        lbinfo.grid(row=9,column=1)

        lblinfo.grid(row=10, column=0,padx=25, pady=5)
        lblinfo = Label(billFrame, font=('aria', 10, 'bold'), text="Rs. "+ rtn[3][1] + "/-", fg="Black", anchor='w', bg="white")
        lblinfo.grid(row=10, column=1,padx=25, pady=5)

        lbinfo = Label(billFrame, font=( 'aria' ,10, ),text="------------------------------------------",fg="black",anchor=W,bg="white")
        lbinfo.grid(row=11,column=0)
        lbinfo = Label(billFrame, font=( 'aria' ,10, ),text="------------------------------------------",fg="black",anchor=W,bg="white")
        lbinfo.grid(row=11,column=1)

        lbinfo = Label(billFrame, font=( 'aria' ,10, 'bold' ),text="This Bill is Auto Generated.",fg="Black",bd=10,anchor='w',bg="white")
        lbinfo.grid(row=13,column=1,padx=10, pady=15)
        
        
        insert(nam, phn, rtn[3][1])   # calling insert function to insert values into the data base
        billWin.mainloop()
            
    
    
    # function to generate sales report
    
    def report():
            
        repo = Tk()
        repo.title("Sales Report")
        screen_width = repo.winfo_screenwidth()
        screen_height = repo.winfo_screenheight()
        width = 800
        height = 400
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        repo.geometry('%dx%d+%d+%d' % (width, height, x, y))
        repo.resizable(0, 0)
        
        
        # funtion to insert values into tree view
        
        def populateView():
            conn = sqlite3.connect('db_saleReports.db')
            cursor = conn.cursor()
            tree.delete(*tree.get_children())
            cursor.execute("SELECT * FROM `SalesRepo` ORDER BY `sales_id` ASC")
            fetch = cursor.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data[0],data[1], data[2], data[3]))

        # creating frames and buttons
        
        Top = Frame(repo, width=700, height=50, bd=2, relief="raise")
        Top.pack(side=TOP)
        Button_Group=Frame(repo, width=700, height=50)
        Button_Group.pack(side=TOP)
        Buttons = Frame(Button_Group, width=200, height=50)
        Buttons.pack(side=LEFT)
        Buttons1 = Frame(Button_Group, width=500, height=50)
        Buttons1.pack(side=RIGHT)
        Body = Frame(repo, width=700, height=300, bd=2, relief="raise")
        Body.pack(side=BOTTOM)

        
        txt_title = Label(Top, width=300, font=('arial', 24), text = "Sales Report")
        txt_title.pack()

        
        btn_display = Button(Buttons,padx=19,pady=10,font=('ariel' ,12,'bold'), width=15, text="Display All", command=populateView,bg="#7D0552",fg='white')
        btn_display.pack(side=LEFT,padx=20, pady=20)

        
        # creating scroll-bar on tree view
        
        scrollbary = Scrollbar(Body, orient=VERTICAL)
        scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
        tree = ttk.Treeview(Body, columns=("sales_id","Name", "Phone", "Sales"), selectmode="extended", height=300, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        
        # setting various headings and columns on tree view
        
        tree.heading('sales_id', text="Sr. no.", anchor=W)
        tree.heading('Name', text="Name", anchor=W)
        tree.heading('Phone', text="Phone", anchor=W)
        tree.heading('Sales', text="Sales", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=200)
        tree.column('#4', stretch=NO, minwidth=0, width=200)
        tree.pack(pady=5)

        repo.mainloop()
        

    # creating varoius control buttons to control the whole GUI interface
    
    btnReset=Button(Controls,padx=19,pady=10, bd=2 ,fg="white",font=('ariel' ,12,'bold'),width=10, text="RESET", bg="#7D0552",command=reset)
    btnReset.grid(row=0, column=1, padx=20, pady=20)

    btnRate=Button(Controls,padx=19,pady=10, bd=2 ,fg="white",font=('ariel' ,12,'bold'),width=10, text="RATE CARD", bg="#7D0552",command=Rate)
    btnRate.grid(row=0, column=2, padx=20, pady=20)

    btnTotal=Button(Controls,padx=19,pady=10, bd=2 ,fg="white",font=('ariel' ,12,'bold'),width=10, text="TOTAL COST", bg="#7D0552",command=Cost)
    btnTotal.grid(row=0, column=3, padx=20, pady=20)

    btnBill=Button(Controls,padx=19,pady=10, bd=2 ,fg="white",font=('ariel' ,12,'bold'),width=10, text="GENERATE BILL", bg="#7D0552",command=customer)
    btnBill.grid(row=0, column=4, padx=20, pady=20)
    
    btnsalesReport=Button(Controls,padx=19,pady=10, bd=2 ,fg="white",font=('ariel' ,12,'bold'),width=10, text="SALES REPORT", bg="#7D0552",command=report)
    btnsalesReport.grid(row=0, column=5, padx=20, pady=20)

    btnExit=Button(Controls,padx=19,pady=10, bd=2 ,fg="white",font=('ariel' ,12,'bold'),width=10, text="EXIT", bg="#7D0552",command=exit)
    btnExit.grid(row=0, column=6,padx=20, pady=20) 


    reset()
    root.mainloop()
    

# funtion to validate user login

def validateLogin(username, password):
    user= username.get()
    passwd = password.get()
    
    if (user == "root" and passwd == "123"):
        
        app()
        
    else:
        
        errorLabel = Label(logFrame, font=('aria', 10, 'bold'), text="Wrong User Name or Password", fg="red", bd=10, anchor='w', justify='left', bg='white').grid(row=4,column=1)
        username.set("")
        password.set("")

        
# creating login window

logWin = Tk()
logWin.geometry("600x520+550+50")
logWin.title("Login")

logFrame = LabelFrame(logWin,width = 580,height=500,relief=SUNKEN, bg="white", text="Login")
logFrame.pack(fill= "both", expand="yes", padx=20, pady=10)

WlcmLabel = Label(logFrame, font=( 'aria' ,15, 'bold' ), text="Welcome!",fg="Black",bd=10,anchor='w',justify='right', bg="white").grid(row=0, column=1,padx=28, pady=19)

usernameLabel = Label(logFrame, font=( 'aria' ,12, 'bold' ), text="User Name:",fg="Black",bd=10,anchor='w',justify='right', bg="white").grid(row=1, column=0,padx=28, pady=5)
username = StringVar()
usernameEntry = Entry(logFrame,font=('ariel' ,12,'bold'),bd=2,justify='right', textvariable=username).grid(row=1, column=1,padx=28, pady=5)  


passwordLabel = Label(logFrame,text="Password:",font=( 'aria' ,12, 'bold' ),fg="Black",bd=10,anchor='w',justify='right', bg="white").grid(row=2, column=0,padx=28, pady=10)  
password = StringVar()
passwordEntry = Entry(logFrame, textvariable=password, show='*',font=('ariel' ,12,'bold'), bd=2,justify='right').grid(row=2, column=1,padx=28, pady=10)  

validateLogin = partial(validateLogin, username, password)


btnEnter=Button(logFrame,padx=19,pady=10, bd=2 ,fg="white",font=('ariel' ,12,'bold'),width=10, text="Enter", bg="#7D0552",command=validateLogin)
btnEnter.grid(row=3, column=1, padx=28, pady=20)  

logWin.mainloop()