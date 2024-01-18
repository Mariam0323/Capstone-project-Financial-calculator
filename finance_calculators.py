
#Python program that allows user to access an investment calculator and a home loan repayment calculator
import math

print (""""
       investment-to calculate the amount of interest you'll earn on your investment
       bond-to calculate the amount you will have to pay on a home loan
       Enter either 'investment' or 'bond' from the menu above to proceed: 
      """ )
calculator=input("Would you like to calculate your investment or bond?: ") 
calculator=calculator.lower() #stops case sensitive errors ie BoNd

if calculator == "investment":
    P=int(input("enter your deposit: "))
    r=int(input("enter the interest rate percentage without symbol, only number eg 4: "))
    t=int(input("enter number of years you plan to investment: "))
    interest=input("Do you want to use simple interest or compound interest?: ")
    interest=interest.lower() #stops case sensitive errors
    
    if interest == "simple":
        A=P*(1+r*t)  #Formulae used to calculate simple interest
        print("simple interest: ", A)
        
    else:
        interest == "compound"
        A=P*math.pow((1+r),t) #Formulae used to calculate compound interest
        print("compound interest: ", A)
        
elif calculator == "bond":
    p=int(input("Enter present value of the house: "))
    i=int(input("Enter the monthly interest rate percentage without symbol, only the number eg 4: "))
    n=int(input("Enter number of months the bond will be repaid: "))
    repayment=(i*p)/(1-(1+i)**(-n))  #Formulae used to calculate monthly loan repayment
    print("repayment per month: ", repayment)
    
else:
    print ("You did not enter investment or bond")