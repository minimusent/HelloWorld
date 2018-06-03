

def calcMonthlyPmt(salePrice, downPmt, intRate, term):

    loanAmount = salePrice - downPmt
    monthlyInt = intRate/100/12
    monthlyPmt = loanAmount * (monthlyInt * (1 + monthlyInt) ** term) / ((1 + monthlyInt) ** term - 1)

    return monthlyPmt

def calcTotalPmt(monthlyPmt, term):
    return monthlyPmt * term


def main():
    print("Welcome to the Mortgage Calculator! \n")
    salePrice = float(input("Sale Price: "))
    downPmt = int(input("Down payment: "))
    intRate = float(input("Annual interest rate: "))
    print("Available actions:\nM = monthly payment\nT = total payment")
    print("I = interest paid")
    action = input("What would you like to calculate? \n")
    term = 360
    monthlyPmt = calcMonthlyPmt(salePrice, downPmt, intRate, term)
    print("$" + str(round(monthlyPmt, 2)))
    print("Total payment: $" + str(round(calcTotalPmt(monthlyPmt, term), 2)))

main()
