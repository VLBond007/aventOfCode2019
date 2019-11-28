data_from_file = []
num = 0

with open('data_game_day1.txt') as file:
    data_from_file = file.readlines()
    prev_num = set()
    while num not in prev_num:
        for data in data_from_file:
            prev_num.add(num)
            num += int(data)
            if num in prev_num:
                print(num)
                break

