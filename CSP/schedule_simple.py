"""
Naive backtracking search without any heuristics or inference.
"""
# DFS 백트랙킹을 직접 구현하는 코드
import time  # 시간 측정을 위한 모듈 추가

start_time = time.time()  # 시작 시간 기록

# 변수와 제약조건 정의, 묶여있는 과목끼리 같은 날이 배정되면 안됨
VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]


def backtrack(assignment):
    """Runs backtracking search to find an assignment."""
    # 백트래킹 탐색을 수행하여 사용 가능한 조합을 찾음
    # assignment : 현재까지 할당된 변수가 저장된 딕셔너리

    # Check if assignment is complete
    # 모든 변수가 할당된 경우 해를 반환
    if len(assignment) == len(VARIABLES):
        return assignment

    # Try a new variable
    var = select_unassigned_variable(assignment)
    for value in ["Monday", "Tuesday", "Wednesday"]:
        new_assignment = assignment.copy()
        new_assignment[var] = value

         # 새로운 값이 제약 조건을 만족하면 재귀 호출
        if consistent(new_assignment):
            result = backtrack(new_assignment)
            if result is not None:
                return result
    return None


# 아직 할당되지 않은 변수 선택 (순차적)
def select_unassigned_variable(assignment):
    """Chooses a variable not yet assigned, in order."""
    for variable in VARIABLES:
        if variable not in assignment:
            return variable
    return None


# 현재 할당된 값들이 제약조건을 만족하는가?
def consistent(assignment):
    """Checks to see if an assignment is consistent."""
    for (x, y) in CONSTRAINTS:

        # Only consider arcs where both are assigned
        # CONSTRAINts에 있는 변수 쌍 중 두 변수 모두 할당된 쌍만 골라서 검사
        if x not in assignment or y not in assignment:
            continue

        # If both have same value, then not consistent
        # 검사한 쌍의 두 변수의 할당값이 같으면 제약 조건 불출족
        if assignment[x] == assignment[y]:
            return False

    # If nothing inconsistent, then assignment is consistent
    return True

# 백트랙킹으로 solution 정의
solution = backtrack(dict())
print(solution)

end_time = time.time()  # 종료 시간 기록
print(f"Execution time: {end_time - start_time:.4f} seconds")
