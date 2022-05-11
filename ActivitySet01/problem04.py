# Conditional Execution

hrs = int(input("Enter hours : "))
rate=float(input("Enter rate :"))
if (hrs>40):
  p=hrs*rate
  extra=(hrs-40)*rate*0.5
  pay=p+extra
else :
  pay=hrs*rate
  
print("pay :",pay)


