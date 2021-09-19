from sols.strings.look_and_say import next_sequence
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.optimize


plt.style.use("seaborn")
plt.rcParams["figure.figsize"] = (6,4)
plt.rcParams["figure.dpi"] = 200

curr_seq = "1"
n = 15
ns = np.zeros(n)
lengths = np.zeros(n)
for i in range(0, n):
    ns[i] = i + 1
    lengths[i] = len(curr_seq)
    curr_seq = next_sequence(curr_seq)

nns = np.linspace(1, 15)
coefs = scipy.optimize.curve_fit(lambda t,a,b: a*np.exp(b*t),  ns,  lengths)
fitted_lengths = coefs[0][0]*np.exp(coefs[0][1]*nns)
plt.plot(nns, fitted_lengths, "b-")
plt.plot(ns, lengths, "r.")
plt.xlabel("n (elemento secuencia)")
plt.ylabel("largo del string (elemento secuencia)")
plt.legend((
    f"${coefs[0][0]:.2f} \\cdot exp\left({coefs[0][1]:.2f} \\cdot n\\right)$",
    "Datos"))
plt.title("Comportamiento Secuencia Look-and-Say")
plt.show()