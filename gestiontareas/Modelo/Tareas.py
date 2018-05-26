#!/usr/bin/env python3
"""
Módulo Tarea: Clase principal (modelo).

Proyecto de ejemplo - Paradigmas de la Programación
"""


class Tarea:
    """Estructura de Gestion de Tareas"""

    def __init__(self, nombre, vencimiento, estado):
        """Constructor: Inicializa propiedades de instancia."""
        self.nombre = nombre
        self.vencimiento = vencimiento
        self.estado = estado

    def __str__(self):
        """Cadena de representación."""

        return "Tarea: {} Vencimiento: {} Estado:{}".format(self.nombre, self.vencimiento, self.estado)


def main():
    """Función principal (ejemplo de uso)."""
    tarea = {}

    tarea["limpiar"] = Tarea("limpiar silla", "25/05/2018")
    tarea["pupitre"] = Tarea("limpiar pupitre","25/05/2018")
    tarea["pieza"] = Tarea("limpiar pieza", "25/05/2018")

    for clave in tarea:
        print(tarea[clave])


if __name__ == "__main__":
    main()
