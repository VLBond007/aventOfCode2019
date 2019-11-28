data_from_file = []
num = 0

with open('data_game_day1.txt') as file:
    data_from_file = file.readlines()
    for data in data_from_file:
        try:
            num += int(data)
        except:
            print('Чет тут не так')

print('И наше число: ', num)