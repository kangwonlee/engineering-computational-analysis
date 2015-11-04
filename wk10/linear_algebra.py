# -*- coding: cp949 -*-
def dot(a, b):
    """
    ũ�Ⱑ ���� �� ���� a, b�� ���� dot product
    """
    # ���� a �� ũ��.
    # ���� b �� ũ��� ���� ���̶�� �����Ѵ�
    #   (� ��� ������ �߻��� �� �ִ°�?)
    n = len(a)
    result = 0.0
    for i in xrange(n):
        result += a[i] * b[i]
    return result


def multiply_matrix_vector(A, x):
    n_row = len(A)
    n_column = len(A[0])

    result = [0.0] * n_row
    for i in xrange(n_row):
        result[i] = 0.0
        for j in xrange(n_column):
            result[i] += A[i][j] * x[j]

    return result


def main():
    a_vector = [1.0, 0.0]
    b_vector = [3.0, 4.0]
    a_dot_b = dot(a_vector, b_vector)

    print "a =", a_vector
    print "b =", b_vector
    print "a dot b =", a_dot_b

    A_matrix = [[0.0, 1.0],
                [1.0, 0.0]]
    x_vector = [3.0, 4.0]
    A_x = multiply_matrix_vector(A_matrix, x_vector)

    print "A =", A_matrix
    print "x =", x_vector
    print "A*x =", A_x

if "__main__" == __name__:
    main()