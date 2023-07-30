
from tkinter import *

ws=Tk()
ws.state('zoomed')
ws.config(bg='#003537')
ws.title('Basic Resume Maker')

# Make Pdf
def print_pdf():
    
    name=str(Name.get())
    surname=str(Surname.get())
    role=str(Role.get())
    from fpdf import FPDF
    pdf=FPDF()
    pdf=FPDF(orientation='P',unit='mm',format='A4')
    pdf.add_page()
    pdf.set_draw_color(r=72, g=61,b=139)
    pdf.set_font('Courier','B',20)
    pdf.set_text_color(r=255, g=250, b=250)
    pdf.set_fill_color(r= 72, g= 61, b = 139)
    pdf.multi_cell(w=0, h=30, txt=name+' '+surname, fill=True)
    pdf.set_font('Arial','B',11)
    pdf.set_xy(x=10, y= 27)
    pdf.cell(w=0, h=12, txt=role, ln=1, fill=True)
    photo=str(Photo.get())
    
    
    Im='C:\\Users\\sohan\\Downloads\\WhatsApp Image 2023-06-27 at 22.17.40.jpg'
    '''
    for i in photo:
        Im+=i
        if i=="\\":
            Im+="\\"
            '''
    pdf.set_xy(x=130, y= 42)
    pdf.set_fill_color(245, 194, 193)
    pdf.cell(w=70, h=234, txt='', ln=0, fill=True)
    pdf.image(Im, 
          x = 146, y = 50, w = 40, h = 50, type = 'JPG')
    pdf.set_font('Times','B',17)
    pdf.set_text_color(r=100, g=0, b=0)

    pdf.set_xy(x=135, y= 105)    
    pdf.cell(w=0,h=15,txt='Contact',fill=True,ln=1,align='C')

    pdf.set_xy(x=135, y= 195)
    pdf.cell(w=0,h=15,txt='Skill',fill=True,ln=1,align='C')

    pdf.set_xy(x=135, y= 234)
    pdf.cell(w=0,h=15,txt='Language',fill=True,ln=1,align='C')

    pdf.set_text_color(r=72, g=61, b=139)
    pdf.set_xy(x=135, y= 115)
    pdf.set_font('Times','B',13)
    pdf.cell(w=0,h=15,txt='Address',fill=True,ln=1)
    pdf.set_xy(x=135, y= 130)
    pdf.cell(w=0,h=15,txt='Phone',fill=True,ln=1)
    pdf.set_xy(x=135, y= 145)
    pdf.cell(w=0,h=15,txt='Email',fill=True,ln=1)
    pdf.set_xy(x=135, y= 160)
    pdf.cell(w=0,h=15,txt='LinkedIn',fill=True,ln=1)


    
    

    github=str(GitHub.get())
    if len(github)!=0:
        pdf.set_xy(x=135, y= 177)
        pdf.cell(w=0,h=15,txt='GitHub Id',fill=True,ln=1)


    city=str(City.get())
    pincode=str(Pin_Code.get())
    country=str(Country.get())

    pdf.set_font('Arial','',10)
    pdf.set_text_color(r=45, g=53, b=69)

    pdf.set_xy(x=135, y= 125)
    pdf.multi_cell(w=0,h=5,txt=city+', '+country+', '+pincode,fill=True)

    phone=str(Phone.get())
    email=str(Email.get())
    
    linkedin=str(LinkedIn.get())
    
    pdf.set_xy(x=135, y= 140)
    pdf.multi_cell(w=0,h=5,txt=phone,fill=True)

    pdf.set_xy(x=135, y= 155)
    pdf.multi_cell(w=0,h=5,txt=email,fill=True)

    pdf.set_xy(x=135, y= 170)
    pdf.multi_cell(w=0,h=5,txt=linkedin,fill=True)
    

    if len(github)!=0:
        pdf.set_xy(x=135, y= 187)
        pdf.multi_cell(w=0,h=5,txt=github,fill=True)

    
    skill1=str(Skill1.get()+' - '+clicked1.get())
    skill2=str(Skill2.get()+' - '+clicked2.get())
    skill3=str(Skill3.get()+' - '+clicked3.get())

    pdf.set_xy(x=135, y= 205)
    pdf.multi_cell(w=0,h=15,txt=skill1,fill=True)
    pdf.set_xy(x=135, y= 217)
    pdf.multi_cell(w=0,h=5,txt=skill2,fill=True)
    pdf.set_xy(x=135, y= 224)
    pdf.multi_cell(w=0,h=5,txt=skill3,fill=True)


    lan1=str(Language1.get()+' - '+clicked4.get())
    lan2=str(Language2.get()+' - '+clicked5.get())
    lan3=str(Language3.get()+' - '+clicked6.get())

    pdf.set_xy(x=135, y= 244)
    pdf.multi_cell(w=0,h=15,txt=lan1,fill=True)
    pdf.set_xy(x=135, y= 256)
    pdf.multi_cell(w=0,h=5,txt=lan2,fill=True)
    pdf.set_xy(x=135, y= 263)
    pdf.multi_cell(w=0,h=5,txt=lan3,fill=True)

    pdf.set_fill_color(r= 240, g= 240, b = 240)
    pdf.set_font('Arial','B',18)
    pdf.set_text_color(r=105, g=105, b=105)

    pdf.set_xy(x=10, y= 42)
    pdf.multi_cell(w=120, h=7, txt='Projects',fill=True)

    pdf.set_xy(x=10, y= 160)
    pdf.multi_cell(w=120, h=7, txt='Education',fill=True)
    
    # Headings
    pdf.set_font('Arial','B',12)
    pdf.set_text_color(r=0, g=0, b=0)
    # Project 1
    pdf.set_xy(x=10, y= 51)
    pdf.multi_cell(w=0, h=5, txt='Name:')
    pdf.set_xy(x=10, y= 58)
    pdf.multi_cell(w=0, h=5, txt='Tech Stack:')
    pdf.set_xy(x=10, y= 65)
    pdf.multi_cell(w=0, h=5, txt='Tools Used:')
    pdf.set_xy(x=10, y= 72)
    pdf.multi_cell(w=0, h=5, txt='Summary:')
    # Project 2
    pdf.set_xy(x=10, y= 105)
    pdf.multi_cell(w=0, h=5, txt='Name:')
    pdf.set_xy(x=10, y= 112)
    pdf.multi_cell(w=0, h=5, txt='Tech Stack:')
    pdf.set_xy(x=10, y= 119)
    pdf.multi_cell(w=0, h=5, txt='Tools Used:')
    pdf.set_xy(x=10, y= 126)
    pdf.multi_cell(w=0, h=5, txt='Summary:')

    # Details
    pdf.set_fill_color(r= 240, g= 240, b = 240)
    pdf.set_font('Arial','',12)
    pdf.set_text_color(r=0, g=0, b=0)

    # Project 1
    pdf.set_xy(x=25, y= 51)
    proname1=str(Project1_Name.get())
    pdf.multi_cell(w=95, h=5, txt=proname1)

    protech1=str(Project1_TechStack.get())
    pdf.set_xy(x=35, y= 58)
    pdf.multi_cell(w=95, h=5, txt=protech1)

    protool1=str(Project1_Tools.get())
    pdf.set_xy(x=35, y= 65)
    pdf.multi_cell(w=95, h=5, txt=protool1)

    prosummary1=str(Project1_Summary.get())
    pdf.set_xy(x=32, y= 72)
    pdf.multi_cell(w=95, h=5, txt=prosummary1)

    # Project 2
    pdf.set_xy(x=25, y= 105)
    proname2=str(Project2_Name.get())
    pdf.multi_cell(w=95, h=5, txt=proname2)

    protech2=str(Project2_TechStack.get())
    pdf.set_xy(x=35, y= 112)
    pdf.multi_cell(w=95, h=5, txt=protech2)

    protool2=str(Project2_Tools.get())
    pdf.set_xy(x=35, y= 119)
    pdf.multi_cell(w=95, h=5, txt=protool2)

    prosummary2=str(Project2_Summary.get())
    pdf.set_xy(x=32, y= 126)
    pdf.multi_cell(w=95, h=5, txt=prosummary2)



    try:
        pdf.output("C:\\Users\\sohan\\Downloads\\demo1.pdf")
        print('printed')
    except:
        print('\n\nerror\n\n')
    


