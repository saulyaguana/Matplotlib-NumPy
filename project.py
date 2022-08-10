import numpy as np
import matplotlib.pyplot as plt



def question(start, stop):
    
    menu = int(input("""
Bienvendio/a. Escribe que relación quieres para los años que quieres comparar:

1. Seno
2. Coseno
3. Tangente
4. X**2
--> """))

    x = np.linspace(start, stop, 1000)

    def data(y, eje_y, titulo, label_tittle):
        fig, axes = plt.subplots(figsize=(10, 8))
        axes.plot(x, y, linewidth=3, label=label_tittle, linestyle="dashed", color="#E0A900")
        axes.set_xlabel("X")
        axes.legend()
        axes.set_ylabel(eje_y)
        axes.set_title(f'{titulo} de los años {start} y {stop}')
        plt.show()


    if menu == 1:
        data(np.sin(x), "Sin(x)", "Seno", "$Sin(x)$")
    elif menu == 2:
        data(np.cos(x), "Cos(x)", "Coseno", "$Cos(x)$")
    elif menu == 3:
        data(np.tan(x), "Tan(x)", "Tangente", "$Tan(x)$")
    elif menu == 4:
        data(x**2, "X**2", "Cuadrado", "$X**2$")
    else:
        print("Ejecuta de nuevo y prueba con una opción válida")


def main():
    plt.style.use('dark_background')
    start = int(input("Escribe un año de origen: "))
    stop = int(input("Escribe el año de parada: "))

    while stop <= start:
        stop = int(input("Escribe un número mayor al de origen: "))

    question(start, stop)


if __name__ == "__main__":
    main()