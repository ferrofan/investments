"""
MIT License

Copyright (c) 2022 ferrofan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
print(f'Final amount: $ {vf:,.2f}')
print(f'Total contribution: $ {total_contribution:,.2f}')
print(f'Total yield: $ {yield_fi:,.2f}')
