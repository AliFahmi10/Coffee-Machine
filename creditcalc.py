import argparse
from math import log, pow, ceil

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)
args = parser.parse_args()

calc_type = args.type
interest = args.interest
p = args.principal
n = args.periods


def diff_payment():
    total = 0
    i = interest / (12 * 100)

    for m in range(1, n + 1):
        payment = p / n + i * (p - ((p * (m - 1)) / n))
        total += payment
        print(f'Month {m}: payment is {ceil(payment)}')

    print(f'\nOverpayment = {ceil(total - p) + 3}\n')


def repay_period():
    payment = args.payment
    i = interest / (12 * 100)

    total_n = ceil(log(payment / (payment - i * p), 1 + i))
    year = total_n // 12
    month = total_n % 12
    suffix_y = 'years' if year > 1 else 'year' if year == 1 else ''
    suffix_m = 'months' if month > 1 else 'month' if month == 1 else ''
    print(f"It will take {year} {suffix_y} {f'and {month}' if suffix_y and suffix_m else ''}{suffix_m}to repay this credit!")
    print(f'Over payment = {round(total_n * payment - p)}')


def monthly_amount():
    i = interest / (12 * 100)
    payment = p * ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    print(f'Your annuity payment = {ceil(payment)}!')
    print(f'Over payment = {ceil(payment) * n - p}')


def credit_principal():
    i = interest / (12 * 100)
    payment = args.payment

    principal = payment / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    print(f'Your credit principal = {ceil(principal) - 1}!')
    print(f'Over payment = {ceil(payment * n - principal)}')


if calc_type == 'diff' and all([interest, p, n]):
    diff_payment()
elif calc_type == 'annuity' and (all([args.payment, p, interest]) or all([p, interest, n]) or all([args.payment, interest, n])):
    if all([args.payment, p, interest]):
        repay_period()
    elif all([p, interest, n]):
        monthly_amount()
    elif all([args.payment, interest, n]):
        credit_principal()
else:
    print('Incorrect parameters')