# Dark Theme
def dark_theme():
    ws.config(bg='black')
    Heading.config(bg='black',fg='white')

# Normal Theme
def normal_theme():
    ws.config(bg='#003537')
    Heading.config(bg='#003537',fg='white')

# Help
def need_help():
    import webbrowser
    url="https://wa.me/6295400770"
    webbrowser.open(url)


# Label
Heading=Label(ws,
              text='B a s i c   R E S U M E   M a k e r',
              bg='#003537',
              fg='white',
              font=('Times New Roman',20))
Heading.place(relx=0.5,rely=0.025,anchor=CENTER)

Name=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Name.place(x=7,y=50,height=25)
Name.insert(0,'Enter Your Name')

Surname=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Surname.place(x=295,y=50,height=25)
Surname.insert(0,'Enter Your Surname')

Role=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Role.place(x=583,y=50,height=25)
Role.insert(0,"Enter Your Role (ex: 'Student')")

Photo=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=72
           
           )
Photo.place(x=871,y=50,height=25)
Photo.insert(0,"Paste your photo's path from file explorer")

City=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
City.place(x=7,y=100,height=25)
City.insert(0,"Enter your city name")

Country=Entry(ws,
            bg='light grey',
            justify='center',
            font=('Lucida',12),
            width=30
           
           )
Country.place(x=295,y=100,height=25)
Country.insert(0,"Enter your Country name")

Pin_Code=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Pin_Code.place(x=583,y=100,height=25)
Pin_Code.insert(0,"Enter your PIN or POSTAL CODE")

Email=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=72
           
           )
