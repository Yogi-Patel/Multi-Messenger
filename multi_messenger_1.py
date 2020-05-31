import os 
from tkinter import filedialog
from tkinter import *
import tkinter 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Main window 
main_window = tkinter.Tk()
main_window.title("Multi-Messenger")
main_window.geometry('250x150')
label1 = tkinter.Label(main_window, text = 'Please click on a button as per your choice')
label1.grid(column = 1,row = 0)

def email():
    #window that opens when email is selected 
    email_window = tkinter.Tk()
    email_window.title("E-mail")
    email_window.geometry('500x300')

    Label2 = tkinter.Label(email_window,text = 'Select mail type')
    Label2.grid(column = 0, row =0, sticky = tkinter.W)

    def norm_mail():
        normal_email.configure(state = 'disabled')
        spam.configure(state = 'disabled')
        '''
        from_address = ''
        to_address = ''
        body_actual = ''
        filename = ''
        file_path = ''
        password = ''
        subject_main = ''
        '''
        
        def Entity():
            #function that is called when Send button is pressed
            flag = 0
            from_address = ''
            to_address = ''
            body =''
            filename =''
            file_path =''
            password =''
            subject=''

            from_address = frm_entry.get()
            to_address = to_entry.get()
            subject = subject_entry.get()
            body = body_entry.get()
            password = password_entry.get()
            '''print(from_address)
            print(to_address)
            print(subject)
            print(body)
            print(password)'''
            if(len(from_address) == 0 or from_address.find('@gmail.com') == -1):
                err_window = tkinter.Tk()
                err_window.title("ERROR")
                tkinter.Label(err_window, text = ' Please enter a valid \'from\' address ').grid(column = 0, row = 0)
                tkinter.Button(err_window, text ='OK', command = err_window.destroy).grid(column = 0, row = 1)
                frm_entry.delete(0,'end')
                flag = 1 
                err_window.mainloop()

            to_address = to_address.replace(" ","")
            to_address = to_address.replace(",",", ")
            
            list1 = to_address.split(', ')
            #print("to :" +to_address) 
            for i in list1:
                if(len(i) == 0 or i.find('@gmail.com') == -1 ):
                    err_window1 = tkinter.Tk()
                    err_window1.title("ERROR")
                    tkinter.Label(err_window1, text = ' Please enter valid \'to\' address(es) ').grid(column = 0, row = 0)
                    tkinter.Button(err_window1, text ='OK', command = err_window1.destroy).grid(column = 0, row = 1)
                    to_entry.delete(0,'end')
                    flag = 1 
                    err_window1.mainloop()
                    break
            msg = MIMEMultipart()

            msg['From'] = from_address
            msg['To'] = to_address

            msg['Subject'] = subject

            #body = "body of the mail"

            msg.attach(MIMEText(body,'plain'))
            filename = "links.txt"
            attachment = open("link of attachment", "r")
            p=MIMEBase('application', ' octet-stream')
            p.set_payload((attachment).read())
            encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename = %s" % filename)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587) 
            s.starttls() 
            try:
                s.login(from_address, password) 
            except Exception:
                rte_window = tkinter.Tk()
                rte_window.geometry('400x100')
                rte_window.title("Runtime error")
                tkinter.Label(rte_window, text = 'Error while logging in. check if mailer ID and password are correct').grid(column=0, row =0)
                frm_entry.delete(0,'end')
                password_entry.delete(0,'end')
                tkinter.Button(rte_window, text ='OK', command = rte_window.destroy).grid(column = 0, row = 1)
                rte_window.mainloop()
                return
            text = msg.as_string()
            
            try:
                s.sendmail(from_address, to_address, text)
                flag = 1
            except NoSuchUser:
                print('No such user ')
                to_entry.delete(0,'end')
            except Exception:
                rte_window = tkinter.Tk()
                rte_window.geometry('300x200')
                rte_window.title("Runtime error")
                tkinter.Label(rte_window, text = 'Runtime error. Try again').grid(column=0, row =0)
                #tkinter.Button(rte_window, text ='OK', command = rte_window.destroy).grid(column = 0, row = 1)
                time.sleep(3)
                email_window.destroy()

                rte_window.mainloop()

                return    
            if(flag ==1):
                email_window.destroy()
            print("message sent")
            s.quit() 
                           
        tkinter.Label(email_window, text = 'From').grid(column = 0,row = 3, sticky = tkinter.W)
        frm_entry = tkinter.Entry(email_window, width = 25)
        frm_entry.grid(column = 1, row = 3)
        
        tkinter.Label(email_window, text ='To').grid(column = 0, row = 4, sticky = tkinter.W)
        to_entry = tkinter.Entry(email_window, width = 25)
        to_entry.grid(column = 1, row = 4)

        tkinter.Label(email_window, text = 'Subject').grid(column =0, row =5, sticky =tkinter.W)
        subject_entry = tkinter.Entry(email_window, width = 25)
        subject_entry.grid(column = 1, row = 5)

        tkinter.Label(email_window, text = 'Body').grid(column =0, row = 6, sticky =tkinter.W)
        body_entry = tkinter.Entry(email_window, width = 25)
        body_entry.grid(column = 1, row = 6)

        tkinter.Label(email_window, text ='Password').grid(column =0, row = 10,sticky = tkinter.W)
        password_entry = tkinter.Entry(email_window, show = '*', width = 25)
        password_entry.grid(column = 1, row = 10)
        
        
        tkinter.Button(email_window, text = ' Send ', command = Entity).grid(column = 1, row = 13)
        
    normal_email = tkinter.Button(email_window, text = 'Just mail', command = norm_mail)
    normal_email.grid(column = 0, row = 1,padx =20,pady = 4)

    def Spam():
        spam.configure(state ='disabled')
        normal_email.configure(state = 'disabled')
        
        def Spam_entity():
            s = smtplib.SMTP('smtp.gmail.com',587)

            s.starttls()

            
            to_address = to_entry.get()
            to_address = to_address.replace(" ","")
            to_address = to_address.replace(",",", ")
            
            list1 = to_address.split(', ')
            #print("to :" +to_address) 
            for i in list1:
                if(len(i) == 0 or i.find('@gmail.com') == -1 ):
                    err_window1 = tkinter.Tk()
                    err_window1.title("ERROR")
                    tkinter.Label(err_window1, text = ' Please enter valid \'to\' address(es) ').grid(column = 0, row = 0)
                    tkinter.Button(err_window1, text ='OK', command = err_window1.destroy).grid(column = 0, row = 1)
                    to_entry.delete(0,'end')
                    flag = 1 
                    err_window1.mainloop()
                    break

            s.login('put_Email_address_here' ,'put_password_here')

            message = "spam"

            
            flag = 0
            no = (int)(no_entry.get())
            while(no>=1):
                try:
                    s.sendmail("email_address", to_address, message)
                    flag = 1
                    time.sleep(0.1)
                except Exception:
                    rte_window = tkinter.Tk()
                    rte_window.geometry('400x100')
                    rte_window.title("Runtime error")
                    tkinter.Label(rte_window, text = 'Error while sending. Make sure ID is correct').grid(column=0, row =0)
                    to_entry.delete(0,'end')
                    password_entry.delete(0,'end')
                    tkinter.Button(rte_window, text ='OK', command = rte_window.destroy).grid(column = 0, row = 1)
                    rte_window.mainloop()
                print(no)
                no=no-1
            if(flag == 1):
                
                print("Spam successful")
                s.quit()
                return
            
        tkinter.Label(email_window, text ='To').grid(column = 0, row = 4, sticky = tkinter.W)
        to_entry = tkinter.Entry(email_window, width = 25)
        to_entry.grid(column = 1, row = 4)
        tkinter.Label(email_window, text = 'Number of spam mails ').grid(column =0, row = 6, sticky =tkinter.W)
        no_entry = tkinter.Entry(email_window, width = 5)
        no_entry.grid(column = 1, row = 6)
        tkinter.Button(email_window, text = ' Send ', command = Spam_entity).grid(column = 1, row = 13)
    
    spam = tkinter.Button(email_window, text = 'Spam' ,command = Spam)
    spam.grid(column =1, row =1, padx = 30)


    email_window.mainloop()

