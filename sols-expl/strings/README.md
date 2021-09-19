# Strings

## Look and Say

### Entendiendo el problema

Primero se debe entender el problema, ya que según la descripción el `string` siguiente depende del anterior. Por ejemplo:

* `1` se lee como _un uno_, por lo tanto el elemento siguiente en la secuencia es `11`
* `11` se lee como _dos unos_, por lo que el elemento siguiente es `21`
* `21` se lee como _un dos un uno_, por lo que el elemento siguiente es `1211`
* `1211` se lee como _un uno, un dos, dos unos_, por lo que el elemento siguiente es `111221`

Se observa el patrón, en que básicamente se cuenta cada elemento y se agrega a la siguiente secuencia como `{conteo}{valor}`

### Algoritmo

Primero debemos resolver el problema de, dado un `string`, encontrar el siguiente elemento de la secuencia. El algoritmo es bastante intuitivo, básicamente se debe contar las ocurrencias de cada elemento y luego agregar al string de salida el valor `{contep}{valor}`. En la siguiente animación se muestra cómo funcionaría esta secuencia de pasos:

![Alt text](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/92247f4305095ce6fd3b110fe9f6b0c29df55b14/look-and-say.gif "Look and Say next")

El algoritmo que implementa este procedimiento:

```
algoritmo next_sequence:
  entrada: seq
  salida: next_seq

  curr_val = seq[0]
  count = 0
  next_seq = ""
  N = length(seq)
  for i = 0 to N:
      if seq[i] == curr_val:
          count += 1
      else:
          next_seq += "${count}${curr_val}"
          count = 1
          curr_val = seq[i]

  if count > 0:
      next_seq += "{count}{curr_val}"
    return next_seq
```

Finalmente para imprimir la secuencia:

```
algoritmo look_and_say_seq
  entrada: n
  curr_seq = "1"
  for i = 1 to n
    print(curr_seq)
    curr_seq = next_sequence(curr_seq)
```

### Preguntas de Seguimiento

* ¿Cómo escala el tamaño de la salida?
* ¿Cuál es el dígito máximo que puede existir en la salida?
* ¿Cuál es la única secuencia que nunca crece en tamaño?

Para la pregunta uno, la intuición dice que escalará de manera exponencial (al menos al ejecutar el código y hacer un breve análisis). Si vamos al detalle, se tiene:

![Alt text](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/60672ff610e32ae04dc0fcd55f5b86bb1371ae3c/look-and-say-exp.png "Look and Say exp")

Para generar el gráfico se utilizó el siguiente código:

```python
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
```

El dígito máximo que puede existir en la salida, comenzando desde el string `1` es `3`. La razón de ello es que no se puede generar la secuencia `1111` comenzando desde `1`. Sólo se puede llegar a `12` que se lee como _Un uno, un dos_, pero no existe una forma de llegar a `un uno un uno`, ya que estaríamos cancelando al leerlo como `2 unos`.

Finalmente, la única secuencia que no cambia es `22`, porque se lee como _dos dos_ que es `22`.
