n = int(input())

count = 99
nums = [str(x) for x in range(100, n+1)]

if n <= 99:
   print(n)
else:
   if n == 1000:
      print(144)
   else:
      for num in nums:
         if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
            count+= 1
      
      print(count)