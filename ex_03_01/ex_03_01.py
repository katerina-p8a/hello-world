hours = input("Enter hours: ")
rate = input("Enter rate: ") 
fhours = float(hours)
frate = float(rate)
# print(fhours, frate)
if fhours > 40 :
    # print("Overtime")
    rpay = fhours * frate
    opay = (fhours - 40.0) * (frate * 0.5)
    # print (rpay,opay)
    xpay = rpay + opay
else : 
    # print("Regular")
    xpay = fhours * frate
print("Pay: ",xpay)
