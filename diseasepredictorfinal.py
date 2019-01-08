from tkinter import *
from texttable import Texttable
from collections import OrderedDict
import os
f=0
t=Texttable()
creds = 'tempfile.temp'
import cx_Oracle
con =cx_Oracle.connect("SYSTEM/smv")
cur=con.cursor()
one=[];
#cur.execute("create table symp(disease varchar(30),symptoms varchar(300),symptoms2 varchar(300))")
def adminpower():
    """cur.execute("insert into symp values('common cold','sneezing','cough')")
    cur.execute("insert into symp values('fever','high temparature','body_pains')")
    cur.execute("insert into symp values('chickenpox','fever','rashes')")
    cur.execute("insert into symp values('Diarrhea','vomitings','weakness')")
    cur.execute("insert into symp values('Fatigue','dizziness','sore')")
    cur.execute("insert into symp values('Rabies','headache','high fever')")
    cur.execute("insert into symp values('Influenza','sore_throat','extreme fatigue')")
    cur.execute("insert into symp values('dengue','severe fever','nausea')")
    cur.execute("insert into symp values('Tuberculosis','chest pain','Persistent fever')")
    cur.execute("insert into symp values('Poliomyliti','Stiffness of neck','loss of head support')")
    cur.execute("insert into symp values('Hepatitis','enlarged liver','Loss of appetite and nausea')")
    cur.execute("insert into symp values('Cholera','Muscular_cramps','dehydration')")
    cur.execute("insert into symp values('Diphtheria','Sore throat','general indisposition')")
    cur.execute("insert into symp values('Leprosy','Scabs','lose sensation')")
    cur.execute("insert into symp values('malaria','weak and anaemic','nausea')")
    cur.execute("insert into symp values('Amoebiasis','abdominal pain','mucus in stool')")
    cur.execute("insert into symp values('Filariasis','Swelling of legs','fever')")
    cur.execute("insert into symp values('Diabetes mellitus','More glucose in blood','Reduced healing capacity of injury')")
    cur.execute("insert into symp values('Cardio vascular diseases','paralysis','bloodpressure')")
    cur.execute("insert into symp values('Coronary heart','pain in the chest','Intense nausea and vomiting')")
    cur.execute("insert into symp values('Osteoporosis','fracure of bones','stress fractures')")
    cur.execute("insert into symp values('Malignant tumour','thickening in tissues','change in the form of mole or wart')")
    cur.execute("insert into symp values('AIDS','abdomen pain','weightloss')")
    cur.execute("insert into symp values('symphilis','White patches in the mouth','Acne-like warts in the groin area')")
    cur.execute("insert into symp values('Gonorrhoea','Rectal discomfort',' Mild sore throat ')")
    cur.execute("insert into symp values('plague','skin turning black','abdominal pain')")
    cur.execute("insert into symp values('swine flu','fatigue','nausea')")
    cur.execute("insert into symp values('ebola','bleeding with out an injury','vomiting')")
    cur.execute("insert into symp values('small pox','pain in muscles','skin rashes')")
    cur.execute("insert into symp values('bird flu','pain in muscles','fever')")
    cur.execute("insert into symp values('Acute Bronchitis','fatigue','chest pressure')")
    con.commit();"""
    #cur.execute('select * from symp')
    c='y'
    print("Hello Admin! Welcome back!")
    while c=='y':
        print("1.insert 2.delete 3.display 4.update 5.Exit")
        ch=int(input("Enter your choice:"))
        if(ch==1):
            d=input("Enter the disease:")
            s1=input("Enter the symptom 1:")
            s2=input("Enter the symptom 2:")
            cur.execute("insert into symp(disease,symptoms,symptoms2) values('%s','%s','%s')"%(d,s1,s2))
        elif(ch==2):
            ds=input("Enter the disease of the row that u wanna delete:")
            cur.execute("delete from symp where disease='%s'"%ds)
        elif(ch==3):
            cur.execute("select * from symp")
            print(cur.fetchmany())
        elif(ch==4):
            print("1.disease 2.symptom1 3.symptom2")
            ans=int(input("Enter the parameter that u wanna update:"))
            if(ans==1):
                d1=input("Enter the new disease:")
                dold=input("Enter the disease of the row that u wanna update:")
                cur.execute("update symp set disease='%s' where disease='%s'"%(d1,dold))
            elif(ans==2):
                sp1=input("Enter the new symptom:")
                sp1old=input("Enter the symptom of the row that u wanna update:")
                cur.execute("update symp set symptoms='%s' where symptoms='%s'"%(sp1,sp1old))
            elif(ans==3):
                sp2=input("Enter the new symptom:")
                sp2old=input("Enter the symptom of the row that u wanna update:")
                cur.execute("update symp set symptoms2='%s' where symptoms2='%s'"%(sp2,sp2old))
        elif(ch==5):
            exit()
        c=input("Do u wanna continue?(y/n):")
         


