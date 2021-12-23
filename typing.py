import random as r
import time


print("\nTyping practice.....\n\n")
time.sleep(2)
print("Use general method to type.....\n\n")
time.sleep(1)
name=input("Enter your name : ")
print("\nType characters...\n")
i=1
c1=0
import time as t
t1c1=0
rrr=t.monotonic()
while i<=40:           
           
           v=r.randint(97,122)
           h=chr(v)
           print("\n",h,"\n")
           
           a=input(f"Enter {i}/40 chr : ")
           if a==h:
                     i=i+1
                     c1=c1+1
                   
           else:
                 time.sleep(1)
                 c1=c1-1  
                 print("\nwrong typed...try again..")          
                                            
yyy=t.monotonic()
t1c1=yyy-rrr

print(f"\nCongratulation {name}, you have successfully completed the first level\n")
time.sleep(2)
print("type words part 1")
w1=0
t1w1=0
n=1   
rrr=t.monotonic()            
while n<=60:
        v=r.randint(2,3)
        d=""
        for i in range(v):
            m=r.randint(97,122)
            
            d=d+chr(m)
        print("\n",d,"\n")    
        c=input(f"Enter {n}/60 string : ")              
        if c==d:
                 n=n+1
                 w1=w1+1

        else:
                 time.sleep(1)
                 w1=w1-1
                 print("\nwrong typed...try again...")                                   
yyy=t.monotonic()
t1w1=yyy-rrr
                  
print(f"\nCongratulation {name}, you have successfully completed the second level\n")
time.sleep(2)
print("type words part 2\n")
w2=0
t1w2=0
rrr=t.monotonic()            
n=1               
while n<=90:
        v=r.randint(5,8)
        d=""
        for i in range(v):
            m=r.randint(97,122)
            
            d=d+chr(m)
        print("\n",d,"\n")    
        c=input(f"Enter {n}/90 string : ")              
        if c==d:
                 n=n+1
                 w2=w2+1
                
        else:  
                time.sleep(1)
                w2=w2-1                 
                print("\nwrong typed...try again...")           
yyy=t.monotonic()
t1w2=(yyy-rrr)                      
print(f"\nCongratulation {name}, you have successfully completed the third level\n")

time.sleep(2)
print("type characters with spaces....\n")                     
n=1             
cs=0  
t1cs=0
rrr=t.monotonic()
while n<=30:
        v=r.randint(5,9)
        d=""
        for i in range(v):
                   
            m=r.randint(97,122)
            
            d=d+chr(m)+" "
            
        print("\n",d,"\n")    
        c=input(f"Enter {n}/30 string : ")              
        if c==d[:-1]:
                 n=n+1
                 cs=cs+1  
        else:
                  time.sleep(1)
                  cs=cs-1    
                  print("\nwrong typed...try again...")         
   
yyy=t.monotonic()
t1cs=(yyy-rrr)    
print(f"\nCongratulation {name}, you have successfully completed the fourth level\n")

time.sleep(2)
print("type sentences part 1\n")                     
n=1    
s1=0
t1s1=0
rrr=t.monotonic()           
while n<=30:
        v=r.randint(3,4)
        d=""
        for j in range(v):
            b=r.randint(2,4)
            for i in range(b):
                   
              m=r.randint(97,122)
              
              d=d+chr(m)
            d=d+" "           
        print("\n",d,"\n")    
        c=input(f"Enter {n}/30 string : ")              
        if c==d[:-1]:
                 n=n+1
                 s1=s1+1  
        else:
                time.sleep(1)
                s1=s1-1
                print("\nwrong typed...try again...")         
yyy=t.monotonic()

t1s1=(yyy-rrr)   
print(f"\nCongratulation {name}, you have successfully completed the fifth level\n")
s2=0
time.sleep(2)
print("type sentences part 2...\n")                     
n=1 
t1s2=0
rrr=t.monotonic()              
while n<=90:
        v=r.randint(3,9)
        d=""
        for j in range(v):
            b=r.randint(2,11)
            for i in range(b):
                   
              m=r.randint(97,122)
              
              d=d+chr(m)
            d=d+" "           
        print("\n",d,"\n")    
        c=input(f"Enter {n}/90 string : ")              
        if c==d[:-1]:
                 n=n+1
                 s2=s2+1  
        else: 
                 time.sleep(1)
                 s2=s2-1
                 print("\nwrong typed...try again...")
yyy=t.monotonic()
t1s2=(yyy-rrr)                 
print(f"\nCongratulation {name}, you have successfully completed the sixth level\n")
print(".....\n\n")
time.sleep(2)
print(f"\n\n{name}, have you noticed that your performance has been improved and become more better than earlier...Congratulation!!!!\n\n")

