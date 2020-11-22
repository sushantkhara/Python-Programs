# without using third or temp variable
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))
print("Before Swap:", x, y)
x = x+y
y = x-y
x = x-y
print("After Swap:", x, y)
'''
Python swap program using temp or third variable   
x = input('Enter value of x: ')  
y = input('Enter value of y: ')  
  
# create a temporary variable and swap the values  
temp = x  
x = y  
y = temp  
  
print('The value of x after swapping: {}'.format(x))  
print('The value of y after swapping: {}'.format(y))  
'''

