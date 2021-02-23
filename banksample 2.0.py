import time
import random
import mysql.connector as sql
import getpass
import pyttsx3

def speak(a):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 0 for male ; 1 for female
    engine.say(a)
    engine.runAndWait()

def insert(acc,pas,fname,lname,phno,address,gender,bal):
    con = sql.connect(host='localhost',user='root',passwd='dikshantgupta',database='bankfile')
    cursor = con.cursor()
    data = "insert into bank values('{}','{}','{}','{}','{}','{}','{}',{})".format(acc,pas,fname,lname,phno,address,gender,bal)
    cursor.execute(data)
    con.commit()
    con.close()
    return 'y'
def delete(acc,pas):
    con = sql.connect(host='localhost',user='root',passwd='dikshantgupta',database='bankfile')
    cursor = con.cursor()
    cursor.execute('select accno,password from bank')
    d = cursor.fetchall()
    for rows in d:
        if acc == rows[0] and pas == rows[1]:
            cursor.execute("delete from bank where accno = '{}'and password = '{}'".format(acc,pas))
    con.commit()
    con.close()
    return 'y'
def addbal(acc,pas):
    con = sql.connect(host='localhost',username='root',passwd='dikshantgupta',database='bankfile')
    cursor = con.cursor()
    cursor.execute('select accno,password,balance from bank')
    d = cursor.fetchall()
    for rows in d:
        if acc == rows[0] and pas == rows[1]:
            amt = int(input('ENTER THE AMOUNT TO ADD :  '))
            balance = rows[2]
            cursor.execute("update bank set balance = {} where accno ='{}' and password ='{}'".format((balance + amt),acc,pas))
    con.commit()
    con.close()
    return 'y'
def stat(acc,pas):
    con = sql.connect(host='localhost',username='root',passwd='dikshantgupta',database='bankfile')
    cursor = con.cursor()
    cursor.execute('select * from bank')
    d = cursor.fetchall()
    for r in d:
        if acc == r[0] and pas == r[1]:
            print('YOUR ACCOUNT STATUS IS AS :\n\tACCOUNT NUMBER - ',r[0],'\n\tPASSWORD - ****\n\tFIRST NAME - ',r[2],'\n\tLAST NAME - ',r[3],'\n\tPHONE NUMBER - ',r[4],'\n\tADDRESS - ',r[5],'\n\tGENDER - ',r[6],'\n\tBALANCE - ',r[7])
    con.close()
    return 'y'
def update(acc,pas):
    con = sql.connect(host='localhost',username='root',passwd='dikshantgupta',database='bankfile')
    cursor = con.cursor()
    cursor.execute('select accno,password,phno from bank')
    d = cursor.fetchall()
    for rows in d:
        if acc == rows[0] and pas == rows[1]:
            ph = input('enter your registered phone number  :')
            if ph == rows[2]:
                ch = int(input('''1. PASSWORD
2. FIRST NAME
3. LAST NAME
4. ADDRESS
5. PHONE NUMBER
6. GENDER
ENTER A CHOICE FOR UPDATION:  '''))
                if ch == 1:
                    npas = str(getpass.getpass('ENTER THE NEW PASSWORD : '))
                    cursor.execute("update bank set password = '{}' where accno = '{}'".format(npas,acc))
                    con.commit()
                    con.close()
                elif ch == 2:
                    nfname = input('ENTER THE CORRECT FIRST NAME  : ')
                    cursor.execute("update bank set fname ='{}' where accno = '{}'".format(nfname,acc))
                    con.commit()
                    con.close()
                elif ch == 3:
                    nlname = input('ENTER THE CORRECT LAST NAME:  ')
                    cursor.execute("update bank set lname = '{}' where accno = '{}'".format(nlname,acc))
                    con.commit()
                    con.close()
                elif ch == 4:
                    naddr = input('ENTER THE NEW ADDRESS:  ')
                    cursor.execute("update bank set address = '{}' where accno = '{}'".format(naddr,acc))
                    con.commit()
                    con.close()
                elif ch == 5:
                    nph = input('ENTER THE NEW PHONE NUMBER:  ')
                    cursor.execute("update bank set phno = '{}' where accno = '{}'".format(nph,acc))
                    con.commit()
                    con.close()
                elif ch == 6:
                    ng = input('ENTER THE CORRECT GENDER:  ')
                    cursor.execute("update bank set gender = '{}' where accno = '{}'".format(ng,acc))
                    con.commit()
                    con.close()
                else:
                    con.close()
                    print('ENTER A VALID CHOICE')
    return 'y'

def deduct(acc,pas):
    con = sql.connect(host='localhost',username='root',passwd='dikshantgupta',database='bankfile')
    cursor = con.cursor()
    cursor.execute('select accno,password,balance from bank')
    d = cursor.fetchall()
    for rows in d:
        if acc == rows[0] and pas == rows[1]:
            balance = rows[2]
            amt = int(input('ENTER THE AMOUNT TO DEDUCE :  '))
            if balance > amt:
                cursor.execute("update bank set balance = {} where accno = '{}' and password = '{}'".format((balance - amt),acc,pas))
            else:
                print('\t\t\tINSUFFICIENT BALANCE')
    con.commit()
    con.close()
    return 'y'

