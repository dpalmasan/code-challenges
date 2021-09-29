# Arreglos (Arrays)

## Matriz en Espiral ([#3][i3])

### Entendiendo el problema

Se debe observar que lo que se genera es una matriz en espiral que tiene un punto de partida y un punto final

![Alt text](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/75640cce34c03b3848ef48114d49d0482e10995b/spiral-pattern.png "Matriz Espiral")

Una matrz en espiral siempre comienza con `1` y termina con el número total de elementos `nxn`.

### Solución Recursiva

Podemos generalizar el problema. En lugar rellenar con valores la matriz completa, podemos considerar llenar sólo los bordes.  

![Alt text](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/75640cce34c03b3848ef48114d49d0482e10995b/spiral-recursive.png "Caso General")

Podemos notar, que para la matriz original, el valor inicial siempre será 1, e irá aumentando en 1 a medida que se recorre la espiral. Por otro lado, podemos ver que el problema se descompuso en 2 sub-problemas, llenar el borde de la matriz y llenar la matriz interna. Se puede observar una recursión en este caso, pues al llenar el borde de una matriz, luego se debe llenar la matriz nueva contenida dentro del borde cuya única diferencia será el valor inicial.

Por otro lado, podemos notar que existen dos casos posibles `n` es par o impar. Para el caso de `n` par, el caso base será una matriz de `2x2`, para el caso de `n` impar, el caso base será una matriz de `1x1` (se debe notar que la siguiente matriz a procesar es siempre de dos dimensiones menos que la matriz original, es decir `n - 2 x n - 2`).

Ahora podemos crear un algoritmo para llenar el borde de la matriz, este algoritmo se definirá como sigue:

```
algoritmo traversal:
  entradas: m: int[][], pos: int, n: int, start: int 
  salida: Valor inicial del siguiente subproblema

  for i = pos to n - 1:
      m[pos][i] = start
      start += 1

    for j = pos + 1 to n - 1
      m[j][i] = start
      start += 1

    for i = n - 2 to pos - 1
      m[j][i] = start
      start += 1

    for j = n - 2 to pos, -1:
      m[j][i] = start
      start += 1

    return start
```

Este algoritmo básicamente itera por todas las filas y columnas del borde de la matriz `m`. Cabe destacar que esta es una versión simple, cuyo tiempo de ejecución es O(4*n). Utilizando información de la matriz, se puede optimizar a O(n), pero esto ya es una micro-optimización, la cual está en las soluciones.

Ahora necesitamos definir el paso recursivo:

```
algoritmo recursive-traversal:
  entradas: m: int[][], pos: int, n: int, start: int 
  salida: Valor inicial del siguiente subproblema
  # Caso base para n impar
  if n - pos == 1:
    m[pos][pos] = start
    return

  # Caso base para n par
  if n - pos == 2:
    m[pos][pos] = start
    m[pos][pos + 1] = start + 1
    m[pos + 1][pos + 1] = start + 2
    m[pos + 1][pos] = start + 3
    return

  # Llenar bordes
  start = traversal(m, pos, n, start)

  # Resolveer subproblema
  recursive_traversal(m, pos + 1, n - 1, start)
```

Finalmente, podemos escribir el procedimiento `spiral` para generar la matriz en espiral:

```
algoritmo spiral
  entrada: n: int
  salida: m: int[][]
  
  # Para entradas inválidas arrojamos error
  if n <= 0:
    throw Exception()

  m = Inicializar Matriz de nxn
  recursive_traversal(m, 0, n, 1)
  return m
```

### Solución Iterativa

Por otro lado, también podemos utilizar un enfoque _greedy_, en el que visitamos cada celda y cambiamos la dirección de movimiento a medida que encontramos algún problema (i.e. fuera de límites, o celda ya fue visitada). El algoritmo sería como sigue:

```
algoritmo spiral-iterativo
  entrada: n: int
  salida: m: int[][]
  
  # Para entradas inválidas arrojamos error
  if n <= 0:
    throw Exception()

  m = Inicializar Matriz de nxn
  dir_row = (0, 1, 0, -1)
  dir_col = (1, 0, -1, 0)
  dir = 0
  val = 1
  while val <= n*n:
    m[row][col] = val
    row += dir_row[cur_dir]
    col += dir_col[cur_dir]
    if invalid_position(m, row, col):
      row -= dir_row[cur_dir]
      col -= dir_col[cur_dir]
      cur_dir = (cur_dir + 1) % 4
      row += dir_row[cur_dir]
      col += dir_col[cur_dir]
    val += 1
  return m
```

Este enfoque es menos propenso a errores al ser programado.

## Suma de diferencias absolutas [#10][i10]

### Enfoque Naïve

Podemos resolver el problema a fuerza bruta, iterando por cada elemento para calcular el elemento en el `array` de salida. El algoritmo sería:

```
algoritmo naive-sum-abs-diff
  entrada: nums: int[]
  salida: result: int[]
  
  N = nums.length
  result = new int[N]
  for i = 0 to N - 1:
    for j = 0 to N - 1:
      if i == j:
        continue
      result[i] += |nums[i] - nums[j]| 

  return result
```

Este algoritmo tiene una complejidad `O(n^2)`. 

* ¿Podemos hacerlo más eficiente?
* ¿Estamos utilizando toda la información?

