"""
Módulo que define las clases base para dispositivos de red.
Implementa el patrón de herencia y polimorfismo para el escaneo de vulnerabilidades.
"""

class Dispositivo:
    """
    Clase base abstracta para todos los dispositivos de red.
    Implementa encapsulamiento mediante propiedades y validaciones.
    """
    
    def __init__(self, modelo, fabricante):
        self._modelo = modelo
        self._fabricante = fabricante

    @property
    def modelo(self):
        """Getter para modelo con encapsulamiento"""
        return self._modelo

    @modelo.setter
    def modelo(self, valor):
        """Setter para modelo con validación"""
        if not valor or not valor.strip():
            raise ValueError("❌ El modelo no puede estar vacío.")
        self._modelo = valor

    @property
    def fabricante(self):
        """Getter para fabricante con encapsulamiento"""
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        """Setter para fabricante con validación"""
        if not valor or not valor.strip():
            raise ValueError("❌ El fabricante no puede estar vacío.")
        self._fabricante = valor

    def escanear_vulnerabilidades(self):
        """
        Método abstracto que debe ser implementado por las subclases.
        Demuestra el concepto de polimorfismo.
        """
        raise NotImplementedError("⚠️ Este método debe implementarse en la subclase.")

    def __str__(self):
        """Representación en string del dispositivo"""
        return f"{self.__class__.__name__}: {self.modelo} ({self.fabricante})"


class Ordenador(Dispositivo):
    """
    Subclase que representa un ordenador en la red.
    Hereda de Dispositivo y implementa escaneo específico.
    """
    
    def escanear_vulnerabilidades(self):
        """
        Implementación polimórfica del escaneo para ordenadores.
        Simula análisis de software y actualizaciones.
        """
        import random
        vulnerabilidades = random.randint(1, 8)
        print(f"💻 {self.modelo}: Análisis de software – {vulnerabilidades} actualizaciones críticas pendientes.")
        print(f"   • Sistema operativo desactualizado")
        print(f"   • {vulnerabilidades} programas requieren parches de seguridad")
        return vulnerabilidades


class Router(Dispositivo):
    """
    Subclase que representa un router en la red.
    Hereda de Dispositivo y implementa escaneo específico.
    """
    
    def escanear_vulnerabilidades(self):
        """
        Implementación polimórfica del escaneo para routers.
        Simula análisis de puertos y configuración.
        """
        import random
        puertos_abiertos = random.randint(1, 5)
        print(f"📡 {self.modelo}: Escaneo de puertos – {puertos_abiertos} puertos abiertos detectados.")
        print(f"   • Configuración WiFi vulnerable")
        print(f"   • Firmware desactualizado")
        print(f"   • Puertos TCP {puertos_abiertos} expuestos")
        return puertos_abiertos


class TelefonoMovil(Dispositivo):
    """
    Subclase que representa un teléfono móvil en la red.
    Hereda de Dispositivo y implementa escaneo específico.
    """
    
    def escanear_vulnerabilidades(self):
        """
        Implementación polimórfica del escaneo para teléfonos.
        Simula análisis de aplicaciones y permisos.
        """
        import random
        apps_vulnerables = random.randint(2, 7)
        print(f"📱 {self.modelo}: Análisis de apps – {apps_vulnerables} aplicaciones con permisos excesivos.")
        print(f"   • Sistema operativo móvil desactualizado")
        print(f"   • {apps_vulnerables} apps con acceso a datos sensibles")
        print(f"   • Configuración de privacidad débil")
        return apps_vulnerables