import math
import random
import pandas as pd
import matplotlib.pyplot as plt
def population_maker(x, k=2, x_mid=5):
    return 1 / (1 + math.exp(-k * (x - x_mid)))
K = 1000 
P0 = 10  
r = 0.1  
T = 25    
lag_min = 5  
lag_max = 15 
exp_min = 10 
exp_max = 30 

growth_curves = []

for i in range(100): 
    lag_phase = random.randint(lag_min, lag_max)
    exp_phase = random.randint(exp_min, exp_max)
    curve = []
    
    for t in range(T):
        if t < lag_phase:
            curve.append(P0)
        elif t < lag_phase + exp_phase:
            curve.append(P0 * math.exp(r * (t - lag_phase)))
        else:
            curve.append(K / (1 + ((K - P0) / P0) * math.exp(-r * (t - lag_phase - exp_phase))))
    
    growth_curves.append(curve)
df = pd.DataFrame(growth_curves).transpose()
df.index = range(T)
df.iloc[:, :5].plot(figsize=(10, 6))
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.title('Logistic Growth Curves')
plt.show()