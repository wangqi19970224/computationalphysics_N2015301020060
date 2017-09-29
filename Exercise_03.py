import numpy as np
import matplotlib.pyplot as plt

plt.figure()
V = [0]
t = [0]
g = -9.8
dt = 0.25
end_time = 10
for i in range(int(end_time/dt)):      
    V.append(V[i] + g * dt)    
    t.append(dt*(i+1))  
    print(t[-1], V[-1])
plt.plot(t,V,label="V(t)",color="red",linewidth=1)
plt.xlabel("t(s)") 
plt.ylabel("V(m/s)") 
plt.legend()  
plt.show()


