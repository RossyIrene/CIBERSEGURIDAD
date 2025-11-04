"""
Módulo utilitario para análisis de red.
Implementa métodos estáticos y de clase para operaciones de red.
"""

import json
from dispositivo import Ordenador, Router, TelefonoMovil

class AnalizadorRed:
    """
    Clase utilitaria para operaciones de análisis de red.
    Demuestra el uso de métodos estáticos y de clase.
    """
    
    @staticmethod
    def validar_ip(ip):
        """
        Método estático para validar formato de dirección IP.
        No requiere instancia de la clase para ser usado.
        """
        if not ip or not isinstance(ip, str):
            return False
            
        partes = ip.split(".")
        if len(partes) != 4:
            return False
            
        for parte in partes:
            if not parte.isdigit():
                return False
            num = int(parte)
            if num < 0 or num > 255:
                return False
                
        return True

    @staticmethod
    def generar_reporte_escaneo(dispositivos_escaneados):
        """
        Método estático para generar reporte consolidado.
        """
        print("\n" + "="*50)
        print("📊 REPORTE FINAL DE VULNERABILIDADES")
        print("="*50)
        
        total_vulnerabilidades = 0
        for dispositivo, resultado in dispositivos_escaneados:
            total_vulnerabilidades += resultado
            print(f"• {dispositivo.modelo}: {resultado} vulnerabilidades encontradas")
        
        print(f"\n🔍 Total de vulnerabilidades detectadas: {total_vulnerabilidades}")
        
        if total_vulnerabilidades > 10:
            print("🚨 ALERTA: Nivel de riesgo ALTO")
        elif total_vulnerabilidades > 5:
            print("⚠️  ADVERTENCIA: Nivel de riesgo MEDIO")
        else:
            print("✅ INFORMACIÓN: Nivel de riesgo BAJO")

    @classmethod
    def desde_json(cls, data_json):
        """
        Método de clase para crear objetos desde JSON.
        Accede a la clase misma (cls) para crear instancias.
        """
        try:
            if isinstance(data_json, str):
                data = json.loads(data_json)
            else:
                data = data_json
                
            objetos = []
            for dispositivo_data in data:
                tipo = dispositivo_data.get("tipo", "")
                modelo = dispositivo_data.get("modelo", "")
                fabricante = dispositivo_data.get("fabricante", "")
                
                if not all([tipo, modelo, fabricante]):
                    print(f"⚠️  Datos incompletos para dispositivo: {dispositivo_data}")
                    continue
                    
                if tipo == "Ordenador":
                    objetos.append(Ordenador(modelo, fabricante))
                elif tipo == "Router":
                    objetos.append(Router(modelo, fabricante))
                elif tipo == "TelefonoMovil":
                    objetos.append(TelefonoMovil(modelo, fabricante))
                else:
                    print(f"❌ Tipo de dispositivo desconocido: {tipo}")
                    
            return objetos
            
        except json.JSONDecodeError as e:
            print(f"❌ Error al decodificar JSON: {e}")
            return []
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            return []


def realizar_escaneo(dispositivo):
    """
    Función que demuestra polimorfismo al trabajar con cualquier tipo de Dispositivo.
    """
    print(f"\n🎯 Iniciando escaneo en {dispositivo.modelo} ({dispositivo.fabricante})...")
    print("-" * 60)
    
    try:
        resultado = dispositivo.escanear_vulnerabilidades()
        return resultado
    except NotImplementedError as e:
        print(f"❌ Error: {e}")
        return 0
    except Exception as e:
        print(f"❌ Error inesperado durante el escaneo: {e}")
        return 0


# Ejemplo de uso y demostración
if __name__ == "__main__":
    print("🚀 DEMOSTRACIÓN DEL SISTEMA DE ESCANEO")
    print("=" * 50)
    
    # Datos de ejemplo en formato JSON
    datos_json = """
    [
        {"tipo": "Ordenador", "modelo": "ThinkPad X1", "fabricante": "Lenovo"},
        {"tipo": "Router", "modelo": "Archer C7", "fabricante": "TP-Link"},
        {"tipo": "TelefonoMovil", "modelo": "Galaxy S23", "fabricante": "Samsung"},
        {"tipo": "Ordenador", "modelo": "MacBook Pro", "fabricante": "Apple"},
        {"tipo": "Router", "modelo": "Nighthawk", "fabricante": "Netgear"}
    ]
    """
    
    # Crear dispositivos desde JSON usando classmethod
    dispositivos = AnalizadorRed.desde_json(datos_json)
    
    # Validar IP usando staticmethod
    ip_test = "192.168.1.1"
    print(f"\n🔍 Validando IP {ip_test}: {AnalizadorRed.validar_ip(ip_test)}")
    
    # Realizar escaneo de todos los dispositivos (polimorfismo)
    resultados = []
    for dispositivo in dispositivos:
        resultado = realizar_escaneo(dispositivo)
        resultados.append((dispositivo, resultado))
    
    # Generar reporte final usando staticmethod
    AnalizadorRed.generar_reporte_escaneo(resultados)