full_name = input('Enter your name separated by spaces:')
names = full_name.strip().split()
print(names)

initials = []

for name in names:
	initials.append(name[0])

print("Your initials are:", end=' ')
for i in initials:
	print(f'{i.upper()}', end='')
print('')

# This is a comment to test windows GUI app.
