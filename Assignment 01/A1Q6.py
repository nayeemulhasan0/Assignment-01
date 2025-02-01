
counts = {}
with open('mbox.txt') as file:
    for line in file:
        if line.startswith('From '):
            counts[line.split()[1]] = counts.get(line.split()[1], 0) + 1
sender = max(counts, key=counts.get)
print(sender, counts[sender])

