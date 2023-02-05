# This is designed under the assumption that someone is legitimately trying to use this as a tool. 

class Rental_prop():
    def __init__(self, price, income=0, expenses=0):
        self.price = price
        self.income = income
        self.expenses = expenses

    def calc_income(self):
        rent_inc = input("How much will you charge monthly in rent? Enter 'quit' to exit ")
        if rent_inc.lower() != "quit":
            self.income += int(rent_inc)
        else:
            print("Thank you.")
        other_inc = input("How much do you expect to receive monthly in other income from the property? ")
        self.income += int(other_inc)
        print("Your income will be $" + str(self.income) + " per month")

    def calc_expenses(self):
        tax_expense = int(input("How much will you pay annually in property taxes? "))/12
        ins_expense = int(input("How much is your homeowners' insurance per month? "))
        print("\n Let's calculate your utility costs.")
        electric_exp = int(input("How much will you pay in electricity costs each month? If your tenant will pay utilities, enter '0'"))
        water_exp = int(input("How much will you pay in water costs each month? If your tenant will pay utilities, enter '0' $"))
        sewer_exp = int(input("How much will you pay in sewer costs each month? If your tenant will pay utilities, enter '0' $"))
        garbage_exp = int(input("How much will you pay in garbage costs each month? If your tenant will pay utilities, enter '0' $"))
        gas_exp = int(input("How much will you pay in gas costs each month? If your tenant will pay utilities, enter '0' $"))
        utility_exp = electric_exp + water_exp + sewer_exp + garbage_exp + gas_exp
        print(f"\n Your total untility expenses will be ${utility_exp}.")
        print("Now let's calculate your other standard expenses.")
        hoa_exp = int(input("How much will you pay in Home Owners' Association fees per month? $"))
        lawn_exp = int(input("How much will you pay in lawn or snow care expenses each month? $"))
        vacancy = int(input("What percentage would you like to set aside for vacancy expenses? ")) * self.income /100
        repair_saving = int(input("How much would you like to set aside for repairs/maintenance? $"))
        cap_exp = int(input("How much would you like to set aside for major replacements? $"))
        prop_man = int(input("How much would you like to pay a property manager per month? $"))
        mortgage = int(input("What's your estimated monthly mortgage cost? $"))
        self.expenses = tax_expense + ins_expense + utility_exp + hoa_exp + lawn_exp + vacancy + repair_saving + cap_exp + prop_man + mortgage
        print("Your expenses will be $" + str(self.expenses) + " per month")

    def calc_cash_flow(self):
        cash_flow = int(self.income) - int(self.expenses)
        print(f"Your anticipated monthly cash flow will be {cash_flow}.")

    def cash_on_cash_roi(self):
        print("Let's calculate how much you'll put into the front end, first.")
        dollarsdown = input("Will you do a downpayment? Y/N ")
        if dollarsdown.lower() == "y":
            calc_down = input("Will you do the standard 20 percent downpayment? Y/N ")
            if calc_down.lower() == "y":
                downpayment = self.price * .20
            elif calc_down.lower() == "n":
                new_down = input("How much do you plan to put down? ")
                downpayment = int(new_down)
            else:
                print("Please type 'y' or 'n' ")
        else:
            downpayment = 0
        closing_costs = input("How much will your closing costs be? ")
        rehab_costs = input("How much do you anticipate doing in repair or rehab cost? ")
        misc_costs = input("Please enter any other miscellaneous up front costs you anticipate: ")
        total_invest = int(downpayment) + int(closing_costs) + int(rehab_costs) + int(misc_costs)
        print(f'Your total investment up front will be ${total_invest}.')
        print("\n Now let's calculate your annual cash flow.")
        annual_cash_flow = int(input("Please enter your monthly cash flow calculated above. ")) * 12
        print(f"\n Your annual cash flow will be {annual_cash_flow}.")
        coc_roi = (int(annual_cash_flow) / int(total_invest)) * 100
        print(f"Your Cash on Cash Return on Investment will be {coc_roi}%.")

        if coc_roi <= 3.5:
            print("The choice is yours, but this may be a risky investment.")
        elif coc_roi > 3.5 and coc_roi < 10:
            print("The choice is yours, but this seems a pretty safe investment.")
        elif coc_roi >= 10:
            print("There are no guarantees, but this seems like a great investment.")


Invest1 = Rental_prop(150000)
Invest1.calc_income()
Invest1.calc_expenses()
Invest1.calc_cash_flow()
Invest1.cash_on_cash_roi()