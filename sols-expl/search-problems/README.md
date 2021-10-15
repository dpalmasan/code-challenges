# Problemas de Búsqueda

## Búsqueda de Palabras [#6][i6]

Este problema puede ser resuelto vía _backtracking_, esto es, explorando diferentes acciones y deshaciendo acciones que no lleven a una solución. Por otro lado, explorar a fuerza bruta todo el tablero puede hacer que el problema no se pueda resolver en tiempos razonables, es por ello, que se debe _podar_ el espacio de búsqueda para generar una búsqueda más eficiente. Antes de comenzar con la solución hay que notar un par de casos de borde:

* El largo de la palabra de entrada es mayor que la cantidad de celdas de la matriz. En este caso no existe solución por lo tanto, no hay que perder tiempo en buscar.
* La matriz no contiene las letras necesarias para formar la palabra. Este es otro caso en el cual no queremos explorar una solución ya que sabemos de antemano que no existe.

Teniendo en cuenta los puntos anteriores, el problema se puede resolver con los siguientes enfoques:

* Modelar el problema como un problema de búsqueda, y asignar a cada _estado_ (nodo), la información sobre la búsqueda
* Utilizar un enfoque recursivo simple, en el cual se hacen y deshacen acciones para continuar la búsqueda

### Modelar como un problema de búsqueda


### Recursión

[i6]: https://github.com/dpalmasan/code-challenges/issues/16