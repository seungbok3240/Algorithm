import sys, copy
from collections import defaultdict, deque

input = sys.stdin.readline

num_node = int(input())
node_info = list(map(int, input().split()))
remove_node = int(input())

tree = defaultdict(list)
count = 0
for i in node_info:
    if i == -1:
        count += 1
        root_index = node_info.index(i)
        continue
    tree[i].append(count)
    count += 1

minus_one_count = node_info.count(-1)

'''
1
-1
0
케이스 처리
'''
if len(tree) == 0:
    print(0)
    sys.exit()

#트리가 여러개일떄 처리
if remove_node in tree:
    if remove_node == root_index:   
        minus_one_count -= 1
        if minus_one_count == 0:     #루트노드가 지워지면 다 지워지므로 0을 출력한다.
            print(0)
            sys.exit()
    visited = deque()               #한 노드가 지워지면 해당 노드의 자식노드들도 다 지워저야 하므로 ~
    visited.append(remove_node)
    while visited:
        tmp = visited.popleft()
        for i in tree[tmp]:
            visited.append(i)
        del tree[tmp]

storage = list()

for i in tree:
    if remove_node in tree[i]:
        tree[i].remove(remove_node)
        if len(tree[i]) == 0 and minus_one_count == 1:
            storage.append(i)

for i in storage:
    del tree[i]
                                    # ~ 여기까지 노드 삭제!
leaf = set()
for i in tree:
    for j in tree[i]:
        if j in tree:
            continue
        leaf.add(j)

#트리가 여러 개 일때 그 중 어떤 트리가 부모만 남았을 경우 처리
final_count = 0
for i in tree:
    if len(tree[i]) == 0:
        final_count += 1

'''

'여기까지 노드 삭제!' 바로 위 코드 때문에 부모가 혼자 남는 케이스에서

부모도 삭제해버리기 때문에 len(tree) == 0 ----> 부모가 혼자 남아있는 케이스라 판단

'''
if len(leaf) == 0:
    print(1)
else:    
    print(len(leaf) + final_count)