import random, time, string, json


def generator(length : int):
    print("Generating Password. It will be printed here when it is complete.")
    characterlist = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    password = []
    for i in range(length):
        password.append(random.choice(characterlist))
    print("\n" + "".join(password) + "\n\n")
    return "\n" + "".join(password) + "\n\n"



def delete_sub_store_confirm(sub : str):
    confirm = input("Are you sure you want to delete this sub store? (y/n)\n")
    if confirm.lower() == "y" or confirm.lower() == "yes":
        del data["subs"][sub]
        with open("passwords.json", "w") as f:
            json.dump(data, f)
        print("\nSuccessfully Deleted\n\n")
        time.sleep(1)

    elif confirm.lower() == "n" or confirm.lower() == "no":
        print("Cancelled")
    else:
        print("Invalid Option. Please try again.")

def create_new_sub(name : str):
    with open("passwords.json", "r+") as f:
        data=json.load(f)
    subs = data["subs"]
    subs[name] = {}
    with open("passwords.json", "w") as f:
        json.dump(data, f)
    print("\nSuccessfully created new sub store\n\n")
    time.sleep(1)
def save_password_in_sub(sub : str):
    with open("passwords.json") as f:
        data=json.load(f)
    if sub.lower() in data["subs"]:
        pswdname = input("What is the new password name?\n")
        if pswdname.lower() in data["subs"][sub.lower()]:
            rep = input("That password name is already taken. Do you want to remove it and replace it with this new password? (y/n)\n")
            if rep.lower() == "y" or rep.lower() == "yes":
                with open("passwords.json", "r+") as f:
                    data=json.load(f)
                del data["subs"][sub][pswdname.lower()]
                with open("passwords.json", "w") as f:
                    json.dump(data, f)
                print("\nSuccessfully Deleted\n\n")
            elif rep.lower() == "n" or rep.lower() == "no":
                print("Cancelled")
                return
            else:
                print("Invalid Option. Please try again.")
                return
        pswdweb = input("What website is this password for?\n")
        pswdemail = input("What email is this password linked to?\n")
        pswdusername = input("What username is this password linked to?\n")
        pswdnotes = input("What notes do you want to add to the password?\n")
        pswdpswd = input("What password do you want to use? Type \"generate\" to generate a random password\n")
        if pswdpswd == "generate":
            try:
                len = int(input("What length do you want the password to be?\n"))
                pswdpswd = generator(len)
            except ValueError:
                print("Invalid input. Automatically set length to 40.")
                pswdpswd =generator(40)
        with open("passwords.json", "r+") as f:
            data=json.load(f)
        subdata = data["subs"][sub.lower()]
        subdata[pswdname.lower()] = {"name" : pswdname.lower(), "website" : pswdweb, "email" : pswdemail, "username" : pswdusername, "notes" : pswdnotes, "password" : pswdpswd}
        with open("passwords.json", "w") as f:
            json.dump(data, f)
        print("\nSuccessfully created new password\n\n")
        time.sleep(1)

    else:
        psubs = input("Cannot find that sub. Do you want to see a list of your current sub stores? (y/n)\n")
        if psubs.lower() == "y" or psubs.lower == "yes":
            no = 1
            for subs in data["subs"]:
                print(f"{no}: {subs}")
                no+=1
            time.sleep(1)
        elif psubs.lower() == "n" or psubs.lower() == "no":
            time.sleep(1)
        else:
            print("Invalid Choice")
            time.sleep(1)

def get_pswd_with_sub(sub : str):
    print(f"Passwords in {sub} sub store")
    for pswds in data["subs"][sub]:
        print(pswds)
    pswd = input("Which password do you want to open?\n")
    if pswd.lower() in data["subs"][sub]:
        name = data["subs"][sub][pswd.lower()]["name"]
        email = data["subs"][sub][pswd.lower()]["email"]
        username = data["subs"][sub][pswd.lower()]["username"]
        website = data["subs"][sub][pswd.lower()]["website"]
        notes = data["subs"][sub][pswd.lower()]["notes"]
        password = data["subs"][sub][pswd.lower()]["password"]
        print("Password Info:\n")
        print(f"Name : {name}")
        print(f"Email : {email}")
        print(f"Username : {username}")
        print(f"Website : {website}")
        print(f"Notes : {notes}")
        print(f"\nPassword: {password}\n\n")
        time.sleep(2)

