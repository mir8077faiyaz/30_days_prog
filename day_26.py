actual=input().split() #this is the actual date of return
expected=input().split() #this is the expected date of return

# dates are in format dd/mm/yyyy

for i in range(len(actual)):
    actual[i]=int(actual[i])
for i in range(len(expected)):
    expected[i]=int(expected[i])
     

if actual[2]>expected[2]:
    print('10000')
elif actual[2]<expected[2]:
    print('0')
else:
    if(actual[1]>expected[1]):
        val=500 * (actual[1] - expected[1])
        print(val)
    elif(actual[0]>expected[0]):
        val=15 * (actual[0] - expected[0])
        print(val)
    else:
        print('0')
        
    
    
    