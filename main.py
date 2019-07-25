print('Hello, Player!')

inputValue = int(input('Input cell address (11,12,13,21,22,23,31,32,33): '))

# border template
border = '+---+---+---+'

# row number
row = inputValue // 10

# column number
col = inputValue - row * 10

print(border)

r1, r2, r3 = ' ', ' ', ' '

if row == 1:
    if col == 1:
        r1 = 'X'

    if col == 2:
        r2 = 'X'

    if col == 3:
        r3 = 'X'

print(f"| {r1} | {r2} | {r3} |")
print(border)

r1, r2, r3 = ' ', ' ', ' '

if row == 2:
    if col == 1:
        r1 = 'X'

    if col == 2:
        r2 = 'X'

    if col == 3:
        r3 = 'X'

print(f"| {r1} | {r2} | {r3} |")
print(border)

r1, r2, r3 = ' ', ' ', ' '

if row == 3:
    if col == 1:
        r1 = 'X'

    if col == 2:
        r2 = 'X'

    if col == 3:
        r3 = 'X'

print(f"| {r1} | {r2} | {r3} |")
print(border)
