# coding: utf-8

import math
import random
import numpy as np
import pandas as pd
import seaborn as sns
import pystan

df = pd.read_csv("data/conflict.dat",encoding = "utf-8", delimiter = " ")
df = df.replace(['Yes', 'No'], [1, 0])
df.shape
X = df[["a1", "a2", "a3", "a4", "a5", "a6", "a7"]]
y = df["cv"]
N = df.shape[0]
M = df.shape[1] - 1
stan_data = {'N': N, 'M':M, 'X': X, 'y': y}
fit = pystan.stan(file='d.stan', data=stan_data, iter=1000, chains=3, thin=10)
