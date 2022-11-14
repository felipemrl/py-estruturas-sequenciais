x = input().split(" ")
v1 = float(x[0])
v2 = float(x[1])
v3 = float(x[2])
total = (v1+v2+v3)
dez = total + total/10
print ("%.2f" % (v1+v1/10),"%.2f" % (v2+v2/10),"%.2f" % (v3+v3/10))
print ("%.2f" % dez)
