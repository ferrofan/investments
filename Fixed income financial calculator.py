contribution = float(input('Insert your monthly contribution: '))
v_ini0 = float(input('Insert your initial contribution: '))
n = int(input('Insert time of your application in months: '))
i_a_a = float(input('Insert your fixed income yearly rentability in % per year: '))
i_a_m = ((i_a_a * 0.01 + 1) ** (1 / 12) - 1) * 100
vf = v_ini0

for x in range(1, n + 1):
    v_ini = vf
    R = v_ini * i_a_m * 0.01
    vf = v_ini + contribution + R
    if x == 1:
        print(f'$ {vf:,.2f} after 1 month')
    if x > 1:
        print(f'$ {vf:,.2f} after {x} months')
    remainder = x % 12
    if remainder == 0 and x == 12:
        print(f'\nYou amassed $ {vf:,.2f} after 1 year\n')
    if remainder == 0 and x != 12:
        print(f'\nYou amassed $ {vf:,.2f} after {x/12} years\n')

total_contribution = contribution * n + v_ini0
yield_fi = vf - total_contribution
print(f'\nO valor final é: $ {vf:,.2f}')
print(f'Total contribution: $ {total_contribution:,.2f}')
print(f'Total yield: $ {yield_fi:,.2f}')
