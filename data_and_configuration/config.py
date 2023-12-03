import numpy as np

young_module = 2.1e11
poisson_ratio = 0.3
E = np.array([[1, poisson_ratio, 0],
              [poisson_ratio, 1, 0],
              [0, 0, (1 - poisson_ratio) / 2]])
E = young_module / (1 - poisson_ratio ** 2) * E

height = 2
length = 4