def get_pswd_with_name(name : str):
    print("Passwords found will be printed below\n\n")
    for sub in data["subs"]:
        if name.lower() in data["subs"][sub]:
            print(f"Password found in {sub} sub store. For more info please use \"gep\" command and choose the \"{sub}\" sub store")
    time.sleep(1)
    print("\n\n")

def edit_pswd_with_sub(sub : str):
    with open("passwords.json") as f:
        data=json.load(f)
    print(f"Passwords in {sub} sub store")
    for pswds in data["subs"][sub]:
        print(pswds)
    pswd = input("Which password do you want to edit?\n")
    if pswd.lower() in data["subs"][sub]:
        with open("passwords.json") as f:
            data=json.load(f)
        edit = str(input("""What would you like to edit? Valid options:
        
- email
- username
- notes
- password\n"""))
        print(edit.lower())
        if edit.lower() != "email" or edit.lower() != "username" or edit.lower() != "notes" or edit.lower() != "password":
            print("Invalid input")
            time.sleep(1)
            return
        editto = "What would you like to change this to?\n"
        if edit.lower() == "email":
            data["subs"][sub][pswd]["email"] = editto
        elif edit.lower() == "username":
            data["subs"][sub][pswd]["username"] = editto
        elif edit.lower() == "notes":
            data["subs"][sub][pswd]["notes"] = editto
        elif edit.lower() == "password":
            data["subs"][sub][pswd]["password"] = editto
    print("Invalid option")
    return

while True:
    option = input("""What would you like to use?:
    
- Password generator (ID: gen)
- Get a saved password (ID: gep)
- Save a new password (ID: sap)
- Create a new sub store (ID: sub)
- Edit a password (ID: edp)\n""")
    if option.lower() == "gen":
        try:
            charamnt = int(input("How many characters do you want the password to be?\n"))
            if charamnt >=1000000:
                print("Why?\n")
            generator(charamnt)
        except ValueError:
            print("Invalid amount. Try again")
    elif option.lower() == "sub":
        name = input("What name do you want to give this sub store?\n")
        with open("passwords.json") as f:
            data=json.load(f)
        if name.lower() in data["subs"]:
            if name.lower() == "main":
                print("You cannot create a store with this name.")
            else:
                dele = input("This is already a sub store. Would you like to remove it and replace it with this new one? (y/n)\n")
                if dele.lower() == "y" or dele.lower() == "yes":
                    delete_sub_store_confirm(name.lower())
                elif dele.lower() == "n" or dele.lower() == "no":
                    print("Cancelled")
                else:
                    print("Invalid Option. Please try again.")
        else:
            create_new_sub(name)
    elif option.lower() == "sap":
        sub = input("What sub do you want to use? Use \"main\" if you don't have a new sub to use.\n")
        save_password_in_sub(sub)
    elif option.lower() == "gep":
        sub = input("What sub store is the password in?\n")
        with open("passwords.json") as f:
            data = json.load(f)
        if sub.lower() in data["subs"]:
            get_pswd_with_sub(sub.lower())
        else:
            name = input("Can't find sub store. Please type the name of the password to find it.\n")
            found = False
            for sub in data["subs"]:
                if name.lower() in data["subs"][sub]:
                    found = True
            if found == True:
                get_pswd_with_name(name.lower())
            else:
                print("Couldn't find password.")
                time.sleep(1)
    elif option.lower() == "edp":
        sub = input("What sub store is the password in?\n")
        with open("passwords.json") as f:
            data = json.load(f)
        if sub.lower() in data["subs"]:
            edit_pswd_with_sub(sub.lower())
    else:
        print("Invalid Option")
