import numpy as np
import matplotlib.pyplot as plt

def dyn_generator(oper, state):
    """ -i[O,y(t)].

    "O" es un operador lineal, i es la variable compleja, "y(t)" es una funcion dependiente del tiempo.
    para terminos de esta implementacion utilizaremos  NumPy importada como "np".

    Examples:
        oOper operador lineal.
        yInit estado inicial.

        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> dyn_generator(oOper, yInit)
       
    Args:
        oper (Numpy array): primer argumento (operador lineal).
        state (Numpy array): Segundo argumento (estado inicial).

    Returns:
        (Numpy array): devuelve el resultado de applicar el operador -i[A.B] = -i(AB - BA), siendo un conmutador.
    """
    return (np.dot(oper, state) - np.dot(state, oper)) * (-1.0j)

def rk4(func, oper, state, h):
    """ Runge-Kutta 4, aplicado a una funcion que no depende del tiempo.

    Este es el metodo numerico en el que se basa todo el codigo

    Args:
        func (Function): primer argumento. Esta sera la funcion a la cual le estaremos aplicando el Rk4 en este caso seria lo obtenido de dyn_generator
        oper (Numpy array): Segundo argumento (operador lineal)
        state (Numpy array): Tercer argumento. Nos permite ir cambiando el estado inicial respecto al paso temporal
        h (float): paso temporal 

    Returns:
        (Numpy array): Retorna el estado del sistema dinamico respecto a un tiempo especifico

    Examples:
        >>> oOper = np.array([[0, 1], [1, 0]])
        >>> yInit = np.array([[1, 0], [0, 0]])
        >>> times=np.linspace(0,10,150)
        >>> h= times[1]-times[0]
        >>> print(rk4(dyn_generator,oOper, yInit, h))
     
    """
    k1 = h*func(oper,state)
    k2 = h*func(oper,state+(k1/2))
    k3 = h*func(oper,state+(k2/2))
    k4 = h*func(oper,state+k3)
    return state + (1/6)*(k1+(2*k2)+(2*k3)+k4)
