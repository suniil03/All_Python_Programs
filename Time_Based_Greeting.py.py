import time 
TimeNow = time.strftime('%H:%M:%S')
print('Current Time is: ' ,TimeNow)

''' 
1. Hour = time.strftime('%H')
- This Hour variable is a string so we will convert it to integer by typecasting
2.print(type(Hour))
- Check type of Hour Varibale
'''

Hour = int(time.strftime('%H'))
print('Current Hour is: ' , Hour)

if 5 <= Hour < 12:
    print('Good Morning!')
elif 12 <= Hour < 17:
    print('Good Afternoon!')
elif 17 <= Hour < 21:
    print('Good Evening!')
else:
    print('Good Night!')