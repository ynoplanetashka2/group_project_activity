import numpy as np

def solve_de_inner(**argv):
    step = argv['step']
    start = argv['start']
    end = argv['end']
    operator = argv['operator']
    initial = argv['initial']

    current = initial
    time = start
    while time <= end:
        delta = np.matmul(operator(time), current) * step
        current += delta
        time += step
    
    return current

def solve_de(**argv):
    delta = argv['delta']
    epsilon = argv['epsilon']
    coef = lambda time: - (delta + epsilon * np.cos(time))
    columns = []
    initials = [
        np.array([1, 0], float),
        np.array([0, 1], float),
    ]
    for initial in initials:
        columns.append(
            solve_de_inner(
                step = .0007,
                start = 0,
                end = 2 * np.pi,
                initial = initial,
                operator = lambda time: np.array([[0, 1], [coef(time), 0]], float),
            )
        )
    
    return np.array(columns)

def is_stable(**argv):
    sol = solve_de(**argv)
    eigvals = np.linalg.eigvals(sol)
    for i in range(2):
        eigen = eigvals[i]
        abs_val = np.abs(eigen)
        if abs_val > 1.005:
            return False
    return True
    #     if abs_val <= 1:
    #         return True
    # return False
