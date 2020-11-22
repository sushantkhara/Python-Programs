# Collect input from the user
# 32 F = 0C, formula: (32F - 32)* 5/9 = 0C
celsius = float(input('Enter temperature in Celsius: '))

# calculate temperature in Fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f  Celsius is equal to %0.1f degree Fahrenheit' % (celsius, fahrenheit))