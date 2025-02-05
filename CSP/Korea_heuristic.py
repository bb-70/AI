from constraint import Problem
import time  # 시간 측정을 위한 모듈 추가
import matplotlib.pyplot as plt
import networkx as nx

VARIABLES = [
    "Seoul", "Gyeonggi", "Incheon", "Gangwon", "Chungbuk", "Chungnam",
    "Daejeon", "Jeonbuk", "Jeonnam", "Gwangju", "Gyeongbuk", "Gyeongnam",
    "Busan", "Ulsan", "Daegu", "Jeju", "Sejong"
]

CONSTRAINTS = {
    "Seoul": ["Gyeonggi"],
    "Gyeonggi": ["Seoul", "Incheon", "Gangwon", "Chungbuk", "Chungnam"],
    "Incheon": ["Gyeonggi"],
    "Gangwon": ["Gyeonggi", "Chungbuk", "Gyeongbuk"],
    "Chungbuk": ["Gangwon", "Gyeonggi", "Chungnam", "Gyeongbuk", "Daejeon"],
    "Chungnam": ["Gyeonggi", "Chungbuk", "Daejeon", "Jeonbuk", "Sejong"],
    "Daejeon": ["Chungbuk", "Chungnam", "Sejong"],
    "Jeonbuk": ["Chungnam", "Jeonnam", "Gwangju"],
    "Jeonnam": ["Jeonbuk", "Gwangju", "Gyeongnam"],
    "Gwangju": ["Jeonbuk", "Jeonnam"],
    "Gyeongbuk": ["Gangwon", "Chungbuk", "Daegu", "Gyeongnam"],
    "Gyeongnam": ["Gyeongbuk", "Jeonnam", "Busan", "Ulsan"],
    "Busan": ["Gyeongnam", "Ulsan"],
    "Ulsan": ["Gyeongnam", "Busan"],
    "Daegu": ["Gyeongbuk"],
    "Jeju": [],  # Jeju는 다른 지역과 인접하지 않음
    "Sejong": ["Chungnam", "Daejeon"]
}

# CSP를 사용한 풀이
def solve_with_csp():
    start_time = time.time()  # 시작 시간 기록

    problem = Problem()
    colors = ["red", "green", "blue", "yellow"]  # 사용할 색상들

    # VARIABLES에 도메인 추가
    problem.addVariables(VARIABLES, colors)

    # CONSTRAINTS 추가 (인접 지역은 같은 색을 가질 수 없음)
    for region, neighbors in CONSTRAINTS.items():
        for neighbor in neighbors:
            problem.addConstraint(lambda x, y: x != y, (region, neighbor))

    # 최소 색상 계산
    min_colors = 1

    while min_colors <= len(colors):
        sub_colors = colors[:min_colors]
        problem = Problem()
        problem.addVariables(VARIABLES, sub_colors)
        for region, neighbors in CONSTRAINTS.items():
            for neighbor in neighbors:
                problem.addConstraint(lambda x, y: x != y, (region, neighbor))

        solutions = problem.getSolutions()
        if solutions:
            execution_time = time.time() - start_time
            return min_colors, solutions[0], execution_time
        min_colors += 1

    return None, None, None

# 결과 출력
min_colors_csp, solution_csp, execution_time_csp = solve_with_csp()

print(f"최소 색상 수: {min_colors_csp}")
print(f"실행 시간: {execution_time_csp:.4f}초")
print("색상 조합 결과:")
for region, color in solution_csp.items():
    print(f"{region}: {color}")

# 지도 시각화 함수
def draw_colored_map(solution):
    G = nx.Graph()

    # 노드 및 엣지 추가
    for region, neighbors in CONSTRAINTS.items():
        for neighbor in neighbors:
            G.add_edge(region, neighbor)

    # 노드의 색상 설정
    node_colors = [solution.get(node, "gray") for node in G.nodes()]

    # 색상 이름을 matplotlib 컬러로 매핑
    color_map = {"red": "red", "green": "green", "blue": "blue", "yellow": "yellow", "gray": "gray"}
    mapped_colors = [color_map[color] for color in node_colors]

    # 그래프 레이아웃 설정
    pos = nx.spring_layout(G, seed=42)  # 고정된 레이아웃
    nx.draw(G, pos, with_labels=True, node_color=mapped_colors, node_size=500, font_weight='bold')
    plt.show()

# 해답 시각화
if solution_csp:
    draw_colored_map(solution_csp)
else:
    print("No solution found!")
