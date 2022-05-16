# Loops & Iterators

#largest = None
#smallest = None
'''a=[]
while True:
    num = input("Enter a number : ")

    if num == "done":
        break
    try:
      x=int(num)
      a.append(x)
      continue
    except:
      print("Invalid input")
b=max(a)
c= min(a)
print("Maximum", b)
print("Minmum", c)'''

#*************************************************

largest= None
smallest=None
while True:
  x=input("Enter the no :")
  if (x == "done"):
    break
  try :
    n=int(x)
    if largest is None:
      largest=n
    elif (largest<n):
      largest=n
    if smallest is None:
      smallest=n
    elif (smallest>n):
      smallest=n
  except:
    print("Invalid input")
print("Largest ->",largest)
print("Smallest ->",smallest)
