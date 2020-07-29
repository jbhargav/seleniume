import urllib
import urllib.request
import os
import tkinter
from tkinter import *
from PIL import Image,ImageTk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

global text

def nextid(id1):
        return ("N"+str(int(id1[1:])+1))
def password(id1):
   a= open('password.txt').read()
   pos1 = a.find(id1)+8
   pos2 = a.find(nextid(id1))-1
   password = a[pos1:pos2]
   return password
# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)

html1=""
def scrape(idn):

   driver.get("http://intranet.rguktn.ac.in/SMS/")


   search_field = driver.find_element_by_name("user1")
   search_field2 = driver.find_element_by_name("passwd1")


   search_field.send_keys(text)
   search_field2.send_keys(password(text))
   search_field.submit()


   driver.get("view-source:http://intranet.rguktn.ac.in/SMS/profile.php")
   html = driver.page_source
   posa1=html.find("profile-user-img img-responsive img-circle")
   posa2=html.find("Semester Course Registration Completed")
   global html1
   html1=html[posa1:posa2]
#   driver.get("http://intranet.rguktn.ac.in/SMS/signout")
   
def refineht(html):
   name,classs,gender,dob,mobile,address = "","","","","",""
   namea=html.find("value=\"275\"")
   nameb=html.find("value=\"276\"")
   newname=html[namea:nameb]
   end=newname.find("<span",199)
   name=newname[199:end]

   classsa=html.find("value=\"277\"")
   classsb=html.find("value=\"278\"")
   newclasss=html[classsa:classsb]
   classstart=newclasss.find("Class Room:")+18
   classend=classstart+8
   classs=newclasss[classstart:classend]

   gendera=html.find("Gender")
   genderb=html.find("<td class=\"line-number\" value=\"282\">")
   newgender=html[gendera:genderb]
   genderstart=188
   genderend=newgender.find("<span class=\"html-tag\">",188)
   gender=newgender[genderstart:genderend]

   doba=html.find("Date of Birth")
   dobb=html.find("&lt;/a&gt",doba)
   newdob=html[doba:dobb]
   dobstart=195
   dobend=newdob.find("<span class=\"html-tag\">",dobstart)
   dob=newdob[dobstart:dobend]

   mobilea=html.find("Mobile")
   mobileb=html.find("&lt;/a&gt",mobilea)
   newmobile=html[mobilea:mobileb]
   mobilestart=188
   mobileend=newmobile.find("<span class=\"html-tag\">",mobilestart)
   mobile=newmobile[mobilestart:mobileend]

   addressa=html.find("value=\"335\"")
   addressb=html.find("value=\"336\"")
   newaddress=html[addressa:addressb]
   addressstart=197
   addressend=newaddress.find("<span class=\"html-tag\">",addressstart)
   address=newaddress[addressstart:addressend]

   return (name,classs,gender,dob,mobile,address)


#############################################
window = tkinter.Tk()


text=" "
imn ="default1.png"        
def check(idn):
        
        if (len(idn)<8) and idn[1:]==str(int(idn[1:])) and idn[0]==str(idn[0]) :
                return (True)
        else:
                L4.config(text="Error with User ID",fg="red",width=15)
                L4.place(x=180, y=258)
global uimg
def click():
        entered_text = E1.get()
        global text
        text=""+(entered_text)
        if check(text):
           scrape(text) #take idn
           L4.place(x=1157, y=1338)
           L3.config(text=refineht(html1)[0])
           L6.config(text=refineht(html1)[1])
           L8.config(text=refineht(html1)[2])
           L10.config(text=refineht(html1)[3])
           L12.config(text=refineht(html1)[4])
           L14.config(text=refineht(html1)[5])
           global photo
           global image
           global imn
           urllib.request.urlretrieve("http://intranet.rguktn.ac.in/SMS/usrphotos/user/"+text+".jpg","img/"+text+".jpg")
           imn=("img/"+text+".jpg")
           image = Image.open(imn)
           image = image.resize((300,300))
           photo = ImageTk.PhotoImage(image)
           
           pic.config(image=photo,width=300, height = 300)
        window.update()
        

image = Image.open(imn)
photo = ImageTk.PhotoImage(image)
username="none"


window.title("User Details")
window.geometry("670x680")
window.resizable(0, 0)
window.configure(background="white")

#userpic = PhotoImage(file=user,width=300, height=300)
butpic = PhotoImage(file="submit.png",width=110, height=30)


pic = Label (window,image=photo) 
pic.pack(side = TOP,pady=30)

L1 = Label (window, text="User ID:",width=10, height=3, bg='white',font="none 12 bold", fg="Black")
L1.place(x=77, y=338)
E1 = Entry(window,width=30, bd=1)
E1.place(x=227, y=360)
B1 = Button(window, image=butpic,command=click,bd=0)
B1.place(x=447, y=355)
L2 = Label (window, text="Name:",width=10, height=3, bg="white",font="none 12 bold", fg="Black")
L2.place(x=77, y=388)
L3 = Label (window, text="none", height=3, bg="white",font="none 12 bold", fg="Black")
L3.place(x=230, y=388)

L4 = Label (window, text="Enter User ID",width=10, height=3, bg="white",font="none 12 bold", fg="red")
L4.place(x=180, y=258)

L5 = Label (window, text="Year:",width=10, height=3, bg="white",font="none 12 bold", fg="Black")
L5.place(x=77, y=428)
L6 = Label (window, text="none", height=3, bg="white",font="none 12 bold", fg="Black")
L6.place(x=230, y=428)

L7 = Label (window, text="Gender:",width=10, height=3, bg="white",font="none 12 bold", fg="Black")
L7.place(x=77, y=468)
L8 = Label (window, text="none", height=3, bg="white",font="none 12 bold", fg="Black")
L8.place(x=230, y=468)

L9 = Label (window, text="Date of Birth:",width=10, height=3, bg="white",font="none 12 bold", fg="Black")
L9.place(x=77, y=508)
L10 = Label (window, text="none", height=3, bg="white",font="none 12 bold", fg="Black")
L10.place(x=230, y=508)

L11 = Label (window, text="Mobile:",width=10, height=3, bg="white",font="none 12 bold", fg="Black")
L11.place(x=77, y=548)
L12 = Label (window, text="none", height=3, bg="white",font="none 12 bold", fg="Black")
L12.place(x=230, y=548)

L13 = Label (window, text="Address:",width=10, height=3, bg="white",font="none 12 bold", fg="Black")
L13.place(x=77, y=588)
L14 = Label (window, text="none", height=3, bg="white",font="none 12 bold", fg="Black")
L14.place(x=230, y=588)

window.mainloop()




