# Constraint Satisfaction Problem, CSP 라이브러리 사용
from constraint import *
import time  # 시간 측정을 위한 모듈 추가

start_time = time.time()  # 시작 시간 기록

#문제 초기화
problem = Problem()

# Add variables
# 각 A, B, C, D, E, F, G 과목은 각각 mon, tue, wed중 하루를 시험 날짜로 가질 수 있음.
problem.addVariables(
    ["A", "B", "C", "D", "E", "F", "G"],
    ["Monday", "Tuesday", "Wednesday"]
)

# Add constraints
# 제약조건 정의, 묶여있는 과목끼리 같은 날이 배정되면 안됨
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

# 위 제약조건 내 각 쌍의 시험요일이 다르게 배정되도록 제약 조건 설정
for x, y in CONSTRAINTS:
    problem.addConstraint(lambda x, y: x != y, (x, y))

# Solve problem
# 가능한 모든 해를 출력
for solution in problem.getSolutions():
    print(solution)

end_time = time.time()  # 종료 시간 기록
print(f"Execution time: {end_time - start_time:.4f} seconds")
