def bwt_transform(text):
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    sorted_rotations = sorted(rotations)
    bwt_result = ''.join([rotation[-1] for rotation in sorted_rotations])
    return bwt_result


def inverse_bwt(bwt_str):
    bwt_transform = list(bwt_str)
    matrix = sorted(bwt_transform)
    
    while len(matrix[0]) < len(matrix):
        matrix = sorted([i + j for i, j in zip(bwt_transform, matrix)])
    
    inverse_bwt_result = matrix[0][1:] + '$'
    return inverse_bwt_result
    
bwt = input()
print(inverse_bwt(bwt))