wA = tkinter.Button(main_window, text = 'Email',command = email)
wA.grid(column = 1, row = 1,sticky = tkinter.W)

def Whatsapp():
    whatsapp_window = tkinter.Tk()
    whatsapp_window.title("WhatsApp") 
    def norm_whatsapp():
        driver = webdriver.Chrome('full path of chromedriver')
        driver.get("https://web.whatsapp.com/")
        wait = WebDriverWait(driver, 600)
        time.sleep(5)
        target = target_entry.get()
        string = string_entry.get()
        no = no_entry.get()
        target = target.replace(" ","")
        target = target.replace(",",", ")
        flag = 0
        list1 = target.split(', ')
        #print(list1)
        for i in list1:
            user = driver.find_element_by_xpath('//span[@title ="{}"]'.format(i))
            user.click()
            no1 = (int)(no)
            while(no1>0):
                inputi = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div')
                inputi.send_keys(string)
                button = driver.find_element_by_class_name('_3M-N-')
                button.click()
                time.sleep(1)
                flag = 1 
                no1 = no1-1
        if(flag == 1):
            driver.quit()
            whatsapp_window.destroy()
            return 
    tkinter.Label(whatsapp_window, text ='To').grid(column =0,row =0, sticky = tkinter.W )
    target_entry = tkinter.Entry(whatsapp_window, width =25)
    target_entry.grid(column =1, row = 0)

    tkinter.Label(whatsapp_window, text ='Message').grid(column =0,row =1,sticky = tkinter.W )
    string_entry = tkinter.Entry(whatsapp_window, width =25)
    string_entry.grid(column =1, row = 1 )

    tkinter.Label(whatsapp_window, text ='Number of times').grid(column =0,row =2,sticky = tkinter.W )
    no_entry = tkinter.Entry(whatsapp_window, width =5)
    no_entry.grid(column =1, row = 2)

    tkinter.Button(whatsapp_window, text = 'Spam ', command = norm_whatsapp).grid(column = 1 , row = 3)

