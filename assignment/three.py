# 7) print right angle with *'' symbol
n=int(input('enter the number of rows:'))
for i in range (n):
    #for j in range(1,i+1):
        print('*'*(i+1))
  
# 8) print right angle tringle with 'A' symbol
n=int (input('enter the number of rows:'))
for i in range (n):
    print('A'*(i+1))
    
     
# 9)print the reverse right angle tringle with '*' symbol
n=int(input('enter the number of rows:'))
for i in range (n):
    print('*'*(n-i))

# 10) print right angle triangle with fixed  alphabat symbol
n=int (input('enter the number of rows:'))
for i in range(n):
    print((chr(65+i)+' ')*(i+1))
    
# 11) print right angle triangle with fixed digit symbol in every row
n=int(input('enter the number of row:'))
for i in range (n):
   print(str(i+1)*(i+1))
   
# 12)print right angle tringle with sequence of digits each row
n=int(input('enter the number of rows:'))
for i in range(n):
    for j in range(i+1):
        print(j+1,end= '')
    print()
    
# 13) write a right angle with sequence of alphabate each row    
n=int(input('enter the number of rows:'))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=' ')
    print()    
      
# 14) print inverted right angle tringle using number
n=int(input('enter the number of rows:'))
for i in range(n):
    for j in range(n-i):
        print(j+1,end=' ')
    print()
    
# 15)print a python program of hallow squre pattern of star
n=int(input('enter the number of rows and col:'))
for i in range(n):
  for j in range(n):
     if i==0 or i==n-1 or j==0 or j==n-1:
        print("*",end="")
     else:
        print(" ",end="")
  print()      
# print  a pyhton  program inverted right angle triangle with sequence of alphabets       
n=int(input('enter the number of rows:'))
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end=' ')
    print()    
    
    
    
    
    
    
    
