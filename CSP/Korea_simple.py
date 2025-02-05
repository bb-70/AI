import time  # 시간 측정을 위한 모듈 추가
import matplotlib.pyplot as plt
import networkx as nx

# 시작 시간 기록
start_time = time.time()

# 변수와 제약조건 설정, 이웃한 도시는 같은 색이 할당되면 안 됨
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

# 백트래킹 카운트 초기화
backtracking_count = {var: 0 for var in VARIABLES}

def backtrack(assignment):
    """Runs backtracking search to find an assignment."""
    # Check if assignment is complete
    if len(assignment) == len(VARIABLES):
        return assignment

    # Try a new variable
    var = select_unassigned_variable(assignment)
    for value in ["red", "green", "blue", "yellow"]:
        new_assignment = assignment.copy()
        new_assignment[var] = value
        if consistent(new_assignment):
            result = backtrack(new_assignment)
            if result is not None:
                return result
        # 값이 재할당될 때 백트래킹 카운트 증가
        backtracking_count[var] += 1
    return None

def select_unassigned_variable(assignment):
    """Chooses a variable not yet assigned, in order."""
    for variable in VARIABLES:
        if variable not in assignment:
            return variable
    return None

def consistent(assignment):
    """Checks to see if an assignment is consistent."""
    for var, neighbors in CONSTRAINTS.items():
        if var in assignment:
            for neighbor in neighbors:
                if neighbor in assignment and assignment[var] == assignment[neighbor]:
                    return False
    return True

# 문제 해결
solution = backtrack({})

# 결과 출력
if solution:
    print("Solution found:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution found!")

print("Backtracking counts:")
print(backtracking_count)

# 종료 시간 기록
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")

# 해답 시각화
CONSTRAINTS_LIST = [(region, neighbor) for region, neighbors in CONSTRAINTS.items() for neighbor in neighbors]

def draw_colored_map(solution):
    # 그래프 초기화
    G = nx.Graph()
    G.add_edges_from(CONSTRAINTS_LIST)

    # 노드의 색상 설정
    node_colors = []
    for node in G.nodes():
        if node in solution:
            node_colors.append(solution[node])
        else:
            node_colors.append("gray")  # 미할당된 경우 기본 회색

    # 색상 이름을 matplotlib 컬러로 매핑
    color_map = {"red": "red", "green": "green", "blue": "blue", "yellow": "yellow", "gray": "gray"}
    mapped_colors = [color_map[color] for color in node_colors]

    # 그래프 레이아웃 설정
    pos = nx.spring_layout(G, seed=42)  # 고정된 레이아웃
    nx.draw(G, pos, with_labels=True, node_color=mapped_colors, node_size=500, font_weight='bold')
    plt.show()

# 해답 시각화
if solution:
    draw_colored_map(solution)
