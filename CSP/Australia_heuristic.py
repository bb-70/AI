from constraint import *
import time  # 시간 측정을 위한 모듈 추가
import matplotlib.pyplot as plt
import networkx as nx

start_time = time.time()  # 시작 시간 기록

# 문제 초기화
problem = Problem()

# 변수 및 도메인 정의
variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
domains = ['red', 'green', 'blue']
problem.addVariables(variables, domains)

# 제약 조건 정의
constraints = [
    ('WA', 'NT'), ('WA', 'SA'),
    ('NT', 'SA'), ('NT', 'Q'),
    ('SA', 'Q'), ('SA', 'NSW'), ('SA', 'V'),
    ('Q', 'NSW'),
    ('NSW', 'V')
]

for x, y in constraints:
    problem.addConstraint(lambda x, y: x != y, (x, y))

# 솔루션 찾기
solutions = problem.getSolutions()

# 솔루션 출력
for solution in solutions:
    print(solution)

# 호주 지도와 제약조건을 그래프로 시각화
def draw_colored_map(solution):
    # 그래프 초기화
    G = nx.Graph()
    G.add_edges_from(constraints)

    # 노드의 색상 설정
    node_colors = []
    for node in G.nodes():
        if node in solution:
            node_colors.append(solution[node])
        else:
            node_colors.append("gray")  # 미할당된 경우 기본 회색

    # 색상 이름을 matplotlib 컬러로 매핑
    color_map = {"red": "red", "green": "green", "blue": "blue", "gray": "gray"}
    mapped_colors = [color_map[color] for color in node_colors]

    # 그래프 레이아웃 설정
    pos = nx.spring_layout(G, seed=42)  # 고정된 레이아웃
    nx.draw(G, pos, with_labels=True, node_color=mapped_colors, node_size=500, font_weight='bold')
    plt.show()

# 첫 번째 솔루션을 시각화
if solutions:
    draw_colored_map(solutions[0])
else:
    print("No solution found!")

end_time = time.time()  # 종료 시간 기록
print(f"Execution time: {end_time - start_time:.4f} seconds")
