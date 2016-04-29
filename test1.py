print ('This is a multiplication table\n')
x = int(input('Enter x : ')) 
for i in range(1,13):
    total = x*i
    print ('%d * %d = %d' %(x,i,total))
