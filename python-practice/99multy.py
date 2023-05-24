line = 1
# straight = 1
while line < 10:
    # print(line)
    for straight in range(1, line+1):
        print(f'{straight}*{line}={line * straight}', end=' ')
    print()
    line += 1
