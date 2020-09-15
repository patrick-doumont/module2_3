full_name = input('Enter your name separated by spaces:')
names = full_name.strip().split()
print(names)
 
initials = []

for name in names:
    initials.append(name[0])

print("Your initials are:", end=' ')
for i in initials:
    print(f'{i.upper()}', end='')  # I like the f string format better too!
print('')

# This is a comment to test windows GUI app.


# Another way to write the above code (lines 5-8) is below
# with list comprehension; the code reads 'put the first
# element of name into the resulting list for each name in the 
# iterable names (in this case also a list)'
initials = [name[0] for name in names]

# I could also write it like this (though its less desirable)
initials = [my_var_name[0] for my_var_name in names]


# ---------------------------------------------------------------
# Rewriting the whole program combining list comprehension and 
# printing into 1 step
full_name = input('Enter your name separated by spaces: ')
names = full_name.strip().split()
print(names)

print("Your initials are:", end=' ')
print(''.join(name[0].upper() for name in names))


# the join function does just what the name implies:
# give it a list of strings and a string to put between
# each element.  another example below:
my_strs = ['this', 'is', 'a', 'test', 'using', 'join']
print(' * '.join(my_strs))

# output > this * is * a * test * using * join

# ~ Doug
