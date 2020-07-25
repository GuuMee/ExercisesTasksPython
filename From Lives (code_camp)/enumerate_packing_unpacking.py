names = ['Sam', 'Tom', 'Steve']

# for i in range(len(names)):
#     print(i+1, names[i])

# for i in enumerate(names, start=1):
#     print(i)

# this is fantastic unpacking
for num, name in enumerate(names, start=1):
    print(num, name)