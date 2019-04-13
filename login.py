from tkinter import *
import os

def main_account_screen():
	global main_screen

	main_screen = Tk()
	main_screen.geometry('300x150')
	main_screen.title('Account Login/Register')

	Label(height='1').pack()

	Button(text='Login', height='2', width='30', command=login).pack()
	Label(text='').pack()

	Button(text='Register', height='2', width='30', command=register).pack()

	main_screen.mainloop()

def register():
	global username
	global password
	global username_entry
	global password_entry
	global register_screen

	register_screen = Tk()
	register_screen.geometry('300x200')
	register_screen.title('Account Registration')

	username = StringVar()
	password = StringVar()

	username_lable = Label(register_screen, text='Username')
	username_lable.pack()
	username = Entry(register_screen, textvariable=username)
	username.pack()

	password_label = Label(register_screen, text='Password')
	password_label.pack()
	password = Entry(register_screen, textvariable=password, show='*')
	password.pack()

	Label(register_screen, text='').pack()
	Button(register_screen, text='Register', command=register_user).pack()
	Button(register_screen, text="Back", command=register_screen.destroy).pack()

def register_user():
	username_info = username.get()
	password_info = password.get()

	file = open("username.txt", "w")
	file.write(username_info + '/n')
	file.write(password_info)
	file.close()

	password.delete(0, END)
	Label(register_screen, text='Registration Success! Back to Login.', fg='blue').pack()

def login():
	global username_verify
	global password_verify

	login_screen = Tk()
	login_screen.geometry('300x180')
	login_screen.title('Account Login')

	username_verify = StringVar()
	password_verify = StringVar()

	username_lable = Label(login_screen, text='Username')
	username_lable.pack()
	username_verify = Entry(login_screen, textvariable=username_verify)
	username_verify.pack()

	password_label = Label(login_screen, text='Password')
	password_label.pack()
	password_verify = Entry(login_screen, textvariable=password_verify, show='*')
	password_verify.pack()

	Label(login_screen, text='').pack()
	Button(login_screen, text='Login', command=login_verify).pack()
	Button(login_screen, text='Back', command=login_screen.destroy).pack()

def login_verify():
	username1 = username_verify.get()
	password1 = password_verify.get()
	password_verify.delete(0,END)

	list = os.listdir()
	print(username1)
	if username1 in list:
		file1 = open('username.txt','r')
		verify = file1.read().splitlines()
		print(verify)
		if password1 in verify:
			login_success()
		else:
			password_not_recognised()

	else:
		user_not_found()

def login_success():
	global loginsuccess_screen
	loginsuccess_screen = Tk()
	loginsuccess_screen.title('Login')
	loginsuccess_screen.geometry('150x50')
	Label(loginsuccess_screen, text='Login Success').pack()
	Button(loginsuccess_screen, text='Ok', command=loginsuccess_screen.destroy).pack()

def password_not_recognised():
	global passwordnot_screen
	passwordnot_screen = Tk()
	passwordnot_screen.title('Login')
	passwordnot_screen.geometry('150x50')
	Label(passwordnot_screen, text='Invalid Password').pack()
	Button(passwordnot_screen, text='Ok', command=passwordnot_screen.destroy).pack()

def user_not_found():
	global usernot_screen
	usernot_screen = Tk()
	usernot_screen.title('Login')
	usernot_screen.geometry('150x50')
	Label(usernot_screen, text='User Not Found').pack()
	Button(usernot_screen, text='Ok', command=usernot_screen.destroy).pack()

main_account_screen()