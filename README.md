# Sistema de Gestión de Base de Datos AVL

Este proyecto implementa un sistema de gestión de base de datos no relacional utilizando árboles AVL para almacenar información de estudiantes, profesores y materias.

## 📁 Estructura del Proyecto

```
BBDD_AVL/
├── main_Consola.py          # Aplicación principal (consola)
├── main_GUI.py              # Aplicación principal (interfaz gráfica)
├── README.md                # Este archivo
├── .gitignore               # Archivos ignorados por Git
│
├── models/                  # 📦 Modelos de datos
│   ├── __init__.py
│   ├── EntidadBase.py       # Clase base abstracta
│   ├── Estudiante.py        # Modelo de estudiante
│   ├── Profesor.py          # Modelo de profesor
│   └── Materia.py           # Modelo de materia
│
├── data_structures/         # 📊 Estructuras de datos
│   ├── __init__.py
│   ├── ArbolAVL.py          # Implementación del árbol AVL
│   └── NodoAVL.py           # Nodo del árbol AVL
│
├── database/                # 🗄️ Gestión de datos
│   ├── __init__.py
│   └── GestorBDGenerico.py  # Gestor genérico de base de datos
│
├── interfaces/              # 🖥️ Interfaces de consola
│   ├── __init__.py
│   ├── InterfazEntidadBase.py
│   ├── InterfazEstudiante.py
│   ├── InterfazProfesor.py
│   └── InterfazMateria.py
│
├── gui/                     # 🎨 Interfaz gráfica (CustomTkinter)
│   ├── __init__.py
│   ├── core/               # Interfaces principales
│   │   ├── __init__.py
│   │   ├── GUI_Estudiante.py
│   │   ├── GUI_Profesor.py
│   │   └── GUI_Materia.py
│   ├── estudiantes/        # Formularios de estudiantes
│   │   ├── __init__.py
│   │   └── gui_estudiante_*.py
│   ├── profesores/         # Formularios de profesores
│   │   ├── __init__.py
│   │   └── gui_profesor_*.py
│   └── materias/           # Formularios de materias
│       ├── __init__.py
│       └── gui_materia_*.py
│
└── data/                   # 📄 Archivos de datos JSON
    ├── estudiantes.json
    ├── profesores.json
    └── materias.json
```

## 🚀 Cómo ejecutar

### Interfaz Gráfica (Recomendado)
```bash
python main_GUI.py
```

### Interfaz de Consola
```bash
python main.py
```

> **✅ Estado:** Ambas aplicaciones funcionan correctamente después de la reorganización y corrección de importaciones.

## 📋 Dependencias

- **Python 3.8+**
- **customtkinter** - Para la interfaz gráfica moderna
- **binarytree** - Para visualización del árbol AVL

### Instalación de dependencias:
```bash
pip install customtkinter binarytree
```

## 🛠️ Características

- ✅ **Árbol AVL balanceado** para almacenamiento eficiente
- ✅ **Interfaz gráfica moderna** con CustomTkinter
- ✅ **Persistencia de datos** en archivos JSON
- ✅ **CRUD completo** para todas las entidades
- ✅ **Búsquedas por múltiples campos**
- ✅ **Visualización del árbol** en consola
- ✅ **Arquitectura modular** y bien organizada

## 📚 Entidades Gestionadas

### 👨‍🎓 Estudiantes
- Código, Nombre, Correo, Facultad, Carrera

### 👨‍🏫 Profesores  
- Código, Nombre, Correo, Vinculación

### 📖 Materias
- Código, Nombre, Créditos, Horas por semana

## 🏗️ Arquitectura

El proyecto sigue una arquitectura modular con separación clara de responsabilidades:

- **Models**: Definición de entidades y su lógica
- **Data Structures**: Implementación del árbol AVL
- **Database**: Gestión de persistencia y carga de datos
- **GUI**: Interfaces gráficas de usuario
- **Interfaces**: Interfaces de consola
- **Data**: Almacenamiento de archivos JSON

## 📝 Mejoras Implementadas

- ✅ Estructura de carpetas organizada por funcionalidad
- ✅ Separación de interfaces gráficas por entidad
- ✅ Modularización correcta con archivos `__init__.py`
- ✅ Importaciones relativas apropiadas
- ✅ Documentación clara del código
- ✅ Gestión centralizada de archivos de datos