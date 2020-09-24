# adjacenecy Matrix

INF = 999999999 # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph1 = [
    [0 , 7, 5],
    [7 , 0, INF],
    [5, INF, 0]
]

print(graph1)

# adjacenecy List
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph2 = [ [] for _ in range(3)]

# node 1(node,distance)
graph2[0].append((1,7))
graph2[0].append((2,5))

#node 2
graph2[1].append((0,7))

#node 3
graph2[2].append((0,5))

print(graph2)
