# 3) print squre pattern witn * sumbol
n=5
for i in range(n):
  for j in range(n):
     print('*',end=' ')
  print()
  
  
# 2) print a squre pattern with 'A' symbol
n=5
for i in range (n):
    for j in range (n):
        print('A',end='  ')
    print()      

# 4) print squre pattern with given number/digit
n=5
for i in range (n):
   for j in range (n):
      print('5',end='')
   print()
   
# 5) print squre pattern given fixed digit in every row 
n=int (input('enter number of rows:'))
for i in range (n):
   print((str(i+1)+' ')*n)
   
# 6) print squre pattern in descending order
n=int(input('enter the number:'))
for i in range(n):
   print((str(n-i)+' ')*n)
   

