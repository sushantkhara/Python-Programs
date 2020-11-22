# Big O Notation is the Asymptotic notation used for Asymptotic Analysis i.e it tells how long a program takes to
# run and deliver output.
list1 = ['nemo', 'dory', 'bruce', 'holly']
print(list1[0])
print(list1[1])  # these two inputs takes O(1) time to produce output individually
for i in range(len(list1)):
    if list1[i] == "nemo":
        print("Nemo is found at:", list1.index("nemo"))
# it take O (n) i.e it takes n no time to perform operations on n no of inputs
# its linear time, O(1) --> it takes constant time to perform operations on any no. of inputs.

