# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이 사용되었다는 점을 표시하는 것임
from math import cos, atan, sqrt, exp


def fwd_euler(f, x_init, t_start, t_end, delta_t):
    """
    상미분 방정식의 초기값 문제를 위한 전진 오일러법

    t[k] 와 t[k+1] 사이에는 dx/dt 가 상수일 것으로 가정함

    dx/dt 로 t[k] 에서의 값을 사용

    delta_t_sec 가 작은 값이 되지 않으면 오차가 커지는 경향이 있음

    :param f: dx/dt = f(x,t)
    :param x_init: x 의 초기값
    :param t_start: 초기 시간
    :param t_end: 끝 시간
    :param delta_t: 시간 간격
    :return: 시간, x 의 list
    """
    # t_start ~ t_end 사이를 delta_t 간격으로 나눈 갯수. 소숫점 아래는 버림? 반올림?
    m_time_step = int((t_end - t_start) * 1.0 / delta_t)

    # 상태의 갯수 == 초기 상태 벡터의 길이
    n_states = len(x_init)

    # time step 인덱스 k를 순서 대로 나열하여 tuple 로 저장 (list 와 달리 이후 변경 불가)
    #   0, 1, ...., m_time_step-1
    list_k = tuple(range(m_time_step))

    # time step tk 를 순서대로 나열하여 tuple 로 저장 (list 와 달리 이후 변경 불가)
    list_t = tuple(([t_start + delta_t * i for i in list_k]))

    # 예를 들어 t_start, t_end, delta_t 이 0.0, 1.0, 0.1 로 주어졌다면
    #   m_time_step 은 10
    #       list_t 에는 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9 가 저장될 것이며
    #       len(list_t) == 10

    # 각 time step 에서의 상태 변수 값을 저장할 list 를 미리 할당(allocate) 시작
    # list_x 를 초기화 함
    # list_x[0] == k = 0 일때의 x 값 == 초기값 x_init
    list_x = [tuple(x_init)]

    # 행 할당 반복문 시작
    #   list_x[0] 는 위에서 이미 초기값 x_init 로 정함
    #   k = [1, 2, ..., n-1] 인 경우 x 즉
    #       list_x[1], list_x[2], ..., list_x[n-1] 의 값은 아직 알 수 없음
    #       따라서 0.0 을 n_states 개 담은 list 를 만듦
    for k in list_t[1:]:
        list_x.append([0.0] * n_states)
    # 행 할당 반복문 종료

    # 이렇게 하면 m_time_step x n_states 의 크기를 갖는 2차원 배열 공간이 준비됨

    # python 의 경우, 위와 같이 미리 할당하지 않고 각 time step 마다 state x 를 append 할 수도 있음
    # 다른 프로그래밍 언어의 경우 자료를 저장하기 전에 저장할 장소를 할당할 필요가 있을 경우가 많음

    # 상태 변수 저장할 공간 할당 끝

    # xk 변수를 x0로 초기화
    xk = x_init

    # time step 반복문 시작
    for k in list_k[:-1]:
        # 이번 time step 에서의 기울기 dx/dt = f(x) 를 계산하여 sk 라는 변수에 저장
        sk = f(xk, list_t[k])

        # 다음 time step 에서의 상태 x[k + 1] 을 저장할 공간을 xk1이라는 이름으로 지정
        xk1 = list_x[k + 1]

        # 각 상태 반복문
        for i in xrange(n_states):
            # 전진 오일러법을 적용
            xk1[i] = xk[i] + sk[i] * delta_t
        # 각 상태 반복문 끝

        # xk 값을 다음 상태 값으로 갱신
        xk = xk1
    # time step 반복문 끝

    # 각 time step 별 시간, 상태 값을 반환
    return list_t, list_x


# fwd_euler() 함수 끝


