# 📚 Proyecto Final - Herramientas de Programación: Algoritmo de Listas

## 📋 Descripción
Este es un proyecto colaborativo en grupo para desarrollar y probar un algoritmo de manejo de listas en Python. Todos los integrantes pueden trabajar juntos en el desarrollo, prueba y mejora del código.

---

## 🎯 Objetivos del Proyecto
- ✅ Crear funciones para manipular listas
- ✅ Implementar algoritmos eficientes
- ✅ Documentar el código
- ✅ Realizar pruebas exhaustivas
- ✅ Aprender a trabajar colaborativamente con Git

---

## 📁 Estructura del Proyecto

```
Proyecto-final-Herr.-program.-Listas/
│
├── README.md                 # Este archivo
├── funciones.py              # Funciones principales del algoritmo
├── algoritmo.ipynb           # Consola interactiva (Jupyter Notebook)
├── test_funciones.py         # Pruebas unitarias
└── documentacion/
    └── GUIA_COLABORACION.md  # Guía para trabajar en equipo
```

---

## 🚀 Cómo Empezar

### 1. Clonar el repositorio
```bash
git clone https://github.com/Leslynha/Proyecto-final-Herr.-program.-Listas.git
cd Proyecto-final-Herr.-program.-Listas
```

### 2. Instalar Jupyter (para usar la consola interactiva)
```bash
pip install jupyter
```

### 3. Abrir la consola interactiva
```bash
jupyter notebook algoritmo.ipynb
```

---

## 💻 Funciones Disponibles

### `ordenar_lista(lista)`
Ordena una lista de números de menor a mayor.
```python
ordenar_lista([5, 2, 9, 1]) → [1, 2, 5, 9]
```

### `buscar_elemento(lista, elemento)`
Busca un elemento en la lista y retorna su posición.
```python
buscar_elemento([5, 2, 9, 1], 9) → 2
```

### `invertir_lista(lista)`
Invierte el orden de los elementos.
```python
invertir_lista([5, 2, 9, 1]) → [1, 9, 2, 5]
```

### `suma_lista(lista)`
Calcula la suma de todos los elementos.
```python
suma_lista([5, 2, 9, 1]) → 17
```

### `promedio_lista(lista)`
Calcula el promedio de los elementos.
```python
promedio_lista([5, 2, 9, 1]) → 4.25
```

---

## 👥 Integrantes del Grupo

| Nombre | Rol | Tarea |
|--------|-----|-------|
| [Nombre 1] | Líder | Coordinar el proyecto |
| [Nombre 2] | Desarrollador | Crear funciones |
| [Nombre 3] | Tester | Hacer pruebas |
| [Nombre 4] | Documentación | Documentar código |

*Actualiza esta tabla con los nombres reales*

---

## 🔄 Flujo de Trabajo Colaborativo

### Paso 1: Actualizar tu código local
```bash
git pull origin main
```

### Paso 2: Crear una rama para tu tarea
```bash
git checkout -b feature/mi-funcionalidad
```

### Paso 3: Hacer cambios y confirmarlos
```bash
git add .
git commit -m "Descripción clara del cambio"
```

### Paso 4: Subir tu rama
```bash
git push origin feature/mi-funcionalidad
```

### Paso 5: Crear un Pull Request en GitHub
- Ve a tu repositorio en GitHub
- Haz clic en "Compare & pull request"
- Describe tu cambio
- Espera que otros revisen y aprueben

---

## ✅ Cómo Probar el Código

### Opción 1: Usar Jupyter Notebook (Recomendado)
```bash
jupyter notebook algoritmo.ipynb
```

### Opción 2: Ejecutar pruebas desde la terminal
```bash
python -m pytest test_funciones.py
```

### Opción 3: Prueba manual en Python
```python
from funciones import ordenar_lista
resultado = ordenar_lista([5, 2, 9, 1])
print(resultado)
```

---

## 📝 Historial de Cambios

| Fecha | Integrante | Cambio |
|-------|-----------|--------|
| 2026-06-26 | Leslynha | Creada estructura inicial del proyecto |
| 2026-06-26 | Leslynha | Agregadas funciones básicas de listas |
| 2026-06-26 | Leslynha | Creada consola interactiva (Jupyter) |

---

## 🤝 Reglas de Colaboración

1. ✅ **Actualiza antes de trabajar**: `git pull origin main`
2. ✅ **Crea ramas descriptivas**: `feature/nombre-de-tu-tarea`
3. ✅ **Commits claros**: Describe qué hiciste en el mensaje
4. ✅ **Revisa el código**: Otros pueden revisar tus cambios antes de hacer merge
5. ✅ **Comunícate**: Avisa al grupo si trabajarás en una función
6. ✅ **Prueba tu código**: Asegúrate de que funcione antes de subir

---

## 🛠️ Herramientas Utilizadas

- **Python 3.9+** - Lenguaje de programación
- **Git** - Control de versiones
- **GitHub** - Repositorio en línea
- **Jupyter Notebook** - Consola interactiva
- **pytest** - Framework para pruebas

---

## 📚 Recursos Útiles

- [Documentación de Python](https://docs.python.org/3/)
- [Guía de Git](https://git-scm.com/doc)
- [Tutorial de Jupyter Notebook](https://jupyter.org/try)
- [Cómo hacer Pull Requests](https://docs.github.com/en/pull-requests)

---

## ❓ Preguntas Frecuentes

**P: ¿Cómo resuelvo conflictos de Git?**
R: Si dos personas editan el mismo archivo, Git te pedirá que resuelvas los conflictos manualmente. Edita el archivo, mantén los cambios que quieras, y haz commit.

**P: ¿Qué debo hacer si rompo el código?**
R: No te preocupes, por eso usamos ramas. Tus cambios están en tu rama. Si algo sale mal, otros pueden seguir trabajando en `main`.

**P: ¿Cómo agrego una nueva función?**
R: Agrégala a `funciones.py`, crea una prueba en `test_funciones.py`, y luego crea un Pull Request.

---

## 📞 Contacto

Para preguntas o problemas, contacta a los integrantes del grupo.

---

**¡Bienvenido al proyecto! 🎉 Vamos a crear algo increíble juntos.**
