import time  # 시간 측정을 위한 모듈 추가

start_time = time.time()  # 시작 시간 기록

# Variables and domains remain the same
variables = ["F", "T", "U", "W", "R", "O"]
domains = {
    "F": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "T": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "U": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "W": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "R": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "O": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
}

# Consistent function remains the same
def consistent(assignment):
    if len(set(assignment.values())) < len(assignment):
        return False
    if len(assignment) < len(variables):
        return True
    T, W, O, F, U, R = [assignment.get(var, 0) for var in "TWOFUR"]
    two = T * 100 + W * 10 + O
    four = F * 1000 + O * 100 + U * 10 + R
    return two + two == four

# Backtrack function with a counter for backtracking steps
def backtrack(assignment, count):
    if len(assignment) == len(variables):
        return assignment if consistent(assignment) else None, count
    
    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]
    
    for value in domains[var]:
        assignment[var] = value
        count += 1  # Increment counter when a value is assigned
        if consistent(assignment):
            result, count = backtrack(assignment.copy(), count)
            if result is not None:
                return result, count
        assignment.pop(var)
    
    return None, count

# Start the backtracking process with an empty assignment and a counter
solution, backtracking_steps = backtrack({}, 0)
print("Solution:", solution)
print("Backtracking steps:", backtracking_steps)

end_time = time.time()  # 종료 시간 기록
print(f"Execution time: {end_time - start_time:.4f} seconds")