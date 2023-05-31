class Area:
    def find_area(self,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("nothing")
            
obj=Area()
obj.find_area()  
obj.find_area(10)
obj.find_area(10,20)

#overriding

class ol:
    def dispinfo(self,name=''):
        print("this is over"+name)
        
obj=ol()
obj.dispinfo()
obj.dispinfo('python')
    
            
         
            
class overriding:
    def displinfo(self):
        print("this is overriding")
        
class IIP(overriding):
    def displinfo(self):
        super().displinfo()
        print("overriding child class")
        
obj=IIP()
obj.displinfo()        
            




#polymorphism having in many f


l=[10,20,30,555]
print(len(l))
s="welcome in ps"
print(len(s))

class AB :
    def disA(self):
        print("welcome in inheritance")
        
class BC(): 
    def disB(self):
        print("welcome in programming")
class CD(AB,BC):
    def deisC(self):
        print("c hild class ehich is acquring all the classs")
        
obj=CD() 
obj.disA() 
obj.disB()     
        
            
#inheritance

class A:
    def dispalyA(self):
        print("welcome in programming")
        
class B():
    def displayB(self):
        print("child class B")
        
        
class C(A,B):
    def displayC(self):
       print("child class c  which is multilevel")
               
obj=C()
obj.dispalyA()
obj.displayB()
obj.displayC()



#encapsulatio

class encap:
        def __init__(self):
           self.__name=""
        def getname(self):
            return self.__name
        def setname(self,__name):
            name=self.__name
            
obj=encap()
obj.setname("This is checking if testing is working or not")
name=obj.getname()
print(name)




#Basic ENcapsualtion

class encaps:
    __name="veena"
    def __init__(self):
        print(self.__name)  
        self.__displayinfo()
    def __displayinfo(self):
        print("welcome in encaps")
        
obj=encaps()    




class enc:
    __name="pradip"
    def __init__(self):
        print(self.__name)
        self.__displayinf()
    def __displayinf(self):
  
        print("new enc")
obj=enc()
            
            
                   

#remove duplicate

s="Enter the String"
output=''
for ch in s:
    if ch not in output:
        output=output+ch
print(output)

#tring ops 


s="ftech the duplics"
l=[]
for ch in s:
        if ch not in l:
            l.append(ch)
        output=' '.join(l)
print(output)

# S to set




            



string = "Great responsibility";  
   
print("Duplicate characters in a given string: ");  
#Counts each character present in the string  
for i in range(0, len(string)):  
    count = 1;  
    for j in range(i+1, len(string)):  
        if(string[i] == string[j] and string[i] != ' '):  
            count = count + 1;  
            #Set string[j] to 0 to avoid printing visited character  
            string = string[:j] + '0' + string[j+1:];  
   
    #A character is considered as duplicate if count is greater than 1  
    if(count > 1 and string[i] != '0'):  
        print(string[i]);  







# #stack

# l=[]
# while True:
#     c=int(input('''
#                 Push
#                 pop
#                 peek
#                 display
#                 exitI()
                
                
                
#                 '''))
#     if c==1:
#        n=input(("enter the value"))
#        l.append()
#        print(l)
#     if c==2:
#         if len(l)==0:
#             print("Empty stack")
#         else:
#             print(c,"not empty")
#             p=l.pop()
#     #         print(p)
#     #         print(l)
#     #     elif c==3:
#     # if len(1)==0:
                
            
           














# l=[10,20,3,0,4,0,56]
# n=[45,54]
# l.insert(3,55)
# l.append("pradip")
# l.extend(n)
# print(l)
# l[2]=90
# print(l)
# print(l.pop(4))
# stre=l.remove(56)
# print(stre)
# #del l[]
# print(l)


# #appending a date into list
# l=[]
# for i in range(1,4):
#     n=input("enter the value"+str(i)+":-")
#     l.append(n)
#     print(l)



# w="welcome {} to {} wscubetech".format("hello",20);
# print(w)

# x="welcome {1} to {0} wscubetech".format("hello",20);
# print(x)
 
# e="enter the value"
# l=e.split()
# print(l)
 
# w="welcome {b:10} to {a} wscubetech".format(a=30,b=40)
# print(w)



# #
# # ascii
# a=65
# print(chr(a))
# b="K"
# print(ord(b))



# w="Welcome"
# print(w.find('e',2))
# print(w.index('c'))
# print(w.isalpha())

# d="1223 a"
# print(d.isdigit())
# print(d.isalnum())
# n=w.lower()
# u=w.upper()
# t=w.title()
# c=w.capitalize()
# print(n,u,t,c,
#       '''sting functiom''')


# for i in w:
#     print(i)
# t=len(w)
# for i in range(t):
#     print(w[i])






# list=['a1c2b','21ang','92c','451c',2,{"23":"4a3","a":"cd2"}] 

# total = 0
# for item in list:
#     if isinstance(item, int):
#         total += item
#     print(total)
# print(total)
# t=len(list)
# t=sum(list)
# print(t,sum)

# #while
# i=1
# while i<=10:
#     print(i,"welcome to wscubetube")
#     i=i+1    

# for n in range(10,-1,-2):
#   print(n)

# table
# for a in range(1,11):
#     print("2*",a,"=",2*a)




# print('''
      
#       +ADD
#       -SUB
#       *MUtli
#       /Divide
      
#       ''')

# num1=int(input("ente r the value :"))
# num2=int(input("ente r the value :"))
# op=input("enter the opr..(+,-,*,/): ")

# if  op== "+":
#     print(num1+num2)
# elif op== "-":
#     print(num1-num2)
# elif op=="*":
#     print(num1*num2)
# elif op=="/":
#     print(num1/num2)
# else:
#     print("invalid ops")
    
    


# t=(10,20,'hello ')
# print(t,type(t))

# l=[10,"string",5.5]
  
# print(l,type(l))

# # bop
# x=10
# y=8
# print(bin(x))
# print(bin(y))
# print(x&y,bin(x&y))
# print(bin(x|y),x|y)
# print(bin(x^y),x^y)

# #string check
# str2= "thiis is string"

# str1=''''
# this is string
# string is this
# '''

# print(str2,type(str1))
# print(str1,type(str2))



# n=25

# count=0




