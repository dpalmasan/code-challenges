# Problemas de Búsqueda

## Búsqueda de Palabras [#6][i6]

Este problema puede ser resuelto vía _backtracking_, esto es, explorando diferentes acciones y deshaciendo acciones que no lleven a una solución. Por otro lado, explorar a fuerza bruta todo el tablero puede hacer que el problema no se pueda resolver en tiempos razonables, es por ello, que se debe _podar_ el espacio de búsqueda para generar una búsqueda más eficiente. Antes de comenzar con la solución hay que notar un par de casos de borde:

* El largo de la palabra de entrada es mayor que la cantidad de celdas de la matriz. En este caso no existe solución por lo tanto, no hay que perder tiempo en buscar.
* La matriz no contiene las letras necesarias para formar la palabra. Este es otro caso en el cual no queremos explorar una solución ya que sabemos de antemano que no existe.

Teniendo en cuenta los puntos anteriores, el problema se puede resolver con los siguientes enfoques:

* Modelar el problema como un problema de búsqueda, y asignar a cada _estado_ (nodo), la información sobre la búsqueda
* Utilizar un enfoque recursivo simple, en el cual se hacen y deshacen acciones para continuar la búsqueda

### Algoritmo

El algoritmo con _estados_ y usando Depth-First search con una pila, se puede encontrar en la solución `python` en la clase `search_problems.depth_first_search.WordSearchProblem`. En la siguiente figura, se muestra el proceso de _backtracking_, para explorar la matriz de palabras:

![Alt text](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/5116d11557f226f96c969b413761b6ce0de532a0/word_search.png "Backtracking Word Search")

El algoritmo recursivo se muestra a continuación:

```
Algoritmo word-search-dfs
  Entradas: board, word, visited, i, j, depth
  Salidas: true si la palabra fue encontrada, false en caso contrario

  # Encontramos la palabra ya que expandimos la última letra
  if depth == word.size - 1:
      return true

  # Visited es un array 1-d de Booleanos, tal que visited.size = board.rows * board.cols
  # En este caso mapeamos (i, j) -> idx donde idx es un índice de visited
  cols = len(board[0])
  visited[cols * i + j] = true

  result = False

  # Buscamos por la izquierda
  if is_valid_move(board, word, i - 1, j, visited, depth + 1):
      result = word-search-dfs(board, word, visited, i - 1, j, depth + 1)
      if result:
          return True
      visited[cols * (i - 1) + j] = false

  # Buscamos por la derecha
  if is_valid_move(board, word, i + 1, j, visited, depth + 1):
      result = word-search-dfs(board, word, visited, i + 1, j, depth + 1)
      if result:
          return true
      visited[cols * (i + 1) + j] = false

  # Buscamos arriba
  if is_valid_move(board, word, i, j - 1, visited, depth + 1):
      result = word-search-dfs(board, word, visited, i, j - 1, depth + 1)
      if result:
          return true
      visited[cols * i + j - 1] = false

  # Buscamos abajo
  if is_valid_move(board, word, i, j + 1, visited, depth + 1):
      result = word-search-dfs(board, word, visited, i, j + 1, depth + 1)
      if result:
          return True
      visited[cols * i + j + 1] = true

  # Si no podemos seguir explorando, entonces fallamos la búsqueda
  return false
```

En el algoritmo anterior, utilizamos una función auxiliar `is_valid_move`, esta chequea si la movida es válida, y se puede definir como:

```
función is_valid_move
  Entrada: board, word, i, j, visited, depth
  Salida: true si la movida es válida, false en caso contrario

  return (
    valid_position(board, i, j)
    and board[i][j] == word[depth]
    and not visited[cols * i + j]
  )
```

Básicamente chequeamos que las coordenadas(i, j) se encuentren dentro de los límites de `board`, que la posición que estamos chequeando contenga una letra válida y además que la letra no haya sido ya utilizada.

Finalmente, el algoritmo final quedaría como:

```
Algoritmo word-exists:
  Entrada: board, word
  Salida: true si la palabra se puede encontrar en el tablero

  if unfeasible(board, word):
    return false

  for i = 0 to board.size:
    for j = 0 to board[0].size:
      if board[i][j] == word[0]:
        visited = new boolean[board.size * board[0].size]
        result = word-search-dfs(board, word, visited, i, j, 0)
        if result:
            return True
```

[i6]: https://github.com/dpalmasan/code-challenges/issues/16