# Declare and initialize variables.
employeeName = None
numShifts = None
numTrans = None
valTrans = None
prodScore = None

#Employee Name
print("Enter Employee Name:")
employeeName = input()
# Number of transactions.
print("Enter number of transactions:")
numTrans = input()
# Employee transactions dollar value.
print("Enter transaction dollar value:")
valTrans = input()
# number of shifts worked.
print("Enter number of shifts worked:")
numShifts = input()
# Calculate productivity score.
prodScore = (int(valTrans)/int(numTrans))/int(numShifts)

if int(prodScore) <= 30:
    print("Employee Name: " + employeeName)
    print("Employee Bonus: $50.00")
elif int(prodScore) >= 200:
    print("Employee Name: " + employeeName)
    print("Employee Bonus: $200.00")
elif int(prodScore) <= 199 or int(prodScore) >= 70:
    print("Employee Name: " + employeeName)
    print("Employee Bonus: $100.00")
elif int(prodScore) <= 69 or int(prodScore) >= 31:
    print("Employee Name: " + employeeName)
    print("Employee Bonus: $75.00")