WhatA = tkinter.Button(main_window, text = ' WhatsApp', command = Whatsapp)
WhatA.grid(column = 1, row = 2, sticky = tkinter.W)

def sms():
    sms_window = tkinter.Tk()
    sms_window.title("SMS via way2sms")
    def sms_web():
        driver = webdriver.Chrome('full path of your chromedriver')
        driver.get("https://www.way2sms.com")
        wait = WebDriverWait(driver,600)
        username = driver.find_element_by_xpath('//*[@id="mobileNo"]')
        username.click()
        str = username_entry.get()
        username.send_keys(str)
        password = driver.find_element_by_xpath('//*[@id="password"]')
        password.click()
        str = pass_entry.get()
        password.send_keys(str)
        login = driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/div[2]/button')
        login.click()
        time.sleep(2)
        mobile_number = driver.find_element_by_xpath('//*[@id="mobile"]')
        mobile_number.click()
        str = to_entry.get()
        mobile_number.send_keys(str)
        message = driver.find_element_by_xpath('//*[@id="message"]')
        message.click()
        str = mess_entry.get()
        message.send_keys(str)
        send = driver.find_element_by_xpath('//*[@id="sendButton"]')
        send.click()
        time.sleep(3)
        driver.quit()
        sms_window.destroy()


    tkinter.Label(sms_window, text = 'Username').grid(column = 0, row =0, sticky = tkinter.W)
    username_entry = tkinter.Entry(sms_window, width =25 )
    username_entry.grid(column = 1, row = 0)

    tkinter.Label(sms_window, text = 'Password').grid(column = 0, row =1, sticky = tkinter.W)
    pass_entry = tkinter.Entry(sms_window, show ='*', width = 25)
    pass_entry.grid(column = 1, row = 1)

    tkinter.Label(sms_window, text = 'To').grid(column = 0, row =2, sticky = tkinter.W)
    to_entry = tkinter.Entry(sms_window, width = 25)
    to_entry.grid(column = 1, row = 2)

    tkinter.Label(sms_window, text = 'Message').grid(column = 0, row =3, sticky = tkinter.W)
    mess_entry = tkinter.Entry(sms_window, width = 25)
    mess_entry.grid(column = 1, row = 3)



    tkinter.Button(sms_window, text ='Send', command = sms_web).grid(column = 1, row = 12 )





sms = tkinter.Button(main_window, text = 'SMS using way2sms', command = sms)
sms.grid(column = 1, row = 3, sticky = tkinter.W)



main_window.mainloop()