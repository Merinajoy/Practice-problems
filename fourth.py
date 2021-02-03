
def frequent_letter(line):
    count = 0
    max_count = 0
    max_letter = line[0]

    for letter in line:
        i = 0
        n = len(line)
        while i < n:
            if line[i] == letter:
                count = count + 1
        if count > max_count:
            max_count = count
            max_letter = letter
    print(max_letter, 'occurs ', max_count, 'times')


s = 'The quick brown fox jumps over the lazy dog'
frequent_letter(s)
