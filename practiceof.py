num=25
count=0

if num>1:
   for i in range (1,num+1):
       if(num%i) == 0:
           count=count+1
           if count ==2:
              print("prime") 
           else:
               print("NOt Prime")
               
               
               
               
n=int(input("enter The number"))
count=0

if n>1:
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
            if count==2:
                print(n,"is prime number")
            else:
                print(n,"It is Not prime number")            
               
               
               
num=45
coount=4

if num>1:
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
            if count==2:
                print("Primr nUmber")
            else:
                print("Not prime")                                  
               
 ###\NEw line 5! = 1*2*3*4*5=120n
 
 #new line 5!
 

 
 
factorial=1
num1=5
 
if num<0:
     print("fctorial does not exixt for neg numbwer")
elif num1==0:
     print("the factorial of 0 is 1")
else:
     for i in range(1,num+1):
         factorial=factorial*i
         print("hte factorial od", num1,"is",factorial)
        

                                    
         
         
 # recursive
 
 
factorialsss=1
nums=5

if nums<0:
    print("factorail;am doesnt exist")
elif num==0:
    print("the factorial of is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial is",nums,"its new",factorialsss,"kkkk",end='\n')
        
        
def factorialss(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorialss(n-1)  
    #return if(n==0 or n==1) else n*factorialss(n-1)  
num=25
print("factoria; of", num, "is",factorialss(num))  


#febbonan
n11=0
n22=1

print(n11)
print(n22)


for i in range(2,10):
    sum = n11+n22
    print(sum)
    n11=n22
    n22=sum
    
#array 
arr=[1,2,3,4,5]
print(sum(arr))   




a=10
b=20
a=b
b=a
print(a)
print(b)


    
        
 
               
           