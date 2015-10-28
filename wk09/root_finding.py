# -*- coding: cp949 -*-
def sequential(f, x0):
    # � ������ �Է°��� ������ �� �� ������
    # xi �� �ʱⰪ�� (�ε��Ҽ���) �Ǽ��� �Ǿ�� �ϹǷ�
    # float() �� �̿��Ѵ�
    xi = float(x0)
    # delta_x �� �ǹ̴�
    # "���� ���� ã�� ������ �� xi�� �󸶸�ŭ ������ų ���ΰ�"
    # �̴�
    delta_x = 1e-6
    counter = 0
    while True:
        fi = f(xi)
        if abs(fi) < epsilon:
            break
        xi += delta_x
        counter += 1
    print "seq_counter =", counter
    return xi
# end of sequential()


def bisection(f, xl, xh, epsilon=1e-6):
    xl = float(xl)
    xh = float(xh)
    
    counter = 0
    function_call_counter = 0

    function_call_counter += 1
    fxl = f(xl)
    function_call_counter += 1
    fxh = f(xh)

    if 0 < fxl * fxh :
        # ���α׷����� ������ �߻������� �˸�
        print "Incorrect initial condition"
        # raise Exception
        return None

    while True:
        xn = 0.5 * (xl + xh)
        function_call_counter += 1
        fxn = f(xn)

        print "%3d xl = %8g f(xl) = %+8g xn = %+8g f(xn) = %+8g xh = %+8g f(xh) = %8g |xh-xl| = %-8g" % (counter, xl, fxl, xn, fxn, xh, fxh, abs(xh-xl))

        if fxn * fxh < 0:
            # xn ������ �Լ����� xh ������ �Լ����� ��ȣ�� �ݴ�
            # f(x) = 0 �� ������Ű�� ���� xn �� xh ���̿� ����
            # xl ~ xn ������ ������ ����
            # xl �� xn ���� ���� ��
            xl = xn
            fxl = fxn
        elif fxn * fxl < 0:
            # xn ������ �Լ����� xl ������ �Լ����� ��ȣ�� �ݴ�
            # f(x) = 0 �� ������Ű�� ���� xl �� xn ���̿� ����
            # xn ~ xh ������ ������ ����
            # xh �� xn ���� ���� ��
            xh = xn
            fxh = fxn
        else:
            # ���α׷����� ������ �߻������� �˸�
            print "Incorrect initial condition"
            # raise Exception
            return None

        counter += 1

        if abs(xh - xl) < epsilon:
            break

    print "bis_counter =", counter
    print "function_call_counter =", function_call_counter
    return xn
# end of bisection()


def newton(f, df, x0):
    counter = 0
    xi = float(x0)
    while True:
        fi = f(xi)
        counter += 1
        if abs(fi) < epsilon:
            break
        else:
            xi += (-fi/df(xi))
            
    print "nr_counter =", counter
    return xi
# end of newton


def func(x):
    return 1.0 * x * x - 2.0
# end of func()
# inspired by Scratch example


def dfunc(x):
    return 2.0 * x
# end of dfunc()
# for later use


# |x| < epsilon == (x = 0)
epsilon = 1e-4

if "__main__" == __name__:
    # initial value
    x0 = "0.01"

    # call sequential method
    x_seq = sequential(func, x0)
    print "x_seq =", x_seq
    print "f(x_seq) =", func(x_seq)

    x_bis = bisection (func, 0.01, 2.0)
    print "x_bis =", x_bis
    print "f(x_bis) =", func(x_bis)

    x_nr = newton (func, dfunc, 2.0)
    print "x_nr =", x_nr
    print "f(x_nr) =", func(x_nr)

    print "error   seq         bis        nr"
    print "        %7g %7g %7g" % ( abs(2.0**0.5 - x_seq), abs(2.0**0.5 - x_bis), abs(2.0**0.5 - x_nr))