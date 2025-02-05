import time  # 시간 측정을 위한 모듈 추가
import matplotlib.pyplot as plt
import networkx as nx

start_time = time.time()  # 시작 시간 기록

# 전역 변수로 백트래킹 횟수를 추적
backtracking_count = {}

# 변수와 제약조건 설정, 이웃한 도시는 같은 색이 할당되면 안됨
VARIABLES = ["WA", "NT", "Q", "NSW", "V", "SA", "T"]
CONSTRAINTS = [
    ("WA", "NT"), ("WA", "SA"),
    ("NT", "SA"), ("NT", "Q"),
    ("SA", "Q"), ("SA", "NSW"), ("SA", "V"),
    ("Q", "NSW"),
    ("NSW", "V"),
]


for var in VARIABLES:
    backtracking_count[var] = 0

def backtrack(assignment):
    """Runs backtracking search to find an assignment."""
    # Check if assignment is complete
    if len(assignment) == len(VARIABLES):
        return assignment

    # Try a new variable
    var = select_unassigned_variable(assignment)
    for value in ["red", "green", "blue"]:
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
    for (x, y) in CONSTRAINTS:
        # Only consider arcs where both are assigned
        if x not in assignment or y not in assignment:
            continue

        # If both have same value, then not consistent
        if assignment[x] == assignment[y]:
            return False

    # If nothing inconsistent, then assignment is consistent
    return True

solution = backtrack(dict())
print(solution)
print(backtracking_count)

end_time = time.time()  # 종료 시간 기록
print(f"Execution time: {end_time - start_time:.4f} seconds")

def draw_colored_map(solution):
    # 그래프 초기화
    G = nx.Graph()
    G.add_edges_from(CONSTRAINTS)

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

# 해답 시각화
if solution:
    draw_colored_map(solution)
else:
    print("No solution found!")