annual_salary=float(input("Enter your annual salary:"))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost=float(input("Enter the cost of your dream home: "))

current_savings=0.00
months=0

while current_savings<0.25*total_cost:
    current_savings+=(portion_saved)*(annual_salary/12)+(current_savings)*(0.04/12)  
    months+=1

print("Number of months: {}".format(int(months)))