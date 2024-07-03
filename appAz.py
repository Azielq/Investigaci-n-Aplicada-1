from os import system

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Pila:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.isEmpty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data
    
    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count

class Cola:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.isEmpty():
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data
    
    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count

class Lista:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        return elements

if __name__ == "__main__":
    while True:
        print("""
                #### 1)Pilas ######
                #### 2)Colas ######                   
                #### 3)Listas #####
                #### 0)Para salir #### """)
        user = int(input("Que opcion quieres ver?[Marcala con un numero]: "))
        if user == 1:
            appPila = Pila()
            print("la pila actualmente esta vacia: ", appPila.isEmpty())
            input("Ok, vamos hacer una pila con tres parametros [presiona enter para continuar: ]")
            print("Vamos a llenar la pila")
            userParametro1 = input("Pasame el primer parametro: ")
            userParametro2 = input("Pasame el segundo parametro: ")
            userParametro3 = input("Pasame el tercer parametro: ")
            appPila.push(userParametro1)
            appPila.push(userParametro2)
            appPila.push(userParametro3)
            input("presiona enter para ver el top de la pila: ")
            print("el top de la pila es: ", appPila.peek())
            input("presiona enter para ver el tamaño de la pila")
            print("el tamaño de la pila es de: ", appPila.size())
            input("presiona enter para eliminar el utlimo parametro de la pila")
            print("el parametro: ", appPila.pop(), "se ha eliminado de la pila")
            input("presiona enter para volver al menu")
            system("clear")

        elif user == 2:
            appCola = Cola()
            print("la cola actualmente esta vacia: ", appCola.isEmpty())
            input("Ok, vamos hacer una cola de tres personas [presiona enter para continuar: ]")
            userParametro1 = input("Pasame la primera persona de la cola: ")
            userParametro2 = input("Pasame la segunda persona de la cola: ")
            userParametro3 = input("Pasame la tercera persona de la cola: ")
            appCola.enqueue(userParametro1)
            appCola.enqueue(userParametro2)
            appCola.enqueue(userParametro3)
            input("press enter para ver las posiciones: ")
            print("posicion 1: ", appCola.dequeue())
            print("posicion 2: ", appCola.dequeue())
            print("posicion 3: ", appCola.dequeue())
            input("presiona enter para ver el tamaño de la cola: ")
            print(appCola.size(), "es el tamaño de la cola")
            input("presiona enter para ver el final de la cola: ")
            print(appCola.dequeue(), "es la persona que esta al final de la cola")
            input("presiona enter para volver al menu")
            system("clear")

        elif user == 3:
            appLista = Lista()
            input("Ok, vamos hacer una lista de la compra de comida con tres parametros [presiona enter para continuar: ]")
            userParametro1 = input("Pasame el primer articulo: ")
            userParametro2 = input("Pasame el segundo articulo: ")
            userParametro3 = input("Pasame el tercero articulo: ")
            appLista.add(userParametro1)
            appLista.add(userParametro2)
            appLista.add(userParametro3)
            userQuestion = input("deseas ver la lista?: [s/n]")
            if userQuestion == "s":
                print(appLista.display())
            input("presiona enter para volver al menu")
            system("clear")
        else:
            break
