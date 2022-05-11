# Functions


def computepay(h, r):
  if (h>40):
    p=h*r
    extra=(h-40)*r*0.5
    pay=p+extra
  else :
    pay=h*r
  return pay

hrs = float(input("Enter hours : "))
rte = float(input("Enter rate per hours :"))
p = computepay(hrs, rte)
print("Pay", p)
