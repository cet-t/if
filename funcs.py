from hashlib import md5
from os import urandom
from typing import Final as const
import matplotlib.pyplot as plt
import numpy as np

#! requirement: f(1) = 1


def randhex6():
    return '#' + md5(urandom(3)).hexdigest()[:6]


if __name__ == '__main__':
    x: const = np.linspace(0, 1, 10**5)
    fx: const = [
        x,
        x**2,
        x**3,
        x**4,
        -x**2+2*x,
        -2*x**3+3*x**2,
        (x*np.sin(((4*1+1)/2)*np.pi*x))**2,
        np.sin(x/2*np.pi),
        np.sin(x*np.pi*10)/10+x,
        1/x**-2
    ]
    for y in fx:
        plt.plot(x, y, alpha=0.75, lw=1, color=randhex6())

    plt.title('Interesting functions')
    plt.grid(True)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()
