
P=int(input("enter principal amount:"))
R=int(input("enter rate of interest per annum:"))
MR=R/(12*100)       #monthly rate of interest 
N=int(input("enter the number of installments:"))
EMI=(P*MR*(1+MR)**N)/(((1+MR)**N)-1)
print("\tEMI calculation")
print("Principal Amount:",P)
print("Rate of Interest(per annum):",R)
print("Number of installments:",N)
print("EMI amount:",EMI)
