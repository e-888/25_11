a1=int(input("введите первое число"))
b1=int(input("введите второе число"))
a=a1//100
b=b1//100
a_str=str(a)
b_str=str(b)
##
if a1<int(a_str+a_str[::-1]):
  print(a_str+a_str[::-1])
##
for i in range(a+1,b):
  print(str(i)+str(i)[::-1])
##
if b1>int(b_str+b_str[::-1]):
  print(b_str+b_str[::-1])


