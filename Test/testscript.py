import cgi, cgitb
form = cgi.FieldStorage()
user =  form.getvalue('userlogin')
password =  form.getvalue('userpassword')

user_passwords = open("Test/userpassword.csv", "r")
user_list = [] 
for line in user_passwords:
    temp_list = line.strip("\n").split(",")
    if temp_list[0] == user:
        if temp_list[1] == password:
            print("Logged in with {} and {}".format(user, password))
    user_list.append(line.strip("\n").split(","))

print(user_list)
user_passwords.close()