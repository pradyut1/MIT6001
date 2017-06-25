annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost=float(input("Enter the cost of your dream home: "))
semi_annual_percentage=float(input("Enter the semiannual raise, as a decimal:"))

current_savings=0.00
months=0

while current_savings<0.25*total_cost:
    current_savings+=(portion_saved)*(annual_salary/12)+(current_savings)*(0.04/12)  
    months+=1
    if months%6==0:
        annual_salary=annual_salary*(1+semi_annual_percentage)

print("Number of months: {}".format(int(months)))