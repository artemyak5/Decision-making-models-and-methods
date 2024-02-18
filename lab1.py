"""
Перевірити, чи буде дане відношення рефлексивним, антирефлексивним,
симетричним, антисиметричним, асиметричним, транзитивним. Відшукати
для нього найбільший, найменший , максимальний та мінімальний елементи,
якщо такі існують, i побудувати обернене й додаткове відношення.
"""

R = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0]
]

R1 = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]
]

R2 = [
    [0, 1, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def check_reflexivity(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            return False
    return True


def check_antireflexivity(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] != 0:
            return False
    return True


def check_symmetry(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def check_antisymmetry(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and matrix[j][i] == 1 and i != j:
                return False
    return True

    return 


def check_asymmetry(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def check_transitivity(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                for k in range(len(matrix)):
                    if matrix[j][k] == 1 and matrix[i][k] != 1:
                        return False
    return True


def find_min_element(matrix):
    num_columns = len(matrix[0])  
    max_ones_count = 0 
    max_ones_column = None

    for j in range(num_columns):  
        ones_count = sum(row[j] for row in matrix)  
        if ones_count > max_ones_count:  
            max_ones_count = ones_count  
            max_ones_column = j  

    return max_ones_column + 1

def find_max_element(matrix):
    num_columns = len(matrix[0])  
    min_ones_count = len(matrix) + 1  
    min_ones_column = None 

    for j in range(num_columns):  
        ones_count = sum(row[j] for row in matrix)  
        if ones_count < min_ones_count:  
            min_ones_count = ones_count  
            min_ones_column = j  

    return min_ones_column + 1  


def result(matrix):
    print("  Рефлексивна: ", check_reflexivity(matrix))
    print("  Антирефлексивна: ", check_antireflexivity(matrix))
    print("  Симетрична: ", check_symmetry(matrix))
    print("  Антисиметрична: ", check_antisymmetry(matrix))
    print("  Асиметрична: ", check_asymmetry(matrix))
    print("  Транзитивна: ", check_transitivity(matrix))
    print("  Максимальний елемент: x{}".format(find_max_element(matrix)))
    print("  Мінімальний елемент: x{}".format(find_min_element(matrix)))

result(R)


def find_inverse_relation(matrix):
    # Створюємо пустий список для збереження оберненого відношення
    inverse_relation = []
    
    # Проходимо через кожний рядок у матриці
    for i in range(len(matrix)):
        inverse_relation.append([])  # Додаємо новий порожній рядок у обернене відношення
        # Проходимо через кожний елемент у поточному рядку
        for j in range(len(matrix[0])):
            # Додаємо до оберненого відношення обернений елемент поточного елементу
            # Якщо поточний елемент 0, обернений елемент буде 1; якщо поточний елемент 1, обернений буде 0
            inverse_relation[i].append(1 - matrix[i][j])
    
    # Повертаємо обернене відношення
    return inverse_relation


def find_complement_relation(matrix):
    # Створюємо пустий список для збереження доповнення відношення
    complement_relation = []
    
    # Проходимо через кожний рядок у матриці
    for i in range(len(matrix)):
        complement_relation.append([])  # Додаємо новий порожній рядок у доповнення відношення
        # Проходимо через кожний елемент у поточному рядку
        for j in range(len(matrix[0])):
            # Додаємо до доповнення відношення 1, якщо поточний елемент матриці дорівнює 0, або 0, якщо він дорівнює 1
            complement_relation[i].append(1 if matrix[i][j] == 0 else 0)
    
    # Повертаємо доповнення відношення
    return complement_relation

