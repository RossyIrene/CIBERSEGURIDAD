<<<<<<< HEAD
# CIBERSEGURIDAD
Trabajo en conjunto
=======
# 🛡️ Sistema de Escaneo de Dispositivos - Simulador de Vulnerabilidades

## 📋 Descripción del Proyecto
Sistema desarrollado en Python que simula un analizador de vulnerabilidades de red, implementando los principios de Programación Orientada a Objetos (POO) para escanear diferentes tipos de dispositivos en una red.

## 🎯 Objetivos Cumplidos
- ✅ Implementar herencia mediante clases base y subclases
- ✅ Demostrar polimorfismo en el escaneo de vulnerabilidades
- ✅ Aplicar encapsulamiento con propiedades y validaciones
- ✅ Utilizar decoradores @staticmethod y @classmethod
- ✅ Crear un sistema modular y extensible

## 👥 Equipo y Roles
| Rol | Responsable | Entregable |
|-----|-------------|------------|
| 🧩 Product Owner | Coordinación general | README.md y supervisión |
| 🧠 Dev Backend 1 | Arquitectura de clases | dispositivo.py |
| 💻 Dev Backend 2 | Polimorfismo y utilidades | analizador_red.py |
| 🧪 QA/Tester | Validación y pruebas | test_resultados.txt |
| 🎥 Documentador | Comunicación y video | video_explicativo.mp4 |

## 🏗️ Arquitectura del Sistema

### Diagrama de Clases


### Puntos clave a destacar:
1. **Herencia**: Cómo las subclases especializan el comportamiento base
2. **Polimorfismo**: Un mismo método con implementaciones diferentes
3. **Encapsulamiento**: Protección de datos internos
4. **Decoradores**: Diferencia entre @staticmethod y @classmethod
5. **Trabajo en equipo**: Cómo los roles se complementaron

## ✅ Respuestas a Preguntas Teórico-Prácticas

1. **Clase vs Objeto**: Una clase es el molde (Dispositivo), un objeto es la instancia concreta (ThinkPad X1)

2. **Parámetro self**: Representa la instancia actual, permite acceder a atributos y métodos del objeto

3. **Prefijo _**: Indica atributo protegido, convención para encapsulamiento

4. **@property**: Permite acceso controlado a atributos con validación

5. **@staticmethod vs @classmethod**: Static no necesita instancia ni clase, Classmethod recibe la clase como primer parámetro

6. **Herencia**: Ordenador, Router y TelefonoMovil heredan de Dispositivo y comparten interfaz

7. **Polimorfismo**: realizar_escaneo() funciona con cualquier Dispositivo gracias a la interfaz común

8. **Método no implementado**: Lanza NotImplementedError, forzando a las subclases a implementarlo

9. **Validaciones**: IP, modelo no vacío, JSON válido, tipos conocidos

10. **Aprendizaje equipo**: Modularidad permite trabajo paralelo, roles definidos mejoran eficiencia
>>>>>>> 0d480f3 (Subiendo mis cambios a mi rama main)

Trello : https://trello.com/invite/b/69097f1c9d6f1cb1cf52eb8a/ATTI02f9e08145f4604c4a4218369ec472a554D33FF2/trabajowil
