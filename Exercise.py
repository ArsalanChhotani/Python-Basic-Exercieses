
#Question 2
import cmath

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

d = (b**2) - (4*a*c)

if (d>0):
    sol1 = (-b+cmath.sqrt(d))/(2*a)
    sol2 = (-b-cmath.sqrt(d))/(2*a)
    print('Solutions {0} and {1}'.format(sol1,sol2))
elif (d==0):
    real=(-b/(2*a))
    print("Root is real {0}".format(real))
else:    
    print("Complex roots")

#Question 3
list1 = [12,24,35,24,88,120,155,88,120,155]
print("Repetition ",len(list1))
set1 = set(list1)
print("No repetitiion",len(set1))

#Question 4
new_list = [12,24,35,24,88,120,155,88,120,155]
new_set = set(new_list)
print(new_set)  