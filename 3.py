a=input("введите число")
first_h=a[0:len(a)//2]
second_h=""
if len(a)%2==0:
  second_h=a[len(a)//2:]
else:
  second_h=a[len(a)//2+1:]
if first_h==second_h[::-1]:
  print("это палиндром")
else: 
  print("это не палиндром")


