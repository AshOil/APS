num_list = []
for number in range(2,10):
    for divide in range(2, number):
        if number%divide == 0:
            continue
        else:
            num_list.append(number)
print(num_list)

