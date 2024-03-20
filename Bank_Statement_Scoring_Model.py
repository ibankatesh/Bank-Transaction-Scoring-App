import streamlit as st



def calculate_interest_received_amount_score(interest_received_amount):
    if interest_received_amount < 13.57:
        return 2.5 * 2
    elif 13.57 <= interest_received_amount <= 27.143:
        return 5.0 * 2
    elif 27.143 < interest_received_amount <= 81.42:
        return 7.5 * 2
    else:
        return 10.0 * 2

def calculate_eod_balance_score(eod_balance):
    if eod_balance <= 3290:
        return 0.0 * 3
    elif 3290 < eod_balance <= 7416:
        return 2.0 * 3
    elif 7416 < eod_balance <= 11541:
        return 4.0 * 3
    elif 11541 < eod_balance <= 32175:
        return 6.0 * 3
    elif 32175 < eod_balance <= 53301:
        return 8.0 * 3
    else:
        return 10.0 * 3

def calculate_total_of_bank_charges_score(total_of_bank_charges):
    if total_of_bank_charges <= 10:
        return 10.0 * 2
    elif 10 < total_of_bank_charges <= 18.8:
        return 8.0 * 2
    elif 18.8 < total_of_bank_charges <= 37.76:
        return 6.0 * 2
    elif 37.7 < total_of_bank_charges <= 94.4:
        return 4.0 * 2
    elif 94.4 < total_of_bank_charges <= 188.8:
        return 2.0 * 2
    else:
        return 0.0 * 2

def calculate_card_settlement_score(card_settlement_amount):
    if card_settlement_amount <= 0 or card_settlement_amount == "":
        return 3.3
    elif card_settlement_amount < 13841:
        return 6.6
    else:
        return 10.0

def calculate_cash_withdrawals_score(cash_withdrawals_amount):
    if cash_withdrawals_amount == 0:
        return 10.0
    elif 0 < cash_withdrawals_amount <= 11071:
        return 7.5
    elif 11071 < cash_withdrawals_amount <= 33214:
        return 5.0
    else:
        return 2.5

def calculate_salary_account_score(is_salary_account):
    return 10.0 if is_salary_account == "Y" else 5.0

def calculate_total_no_of_bank_charges_score(total_no_of_bank_charges):
    if total_no_of_bank_charges == 0:
        return 10.0
    elif 0 < total_no_of_bank_charges <= 0.625:
        return 6.6
    else:
        return 3.3

def calculate_max_eod_balance_score(max_eod_balance):
    if max_eod_balance < 14251:
        return 2.0 * 2
    elif 14251 <= max_eod_balance < 33752:
        return 4.0 * 2
    elif 33752 <= max_eod_balance < 43492:
        return 6.0 * 2
    elif 43492 <= max_eod_balance < 136054:
        return 8.0 * 2
    else:
        return 10.0 * 2

def calculate_investment_score(total_investment):
    if total_investment == 0:
        return 3.3
    elif 0 < total_investment <= 0.7:
        return 6.6
    else:
        return 10.0

def calculate_ecs_nach_transaction_score(total_ecs_nach_transactions):
    if total_ecs_nach_transactions == 0:
        return 3.3
    elif 0 < total_ecs_nach_transactions <= 1:
        return 6.6
    else:
        return 10.0

def calculate_atm_transaction_score(atm_transaction_percentage):
    if atm_transaction_percentage == 0:
        return 10.0
    elif 1 <= atm_transaction_percentage <= 6:
        return 7.5
    elif 7 <= atm_transaction_percentage <= 14:
        return 5.0
    else:
        return 2.5

def calculate_digital_debit_transaction_score(digital_debit_percentage):
    if digital_debit_percentage < 60:
        return 3.3
    elif 60 <= digital_debit_percentage <= 80:
        return 6.6
    else:
        return 10.0

def calculate_utility_bill_transaction_score(utility_bill_transaction_amount):
    if utility_bill_transaction_amount == 0:
        return 2.5
    elif utility_bill_transaction_amount < 471:
        return 5.0
    elif 471 <= utility_bill_transaction_amount <= 1178:
        return 7.5
    else:
        return 10.0

