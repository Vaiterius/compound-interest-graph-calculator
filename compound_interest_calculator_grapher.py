"""
Created on Thur Sept 18 2020

@author: Gerard Gandionco

Calculates and graphs compound interest (NOTE: must have matplotlib installed)
"""
# NOTE: format floats into USD form:
# '${:,.2f}'.format(1234.5) ---> $1,234.50
# (:,) adds comma as thousands separator
# (.2f) limits string to two decimal places (or adds enough zeroes to get to 2)

import matplotlib.pyplot as plt  # Module to graph our results
from time import sleep  # Module to add time delay as effect


def plot_and_table(principal, rate, num_times, time):
    """
    Graphs interest compounded over time given the parameters
    & also prints amount per every year
    """
    year_axis = [year for year in range(1, int(time)+1)]
    amount_axis = []
    table_dict = {}
    print()

    for iter in year_axis:  # Loops over every year and attaches amount to it
        yearly_amount = 0
        yearly_amount += round(calculate(principal, rate, num_times, iter), 2)
        amount_axis.append(yearly_amount)
        table_dict[iter] = yearly_amount  # Adds every iteration to table
        iter_year = f"Year {iter}: {'${:,.2f}'.format(yearly_amount)}"
        print(iter_year)

    # Creates graph from data above
    plt.title("Compounded Amount Over Time")
    plt.xlabel("Number of Years")
    plt.ylabel("Amount (USD)")
    plt.style.use("seaborn")
    plt.plot(year_axis, amount_axis)


def calculate(P, r, n, t):
    """
    FORMULA: A = P(1 + r/n)^nt
    - A is amount calculated, P is principal (initial) amount, r is
    - interest rate (decimal), n is number of times interest is compounded
    - per unit 't', & t is time

    Input: P, r, n, t
    Output: A
    """
    A = P * ((1 + ((r/100)/n))**(n*t))
    return A


def ask():
    """Asks user to input variables for formula, returns calculated result"""
    while True:
        try:
            principal = float(input("\nEnter intial amount: "))
            rate = float(input("\nEnter interest rate (ex: 5 if 5%): "))
            num_times = float(input(
                "\nHow many times compounded per year? (1 if annual): "
                ))
            time = float(input("\nHow many years?: "))
        except ValueError:  # Catches error if user doesn't input numbers
            print("\nPlease enter only numbers unless otherwise asked!")
        else:  # Calculate and plot table and graph if all else is fine
            final_amount = calculate(principal, rate, num_times, time)
            plot_and_table(principal, rate, num_times, time)
            percent_increase = ((final_amount-principal)/principal)*100
            sleep(1)
            print(f"\nWith an increase of {round(percent_increase, 2)}% by \
the end of {time} years...")
            sleep(1)
            return final_amount


def main():
    value = ask()
    print(f"It will amount to {'${:,.2f}'.format(round(value, 2))}")
    sleep(2)
    plt.show()

    # If user wants to do another without running script every time
    while input("\nCalculate another? (Y/N): ").upper() == "Y":
        value = ask()
        print(f"It will amount to {'${:,.2f}'.format(round(value, 2))}")
        sleep(2)
        plt.show()


if __name__ == '__main__':
    print("\nCOMPOUND INTEREST CALCULATOR")
    main()