Email.place(x=871,y=100,height=25)
Email.insert(0,"Enter your email address")

Phone=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Phone.place(x=7,y=150,height=25)
Phone.insert(0,"Enter your conatact number")

LinkedIn=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=70
           
           )
LinkedIn.place(x=295,y=150,height=25)
LinkedIn.insert(0,"Enter your LinkedIn account link")

GitHub=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=64
           
           )
GitHub.place(x=944,y=150,height=25)
GitHub.insert(0,"Enter your GitHub Id (optional)")

options = [
    "Basic",
    "Intermediate",
    "Advanced"
]

Skill1=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Skill1.place(x=20,y=220,height=25)
Skill1.insert(0,"Enter your one skill")
clicked1 = StringVar()
clicked1.set( "Advanced" )
drop1 = OptionMenu( ws , clicked1 , *options )
drop1.place(x=298,y=220,height=25)

Skill2=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Skill2.place(x=568,y=220,height=25)
Skill2.insert(0,"Enter your another skill")
clicked2 = StringVar()
clicked2.set( "Advanced" )
drop2 = OptionMenu( ws , clicked2 , *options )
drop2.place(x=846,y=220,height=25)

Skill3=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Skill3.place(x=1123,y=220,height=25)
Skill3.insert(0,"Enter your another skill")
clicked3 = StringVar()
clicked3.set( "Advanced" )
drop3 = OptionMenu( ws , clicked3 , *options )
drop3.place(x=1401,y=220,height=25)

Language1=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Language1.place(x=20,y=250,height=25)
Language1.insert(0,"Enter your one language skill")
clicked4 = StringVar()
clicked4.set( "Advanced" )
drop4 = OptionMenu( ws , clicked4 , *options )
drop4.place(x=298,y=250,height=25)

Language2=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Language2.place(x=568,y=250,height=25)
Language2.insert(0,"Enter your other language skill")
clicked5 = StringVar()
clicked5.set( "Advanced" )
drop5 = OptionMenu( ws , clicked5 , *options )
drop5.place(x=846,y=250,height=25)

Language3=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Language3.place(x=1123,y=250,height=25)
Language3.insert(0,"Enter your other language skill")
clicked6 = StringVar()
clicked6.set( "Advanced" )
drop6 = OptionMenu( ws , clicked6 , *options )
drop6.place(x=1401,y=250,height=25)



Project1_Name=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Project1_Name.place(x=50,y=320,height=25)
Project1_Name.insert(0,'Enter Your Best Project Name')
Project1_TechStack=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Project1_TechStack.place(x=598,y=320,height=25)
Project1_TechStack.insert(0,'Tech Stack Used')
Project1_Tools=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Project1_Tools.place(x=1123,y=320,height=25)
Project1_Tools.insert(0,'Tools Used')
Project1_Summary=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=168
           
           )
Project1_Summary.place(x=7,y=350,height=40)
Project1_Summary.insert(0,'Summary within 170 words')

Project2_Name=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Project2_Name.place(x=50,y=405,height=25)
Project2_Name.insert(0,'Enter Your Another Best Project Name')
Project2_TechStack=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Project2_TechStack.place(x=598,y=405,height=25)
Project2_TechStack.insert(0,'Tech Stack Used')
Project2_Tools=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
Project2_Tools.place(x=1123,y=405,height=25)
Project2_Tools.insert(0,'Tools Used')
Project2_Summary=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=168
           
           )
Project2_Summary.place(x=7,y=435,height=40)
Project2_Summary.insert(0,'Summary within 170 words')

# College
College=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )
College.place(x=18,y=515,height=25)
College.insert(0,'Enter Your College Name')

College_Degree=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )

College_Degree.place(x=333,y=515,height=25)
College_Degree.insert(0,'Enter Your College Degree Name')

College_Time=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )

College_Time.place(x=633,y=515,height=25)
College_Time.insert(0,'Enter College Duration(ex:2019-2023)')

College_Percentage=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )

College_Percentage.place(x=930,y=515,height=25)
College_Percentage.insert(0,'Enter College Percentage')

College_Address=Entry(ws,
           bg='light grey',
           justify='center',
           font=('Lucida',12),
           width=30
           
           )

College_Address.place(x=1230,y=515,height=25)
College_Address.insert(0,'Enter College Address')




# Menu
menubar=Menu(ws)

file=Menu(menubar,tearoff=0,background='lightyellow',activebackground='darkred')
menubar.add_cascade(label='File',menu=file)
file.add_command(label='print',command=print_pdf)

theme=Menu(menubar,tearoff=0,background='lightyellow',activebackground='darkred')
menubar.add_cascade(label='Theme',menu=theme)
theme.add_command(label='Dark',command=dark_theme)
theme.add_command(label='Normal',command=normal_theme)

help=Menu(menubar,tearoff=0,background='lightyellow',activebackground='darkred')
menubar.add_cascade(label='Help',menu=help)
help.add_command(label='Help',command=need_help)

ws.config(menu=menubar)


ws.mainloop()
