# num=55
# for n in range(2,num):缩小范围：判断prime number仅需判断一个因数小于平方根
#     if  num%n==0:
#      print(f"{num}不是prime number!")
#      break  
# else:
#      print(f"{num}是prime number!!")
num=89
if num<=1:
  print(f"{num}不是prime number!")
else:
  for n in range(2,int(num**0.5)+1):
    if num%n==0:
      print(f"{num}不是prime number!!!")
      break
  else:#for-else结构而不是if-else结构
      print(f"{num}是prime number!")
