# @Time    : 2020/4/18 21:42
# @Author  : gzzang
# @File    : _template
# @Project : comparison


import time
import numpy as np

n = int(1e6)


def function1():
    for _ in range(n):
        a = np.power(2, 4)


def function2():
    for _ in range(n):
        a = 2 * 2 * 2 * 2


def function3():
    for _ in range(n):
        a = 2 ** 4


function_list = [function1, function2, function3]

for i, function in enumerate(function_list):
    start_time = time.time()
    function()
    end_time = time.time()
    print(f'{i}:{end_time - start_time}')

# 0:1.5688252449035645
# 1:0.02894115447998047
# 2:0.03585624694824219
