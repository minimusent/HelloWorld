

def calcMonthlyPmt(salePrice, downPmt, intRate, term):

    loanAmount = salePrice - downPmt
    monthlyInt = intRate/100/12
    monthlyPmt = loanAmount * (monthlyInt * (1 + monthlyInt) ** term) / ((1 + monthlyInt) ** term - 1)

    return monthlyPmt

def calcTotalPmt(monthlyPmt, term):
    return monthlyPmt * term

def actionSelector(action, monthlyPmt, term):
    action = action.lower()
    if action == "t":
        print("Total payment: $" + str(round(calcTotalPmt(monthlyPmt, term), 2)))
    elif action == "m":
        print("$" + str(round(monthlyPmt, 2)))
    elif action == "i":

def main():
    print("Welcome to the Mortgage Calculator! \n")
    salePrice = float(input("Sale Price: "))*1.00
    downPmt = float(input("Down payment: "))*1.00
    intRate = float(input("Annual interest rate: "))
    term = 360
    getAction(salePrice, downPmt, intRate, term)

def getAction(salePrice, downPmt, intRate, term):
    print("\nSale price: $" + str(round(salePrice, 2)))
    print("Down Payment: $" + str(round(downPmt, 2)))
    print("Interest Rate: " + str(intRate)+"%")
    print("Term: " +str(term) +" (months), " + str(term/12) + " (years)\n")
    print("Available actions:\nM = monthly payment\nT = total payment")
    print("I = interest paid")
    monthlyPmt = calcMonthlyPmt(salePrice, downPmt, intRate, term)
    action = input("What would you like to calculate? \n")
    actionSelector(action, monthlyPmt, term)
    getAction(salePrice, downPmt, intRate, term)

main()
