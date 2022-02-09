time = [300, 60, 10]

t = int(input())

cnt = list()
for sec in time:
    if t < sec:
        cnt.append(0)
        continue
    else:
        cnt.append(t // sec)
        t = t % sec

print(' '.join([str(c) for c in cnt])) if t == 0 else print(-1)
