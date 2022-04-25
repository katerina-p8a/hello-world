hours = input("Enter hours: ")
rate = input("Enter rate: ") 
try:
    fhours = float(hours)
    frate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
    
#print(fhours, frate)
if fhours > 40 :
    rpay = fhours * frate
    opay = (fhours - 40.0) * (frate * 0.5)
    xpay = rpay + opay
else : 
    xpay = fhours * frate
print("Pay: ",xpay)
 