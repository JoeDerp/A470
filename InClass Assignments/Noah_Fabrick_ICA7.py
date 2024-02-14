import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Part 1
A = np.array([[1,3,5],[2,5,1],[2,3,8]])
B = np.array([[10],[8],[3]])
A_inv = sp.linalg.inv(A)
A_det = sp.linalg.det(A)
A_norm = sp.linalg.norm(A)
A_eigVal, A_eigVec = sp.linalg.eig(A)
A_U,A_s,A_Vh = sp.linalg.svd(A)
A_p,A_l,A_u = sp.linalg.lu(A)

print(A_det)
print(A_norm)
print(A_u)

# Part 2
def vanDerPol(y, t):
    xBar, xBarDot = y
    dydt = [xBarDot, (1-xBar**2)*xBarDot-xBar]
    return dydt

y0 = np.linspace(-5,5)
dy0 = np.linspace(-5,5)
t = np.linspace(0, 20, 1001)

fig, ax = plt.subplots()
for i in range(len(y0)):
    sol = sp.integrate.odeint(vanDerPol, [y0[i],dy0[i]], t)
    ax.plot(sol[:, 0],sol[:, 1])
plt.show()