def mod_euler(f, x_init, t_start, t_end, delta_t):
    """
    상미분 방정식의 초기값 문제를 위한 수정 오일러법

    t[k] 와 t[k+1] 사이에는 dx/dt 가 선형으로 변화할 것으로 가정함

    dx/dt 로 t[k] 에서의 값을 사용

    :param f: dx/dt = f(x,t)
    :param x_init: x 의 초기값
    :param t_start: 초기 시간
    :param t_end: 끝 시간
    :param delta_t: 시간 간격
    :return: 시간, x 의 list

    Examples
    --------
    >>> list_t, list_x = mod_euler(lambda x, t:[(math.sin(math.pi*t) - x[0])*0.5],[0],0.0, 0.5, 0.1)
    >>> print list_t
    [0.0, 0.10000000000000001, 0.20000000000000001, 0.30000000000000004, 0.40000000000000002, 0.5]
    >>> print list_x
    [[0], [0.0077254248593736849], [0.029382595321196046], [0.062135518400607666], [0.10209697840236187], [0.14470734296725662]]
    """

    x_list = [tuple(x_init)]  # init x buffer
    t_list = [t_start]

    tk = t_start
    tk1 = tk + delta_t

    # to make t_end the last element of t_list
    t_end += ((-0.5) * delta_t)

    # time step loop
    while tk < t_end:
        xk = x_list[-1]

        # step 1 : same as forward Euler
        sk = f(xk, tk)
        xk1_p = [(x + sk[i] * delta_t) for i, x in enumerate(xk)]

        # step 2 : calculate slope at (xk + f(xk, tk) * delta_t, tk + delta_t)
        sk1_p = f(xk1_p, tk1)

        # step 3 : average of f(xk, tk) and f(xk + f(xk, tk) * delta_t, tk + delta_t)
        sk_c = [(0.5 * (s + sk1_p[i])) for (i, s) in enumerate(sk)]

        # step 4 : go forward using averaged slope
        xk1_c = [(x + sk_c[i] * delta_t) for i, x in enumerate(xk)]

        x_list.append(xk1_c)

        # time advance
        tk += delta_t
        tk1 += delta_t

        # append time
        t_list.append(tk)

    return t_list, x_list


def runge_while(f, x_init, t_init, t_end, delta_t):
    """
    Runge Method Solver
    Usage: listT, listX = runge_while(f, x_init, t_init, t_end, delta_t)

    Calculate four slopes and take weighted average

    Parameters
    ----------
    f : callable(x, t)
        Computes the derivatives of x at 0.
        Returns a list of [x_init, x1, ... ]
    x_init : list or tuple
        Initial state of x
    t_init : float
        Initial time
    t_end : float
        Ending time
    delta_t : float
        Sampling time

    Returns
    -------
    t_list : list, shape(int(te-ti)/deltaT + 1,1)
    x_list : list, shape(int(te-ti)/deltaT + 1,len(x_init))


    Examples
    --------
    >>> list_t, list_x = runge_while(lambda x, t:[(math.sin(math.pi*t) - x[0])*0.5],[0],0.0, 0.5, 0.1)
    >>> print list_t
    [0.0, 0.10000000000000001, 0.20000000000000001, 0.30000000000000004, 0.40000000000000002, 0.5]
    >>> print list_x
    [[0], [0.0076608912592762328], [0.029394418941171337], [0.062350250267466614], [0.10261479161461737], [0.14559255884915154]]
    """

    listX = [x_init]  # init x buffer
    listT = [t_init]

    deltaThalf = 0.5 * delta_t
    deltaTsixth = delta_t / 6.0

    tk = t_init
    tk_half = tk + deltaThalf
    tk1 = tk + delta_t

    # time step loop
    while tk < t_end:
        xk = listX[-1]

        # step 1
        k1 = f(xk, tk)

        # step 2
        xk1_p = [(xk[i] + k * deltaThalf) for (i, k) in enumerate(k1)]
        k2 = f(xk1_p, tk_half)

        # step 3
        xk2_p = [(xk[i] + k * deltaThalf) for (i, k) in enumerate(k2)]
        k3 = f(xk2_p, tk_half)

        # step 4
        xk3_p = [(xk[i] + k * delta_t) for (i, k) in enumerate(k3)]
        k4 = f(xk3_p, tk1)

        # step 5
        xk1_c = [x + deltaTsixth * (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) for (i, x) in enumerate(xk)]

        listX.append(xk1_c)
        tk += delta_t
        tk_half += delta_t
        tk1 += delta_t
        listT.append(tk)

    return listT, listX


