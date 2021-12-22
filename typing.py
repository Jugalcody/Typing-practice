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
                                            

print(f"\nCongratulation {name}, you have successfully completed the first level\n")
time.sleep(2)
print("type words part 1")
w1=0

n=1               
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
                     
print(f"\nCongratulation {name}, you have successfully completed the second level\n")
time.sleep(2)
print("type words part 2\n")
w2=0
            
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
                        
print(f"\nCongratulation {name}, you have successfully completed the third level\n")

time.sleep(2)
print("type characters with spaces....\n")                     
n=1             
cs=0  
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
   
    
print(f"\nCongratulation {name}, you have successfully completed the fourth level\n")

time.sleep(2)
print("type sentences part 1\n")                     
n=1    
s1=0           
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

    
print(f"\nCongratulation {name}, you have successfully completed the fifth level\n")
s2=0
time.sleep(2)
print("type sentences part 2...\n")                     
n=1               
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
print(f"\nCongratulation {name}, you have successfully completed the sixth level\n")
print(".....\n\n")
time.sleep(2)
print(f"\n\n{name}, have you noticed that your performance has been improved and become more better than earlier...Congratulation!!!!\n\n")
import mysql.connector as mycon
mm=mycon.connect(host="localhost",user="jugal",password="Jugal2002@")
cursor=mm.cursor(buffered=True)
cursor.execute("create database if not exists typing")
cursor.execute("use typing")
cursor.execute("create table if not exists score ( sno varchar(100),Name varchar(100),character1(40) varchar(200),words_part1(60) varchar(100),words_part2(90) varchar(100),character_with_spaces(30) varchar(100),sentence_part1(30) varchar(100),sentence_part2(90) varchar(100),status varchar(100))")

cursor.execute("select * from score order by sno desc")
aa=cursor.fetchone()

if aa is None:
       k=0
else:
       k=int(aa[0])
print(k)
bb="completed"         
a="insert into score values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
b=(str(k+1),str(name),str(c1),str(w1),str(w2),str(cs),str(s1),str(s2),str(bb))
cursor.execute(a,b)
mm.commit()

