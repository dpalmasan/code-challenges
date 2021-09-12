# Árboles Binarios (Binary Trees)

## Zig-Zag Traversal

### Caso de Borde

Primero debemos comenzar con el caso trivial, en que la raíz del árbol es `null` (caso de borde). En este caso retornamos una lista vacía, ya que no hay nodos que procesar.


### Caso General

Para el caso general, podemos reconocer que es una variación de recorrer el árbol en orden (_in order traversal_). Consideremos el ejemplo mostrado en la figura 1.


![Alt text](https://raw.githubusercontent.com/dpalmasan/code-challenges/master/imgs/binary_tree/zigzag_s1.png "Optional Title")