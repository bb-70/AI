from constraint import *
import time  # 시간 측정을 위한 모듈 추가

start_time = time.time()  # 시작 시간 기록

# 사용자 정의 제약 조건 함수
def check_constraints(t, w, o, f, u, r, x1, x2, x3):
    """
    사용자 정의 제약 조건 함수:
    연산이 불가능한 경우 False를 반환.
    """
    # 주어진 제약 조건 평가
    if 2 * o != r + 10 * x1:
        return False
    if 2 * w + x1 != u + 10 * x2:
        return False
    if 2 * t + x2 != o + 10 * x3:
        return False
    if f != x3:
        return False
    return True

# 문제 초기화
problem = Problem()

# 변수 정의
problem.addVariables(['T'], range(1, 10))  # T, F는 1~9의 값을 가짐 (첫 번째 자리 숫자)
problem.addVariables(['F','W', 'O', 'U', 'R'], range(10))  # W, O, U, R은 0~9의 값을 가짐
problem.addVariables(['X1', 'X2', 'X3'], [0, 1])  # 자리 올림 변수는 0 또는 1

# 모든 숫자는 서로 달라야 함
problem.addConstraint(lambda F, T, U, W, R, O: len(set([F, T, U, W, R, O])) == 6, ('F', 'T', 'U', 'W', 'R', 'O'))

# 사용자 정의 제약 조건 추가
problem.addConstraint(check_constraints, ('T', 'W', 'O', 'F', 'U', 'R', 'X1', 'X2', 'X3'))

# 해답 구하기
solutions = problem.getSolutions()

# 해답 출력
for solution in solutions:
    print(f"T={solution['T']} W={solution['W']} O={solution['O']} F={solution['F']} U={solution['U']} R={solution['R']}")

end_time = time.time()  # 종료 시간 기록
print(f"Execution time: {end_time - start_time:.4f} seconds")
