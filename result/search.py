import util

class SearchProblem:
    def __init__(self, start_state):
        self.start_state = start_state

    # 초기 상태 반환
    def getStartState(self):
        util.raiseNotDefined()

    # 목표 상태 여부 확인
    def isGoalState(self, state):
        util.raiseNotDefined()

    # 현재 상태에서 이동 가능한 후속 상태, 액션, 비용 반환
    def getSuccessors(self, state):
        util.raiseNotDefined()

    # 총 비용 계산
    def getCostOfActions(self, actions):
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

# DFS 깊이우선탐색 #
def depthFirstSearch(problem):
    stack = util.Stack() # DFS의 후입선출(LIFO) 방식을 구현하기 위해 스택 사용
    start_state = problem.getStartState() # problem에서 시작 상태를 가져옴
    stack.push((start_state, [])) # 스택에 (현재 상태, 이동 경로)을 튜플로 저장
    # 처음에는 현재 상태=start_state, 이동 경로=[](빈 리스트)

    visited = set() # 방문한 노드를 기록하는 집합. 중복 방문을 방지하기 위해 사용

    while not stack.isEmpty(): # 스택이 비어 있을 때까지 탐색 반복
        state, actions = stack.pop()  # 가장 마지막에 추가된 노드를 꺼내 현재 상태와 이동 경로 저장

        if problem.isGoalState(state): # 현재 상태가 목표 상태인지 확인
            return actions # 목표 상태에 도달하면 그때까지의 경로(actions)를 반환

        visited.add(state) # 현재 상태를 방문한 상태로 기록

        successors = problem.getSuccessors(state) # 현재 상태에서 갈 수 있는 후속 상태들 가져옴
        # getSuccessors는 (다음 상태, 그 상태로 가는 action, cost) 튜플을 반환

        for next_state, action, _ in successors:
            if next_state not in visited: # 만약 후속 상태가 아직 방문되지 않았다면
                next_actions = actions + [action] # 현재까지의 경로에 다음 상태로 가는 action 추가
                stack.push((next_state, next_actions)) # 새로운 상태와 경로를 스택에 추가
    return None # 스택이 비었으나 목표 상태에 도달하지 못한 경우 None 반환 (목표 상태가 없다는 의미)


# BFS 너비우선탐색 #
def breadthFirstSearch(problem):
    queue = util.Queue() # BFS의 선입선출 (FIFO) 구현을 위해 큐 사용
    start_state = problem.getStartState() # problem에서 시작 상태를 가져옴
    queue.push((start_state, [])) # 스택에 (현재 상태, 이동 경로)을 튜플로 저장
    # 처음에는 현재 상태=start_state, 이동 경로=[](빈 리스트)

    visited = set() # 방문한 노드를 기록하는 집합. 중복 방문을 방지하기 위해 사용

    while not queue.isEmpty(): # 큐가 비어 있을 때까지 과정 반복
        state, actions = queue.pop() # 가장 먼저 추가된 노드를 큐에서 꺼내 정보 저장

        if problem.isGoalState(state): # 현재 노드가 목표 상태인지 확인
            return actions # 목표 상태에 도달하면 그때까지의 경로(actions)를 반환

        if state not in visited: # 아직 방문하지 않은 상태일 때만 처리
            visited.add(state) # 현재 노드를 방문한 노드 집합에 추가
            successors = problem.getSuccessors(state) # 현재 상태에서 이동할 수 있는 후속 상태들을 가져옴
            # getSuccessors는 (다음 상태, 그 상태로 가기 위한 action, cost) 형태의 튜플을 반환

            for next_state, action, _ in successors: 
                if next_state not in visited: # 만약 후속 상태가 방문된 노드에 없다면
                    next_actions = actions + [action] # 현재 경로에 action 추가한 새로운 경로를 저장
                    queue.push((next_state, next_actions)) # 업데이트된 (상태, 경로)를 큐에 추가
    return None # 큐가 비었지만 목표 상태를 찾지 못한 경우 None 반환 (목표 상태가 없다는 의미)

# UCS 균일비용탐색 #
def uniformCostSearch(problem):
    start_node = (problem.getStartState(), [], 0)  # 시작 노드: (현재 상태, 이동 경로, 현재까지의 비용)
    open_set = util.PriorityQueue()  # 우선순위 큐 초기화 (경로 비용이 작은 순으로 노드를 처리)
    open_set.push(start_node, 0)  # 시작 노드를 우선순위 큐에 넣고, 우선순위는 0 (시작 비용)
    closed_set = set()  # 방문한 노드를 기록하는 집합. 중복 방문을 방지

    while not open_set.isEmpty():  # 우선순위 큐가 비어 있을 때까지 탐색 반복
        current_state, actions, current_cost = open_set.pop()  # 큐에서 비용이 가장 작은 노드 꺼냄

        if problem.isGoalState(current_state):  # 현재 상태가 목표 상태인지 확인
            return actions  # 목표 상태에 도달하면, 그때까지의 경로(actions)를 반환

        if current_state not in closed_set:  # 현재 상태가 아직 방문되지 않았다면
            closed_set.add(current_state)  # 상태를 방문한 상태로 기록

            for next_state, action, step_cost in problem.getSuccessors(current_state):
                next_actions = actions + [action]  # 현재까지의 경로에 다음 상태로 가는 action 추가
                next_cost = current_cost + step_cost  # 현재까지의 비용에 다음 상태로 가는 비용 추가

                # 우선순위 큐에 다음 상태와 경로, 새로운 비용을 추가. 새로운 비용이 우선순위
                open_set.push((next_state, next_actions, next_cost), next_cost)

    return None  # 우선순위 큐가 비었으나 목표 상태에 도달하지 못한 경우 None 반환 (목표 상태가 없다는 의미)


def nullHeuristic(state, problem=None):
    return 0

# A* Search #
def aStarSearch(problem, heuristic=nullHeuristic):
    start_node = (problem.getStartState(), [], 0)  # 시작 노드를 (상태, 이동 경로, 현재 비용) 형식으로 설정
    open_set = util.PriorityQueue()  # 우선순위 큐(가장 낮은 f(n) 값을 우선적으로 처리)
    open_set.push(start_node, 0)  # 우선순위 큐에 시작 노드와 우선순위 0을 넣음
    closed_set = set()  # 이미 방문한 노드를 저장하여 중복 방문을 방지

    while not open_set.isEmpty():  # 큐가 빌 때까지 반복
        current_state, actions, current_cost = open_set.pop()  # 가장 우선순위가 높은 노드를 꺼냄 (상태, 경로, 비용)
        
        if problem.isGoalState(current_state):  # 현재 상태가 목표 상태라면
            return actions  # 목표에 도달한 경로를 반환
        
        if current_state not in closed_set:  # 만약 현재 상태가 아직 방문되지 않았다면
            closed_set.add(current_state)  # 현재 상태를 방문 처리
            
            for next_state, action, step_cost in problem.getSuccessors(current_state):  # 현재 상태에서 갈 수 있는 자식 노드들 탐색
                next_actions = actions + [action]  # 새로운 상태로 가기 위한 액션을 기존 경로에 추가
                next_cost = current_cost + step_cost  # 현재 비용에 자식 노드로 가는 비용을 더함
                priority = next_cost + heuristic(next_state, problem)  # 우선순위 계산: f(n) = g(n) + h(n)
                
                open_set.push((next_state, next_actions, next_cost), priority)  # 자식 노드를 우선순위 큐에 추가
                
    return None  # 목표 상태에 도달하지 못한 경우 None을 반환


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
