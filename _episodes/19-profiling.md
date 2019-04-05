---
title: Check and improve the performance of your code
teaching: 0
exercises: 0
questions:
- "How to assess the performance of Python codes?"
---

# Timing your codes

~~~
import timeit
def my_function():
    y = 3.1415
    for x in range(100):
        y = y ** 0.7
    return y

print(timeit.timeit(my_function, number=100000))
~~~
{: .language-python}

~~~
14.254935225006193
~~~
{: .output}

## Within jupyter notebooks

~~~
import time

def sleeping(arg):
    time.sleep(0.1)

%timeit list(map(sleeping, range(24)))
~~~
{: .language-python}


# Cython

- [Cython tutorial](https://github.com/kwmsmith/scipy-2017-cython-tutorial)

# [Python Performance tips](https://nyu-cds.github.io/python-performance-tips/)

{% include links.md %}
