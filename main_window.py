#login section|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


def login1():
    from tkinter import Tk,Label,Entry,Button,Checkbutton
    from tkinter.constants import BOTTOM, TOP

    global entry1
    global entry2

    def check():

        from tkinter import messagebox
        username=entry1.get()
        password=entry2.get()

        if (username=="" and password==""):
           messagebox.showinfo("","Blank Not Allowed")

        elif (username=="AAAAA" and password=="12345"):  
           messagebox.showinfo("","login success")

        else:
           messagebox.showinfo("","incorrect username and password")

    root=Tk()
    root.title("Login")
    root.geometry("1300x700+20+10")
    root.configure(bg='sky blue')

    Label(root,text="FILLUP LOGIN FORM",font="Arial 20 bold underline",bg="pink",height="2",width="100").pack(side=TOP)
    Label(root,text="\n\n\n\n",bg="sky blue").pack()
   
    Label(root,text="USERNAME",bg="black",fg="orange",font="Arial 13 bold",height="1",width="10",bd=4).place(x=600,y=150)
    entry1=Entry(root,bd=5,width="25").place(x=580,y=200)
  
    Label(root,text="PASSWORD",font="Arial 13 bold",bg="black",fg="orange",height="1",width="10",bd=4).place(x=600,y=250)
    entry2=Entry(root,bd=5,width="25").place(x=580,y=300)

    Button(root,text="LOGIN",font="arial 10 bold",command=check ,height=1,width=8,bd=5,bg="black",fg="gold").place(x=620,y=350)

    Label(root,text="",bg="pink",height="4",width="500").pack(side=BOTTOM)

    root.mainloop()

#Registration form\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def register1():
   
    from tkinter import Tk,Entry,StringVar,IntVar,Checkbutton, OptionMenu,PhotoImage,Button,Label 
    from tkinter import messagebox
    import sql_entry as so 
    from  tkinter.font import names

    object=Tk()
    object.title("Secure Place : Login and Registration")
    object.geometry("1300x700+20+10")
    object.configure(bg="grey")

   

    def submit():

        
        fname=NameBoxx1.get()
        mname=NameBoxx2.get()
        lname=NameBoxx3.get()
        so.sql_entry(fname,mname,lname)
       
    def clear():
        pass

    NameBoxx1=StringVar()
    NameBoxx2=StringVar()
    NameBoxx3=StringVar()

    Heading=Label(object,text="STUDENT LOGIN AND REGISTRATION FORM",font="Arial 15 bold underline",bg="BLACK",fg="GOLD",bd=5).place(x=500,y=20)
    NameUser1=Label(object,text="FIRST NAME ",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=70)
    NameBox1=Entry(object,bd=3,width=40,textvariable=NameBoxx1).place(x=700,y=70)

    NameUser2=Label(object,text="MIDDLE NAME ",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=100)
    NameBox2=Entry(object,bd=3,width=40,textvariable=NameBoxx2).place(x=700,y=100)

    NameUser3=Label(object,text="LAST NAME ",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=130) 
    NameBox3=Entry(object,bd=3,width=40,textvariable=NameBoxx3).place(x=700,y=130)

    RnUser=Label(object,text="ROLL NUMBER ",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=160)
    RnBox=Entry(object,bd=3,width=40).place(x=700,y=160)

    BranchUser=Label(object,text="BRANCH ",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=190)
    BranchBox=Entry(object,textvariable=StringVar,bd=3,width=40).place(x=700,y=190)

    SemesterUser=Label(object,text="SEMESTER ",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=220)
    SemesterBox=Entry(object,textvariable=StringVar,bd=3,width=40).place(x=700,y=220)

    YearUser=Label(object,text="CURRENT_YEAR",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=250)
    YearBox=Entry(object,textvariable=IntVar,bd=3,width=40).place(x=700,y=250)

    AddUser=Label(object,text="ADDRESS",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=280)
    AddBox=Entry(object,textvariable=StringVar,bd=3,width=40).place(x=700,y=280)

    EntryYearUser=Label(object,text="ADMISSION YEAR",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=310)
    EntryBox=Entry(object,textvariable=IntVar,bd=3,width=40).place(x=700,y=310) 

    ExitYearUser=Label(object,text="PASSOUT YEAR",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=340)
    ExitYearBox=Entry(object,textvariable=IntVar,bd=3,width=40).place(x=700,y=340)

    PerUser=Label(object,text="TOTAL PERCENTAGE",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=370)
    PerBox=Entry(object,textvariable=StringVar,bd=3,width=40).place(x=700,y=370)

    GmailUser=Label(object,text="GMAIL_ID",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=400)
    GmailBox=Entry(object,textvariable=StringVar,bd=3,width=40).place(x=700,y=400)

    MnUser=Label(object,text="MOBILE NO.",font="Arial 10 bold",bg="pink",bd=2).place(x=500,y=430)
    MnBox=Entry(object,textvariable=IntVar,bd=3,width=40).place(x=700,y=430)


    CheckBox=Checkbutton(text="Remember Information !!!!!",bg="silver",font="Arial 10 bold").place(x=600,y=500)
    Button(text="Submit",command=submit ,fg="GOLD",bg="BLACK",bd=5,font="arial 10 bold").place(x=600,y=550)
    Button(text="Clear",command=clear ,fg="GOLD",bg="BLACK",bd=5,font="arial 10 bold").place(x=750,y=550) 

    object.mainloop()

#home page|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

from tkinter import *
from tkinter import Toplevel
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP

ob = Tk()

ob.geometry("1300x700+20+10")
ob.title("LOGIN AND REGISTRATION HOME PAGE : SECURE APPLICATION")  
ob.configure(bg="pink")
    
Label(ob,text="CHOOSE LOGIN OR REGISTER", bg="grey",fg="Gold", width="30", height="3", font="Arial 20 bold underline").pack(side=TOP)   
Label(ob,text="",bg="grey",width="10",height="500").pack(side=LEFT)
Label(ob,text="",bg="grey",width="10",height="500").pack(side=RIGHT)
Label(ob,text="",bg="grey",width="300",height="5").pack(side=BOTTOM)

Label(ob,text="\n\n",bg="pink").pack() 
Button(ob,text="LOGIN", command=login1, height="2", width="20",bg="black",fg="gold", font=("Calibri",18),bd="7").pack() 
Label(ob,text="\n\n",bg="blue").pack() 
    
Button(ob,text="REGISTER", command=register1 , height="2", width="20", font=("Calibri",18),bg="black",fg="gold",bd=7).pack()


ob.mainloop()
