n, m = map(int,input().split())

input_info = []

human_relations = dict()

for i in range(1,n+1):
    human_relations[i] = 1

for i in range(m):
    a = input().split()
    if a[0] == 'Q':
        a[1] = int(a[1])
        print(human_relations[a[1]])
    elif a[0] == 'M':
        a[1] = int(a[1])
        a[2] = int(a[2])
        num_friend_1 = human_relations[a[1]]
        num_friend_2 = human_relations[a[2]]
        human_relations[a[1]] = num_friend_1 + num_friend_2
        human_relations[a[2]] = human_relations[a[1]]



