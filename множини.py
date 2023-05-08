#A:
numbers = {'1', '2', '3', '2', '1'}
unique_numbers = set(numbers)

print(len(unique_numbers))


#B:
list1 = [1, 2, 3]
list2 = [4, 3, 2]
count = len(set(list1) & set(list2))

print(count)



#C:

list1 = [1, 2, 3]
list2 = [4, 3, 2]
growth = sorted(set(list1) & set(list2))

print(growth)


#D:

numbers_list = "1 2 3 2 3 4"
numbers_list = numbers_list.split()
used = set()
for num in numbers_list:
    if num in used:
        print("YES")
    else:
        print("NO")
        used.add(num)


#E:

with open('Е.txt', 'r') as f:
    lines = f.readlines()
num_balls = list(map(int, lines[0].split()))
irina_balls = set(map(int, lines[1:num_balls[0]+1]))
igor_balls = set(map(int, lines[num_balls[0]+1:]))
common_balls = sorted(irina_balls & igor_balls)
irina_only_balls = sorted(irina_balls - igor_balls)
igor_only_balls = sorted(igor_balls - irina_balls)

print(*common_balls)

print(len(common_balls))

print(*irina_only_balls)

print(len(irina_only_balls)-1)

print(*igor_only_balls)


#F:

with open('F.txt', 'r') as text:
    text_str = str(text.readlines())
    w = text_str.split(' ')

    print(len(set(w))+1)


#G:

with open('G.txt', 'r') as f:
    n = int(f.readline().strip())
    print(n)
    nums1 = set(map(int, f.readline().strip().split()))
    answer1 = f.readline().strip()
    nums2 = set(map(int, f.readline().strip().split()))
    answer2 = f.readline().strip()

    print(' '.join(map(str, sorted(nums1.difference(nums2)))))

#H:

with open('r.txt', 'r') as f:
    lines = f.readlines()
    first_row = lines[0].strip().split(' ')
    second_row = lines[1].strip().split(' ')
    third_row = lines[2].strip().split(' ')

    if len(second_row) <= 5:
        print("NO")

    else:
        print("YES")

    if len(third_row) >= 5:
        print("YES")

    else:
        print("NO")
    yes_numbers = []
    for number in third_row:

        if len(second_row) <= 5 and number in third_row and number not in second_row:
            yes_numbers.append(number)

        elif len(second_row) > 5 and number in second_row and number not in third_row:
            yes_numbers.append(number)
print(' '.join(yes_numbers))


#I:

my_dict = {}
with open('I.txt', 'r') as f:
    line = f.readline()
    j = int(line)
    while line:
        words = line.strip().split()
        for word in words:
            if not word.isdigit():
                my_dict[word] = my_dict.get(word, 0) + 1
        line = f.readline()
lng_lst = []
shr_lst = []
for key, value in my_dict.items():
    if value == j:
        lng_lst.append(key)
    if value >= 1:
        shr_lst.append(key)

h = len(lng_lst)
print(h)

for key in lng_lst:
    print(key)

k = len(shr_lst)
print(k)

for key in shr_lst:
    print(key)
