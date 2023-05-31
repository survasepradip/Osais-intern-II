#python function

inte=41
print("print the absoulute int value",abs(int))

floate=20.45
print("print the absokute float valut",abs(float))


compile=(3 + 7j)
print(type(compile))

allfinc=[1,2,45,54]
print(all(allfinc))

k=[0,False,5]
print(all(k))

#bin
b=10
y=(bin)
print(y)

#bool 

test=[]
print(test,'is',bool(test))

test1=[0]
print(test1,'is',bool(test1))











# #bikeshop
# import sqlite3
# conn=sqlite3.connect("sqlite.db")
# conn.execute('''
#              Create table studemt(
#                 st_id INT AUTO_INCREMENT PRIMAry KEY,
#                 st_name VARCHAR(50),
#                 st_calss VARCHAR(10),
#                 st_cont VARCHAR(30)
                 
#                )
             
#             ''')
# conn.close()

# ins= '''
#     insert into student(st_name,st_class,st_cont)VALUES
#     ("pradp","MCA-ll","7620739623")

# '''

# conn.execute(ins)
# conn.commit()
# conn.close()




# class bikeshop:

#     def __init__(self, stock):
#         self.stock = stock

#     def displayBikes(self):
#         print("Total bikes", self.stock)

#     def rentbike(self, q):
#         if q <= 0:
#             print("enter posive or greater than zero q value")
#         elif q > self.stock:
#             print("Enter the value (less then Stock) ")
#         else:
#             self.stock=self.stock
#             print("Total prices", q*100)
#             print("Total bikes", self.stock)


# while True:
#     obj = bikeshop(100)
#     uc = int(input('''
#                     Display bikes
#                     rent bike
#                     exit :     
#                      : '''))
#     if uc == 1:
#      obj.displayBikes()
#     elif uc == 2:
#           n = int(input("Enter the qty:--"))
#           obj.rentbike(n)
#     else:
#       break
  
  
  
  
  
                    
                 
                    


            
        
    