### Enfoque optimizado

¿Qué información extra tenemos en el problema? Se dice que el `array` se encuentra ordenado, ¿Se puede usar esta información para hacer un algoritmo más eficiente?

Probemos con el siguiente ejemplo: `[1, 5, 10, 13]`. El resultado debiese ser:

* `result[0] = |1 - 5| + |1 - 10| + |1 - 13| = 25`
* `result[1] = |5 - 1| + |5 - 10| + |5 - 13| = 17`
* `result[2] = |10 - 1| + |10 - 5| + |10 - 13| = 17`
* `result[3] = |13 - 1| + |13 - 5| + |13 - 10| = 23`

También tenemos que la suma total de los elementos es `1 + 5 + 10 + 13 = 29`, y la suma acumulada es `[0, 1, 6, 16, 29]`. Por otro lado la suma de las diferencias absolutas siempre será `<=` que la suma de los elementos, ya que los elementos son todos positivos. Como los elementos están ordenados de forma creciente, desde `0` hasta el elemento `i`, hemos agregado a la suma `i * nums[i]`, por ejemplo en el caso `results[2]`, tenemos `|10 - 1| + |10 -5| = 10 - 1 + 10 - 5 = 2 * 10 - 1 - 5`. También podemos observar que estamos restando la suma acumulada hasta el elemento `i`, siguiendo el ejemplo tenemos  `|10 - 1| + |10 -5| = 2 * 10 - (1 + 5)`. También observamos que desde `i` en adelante estamos quitando `n - i - 1` veces el elemento `nums[i]`. Por ejemplo, para el caso `i = 0`, tenemos `|1 - 5| + |1 - 10| + |1 - 13| = 5 + 10 + 13 - 1 - 1 - 1 = 5 + 10 + 13 - (4 - 0 - 1) * 1`. El término `5 + 10 + 13` es la suma acumulada desde `i + 1` en adelante. Finalmente, generalizando llegamos a:

* `result[i] = cumsum[n] - cumsum[i + 1] - nums[i] * (n - i - 1) - cumsum[i] + nums[i] * i`

Por lo tanto, llegamos al siguiente algoritmo:

```
algoritmo sum-abs-diff
  entrada: nums: int[]
  salida: result: int[]
  
  # cumsum se inicializa con ceros
  cumsum = new int[N + 1]
  for i in 1 to N:
    cumsum[i] = cumsum[i - 1] + nums[i - 1]

  result = new int[nums.length]
  for i = 0 to N - 1:
    result[i] = cumsum[n] - cumsum[i + 1] - nums[i] * (n - i - 1) - cumsum[i] + nums[i] * i

  return result
```

En este caso podemos observar un intercambio memoria/tiempo de ejecución, ya que ahora la complejidad en tiempo de ejecución es `O(N)`, y la complejidad en memoria es también `O(N)` ya que necesitamos pre-calcular la suma acumulada.

### Enfoque optimizado en memoria

Tomando ideas del enfoque optimizado, podemos darnos cuenta que no necesitamos pre-calcular la suma acumulada, y podemos hacer el cálculo _in place_ si modificamos el algoritmo como sigue:

```
algoritmo sum-abs-diff-mem-opt
  entrada: nums: int[]
  salida: result: int[]
  
  total_sum = 0
  for i in 1 to N:
    total_sum += nums[i]

  result = new int[nums.length]
  cum_sum = 0
  cum_sum_next = 0
  for i = 0 to N - 1:
    cum_sum_next += nums[i]
    result[i] = total_sum - cum_sum_next - nums[i] * (n - i - 1) - cum_sum + nums[i] * i
    cum_sum += nums[i]

  return result
```

En este caso, la complejidad en tiempo es `O(N)`, pero se redujo la complejidad en memoria a `O(1)`.


## Rotar array `k` veces hacia la derecha [#18][i18]

### Enfoque Simple

Primero debemos pensar, qué pasa si `k >= nums.length`. En este caso, como son rotaciones, tenemos básicamente ciclos que se repetirán. Para ello, es común calcular el módulo. Por ejemplo `k % nums.length` sería igual a `k` si `k < nums.length`, sería igual a `0` si `k == nums.length` y sería igual a `3` si `k == nums.length + 3`. Por lo tanto, podemos definir `k' = k % nums.length`. Como debemos mover al menos todos los elementos del `array` `k` veces, la complejidad en tiempo de ejecución tiene como límite inferior ser `O(n)`.

Para simplificar el problema, podemos crear una copia del `array` original, y el algoritmo quedaría como sigue:

```
algoritmo rotate-o_n
  entrada: nums: int[], k
  
  k' = k % len(nums)
  if k' == 0:
      return
  backup = new int[nums.length]

  # Se asume índices comienzan de 0
  for i = 0 to nums.length - 1:
    backup[i] = nums[i]

  for i = 0 to nums.length - 1:
      new_idx = (i + k') % nums.length
      nums[new_idx] = backup[i]
```

Este algoritmo tiene una complejidad de `O(n)` en tiempo de ejecución y `O(n)` en memoria. ¿Se puede hacer en `O(1)` en memoria?


[i3]: https://github.com/dpalmasan/code-challenges/issues/3
[i10]: https://github.com/dpalmasan/code-challenges/issues/10
[i18]: https://github.com/dpalmasan/code-challenges/issues/18