#query
def userpower():    
    n = int(input("Enter the number of symptoms:"))
    s=[]
    st=[]
    l1=[]
    for i in range (n):
        s.append(input("enter symptom:"))
        st.append(s[i].casefold())    
    for k in range(len(st)):
        q = "%" + st[k] + "%"
        cur.execute("select * from symp,sy2 where (symptoms like '%s' or symptoms2 like '%s') and symp.disease=sy2.disease"%(q,q))
        #cur.execute("select * from symp where (concat(symptoms,symptoms2) like '%s')"%q)
        l1+=cur.fetchall()
    for i in range(len(l1)):
        one.append(list(l1[i]))   
    #some=[['disease','symptom1','symptom2']]+one
    tbl=Tk()
    tbl.title("RESULT")
    button1=Button(tbl,text="Print Result",command=table)
    button1.pack()
    tbl.mainloop()
def table():
    some=[['disease','symptom1','symptom2','disease','caused_by','precautions','transmission_mode']]+one
    t=Texttable()
    t.add_rows(some)
    print(t.draw())
    
def FSSignup(nameE,pwordE):
    with open(creds, 'w') as f: 
        f.write(nameE) 
        f.write('\n') 
        f.write(pwordE) 
        f.close()
    roots = Tk() 
    roots.destroy()
    if os.path.isfile(creds):
        Login()
 
def Login():
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk()
    rootA.title('Login') 
 
    intruction = Label(rootA, text='Please Login\n') 
    intruction.grid(sticky=E) 
    nameL = Label(rootA, text='Username: ') 
    pwordL = Label(rootA, text='Password: ') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin)
    loginB.grid(columnspan=2, sticky=W)
    
    rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser)
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() 
        uname = data[0].rstrip() 
        pword = data[1].rstrip() 
 
    if nameEL.get() == uname and pwordEL.get() == pword: 
        r = Tk()
        r.configure(background='green')
        r.title('Welcome, Admin ')
        r.geometry('150x50')
        rlbl = Label(r, text='\n Login Successful!')
        rlbl.pack() 
        r.mainloop()
        f=1
        adminpower()
    else:
        r = Tk()
        r.configure(background='red')
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
        exit()
 
def DelUser():
    os.remove(creds) 
    rootA.destroy()

def function():
    r=Tk()
    r.title('Symptoms-Diseases Predictor')
    lbl= Label(r, text='Welcome to our Disease Predictor System')
    frame=Frame(r,bg='blue')
    frame.pack(side=LEFT,fill=BOTH)
    btn = Button(frame,text="Proceed to Login...",command=r.destroy,padx=20)
    btn.pack(pady=20,padx=20)
    lbl.pack()
    r.mainloop()




global nameE 
global wordE 
nameE = 'lol'
wordE = 'hola'
function()
choice=input("Enter how you want to login(user/admin):")
if choice.casefold()=='admin':
    FSSignup(nameE,wordE)
elif(choice.casefold()=='user'):
    userpower()
    
    





























