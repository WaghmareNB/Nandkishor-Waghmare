n=153
cubsum=0
temp =n
while n>0:
    rem= n%10
    cube = rem * rem * rem
    cubsum = cubsum + cube
    n = n // 10
if temp == cubsum:
     print("no is almanstron")
else:
    print("no is  not almanstrong")