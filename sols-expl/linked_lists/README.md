# Linked Lists

## Remover el n-ésimo nodo desde el final [#22][i22]

### Enfoque simple (dos pasadas)

Una forma simple de resolver este problema es recorrer la lista dos veces, para contar el número de elementos. Iniciamos desde el primer nodo de la lista (`head`), y llegamos hasta que no hayan elementos siguientes. Tenemos un caso de borde, que es cuando `n == sz`. En este caso, simplemente reemplazamos `head` por `head.next`.

Para cualquier otro caso, comenzamos desde el primer elemento de la lista, que tendrá un índice `idx = 1`. Debemos llegar al nodo anterior al que queremos eliminar, esto se ilustra en la siguiente figura:

![Alt text](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/829439966877ad3b36bf568764e0e91cbbd3f8f9/linked-list-nth-node-2pass.png "two pass")

De esta forma, el algoritmo queda como sigue:

```
algoritmo remove-nth-from-end-two-pass:
  entradas: (head) Primer elemento de la lista, (n): Elemento a remover desde el final
  salida: (head) Lista con nodo n eliminado

  if head == null:
    return null

  sz = 0
  pointer = head
  while pointer:
      sz += 1
      pointer = pointer.next

  # Remover primer nodo de la lista
  if n == sz:
    head = head.next
    return head
      
  pos = 1
  pointer = head

  # Encontrar nodo previo al que deseamos remover
  while sz - pos != n:
      pointer = pointer.next
      pos += 1

  pointer.next = pointer.next.next
  return head
```

Este algoritmo es `O(sz)` en complejidad de tiempo y `O(1)` en memoria. Sin embargo, necesitamos recorrer la lista dos veces. ¿Se puede lograr lo mismo en sólo una pasada a la lista?

### Enfoque de 2-punteros (una sola pasada)

Esto es una micro-optimización, ya que de todas formas la complejidad mínima para este problema será `O(sz)`, pues necesitamos recorrer toda la lista. Sin embargo, podemos utilizar dos punteros para recorrer la lista sólo una vez:

![Alt text](https://gist.githubusercontent.com/dpalmasan/103d61ae06cfd3e7dee7888b391c1792/raw/cb92ea56d23897596936947887ef5f5b490e3e5d/linked-list-nth-node.png "two pass")

En este caso, debemos encontrar `vx`, sabemos que este puntero estará a una distancia `n` desde el final, por lo que teniendo un puntero extra que se encuentre siempre a una distancia `n` del puntero rápido (en azul), entonces cuando lleguemos al final de la lista, el puntero lento (en verde) estará en `vx` y simplemente tenemos que hacer `vx.next = vx.next.next`:

```
algoritmo remove-nth-from-end:
  entradas: (head) Primer elemento de la lista, (n): Elemento a remover desde el final
  salida: (head) Lista con nodo n eliminado

  if head == null:
    return null
    
  slow_pointer = null
  pointer = head
  idx = 1
  while pointer.next:
    pointer = pointer.next
    idx += 1
    if idx - 1 == n:
      slow_pointer = head

    # Queremos llegar hasta el último nodo
    if slow_pointer and pointer.next:
      slow_pointer = slow_pointer.next

  # Queremos remover el nodo n
  if slow_pointer == null:
    head = head.next
    return head
  slow_pointer.next = slow_pointer.next.next
  return head
```

En este caso, recorremos la lista sólo una vez.

[i11]: https://github.com/dpalmasan/code-challenges/issues/22