count = 0
with open('mbox.txt','r') as file:
    for line in file:
        if line.startswith('From '):
            print(line.split()[1])
            count += 1
print(f"there were {count} senders in the file")

