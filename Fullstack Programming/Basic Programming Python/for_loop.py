# for loop is repeated a task of statement over a group of values
# for variableName in groupOfValues
# statement

print('Basic Loop: ')
for x in range(1, 6):
    print(x, "squared is", x * x)

for y in range(5, 0):  # won't work
    print(y)

print('Cumulative Loop: ')
sum = 0
for i in range(1, 11):
    sum = sum + (i * i)
print('sum of first 10 is ', sum)
