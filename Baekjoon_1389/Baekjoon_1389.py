user, friends_num = map(int,input().split())


#친구관계
relation = [[100 for i in range(user)]for i in range(user)]

for i in range(friends_num):
    one, two = map(int, input().split())
    relation[one-1][two-1] = 1
    relation[two-1][one-1] = 1


#플로이드 워셜
for k in range(user):
    for i in range(user):
        for j in range(user):
            if i == j:
                pass
            else:
                relation[i][j] = min(relation[i][k] + relation[k][j], relation[i][j])

final_relation = []


for i in relation:
    final_relation.append(sum(i))

print(final_relation.index(min(final_relation)) + 1)