print("saving.........")
time.sleep(2)
yn=input("do you have mysql server installed in your pc?(y/n)")
if yn=='y':
   point=0
   import mysql.connector as mycon
   u=input("Enter username of your mysql server : ")
   p=input("Enter password of your mysql server : ")
   
   try:
       
                    global mm 
                    mm=mycon.connect(host="localhost",user=u,password=p) 
          
   except:
      
      
      
        point=1
        print("Unable to connect to mysql server...\n")
        print("saving your score content into a file........\n")
        time.sleep(2)      
        f=open('typing-score.txt','a+')
        f.write("\n"+15*" "+"Typing practice score")
        f.write("\n\n")
        na="Name"
        f.write(f"{na.ljust(40)} :  {name}\n")
        ty1="Typing character score"
        f.write(f"{ty1.ljust(40)} :  {c1}/40 -- completed in {t1c1//60} minutes {round(t1c1%60,0)} seconds\n")
        ty2="Typing word part 1 score"
        f.write(f"{ty2.ljust(40)} :  {w1}/60 -- completed in {t1w1//60} minutes {round(t1w1%60,0)} seconds \n")
        ty3="Typing word part 2 score"
        f.write(f"{ty3.ljust(40)} :  {w2}/90 -- completed in {t1w2//60} minutes {round(t1w2%60,0)} seconds\n")
        ty4="Typing characters with spaces score"
        f.write(f"{ty4.ljust(40)} :  {cs}/30 -- completed in {t1cs//60} minutes {round(t1cs%60,0)} seconds\n")
        ty5="Typing sentences part 1 score"
        f.write(f"{ty5.ljust(40)} :  {s1}/30 -- completed in {t1s1//60} minutes {round(t1s1%60,0)} seconds\n")
        ty6="Typing sentences part 2 score"
        f.write(f"{ty6.ljust(40)} :  {s2}/90 -- completed in {t1s2//60} minutes {round(t1s2%60,0)} seconds\n")
        f.write(f"Status                                   :  Completed\n\n")
        print("\nYour score has been saved successfully in a file named typing-score.txt in your current directory/folder")
  
               
                   
   if point==0:         
       
           
      cursor=mm.cursor(buffered=True)
      cursor.execute("create database if not exists typing")
      cursor.execute("use typing")
      cursor.execute("create table if not exists score ( sno varchar(100),Name varchar(100),character1 varchar(200),words_part1 varchar(100),words_part2 varchar(100),character_with_spaces varchar(100),sentence_part1 varchar(100),sentence_part2 varchar(100))")

      cursor.execute("select * from score order by sno desc")
      aa=cursor.fetchone()

      if aa is None:
       k=0
      else:
       k=int(aa[0])
   
   
      a="insert into score values(%s,%s,%s,%s,%s,%s,%s,%s)"
      b=(str(k+1),str(name),str(c1)+"/40("+str(t1c1//60)+" min "+str(round(t1c1%60,0))+" sec)",str(w1)+"/60("+str(t1w1//60)+" min "+str(round(t1w1%60,0))+" sec)",str(w2)+"/90("+str(t1w2//60)+" min "+str(round(t1w2%60,0))+" sec)",str(cs)+"/30("+str(t1cs//60)+" min "+str(round(t1cs%60,0))+" sec)",str(s1)+"/30("+str(t1s1//60)+" min "+str(round(t1s1%60,0))+" sec)",str(s2)+"/90("+str(t1s2//60)+" min "+str(round(t1s2%60,0))+" sec)")
      cursor.execute(a,b)
      mm.commit()
      print("\nYour score has been successfully saved in your mysql database sever with database name - typing, table name - score")
   
 
 
               
elif yn=='n':
        f=open('typing-score.txt','a+')
        f.write("\n"+15*" "+"Typing practice score")
        f.write("\n\n")
        na="Name"
        f.write(f"{na.ljust(40)} :  {name}\n")
        ty1="Typing character score"
        f.write(f"{ty1.ljust(40)} :  {c1}/40 -- completed in {t1c1//60} minutes {round(t1c1%60,0)} seconds\n")
        ty2="Typing word part 1 score"
        f.write(f"{ty2.ljust(40)} :  {w1}/60 -- completed in {t1w1//60} minutes {round(t1w1%60,0)} seconds \n")
        ty3="Typing word part 2 score"
        f.write(f"{ty3.ljust(40)} :  {w2}/90 -- completed in {t1w2//60} minutes {round(t1w2%60,0)} seconds\n")
        ty4="Typing characters with spaces score"
        f.write(f"{ty4.ljust(40)} :  {cs}/30 -- completed in {t1cs//60} minutes {round(t1cs%60,0)} seconds\n")
        ty5="Typing sentences part 1 score"
        f.write(f"{ty5.ljust(40)} :  {s1}/30 -- completed in {t1s1//60} minutes {round(t1s1%60,0)} seconds\n")
        ty6="Typing sentences part 2 score"
        f.write(f"{ty6.ljust(40)} :  {s2}/90 -- completed in {t1s2//60} minutes {round(t1s2%60,0)} seconds\n")
        f.write(f"Status                                   :  Completed\n\n")
        print("\nYour score has been successfully saved into a file named typing-score.txt")
