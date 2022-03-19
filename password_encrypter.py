from cryptography.fernet import Fernet
import csv,os
import sqlite3

connection=sqlite3.connect('key.db')
cursor=connection.cursor()
key=list(cursor.execute('SELECT * FROM KEY'))[0][0]
cursor.close()

fernet = Fernet(key)
file_name = 'passwords.csv'
def add(website,username,password):
    mydict.append({'website':website,'username':fernet.encrypt(username.encode()),'password':fernet.encrypt(password.encode())})
    print('Entry Added')
def remove(website,username,password):
    val=''
 
    for i in mydict:
        x=str(i['username'][2:])
       
        y=str(i['password'][2:])
        
        if i['website']==website and username == fernet.decrypt(x.encode()).decode() and password==fernet.decrypt(y.encode()).decode():
            val=i
    try:        
        mydict.remove(val)
        print('Entry Removed')
    except ValueError:
        print('No Such Value ')
    except Exception as e:
        print(e)

        print('Invalid,Enter ~ to stop')
        
def update(website,username,password,website2,username2,password2):
    val=''
 
    for i in mydict:
        x=str(i['username'])[2:]
       
        y=str(i['password'])[2:]
        
        if i['website']==website and username == fernet.decrypt(x.encode()).decode() and password==fernet.decrypt(y.encode()).decode():
            i['website']=website2
            i['username']=fernet.encrypt(username2.encode())
            i['password']=fernet.encrypt(password2.encode())
            val=1
    if val:
        print('Entry Updated')
    else:
        print("Couldn't find the value")

global data
global mydict
if file_name in os.listdir():
    file= open(file_name,'r')
    data= list(csv.DictReader(file))
    file.close()
else:
    file= open(file_name,'w')
    file.close()
    try:
        data= list(csv.DictReader(file))
    except:
        data=[]
mydict=data

def view (website=''):
    
    if website:
        print('Filterd by website containing',website )

        print('website'.center(30),'|','username'.center(30),'|','password'.center(30))
        print('-'*100)
        for i in mydict:
            if website.lower() in i['website'].lower():
                x=str(i['username'])[2:]
                y=str(i['password'])[2:]
                print(i['website'].center(30),'|',fernet.decrypt(x.encode()).decode().center(30),'|',fernet.decrypt(y.encode()).decode().center(30))        
    else:
        print('website'.center(30),'|','username'.center(30),'|','password'.center(30))
        print('-'*100)
        for i in mydict:
            x=str(i['username'])[2:]          
            y=str(i['password'])[2:]
            print(i['website'].center(30),'|',fernet.decrypt(x.encode()).decode().center(30),'|',fernet.decrypt(y.encode()).decode().center(30))
    print('-'*100)
view()    
fields=['website','username','password' ]

print('Enter ~ to stop and Save')
print("Enter view 'optional website' to view")
print("Enter add 'website' 'username' 'password' to encrypt and add to csv: ")
print("Enter remove 'website' 'username' 'password' to remove entry from csv ")
print("Enter update 'website' 'username' 'password' 'website2' 'username2' 'password2' to update an existing data ")
print('-'*100)


while True:
    x=input("Enter Query: ")
    if x=='~':
        
        break
    try:
        a=list(map(lambda x:x.strip(),x.split("'")))
        x=''
        for i in range(len(a)):
            if a[i]:
                if i==0:
                    x+=a[i]+'('
                else:
                    x+="'"+a[i]+"',"
        x.strip(",")            
        x+=")"        
        eval(x)
    except Exception as e:
        print(e)
        print('Invalid,Enter ~ to stop')

with open(file_name, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames = fields)
     
    # writing headers (field names)
    writer.writeheader()
     
    # writing data rows
    writer.writerows(mydict)
print('File Saved')   
view()    


