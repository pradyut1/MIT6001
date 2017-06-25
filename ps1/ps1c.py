annual_salary=float(input("Enter the starting salary:"))
salary=annual_salary
total_savings=250000
semi_annual_percentage=.07
months=36
steps=0
high=10000
low=0
current_savings=0
if annual_salary<70000:
    print("It is not possible to pay the down payment in three years.")
else:    
    while abs(current_savings-total_savings>100):   
        guess=(high+low)/20000        
        annual_salary=salary
        current_savings=0
        for i in range(1,months+1):
            current_savings+=(guess)*(annual_salary/12)+(current_savings)*(0.04/12)  
            if i%6==0:
                annual_salary=annual_salary*(1+semi_annual_percentage)
        if current_savings>total_savings:
            high=guess*10000
        else:
            low=guess*10000
        steps+=1

    print("Best savings rate: {0:.4f}".format(guess))
    print("Steps in bisection search: {}".format(steps))
    