def calculate_emi_amount_score(emi_amount):
    if emi_amount < 0:
        return 2.5
    elif emi_amount < 7059:
        return 5.0
    elif 7059 <= emi_amount <= 20663:
        return 7.5
    else:
        return 10.0

def calculate_salary_over_sanction_score(salary_over_sanction_percentage):
    if salary_over_sanction_percentage <= 2:
        return 2.5 * 2
    elif 2 < salary_over_sanction_percentage <= 6:
        return 5.0 * 2
    elif 6 < salary_over_sanction_percentage <= 11:
        return 7.5 * 2
    else:
        return 10.0 * 2

def main():
    st.title("Bank Transaction Scoring App")



    # Add Streamlit widgets for user input
    interest_received_amount = st.number_input("Interest Received Amount", value=35.00)
    eod_balance = st.number_input("EOD Balance", value=8000)
    total_of_bank_charges = st.number_input("Total of Bank Charges", value=0.3)
    card_settlement_amount = st.number_input("Card Settlement Amount", value=15000)
    cash_withdrawals_amount = st.number_input("Cash Withdrawals Amount", value=20000)
    is_salary_account = st.radio("Is Salary Account?", ('Y', 'N'))
    total_no_of_bank_charges = st.number_input("Total No. of Bank Charges", value=15)
    max_eod_balance = st.number_input("Maximum EOD Balance", value=25000)
    total_investment = st.number_input("Total No. of Investment", value=0.8)
    total_ecs_nach_transactions = st.number_input("Total No. of ECS/NACH Transactions", value=3)
    atm_transaction_percentage = st.number_input("ATM transactions over total debit - Amt (%)", value=8)
    digital_debit_percentage = st.number_input("Digital Debit transaction %", value=75)
    utility_bill_transaction_amount = st.number_input("Total of Utility Bill Transaction Amount", value=800)
    emi_amount = st.number_input("Total of EMI Amount", value=18000)
    salary_over_sanction_percentage = st.number_input("Salary over sanction amount (%)", value=50)

    # Calculate scores based on user inputs
    interest_received_amount_score = calculate_interest_received_amount_score(interest_received_amount)
    eod_balance_score = calculate_eod_balance_score(eod_balance)
    total_of_bank_charges_score = calculate_total_of_bank_charges_score(total_of_bank_charges)
    card_settlement_score = calculate_card_settlement_score(card_settlement_amount)
    cash_withdrawals_score = calculate_cash_withdrawals_score(cash_withdrawals_amount)
    salary_account_score = calculate_salary_account_score(is_salary_account)
    total_no_of_bank_charges_score = calculate_total_no_of_bank_charges_score(total_no_of_bank_charges)
    max_eod_balance_score = calculate_max_eod_balance_score(max_eod_balance)
    investment_score = calculate_investment_score(total_investment)
    ecs_nach_transaction_score = calculate_ecs_nach_transaction_score(total_ecs_nach_transactions)
    atm_transaction_score = calculate_atm_transaction_score(atm_transaction_percentage)
    digital_debit_transaction_score = calculate_digital_debit_transaction_score(digital_debit_percentage)
    utility_bill_transaction_score = calculate_utility_bill_transaction_score(utility_bill_transaction_amount)
    emi_amount_score = calculate_emi_amount_score(emi_amount)
    salary_over_sanction_score = calculate_salary_over_sanction_score(salary_over_sanction_percentage)

    # Sum of individual scores
    final_score = (interest_received_amount_score + eod_balance_score + total_of_bank_charges_score +
                   card_settlement_score + cash_withdrawals_score + salary_account_score +
                   total_no_of_bank_charges_score + max_eod_balance_score + investment_score +
                   ecs_nach_transaction_score + atm_transaction_score +
                   digital_debit_transaction_score + utility_bill_transaction_score +
                   emi_amount_score + salary_over_sanction_score)

    # Display the final score in Streamlit
    st.write("Final Score:", final_score)

if __name__ == "__main__":
    main()