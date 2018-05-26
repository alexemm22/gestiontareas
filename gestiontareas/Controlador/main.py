#!/usr/bin/env python3
"""
Módulo Main: Programa principal (controlador).

Gestion de Tareas - Alexander Emmanuel Orlandini Randazzo
Ejecute "ayuda" para más información
"""
from Modelo.Tareas import Tarea
from estante import Estante
from Vista.repl import REPL
from Vista.repl import strip
import os

class Main:
    """Clase principal."""

    def __init__(self):
        """Constructor: Inicializa propiedades de instancia y ciclo REPL."""
        self.comandos = {
            "agregar": self.agregar,
            "borrar": self.borrar,
            "modificar": self.modificar,
            "terminar": self.terminar,
            "listar": self.listar,
            "buscar": self.buscar,
            "ayuda": self.ayuda,
            "salir": self.salir
        }
        archivo = "tarea.db"
        introduccion = strip(__doc__)
        self.task = Estante(archivo)
        if not self.task.esarchivo():
            introduccion += '\nError: No se pudo abrir "{}"'.format(archivo)
        REPL(self.comandos, introduccion).ciclo()

    def agregar(self, nombre, vencimiento):
        """
        Agrega una Tarea  con su vencimiento.

        Ejemplo: agregar "nombre de Tarea"  "Vencimiento"
        """
        self.task[nombre] = Tarea(nombre, vencimiento, 'Pendiente')

    def borrar(self, nombre):
        """
        Borrar una Tarea.

        Ejemplo: Borrar [nombre de tarea]
        """
        del self.task[nombre]
        return print("Se borro la tarea indicada")

    def modificar(self, nombre, vencimiento):
        """
         Modificar una Tarea

          Ejemplo: modificar [nombre de su Tarea] [vencimiento]
        """
        self.task[nombre] = Tarea(nombre, vencimiento, 'Pendiente')
        return "{}--> Se modifico exitosamente".format(self.task[nombre])

    def terminar(self, nombre, vencimiento):
        """
        Cambia el estado de la Tarea  a Finalizada

          Ejemplo: terminar [nombre de su Tarea] [vencimiento]
        """
        self.task[nombre] = Tarea(nombre, vencimiento, 'Finalizada')
        return print('Se Completo la Tarea Exitosamente')

    def listar(self):
        """
        Todas las Tareas

        Este comando no requiere de parámetros.
        """
        if os.stat("tarea.db.dat").st_size == 0:
            return "No existen Tareas"
        else:
            return (self.task[nombre]
                    for nombre in sorted(self.task))

    def buscar(self, cadena):
        """
        Retorna una Tarea

          Ejemplo: buscar "nombre de su Tarea"
        """
        return (self.task[nombre]
                for nombre in sorted(self.task)
                if cadena in nombre)

    def ayuda(self, comando=None):
        """
        Retorna la lista de comandos disponibles.

        comando -- Comando del que se desea obtener ayuda (opcional).
        """
        if comando in self.comandos:
            salida = strip(self.comandos[comando].__doc__)
        else:
            salida = "Sintaxis: comando [parámetro1] [parámetro2] [..]\n" + \
                     "Comandos: " + \
                     ", ".join(sorted(self.comandos.keys()))
        return salida

    def salir(self):
        """
        Salir de la aplicación.

        Este comando no requiere de parámetros.
        """
        quit()


if __name__ == "__main__":
    Main()
