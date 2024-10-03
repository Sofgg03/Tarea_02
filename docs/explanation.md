#Explicacion

# Sistemas dinamicos 

Los sistemas dinámicos son modelos de suma importancia en las ciencias. En general, un modelo dinámico intenta resolver la trayectoria temporal de alguna cantidad física como función de algún generador dinámico; este último usualmente representado de forma funcional.


## Metodo Runge-Kutta 4

Es un método numérico para resolver ecuaciones diferenciales de primer orden que no tienen solución análitica. Es un método iterativo en el que cada iteración da como resultado un punto temporal con las iteraciones se van obteniendo puntos, estos puntos se grafican y se obtiene la gráfica de la solución de la ecuación diferencial.


\begin{aligned} %se abre el ambiente para lenguaje matematico. 
     y_n+1  = y_n +  \frac{1}{6}(k_1 +2k_2 +2k_3 +k_4) %se establece la función del metodo runge-kutta con base a la solución en ese punto temporal. 
    k_1 = h*f(t_n , y_n ) \\
    k_2 = h*f(t_n + h/2 , y_n + (k_1)/2)\\
    k_3 = h*f(t_n + h/2 , y_n + (k_2)/2)\\
    k_4 = h*f(t_n + h , y_n + k_3)\\ %se establecen las variables necesarias para la función; h: espaciamiento temporal, y las k.
\end{aligned}