tau = 0.5
m_kg = 10.0
c_newton_per_meter_per_sec = 100.0
k_newton_per_meter = 1000.0


def func(xk, tk):
    """
    Differential equation

    m_kg x2dot(t) + c_newton_per_meter_per_sec xdot(t) + k_newton_per_meter x(t) = u(t)
    u(t) = 1

    Use m_kg, c_newton_per_meter_per_sec, k_newton_per_meter defined outside of this function

    Parameters
    ----------
    xk: state vector at time step k_newton_per_meter
        xk[0] = x
        xk[1] = xdot

    Returns
    -------
    ydot : list of derivatives
    """
    # step input
    u = 1

    y1, y2 = xk[0], xk[1]

    y1dot = y2
    y2dot = (u - (k_newton_per_meter * y1 + c_newton_per_meter_per_sec * y2)) / m_kg

    return (y1dot, y2dot)


# end of function func()


def exact(t):
    """
    Exact solution of a  1-DOF mechanical vibration
    Ref : Rao, Mechanical Vibration, 2nd ed,
        ISBN 0-201-55693-6, Example 4.3
    """
    # step input
    u = 1
    # natural frequency (rad/sec)
    wn = sqrt(k_newton_per_meter / m_kg)
    # damping ratio
    zeta = c_newton_per_meter_per_sec / (2.0 * m_kg * wn)

    s = sqrt(1.0 - zeta * zeta)
    s1 = 1.0 / s

    # damped frequency (rad/sec)
    wd = wn * s
    # phase (rad)
    phi = atan(zeta * s)

    y1 = (u / k_newton_per_meter) * (1.0 - s1 * exp(-zeta * wn * t) * cos(wd * t - phi))

    return (y1)


# end of function exact()


def main():
    help(fwd_euler)

    ti = 0.0
    te = 2.0
    delta_T = 0.01
    x0 = (0.0, 0.0)
    vT, vX = fwd_euler(func, x0, ti, te, delta_T)
    t_list_mod_euler, x_list_mod_euler = mod_euler(func, x0, ti, te, delta_T)
    t_list_runge, x_list_runge = runge_while(func, x0, ti, te, delta_T)

    delta_T = 0.001
    vT01, vX01 = fwd_euler(func, x0, ti, te, delta_T)

    # exact solution
    vXexact = tuple([exact(tk) for tk in vT])

    # 그래프 그리기 관련 기능 등을 담고 있는 pylab 모듈을 불러 들임
    import pylab

    pylab.plot(vT, vX, 'b', label='fwd Euler(0.01)')
    pylab.plot(vT01, vX01, 'g', label='fwd Euler(0.001)')
    pylab.plot(t_list_mod_euler, x_list_mod_euler, '*', label='Modified Euler(0.01)')
    pylab.plot(t_list_runge, x_list_runge, 'x-', label='Runge(0.01)')
    pylab.plot(vT, vXexact, 'ko-', label='exact')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('x')
    pylab.xlabel('t')
    pylab.show()

    vP, vV = zip(*vX)
    vP01, vV01 = zip(*vX)
    p_list_mod_euler, v_list_mod_euler = zip(*x_list_mod_euler)
    p_list_runge, v_list_runge = zip(*x_list_runge)

    pylab.plot(vP, vV, label='fwd Euler (0.01)')
    pylab.plot(vP01, vV01, label='fwd Euler(0.001)')
    pylab.plot(p_list_mod_euler, v_list_mod_euler, label='Modified Euler(0.01)')
    pylab.plot(p_list_runge, v_list_runge, label='Runge(0.01)')
    pylab.legend(loc=0)
    pylab.grid(True)
    pylab.ylabel('xdot')
    pylab.xlabel('x')
    pylab.show()


if "__main__" == __name__:
    main()
