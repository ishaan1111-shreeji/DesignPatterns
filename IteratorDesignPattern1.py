# printing fibonnaci series upto n without using iterator

import time

def fibonacci():
   a, b = 0, 1
   while True:
      yield b
      a, b = b, a + b

fib = fibonacci()

try:
   for i in fib:
      print(i)
      time.sleep(1)

except KeyboardInterrupt:
   print("Calculation stopped")