#A1Q3

unique_words = []

with open('amth.txt', 'r') as file:

    for _ in range(1):               ## 
        next(file)

        for line in file:
            words = line.split()
            for word in words:
                if word not in unique_words:
                    unique_words.append(word)

unique_words.sort()

for word in unique_words:
    print(word)


