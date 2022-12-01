# Part 1
with open('input.txt') as fp:
    data = fp.read()
    data = data.split('\n\n')
    top = 0
    elf_no = ''
    for (i, elf_cal) in enumerate(data):
        print(f"Checking Elf No {i}")
        cal_d = filter(lambda x: x != '', elf_cal.split('\n'))
        total = sum(list(map(lambda x: int(x), cal_d)))
        
        if total > top:
            top = total
        elf_no = i
        
    print(top)
            

# Part 2
total_calories = []
with open('input.txt') as fp:
    data = fp.read()
    data = data.split('\n\n')
    for (i, elf_cal) in enumerate(data):
        cal_d = filter(lambda x: x != '', elf_cal.split('\n'))
        total = sum(list(map(lambda x: int(x), cal_d)))
        total_calories.append(total)

total_calories.sort(reverse=True)
print(sum(total_calories[:3]))



