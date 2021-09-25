# Árboles Binarios (Binary Trees)

## Zig-Zag Traversal [#11][i11]

### Caso de Borde

Primero debemos comenzar con el caso trivial, en que la raíz del árbol es `null` (caso de borde). En este caso retornamos una lista vacía, ya que no hay nodos que procesar.


### Caso General

Para el caso general, podemos reconocer que es una variación de recorrer el árbol en post-orden (_post order traversal_). Consideremos el ejemplo mostrado en la siguiente figura:

![Alt text](https://raw.githubusercontent.com/dpalmasan/code-challenges/master/imgs/binary_tree/zigzag_s1.png "Ejemplo BT")

En este ejemplo, primero visitaríamos la raíz del árbol (nodo cuyo valor es `3`). Luego _expandiríamos_ este nodo, y podríamos visitar el nodo `9` o el nodo `20`. Sin embargo, como visitamos los nodos en zig-zag, el órden sería `[20, 9]` en el nivel 2. Debemos tener en cuenta, que cada nodo a visitar se expande y deberán visitarse los hijos izquierdo y derecho de cada nodo en cada paso. Si nos detenemos a pensar, este es un caso de búsqueda en anchura o `BST` (_Breadth First Search_).

En `BST` podemos visitar los nodos del árbol por nivel, partiendo desde la raíz hasta los niveles más profundos, como se muestra en la siguiente animación:

![Alt text](https://raw.githubusercontent.com/dpalmasan/code-challenges/master/imgs/binary_tree/zigzag_steps.gif "BST")

Básicamente, debemos expandir los nodos en el órden en que se van descubriendo, y generar la lista de resultados y alternar de acuerdo al nivel. Como abstracción, supongamos que un nodo tiene el nivel al que pertenece, comenzando desde el nivel 1. Para procesar los nodos en el orden en que se descubren, necesitamos una estructura de datos tipo `FIFO` (_first in first out_), por lo cual utilizaremos una cola (`queue`). 


Primero debemos chequear si la raíz del árbol es `null`:

```
algoritmo ZigZag-Traversal:
  entrada: (root) raíz del árbol
  salida: Lista de nodos visitados por nivel en orden Zig-Zag

  if root == null:
    return []
```

El primer elemento que agregamos a la cola es la raíz del árbol, además debemos inicializar la salida como una lista vacía y un flag para indicar el orden en que estamos recorriendo el nivel (por convención lo llamamos left):

```
algoritmo ZigZag-Traversal:
  entrada: (root) raíz del árbol
  salida: Lista de nodos visitados por nivel en orden Zig-Zag

  if root == null:
    return []

  queue = new Queue()
  queue.enqueue(root)
  output = []
  nodes_in_level = []
  left = False
  current_level = root.level
```

Procesamos la cola, mientras tenga elementos que procesar (es decir, no hayamos recorrido todo el árbol) y vamos agregando nodos a medida que vamos descubriendo (es decir, si el nodo expandido tiene hijos, se agregan a la cola):

```
algoritmo ZigZag-Traversal:
  entrada: (root) raíz del árbol
  salida: Lista de nodos visitados por nivel en orden Zig-Zag

  if root == null:
    return []

  queue = new Queue()
  queue.enqueue(root)
  output = []
  nodes_in_level = []
  left = False
  current_level = root.level

  while not queue.empty():
    node = queue.dequeue()
    if node.left != null:
      queue.enqueue(node.left)
    if node.right != null:
      queue.enqueue(node.right)
```

Aquí es donde depende de la implementación anterior. Si encolamos los nodos de izquierda a derecha, entonces el siguiente nodo a procesar siempre será el de más a la derecha. Por lo tanto, cuando el flag `left` sea `False`, entonces insertamos los nodos en la lista `nodes_in_level` en orden inverso. Finalmente el algoritmo queda como:

```
algoritmo ZigZag-Traversal:
  entrada: (root) raíz del árbol
  salida: Lista de nodos visitados por nivel en orden Zig-Zag

  if root == null:
    return []

  queue = new Queue()
  queue.enqueue(root)
  output = []
  nodes_in_level = []
  left = False
  current_level = root.level

  while not queue.empty():
    node = queue.dequeue()
    if node.left != null:
      queue.enqueue(node.left)
    if node.right != null:
      queue.enqueue(node.right)

    if node.level == curr_level:
      if not left:
        nodes_in_level.insert(0, node.val)
      else:
        nodes_in_level.append(node.val)
    else:
      left = not left
      result.append(nodes_in_level)
      nodes_in_level = [node.val]
      curr_level = level
  if not nodes_in_level.empty():
    result.append(nodes_in_level)
  return result
```

[i11]: https://github.com/dpalmasan/code-challenges/issues/11