def bank(acc,pas):
    con = sql.connect(host='localhost',user='root',passwd='dikshantgupta',database='bankfile')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM bank_id')
    d = cursor.fetchall()
    for row in d:
        if row[0] == acc and row[1] == pas:
            con.close()
            return 'y'
def bankinfo():
    con = sql.connect(host='localhost', user='root', passwd='dikshantgupta', database='bankfile')
    cursor = con.cursor()
    cursor.execute('SELECT fname,lname,phno,address,gender from bank')
    d = cursor.fetchall()
    for i in d:
        print(i,end='\n\n')
    con.close()
7
# main--------------------------------------------------------------------------
print('BANKING SAMPLE USING MySQL && PYTHON')
speak('HELLO USER , HOW MAY I HELP YOU ?')
time.sleep(3)
while True:
    for a in range(90):
        a = '-'
        print(a,end='')
    print()   
    ch = input('''\n1. CREATE A NEW ACCOUNT
2. ADD BALANCE TO YOUR ACCOUNT
3. CHECK YOUR ACCOUNT STATUS
4. UPDATE YOUR INFORMATION
5. DEDUCT BALANCE FROM YOUR ACCOUNT
6. DELETE YOUR ACCOUNT
7. BANK PERSONNAL LOGIN
8. EXIT

ENTER YOUR CHOICE : ''')

    if ch == '1':
        fname = input('ENTER YOUR FIRST NAME:  ')
        lname = input('ENTER YOUR LAST NAME:   ')
        phno = input('ENTER YOUR PHNUMBER:  ')
        if len(phno) != 10:
            print('PLEASE ENTER A VALID PHONE NUMBER')
        else:
            address = input('ENTER YOUR ADDRESS:  ')
            gender = input('ENTER YOUR GENDER m/f/o:  ')
            if gender not in ['m','f','o','M','F','O']:
                print('PLEASE ENTER A VALID CHOICE')
            else:
                acc = random.randint(1000,9999)
                acc = str(acc)
                print('YOUR COMPUTER GENERATED ACCOUNT NUMBER IS : ',acc)
                pas = input('PLEASE ENTER A 4-digit PASSWORD FOR YOUR ACCOUNT: ')
                if len(pas) != 4:
                    print('PLEASE FOLLOW GUIDELINES')
                else:
                    bal = int(input('ENTER THE AMOUNT YOU WANT TO ADD : '))
                    if bal>500 and bal<50000:
                        t = insert(acc,pas,fname,lname,phno,address,gender,bal)
                        if t == 'y':
                            print(time.process_time())
                        print('THANK YOU FOR CHOSING US')
    elif ch == '2':
        acc = input('ENTER YOUR ACCOUNT NUMBER:   ')
        pas = str(getpass.getpass('ENTER YOUR PASSWORD:   '))
        t = addbal(acc,pas)
        if t == 'y':
            print(time.process_time())

    elif ch == '3':
        acc = input('ENTER YOUR ACCOUNT NUMBER:   ')
        pas = str(getpass.getpass('ENTER YOUR PASSWORD:   '))
        t = stat(acc,pas)
        if t == 'y':
            print(time.process_time())

    elif ch == '4':
        acc = input('ENTER YOUR ACCOUNT NUMBER:   ')
        pas = str(getpass.getpass('ENTER YOUR PASSWORD:   '))
        t = update(acc,pas)
        if t == 'y':
            print(time.process_time())
            
    elif ch == '5':
        acc = input('ENTER YOUR ACCOUNT NUMBER:   ')
        pas = str(getpass.getpass('ENTER YOUR PASSWORD:   '))
        t = deduct(acc,pas)
        if t == 'y':
            print(time.process_time())
    
    elif ch == '6':
        acc = input('ENTER YOUR ACCOUNT NUMBER :  ')
        pas = str(getpass.getpass('ENTER YOUR PASSWORD:   '))
        t = delete(acc,pas)
        if t =='y':
            print(time.process_time())
    elif ch == '7':
        acc = input('ENTER YOUR ID : ')
        pas = str(getpass.getpass('ENTER YOUR PASSWORD : '))
        t = bank(acc,pas)
        if t == 'y':
            print('HELLO SIR/MAM')
            print('THE TOTAL BANK ACCOUNT HOLDERS IN THIS BRANCH ARE AS : ')
            bankinfo()
        else:
            print('NOT AN AUTHORIZED PERSONNAL')
            break
    elif ch == '8':
        print('THANK YOU')
        speak('THANK YOU')
        time.sleep(3)
        break

    else:
        speak('PLEASE RECHECK YOUR INPUT')
        print('''PLEASE ENTER A VALID CHOICE''')
        time.sleep(2)
time.sleep(8)
