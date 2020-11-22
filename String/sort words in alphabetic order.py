'''my_str = input("Enter a string: ")
# breakdown the string into a list of words
words = my_str.split()
# sort the list
words.sort()
# display the sorted words
for word in words:
   print(word)'''

   # To sort characters in a string
a = 'ZENOVW'
b = sorted(a)
print(b) # it gives output: ['E', 'N', 'O', 'V', 'W', 'Z']
# sorted returns a list, so you can make it a string again using join:
c = ''.join(b)
# which joins the items of b together with an empty string '' in between each item.
print(c) # gives output: 'ENOVWZ'

# To Sort letters and make them distinct:
s = "Bubble Bobble"
print(''.join(sorted(set(s.lower())))) # it gives output: ' belou'

# To Sort letters and make them distinct while keeping caps:
s = "Bubble Bobble"
print(''.join(sorted(set(s)))) # It gives output: ' Bbelou'

# To Sort letters and keep duplicates:
s = "Bubble Bobble"
print(''.join(sorted(s)))  # It gives output: ' BBbbbbeellou'

# If you want to get rid of the space in the result, add strip() function in any of those mentioned cases:
s = "Bubble Bobble"
print(''.join(sorted(set(s.lower()))).strip())  # it gives output: 'belou'
