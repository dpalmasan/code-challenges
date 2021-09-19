# Arreglos (Arrays)

## Matriz en Espiral

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
