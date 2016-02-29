print 'This is a multiplication table\n'
x = input('Enter X : ')
for i in range(1,13):
    total = x*i
    print(str(x)+' * '+str(i)+' = '+str(total))
