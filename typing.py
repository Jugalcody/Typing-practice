import random as r
import time
print("\nTyping practice.....\n\n")
time.sleep(2)
print("Use the general method to type.....\n\n")
time.sleep(1)
print("\nType characters...\n")
i=1
while i<=40:           
           
           v=r.randint(97,122)
           h=chr(v)
           print("\n",h,"\n")
           a=input(f"Enter {i}/40 chr : ")
           if a==h:
                     i=i+1
                                            

print("\nCongratulation, you have successfully completed the first level\n")
time.sleep(2)
print("type words part 1")

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
                     
print("\nCongratulation, you have successfully completed the second level\n")
time.sleep(2)
print("type words part 2\n")                     
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
                        
print("\nCongratulation, you have successfully completed the third level\n")

time.sleep(2)
print("type characters with space....\n")                     
n=1               
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
                 
   
    
print("\nCongratulation, you have successfully completed the fourth level\n")

time.sleep(2)
print("type sentences part 1\n")                     
n=1               
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
                 

    
print("\nCongratulation, you have successfully completed the fifth level\n")

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

print("\nCongratulation, you have successfully completed the sixth level\n")
print(".....")
time.sleep(2)
print("\n\n{name}, have you noticed that your performance has been improved and become better than earlier...Congratulation!!!!")
                  
