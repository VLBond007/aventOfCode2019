count_2 = 0
count_3 = 0
data_from_file = []
let_check = 0

with open('data_day2.txt') as file:
    data_from_file = file.readlines()
    count = 0
    for data in data_from_file:
        letter_in_data = set()
        was_2 = False
        was_3 = False
        for i in range(len(data)):
            let_check = 0
            if data[i] not in letter_in_data:
                letter_in_data.add(data[i])
                for k in range(len(data)):
                    if data[k] == data[i]:
                        let_check += 1
                if let_check == 2:
                    if was_2 == False:
                        count_2 += 1
                        was_2 = True
                if let_check == 3:
                    if was_3 == False:
                        was_3 = True
                        count_3 += 1
    print('Checksum = ', count_2 * count_3)