file = open('data_day2.txt')

data_from_file = file.readlines()

for line1 in data_from_file:
    for line2 in data_from_file:
        x = ''.join(a for a, b in zip(line1, line2) if a == b)
        if len(x) == len(line1) - 1:
            print('Это', x)