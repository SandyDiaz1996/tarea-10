class Ordenar:
    def __init__(self, lista):
        self._lista = lista

    def burbuja(self):
        for i in range(len(self._lista)):
            for j in range(i+1, len(self._lista)):
                if self._lista[i] > self._lista[j]:
                    aux = self._lista[i]
                    self._lista[i] = self._lista[j]
                    self._lista[j] = aux

    def insertar(self, valor):
        self.burbuja()
        aux_lista = []
        enc = False
        for pos, ele in enumerate(self._lista):
            if ele > valor:
                aux_lista.append(valor)
                enc = True
                break
        if enc: self._list = self._lista[0:pos] + aux_lista + self._lista[pos:]
        else: self._lista.append(valor)
        return self._lista

    def insertar2(self, valor):
        self.burbuja()
        aux_lista = []
        enc = False
        for pos, ele in enumerate(self._lista):
            if ele > valor:
                enc = True
                break
        if enc:
            for i in range(pos):
                aux_lista.append(self._lista[i])
            aux_lista.append(valor)
            for j in range(pos, len(self._lista)):
                aux_lista.append(self._lista[j])
            self._lista = aux_lista
            self._lista = self._lista[0:pos] + aux_lista + self._lista[pos:]
        else:
            self._lista.append(valor)
        return self._lista


o1 = Ordenar([10, 15, 20, 70, 80])
o1.insertar(5)
o1.burbuja()
print(o1._lista)