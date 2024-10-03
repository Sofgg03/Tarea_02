# Estado a estudiar 

Se quiere estudiar la evolución temporal de un estado $\mathbf{y}(t)$. Este estado será representado mediante una matriz 2x2 que corresponde a algún operador lineal. La función que genera la dinámica del problema es 
$$
f(t, \mathbf{y}) = -{\rm{i}} [\mathbf{O}, \mathbf{y}(t)],
$$
donde $\mathbf{O}$ es otro operador lineal, ${\rm{i}}$ es la constante compleja y $[A, B] = AB - BA$ es un operación de conmutación. Note que **la función $f(t, \mathbf{y})$

La dinámica del problema depende intrínsicamente del operador $\mathbf{O}$

oOper = np.array([[0, 1], [1, 0]])

\begin{equation}
\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix}
\end{equation}

Y es necesario definir un estado inicial 

yInit = np.array([[1, 0], [0, 0]])

\begin{equation}
\begin{bmatrix}
1 & 0\\
0 & 0
\end{bmatrix}
\end{equation}

Dicho operador puede tener distintos significados físicos dependiendo del problema dinámico en cuestión. Puede representar un mapa algebraico, el generador dinámico de un sistema caótico, un Hamiltoniano, etc


