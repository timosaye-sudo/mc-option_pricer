import math
import random


def increment_brownien(dt):
    return math.sqrt(dt) * random.gauss(0, 1)


def prix_gbm(s0, mu, sigma, t, W):
    return s0 * math.exp((mu - 0.5 * sigma**2) * t + sigma * W)


def simule_trajectoire(s0, mu, sigma, T, n_pas):
    dt = T / n_pas
    trajectoire = [s0]
    W = 0.0

    for i in range(1, n_pas + 1):
        W += increment_brownien(dt)
        t = i * dt
        prix = prix_gbm(s0, mu, sigma, t, W)
        trajectoire.append(prix)

    return trajectoire


def simule_trajectoires(
    s0: float,
    mu: float,
    sigma: float,
    T: float,
    n_pas: int,
    n_trajectoires: int,
    seed: int | None = None,
) -> list[list[float]]:
    if seed is not None:
        random.seed(seed)
    return [simule_trajectoire(s0, mu, sigma, T, n_pas) for i in range(n_trajectoires)]


if __name__ == "__main__":
    # la moyenne des prix finaux doit être proche de 100 * exp(0.04) = 104.08
    trajectoires = simule_trajectoires(
        100, 0.04, 0.2, 1, n_pas=10, n_trajectoires=20000, seed=0
    )
    moyenne = sum(trajectoire[-1] for trajectoire in trajectoires) / len(trajectoires)
    print(f"Moyenne des prix finaux : {moyenne:.2f}")
