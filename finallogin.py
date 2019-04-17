from tkinter import *
import MySQLdb

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
	global passwordr2
	global username_entry
	global password_entry
	global register_screen

	register_screen = Tk()
	register_screen.geometry('300x250')
	register_screen.title('Account Registration')

	username = StringVar()
	password = StringVar()
	passwordr2 = StringVar()

	username_lable = Label(register_screen, text='Username').pack()
	username = Entry(register_screen, textvariable=username)
	username.pack()

	password_label = Label(register_screen, text='Password').pack()
	password = Entry(register_screen, textvariable=password, show='*')
	password.pack()

	password_label2 = Label(register_screen, text='Re-enter Password').pack()
	passwordr2 = Entry(register_screen, textvariable=passwordr2, show='*')
	passwordr2.pack()

	# Label(register_screen, text='').pack()
	Button(register_screen, text='Register', command=verify_field).pack()
	Button(register_screen, text="Back", command=register_screen.destroy).pack()

def verify_field():
	global username_info
	global password_info
	global password_info2

	username_info = username.get()
	password_info = password.get()
	password_info2 = passwordr2.get()

	if len(username_info) > 8:
		Label(register_screen, text='Username too long!', fg='red').pack()

	if not username_info:
		Label(register_screen, text='Please enter required fields!', fg='red').pack()
	else:
		select_user()
		# verify_pw()

def select_user():

	db = MySQLdb.connect(host='127.0.0.1', user='root', password='*****', database='mydatabase')
	cur = db.cursor()
	select_val = "SELECT * FROM users WHERE username = %s"
	user = username_info,
	cur.execute(select_val, user)
	user_db = cur.fetchone()

	if not user_db:
		verify_pw()
	else:
		Label(register_screen, text='Username already taken.', fg='red').pack()

def verify_pw():

	if password_info == password_info2:
		pw_strength()
	else:
		Label(register_screen, text='Password do not match!', fg='red').pack()
		password.delete(0,END)
		passwordr2.delete(0,END)

def pw_strength():

	# calculating the length
    length_error = len(password_info) < 8
    # searching for digits
    digit_error = re.search(r"\d", password_info) is None
    # searching for uppercase
    uppercase_error = re.search(r"[A-Z]", password_info) is None
    # searching for lowercase
    lowercase_error = re.search(r"[a-z]", password_info) is None
    # searching for symbols
    symbol_error = re.search(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password_info) is None
    # overall result
    password_ok = not ( length_error or digit_error or uppercase_error or lowercase_error or symbol_error )

    if len(password_info) > 10:
    	Label(register_screen, text='Password too long!', fg='red').pack()
    	password.delete(0,END)
    	passwordr2.delete(0,END)
    else:
    	if password_ok:
    		register_user()
    	else:
    		Label(register_screen, text='Password not strong!', fg='red').pack()

def register_user():

	db = MySQLdb.connect(host='127.0.0.1', user='root', password='*****', database='mydatabase')
	cur = db.cursor()
	sql_insert = '''
			INSERT INTO mydatabase.users(username, password)
			VALUES
			(%s, %s)
			'''
	insert_val = (username_info, password_info)
	result = cur.execute(sql_insert, insert_val)
	db.commit()
	db.close()

	password.delete(0, END)
	passwordr2.delete(0, END)
	Label(register_screen, text='Registration Success! Back to Login.', fg='blue').pack()

def login():
	global username_verify
	global password_verify
	global login_screen

	login_screen = Tk()
	login_screen.geometry('300x180')
	login_screen.title('Account Login')

	username_verify = StringVar()
	password_verify = StringVar()

	username_lable = Label(login_screen, text='Username').pack()
	username_verify = Entry(login_screen, textvariable=username_verify)
	username_verify.pack()

	password_label = Label(login_screen, text='Password').pack()
	password_verify = Entry(login_screen, textvariable=password_verify, show='*')
	password_verify.pack()

	# Label(login_screen, text='').pack()
	Button(login_screen, text='Login', command=login_verify).pack()
	Button(login_screen, text='Back', command=login_screen.destroy).pack()

def login_verify():
	global username1

	username1 = username_verify.get()
	password1 = password_verify.get()
	username_verify.delete(0,END)
	password_verify.delete(0,END)

	print('username: ' + username1)

	db = MySQLdb.connect(host='127.0.0.1', user='root', password='*****', database='mydatabase')
	cur = db.cursor()
	select_val = "SELECT password FROM users WHERE username = %s"
	user = username1,
	cur.execute(select_val, user)
	pw_db = cur.fetchone()
	print('input pass: ' + password1)
	print('table pass: ', pw_db)

	if not pw_db:
		user_not_found()
	else:
		if password1 == pw_db[0]:
			login_success()
		else:
			password_not_recognised()

def login_success():
	global loginsuccess_screen
	loginsuccess_screen = Tk()
	loginsuccess_screen.title('Login')
	loginsuccess_screen.geometry('250x50')
	Label(loginsuccess_screen, text='Hello ' + username1 + ' you are now logged in.').pack()
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
