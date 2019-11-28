# Simulación del Comportamiento de un Sistema Coloidal por el Método de Monte Carlo
Realizá la simulación de la dinámica molecular para un sistema coloidal con partículas de radio  1x10^-6 m que se encuentran dispersas en una caja cuadrada de longitud L=20x10^-6 m.,sometidas a los potenciales de London repulsivo y Lennard-Jones. Utilizando los métodos de Metrópolis y Montercalo, determina la configuración de menor energía para cada sistema y realiza el poliedro de Voronoi para determinar la estructura del sistema

El orden de ejecución de los archivos es el siguiente:

1) conf_inicial.py # genera una una configuración inicial de particulas con un porcentaje de ocupación dado, y las guarda en un archivo .txt
2) Metropolis.py # con el archivo generado en 1) realizala simulación utilizando el algoritmo de metropolis.
3) Montecarlo.py # con el archivo generado en 1) realizala simulación utilizando el algoritmo de enfriamiento simulado.
4) Graficas.py #genera las graficas con las configuraciones inciales, finales y con el poliedro de voronoi.
