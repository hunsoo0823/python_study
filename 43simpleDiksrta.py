
import sys
input = sys.stdin.readline

INF = int(1e9)

# 노드의 개수, 간선의 개수 입력 받기
n, m = map(int, input().split())

# 시작 노드의 번호 입력받기
start = int(input())

# 각 노드와 연결 되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]
# 방문한 적이 있는지 체크하기 위한 목적의 리스트를 만들기
visted = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c  = map(int, input().split())
    # a에서 b로 가는 비용 c
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    for i in range(1, n+1):
        if distance[i] < min_value and not visted[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visted[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n - 1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visted[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            if distance[j[0]] > distance[now] + j[1]:
                distance[j[0]] = distance[now] + j[1]

dijkstra(start)

for i in range(1, n+1):
    # 도달할 수없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
