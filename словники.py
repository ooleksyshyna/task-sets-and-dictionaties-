#K:

with open('input.txt', 'r') as text:
    d = {}
    result_list = []

    for line in text:
        line = line.strip().lower().replace(';','').replace('.', '').replace(',', '')
        words = line.split()

        for word in words:

            if word not in d:
                result_list.append(0)
                d[word] = 1

            else:
                result_list.append(d[word])
                d[word] += 1

    print(result_list)


#L:

with open('L.txt', 'r') as text:

    for line in text:
        words = line.strip().split()
        it = iter(words)
        res_dct = dict(zip(it, it))

        if 'Goodbye' in res_dct:
            print(res_dct['Goodbye'])

        elif 'Goodbye' in res_dct.values():
            result = [k for k, v in res_dct.items() if v == 'Goodbye'] [0]
            print(result)

        else:
            pass


#M:

with open('Mc.txt', 'r') as f:
    for line in f:
        key, value = line.strip().split()

        if key in d:
            d[key] += int(value)

        else:
            d[key] = int(value)

for key, value in d.items():

    print('{} {}'.format(key, value))

#N:
with open('N.txt', 'r') as f:
    d = {}

    words = f.readlines()[0].strip().split()
    print(words)

    for word in words:
        if word not in d:
            d[word] = 0
        d[word] += 1

print(d)

max_word = ''
max_count = -1

for word, count in sorted(d.items()):
    if count > max_count:
        max_word = word
        max_count = count

print(max_word)


#P:

with open('countr.txt', 'r') as f:
    num_lists = int(f.readline().strip())
    cities = {}

    for i in range(num_lists):
        line = f.readline().strip().split()
        country = line[0]
        cities[country] = line[1:]

    while True:
        line = f.readline().strip()

        if not line:

            break

        for country, city_list in cities.items():

            if line in city_list:

                print(country)

                break


#S:

with open('fi.txt', 'r') as f:
    num_lines = int(f.readline().strip())
    slovnyk = [f.readline().strip() for _ in range(num_lines)]
    words_count = 0

    for line in f:

        for word in slovnyk:
            if word in line:
                words_count += 1

print(words_count)


#T:

total_amounts = {}

with open('ivanenko.txt', 'r') as file:
    for line in file:
        name, item, amount = line.split()
        amount = int(amount)

        if name not in total_amounts:
            total_amounts[name] = {}

        if item not in total_amounts[name]:
            total_amounts[name][item] = 0
        total_amounts[name][item] += amount

for name in sorted(total_amounts):
    print(f"{name}:")

    for item, amount in sorted(total_amounts[name].items()):
        print(f"{item} {amount}")


#V:

with open('vyb.txt', 'r') as f:
    num_states = int(f.readline().strip())
    states = []
    vote_counts = {}

    for i in range(num_states):
        state, votes = f.readline().strip().split()
        states.append(state)
        vote_counts[state] = {'Bush': 0, 'Gore': 0}
        vote_counts[state][state] = int(votes)

    for line in f:
        state, candidate = line.strip().split()
        vote_counts[state][candidate] += 1

for state in states:
    total_votes = vote_counts[state][state]
    bush_votes = vote_counts[state]['Bush']
    gore_votes = vote_counts[state]['Gore']

    if bush_votes > gore_votes:
        winner = 'Bush'

    elif gore_votes > bush_votes:
        winner = 'Gore'

    else:
        winner = 'Draw'

    print(f"{winner} {total_votes}")
