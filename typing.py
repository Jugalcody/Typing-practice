import random as r
import time
print("\nTyping practice.....\n\n")
time.sleep(2)
print("\nType character...\n")
i=0
while i<=20:           
           
           v=r.randint(97,122)
           h=chr(v)
           print("\n",h,"\n")
           a=input(f"Enter {i+1}/20 chr : ")
           if a==h:
                     i=i+1
                                            

print("\nCongratulation, you have successfully completed the first level\n")
time.sleep(2)
print("type character.....")

n=1               
while n<=30:
        v=r.randint(2,3)
        d=""
        for i in range(v):
            m=r.randint(97,122)
            
            d=d+chr(m)
        print("\n",d,"\n")    
        c=input(f"Enter {n}/30 string : ")              
        if c==d:
                 n=n+1                          
                     
print("\nCongratulation, you have successfully completed the second level\n")
time.sleep(2)
print("Third level..\n")                     
n=1               
while n<=60:
        v=r.randint(5,8)
        d=""
        for i in range(v):
            m=r.randint(97,122)
            
            d=d+chr(m)
        print("\n",d,"\n")    
        c=input(f"Enter {n}/60 string : ")              
        if c==d:
                 n=n+1  
                        
print("\nCongratulation, you have successfully completed the levels\n")
    
    

    

