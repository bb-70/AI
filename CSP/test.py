# 제약 조건 정의
CONSTRAINTS = [
    ("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"),
    ("B", "E"), ("C", "E"), ("C", "F"), ("D", "E"),
    ("E", "F"), ("E", "G"), ("F", "G")
]

# 첫 번째 결과 (heuristics)에서 출력된 해들
solutions_heuristics = [
    {'E': 'Wednesday', 'B': 'Tuesday', 'C': 'Monday', 'F': 'Tuesday', 'A': 'Wednesday', 'D': 'Monday', 'G': 'Monday'},
    {'E': 'Wednesday', 'B': 'Monday', 'C': 'Tuesday', 'F': 'Monday', 'A': 'Wednesday', 'D': 'Tuesday', 'G': 'Tuesday'},
    {'E': 'Tuesday', 'B': 'Wednesday', 'C': 'Monday', 'F': 'Wednesday', 'A': 'Tuesday', 'D': 'Monday', 'G': 'Monday'},
    {'E': 'Tuesday', 'B': 'Monday', 'C': 'Wednesday', 'F': 'Monday', 'A': 'Tuesday', 'D': 'Wednesday', 'G': 'Wednesday'},
    {'E': 'Monday', 'B': 'Tuesday', 'C': 'Wednesday', 'F': 'Tuesday', 'A': 'Monday', 'D': 'Wednesday', 'G': 'Wednesday'},
    {'E': 'Monday', 'B': 'Wednesday', 'C': 'Tuesday', 'F': 'Wednesday', 'A': 'Monday', 'D': 'Tuesday', 'G': 'Tuesday'}
]

# 두 번째 결과 (simple)의 해
solution_simple = {'A': 'Monday', 'B': 'Tuesday', 'C': 'Wednesday', 'D': 'Wednesday', 'E': 'Monday', 'F': 'Tuesday', 'G': 'Wednesday'}

# 유효성 검사 함수
def is_valid(solution):
    for x, y in CONSTRAINTS:
        if solution[x] == solution[y]:  # 제약 조건을 위반하면 False
            return False
    return True

# 첫 번째 결과의 유효성 검사
valid_heuristics = [sol for sol in solutions_heuristics if is_valid(sol)]
print("Valid solutions from heuristics:", valid_heuristics)

# 두 번째 결과의 유효성 검사
valid_simple = is_valid(solution_simple)
print("Is the simple solution valid?", valid_simple)

# 중복 여부 확인
print("Is the simple solution in heuristics?", solution_simple in valid_heuristics)
