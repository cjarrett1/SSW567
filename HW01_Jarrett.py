'''
Created on Sep 1, 2019

@author: Craig Jarrett
SSW-567-WS
HW01
'''
def main():
    print("Input the length of each side of the triangle: ")
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    return a,b,c
    
def classifyTriangle(a,b,c):    
    
    a_int = isinstance(a,int)
    b_int = isinstance(b,int)
    c_int = isinstance(c,int)
    
    if a_int == False or b_int == False or c_int == False:
        return 'Some or all of the values are not integers'
    
    elif a == b == c:
        return 'Equilateral triangle'
        
    elif a==b or b==c or c==a:
        return 'Isosceles triangle'
        
    else: 
        return 'Scalene triangle'

def rightTriangle(a,b,c):
    a_sq = int(a*a)
    b_sq = int(b*b)
    c_sq = int(c*c)
    
    if (a_sq + b_sq == c_sq):
        print('Right Triangle')
    else:
        print('Not a Right Triangle')
        
a,b,c = main()
result = classifyTriangle(a,b,c)
print(result)
rightTriangle(a,b,c)

     


