import math
from typing import List

GMs = (1.32712440018) * 1e20


def f1(x: float, y: float) -> float:
    return GMs * x / math.sqrt((x * x + y * y) ** 3)


def f2(x: float, y: float) -> float:
    return GMs * y / math.sqrt((x * x + y * y) ** 3)


def calc(
    x0: float,
    y0: float,
    vx0: float,
    vy0: float,
    t0: float,
    tmax: float,
    dt: float = 0.1,
) -> List[List[float]]:
    """
    Inputs:
    x0: Inital Position (x component)
    y0: Initial Position (y component)
    vx0: Initial Velocity (x component)
    vy0: Initial Velocity (y component)
    t0: Initial Time
    tmax: Final Time
    dt: Step Size (generally 0.1)

    Output:
    Trajectory 2D vector = number_of_time_steps*(x, y, vx, vy)
    """

    x, y = x0, y0
    vec = [x0, y0, vx0, vy0]
    Traj = []
    while t0 <= tmax:
        val = [0.0] * 4
        x = vec[0]
        y = vec[1]
        k1x = dt * vec[2]
        k1y = dt * vec[3]
        k1vx = dt * f1(x, y)
        k1vy = dt * f2(x, y)

        k2x = dt * (vec[2] + 0.5 * k1vx)
        k2y = dt * (vec[3] + 0.5 * k1vy)
        k2vx = dt * f1(x + k1x, y + k1y)
        k2vy = dt * f2(x + k1x, y + k1y)

        k3x = dt * (vec[2] + 0.5 * k2vx)
        k3y = dt * (vec[3] + 0.5 * k2vy)
        k3vx = dt * f1(vec[0] + 0.5 * k2x, vec[1] + 0.5 * k2y)
        k3vy = dt * f2(vec[1] + 0.5 * k2x, vec[1] + 0.5 * k2y)

        k4x = dt * (vec[2] + k3vx)
        k4y = dt * (vec[3] + k3vy)
        k4vx = dt * f1(vec[0] + k3x, vec[1] + k3y)
        k4vy = dt * f2(vec[0] + k3x, vec[1] + k3y)

        vec[0] += k1x / 6 + k2x / 3 + k3x / 3 + k4x / 6
        vec[1] += k1y / 6 + k2y / 3 + k3y / 3 + k4y / 6
        vec[2] += k1vx / 6 + k2vx / 3 + k3vx / 3 + k4vx / 6
        vec[3] += k1vy / 6 + k2vy / 3 + k3vy / 3 + k4vy / 6

        val[0] = vec[0]
        val[1] = vec[1]
        val[2] = vec[2]
        val[3] = vec[3]

        t0 += dt
        Traj.append(val)

    return Traj
