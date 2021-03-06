# Árboles Binarios (Binary Trees)

## Zig-Zag Traversal [#11][i11]

### Caso de Borde

Primero debemos comenzar con el caso trivial, en que la raíz del árbol es `null` (caso de borde). En este caso retornamos una lista vacía, ya que no hay nodos que procesar.


### Caso General

Para el caso general, podemos reconocer que es una variación de recorrer el árbol en post-orden (_post order traversal_). Consideremos el ejemplo mostrado en la siguiente figura:

![Alt text](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/611501be9fe2d11dad856cfa8fbe62f6eb1d3086/zigzag_s1.png "Ejemplo BT")

En este ejemplo, primero visitaríamos la raíz del árbol (nodo cuyo valor es `3`). Luego _expandiríamos_ este nodo, y podríamos visitar el nodo `9` o el nodo `20`. Sin embargo, como visitamos los nodos en zig-zag, el órden sería `[20, 9]` en el nivel 2. Debemos tener en cuenta, que cada nodo a visitar se expande y deberán visitarse los hijos izquierdo y derecho de cada nodo en cada paso. Si nos detenemos a pensar, este es un caso de búsqueda en anchura o `BST` (_Breadth First Search_).

En `BST` podemos visitar los nodos del árbol por nivel, partiendo desde la raíz hasta los niveles más profundos, como se muestra en la siguiente animación:

![Alt text](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/611501be9fe2d11dad856cfa8fbe62f6eb1d3086/zigzag_steps.gif "BST")

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

## Nodos "Buenos" en un Árbol Binario [#31][i31]

La solución de este problema es fácil de visibilizar si se piensa de forma recursiva. Lo que debemos hacer en simples términos, es guardar el valor máximo visto desde la raíz hasta un nodo `n` y propagar dicho valor a los descendientes. Si se cumple la condición de que el valor del nodo `n` es mayor que el máximo visto en el camino desde la raíz hasta dicho nodo, entonces actualizar el conteo de nodos buenos. Posteriormente, se deben visitar los hijos a la izquierda y derecha del nodo actual y seguir hasta llegar a los nodos hojas o hasta haber explorado todos los caminos posibles desde `n`. El procedimiento se muestra en la siguiente animación:

![Alt text](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/7545e3d69882e0e22bf5f09ecc51c24bde99fa04/good_nodes.gif "Good Nodes")

Dicho procedimiento es simple de implementar con un algoritmo recursivo. Cabe destacar que también se puede hacer utilizando una `stack`, al menos en las soluciones en `python` se muestran ambas posibilidades. Vamos a requerir dos métodos:

* `visit_node` (llamada recursiva)
* `count_good_nodes`

```
algoritmo visit_nodes:
  entradas: node, max_seen
  salida: good_node_count

  if node == null: return 0

  cnt = 0
  if node.val >= max_seen:
    cnt += 1

  return cnt
    + visit_nodes(node.left, max(max_seen, node.val))
    + visit_nodes(node.right, max(max_seen, node.val))


algoritmo count_good_nodes:
  entrada: root
  salida: Cantidad de nodos buenos

  return visit_nodes(root, root.val)
```

[i11]: https://github.com/dpalmasan/code-challenges/issues/11
[i31]: https://github.com/dpalmasan/code-challenges/issues/31