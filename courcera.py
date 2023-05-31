def computepay(h,r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p
    
hrs = input("Enter Hours:")
hr = float(hrs)
rphrs = input("Enter rate per hour:")
rphr = float(rphrs)

p = computepay(hr,rphr)
print("Pay",p)


def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')



def func(x) :
    print(x)

func(10)
func(20)

def thing():
    print('Hello') 

print('There')

astr = 'Hello Bob'
istr = int(astr)
astr = '123'
istr = int(astr)
print('Second', istr)


x=-2
if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')

x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')


x=6

if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')

x = 1 + 2 * 3 - 8 / 4
print(x)
a=10
b=20
print(20*45)
print(10%3)
#arthematic
print(5**2)
print(5**3)
print(10//3)
#Assignment


x=5
print(x)

x=x+5
print(x)

x+=5
print(x)

x=x-5
print(x)

#comparison

x=100
y=20
if x==10:
    print(x)
print(x,"not")    
print(x!=y)
print(x>y)


x=0
if x<2:
    print("small")
elif x<10:
    print("meduim")
else:
    print("large")
print("all done")    



i='123'
try:
    print(int(i))
except:
    i="ps"
print("this try")
print("all is well")

