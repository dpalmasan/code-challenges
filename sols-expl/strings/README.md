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

## One Edit Apart (#8)

La primera observación que hay que tener en este problema, es que si el largo de los strings difiere en 2 o más, significa que se necesita más de una edición para convertir `s1` en `s2`, por lo tanto para este caso siempre deberíamos retornar `false`. Por ejemplo si consideramos los strings `"c"` y `"cat"`, necesitamos o insertar dos caracteres en `"c"` o eliminar dos caracteres en `"cat"`. Esta regla nos da una idea de cómo podemos abordar el problema, debido a la simetría de las operaciones.

Primero debemos chequear si `|s1 - s2| <= 1`, en caso contrario siempre retornamos `false`. Luego, podemos definir `s1'` y `s2'`, tal que `s1'.length >= s2'.length`. En esta definición tenemos un caso de borde extra, por ejemplo si `s1'` o `s2'` son de largo 1, significa que siempre van a estar a una distancia de edición o menos. Por lo tanto retornamos `true`.

Finalmente, debemos considerar los siguientes 3 casos para `s1'` y `s2'`:

* `"cat"` y `"at"`
* `"cat"` y `"ca"`
* `"cat"` y `"cut"`

Para el primer caso, chequeamos el primer caracter y lo "ignoramos" si es diferente. Luego, iteramos sobre `s2'` y contamos las diferencias. Si hay más de dos diferencias, significa que los strings no están a una distancia de edición igual 1 y por lo tanto retornamos `false`, en caso contrario, retornamos `true`. Se llega al siguiente algoritmo:

```
algoritmo one_edit_apart:
  entrada: s1, s2
  salida: true si s1 y s2 están a una distancia de edición igual a 1, false en caso contrario

  len_diff = |s1.length - s2.length|

    if len_diff > 1:
        return false

    if s1.length > s2.length:
        s1' = s1
        s2' = s2
    else:
        s1' = s2
        s2' = s1

    if s1'.length == 1:
        return True

    diffs = 0

    # Caso de borde
    s1_idx = 1 if s1p[0] != s2p[0] else 0
    for s2_idx = 0 to s2'.length - 1
        if s1_idx < s1'.length and s2'[s2_idx] != s1'[s1_idx]:
            if diffs < 1 and len_diff > 0:
                s1_idx += 1
            diffs += 1
        s1_idx += 1
    return diffs <= 1
```