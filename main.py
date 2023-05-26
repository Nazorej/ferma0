# Поиск не целых x³+y³=z³
# Автор: https://qna.habr.com/user/mayton2019
import random
from math import exp, log

def power(y:float, x:float) -> float:
    return exp(y * log(x))

def cubeRoot(x:float) -> float:
    return power(1.0/3.0, x)

for i in range(1, 21):
    x = 1.0 + 15.0 * random.random()
    y = 1.0 + 15.0 * random.random()
    print(f"{x}^3 + {y}^3 = {cubeRoot(x*x*x+y*y*y)}^3")