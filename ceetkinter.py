from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry('500x889')
root.title('Ceefoon')

firstname = StringVar()
lastname = StringVar()
var = StringVar()
var1 = StringVar()
radiovar = IntVar()

camvas1 = Canvas(root)
camvas1.pack()

bgimage = Image.open('C:/Users/Ceefoon/Pictures/Camera Roll/hhh1.jpg')
photo = ImageTk.PhotoImage(bgimage)
lab = Label(root, image=photo)
lab.place(relwidth = 1, relheight = 1)

'''
l1= Label(root, text= 'BASE64', fg ='grey' , bg = 'white', relief = SOLID, font = ('Times New Roman', 16, 'bold'))
l1.place(x = 0, y = 1, relwidth = 1)
'''

l2= Label(root, text= 'FIRSTNAME', fg ='white' , bg = 'grey', font = ('Times New Roman',10,  'bold'))
l2.place(x = 290, y = 450)

entry1 = Entry(root, bg = 'grey', fg = 'white', textvar = firstname)
entry1.place(x = 375, y = 450)

l3= Label(root, text= 'SURNAME', fg ='white' , bg = 'grey', font = ('Times New Roman',10, 'bold'))
l3.place(x = 290, y = 470)

entry2 = Entry(root, fg = 'white', bg ='grey', textvar = lastname)
entry2.place(x = 375, y = 470)

l4= Label(root, text= 'YOB', fg ='white' , bg = 'grey', font = ('Times New Roman',10, 'bold'))
l4.place(x = 290, y = 495)

list1 = ['1990', '1991', '1992', '1993', '1994','Underaged']
listmenu = OptionMenu(root,var, *list1)
var.set('Select year')
listmenu.config(width = 10, bg= 'grey', fg = 'white', height = '1')
listmenu.place(x= 375, y = 495)


l4= Label(root, text= 'COUNTRY', fg ='white' , bg = 'grey', font = ('Times New Roman',10, 'bold'))
l4.place(x = 290, y = 525)


list2 = ['Nigeria', 'Canada', 'Benin', 'Turkey', 'England']
listmenu = OptionMenu(root,var1, *list2)
var1.set('Select Country')
listmenu.config(width = 10, bg= 'grey', fg = 'white', height = '1')
listmenu.place(x= 375, y = 530)

l5= Label(root, text= 'GENDER', fg ='white' , bg = 'grey', font = ('Times New Roman',10, 'bold'))
l5.place(x = 290, y = 560)

radio1 = Radiobutton(root, text ='Male', value = 'Male', fg ='white' , bg = 'grey')
radio1.place(x = 375, y= 560)

radio2 = Radiobutton(root, text ='Female' , value = 'Femaie', fg ='white' , bg = 'grey')
radio2.place(x = 425, y = 560)

l6= Label(root, text= 'PASSKEY', fg ='white' , bg = 'grey', font = ('Times New Roman',10, 'bold'))
l6.place(x = 290, y = 580)

entry4 = Entry(root, fg = 'white', bg ='grey', show = '#')
entry4.place(x = 375, y = 580)

l7= Label(root, text= 'RE-PASSKEY', fg ='white' , bg = 'grey', font = ('Times New Roman',10, 'bold'))
l7.place(x = 290, y = 600)

entry5 = Entry(root, fg = 'white', bg ='grey', show = '#')
entry5.place(x = 375, y = 600)
def button1proceed():
    question = tkinter.messagebox.askquestion('Confirm', 'Your details are going to be sent to the database. Proceed?')
    if question == 'yes':
        print()
        tkinter.messagebox.showinfo('Success', 'Congratulations, You have been registered in Ceefoon\'s database. Sign in to continue')
    elif question == 'no':
        print()
        tkinter.messagebox.showinfo('Error', 'You have cancelled the registration.')

button1 = Button(root, text= 'PROCEED', fg ='white', bg = 'grey', font = ('Times New Roman',10, 'bold'), command = button1proceed)
button1.place(x= 420, y= 650)

def signin():
    window = Tk()
    window.geometry('300x150')
    window.title('Sign into Ceefoon')
    window.configure(background = 'grey')

    label1 = Label(window, text = 'SURNAME', fg = 'white', bg = 'grey', font = ('Times New Roman',10,  'bold'))
    label1.place(x = 5, y = 5)

    entry1 = Entry(window, fg = 'white', bg = 'grey')
    entry1.place(x = 70, y = 5)

    label2 = Label(window, text = 'PASSKEY', fg = 'white', bg = 'grey', font = ('Times New Roman',10,  'bold'))
    label2.place(x = 5, y = 50)

    entry2 = Entry(window, show = '#', fg = 'white', bg = 'grey')
    entry2.place(x = 70, y = 50)

    button1 = Button(window, text = 'LOGIN', fg = 'white', bg = 'grey', font = ('Times New Roman',10,  'bold'))
    button1.place(x = 70, y = 100)

    button2 = Button(window, text = 'REGISTER', fg = 'white', bg = 'grey', font = ('Times New Roman',10,  'bold'))
    button2.place(x = 137, y = 100)

    window.mainloop()
    

button2 = Button(root, text= 'SIGN IN', fg ='white', bg = 'grey', font = ('Times New Roman',10, 'bold'), command = signin)
button2.place(x= 430, y= 20)

def helpregister():
    tkinter.messagebox.showinfo('Registration', 'Sign up by simply filling in your details then click on proceed.')

button3 = Button(root, text = 'HELP', fg = 'white', bg = 'grey', font = ('Times New Roman', 10, 'bold'), command = helpregister)
button3.place(x = 443, y = 60)

def quitbutton():
    tkinter.messagebox.showinfo('Ceefoon', 'Thank you for using our software. Visit official website for more applications.')
    quit()

button4 = Button(root, text = 'QUIT', fg = 'white', bg ='grey', font = ('Times New Roman', 10, 'bold'), command = quitbutton)
button4.place(x = 445, y = 100)
root.mainloop()