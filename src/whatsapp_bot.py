import pyautogui
import webbrowser
from time import sleep


class WhatsAppBot:
    def __init__(self, pais: str, contacto: str, ruta_archivo: str):
        self.pais = pais
        self.contacto = contacto
        self.ruta_archivo = ruta_archivo
        self.numeros = self.obtener_numeros_whatsapp()
        self.codigos_pais = self.obtener_codigos_pais()

    
    def obtener_numeros_whatsapp(self) -> dict:
        """
            Retorna un diccionario con nombres y números de WhatsApp.

            📌 Aquí colocar los números a los que se enviarán los mensajes.
            ⚠️ Se han colocado números de ejemplo que no son válidos para evitar uso indebido.
        """
        return {
            "mio": 0000000000,
            "amigo1": 1111111111,
            "amigo2": 2222222222,
            "amigo3": 3333333333,
            "amigo4": 4444444444,
            "amigo5": 9999999999  # ⚠️ Número de ejemplo no válido
        }
    
    def obtener_codigos_pais(self) -> dict:
        """
        Retorna un diccionario con los códigos de países.
        """
        return {
            "Afganistán": 93, "Albania": 355, "Argelia": 213, "Andorra": 376,
            "Angola": 244, "Argentina": 54, "Brasil": 55, "Canadá": 1,
            "Colombia": 57, "China": 86, "Francia": 33, "India": 91,
            "Italia": 39, "Japón": 81, "México": 52, "Rusia": 7,
            "España": 34, "Estados Unidos": 1, "Bangladesh": 880
        }

    def generar_numero_completo(self) -> str:
        """
        Genera el número completo con código de país y número local.
        """
        codigo = self.codigos_pais.get(self.pais)
        numero = self.numeros.get(self.contacto)

        if codigo and numero:
            return f"{codigo}{numero}"
        else:
            raise ValueError(f"Datos inválidos: {self.pais} o {self.contacto}")

    def enviar_mensajes(self):
        """
        Envía los mensajes de un archivo de texto a un número de WhatsApp específico.
        """
        numero_completo = self.generar_numero_completo()
        webbrowser.open(f'https://web.whatsapp.com/send?phone={numero_completo}')
        sleep(10)  # Tiempo para escanear el código QR

        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    pyautogui.typewrite(linea.strip())
                    pyautogui.press('enter')
                    sleep(1)
            print("✅ Mensajes enviados con éxito.")
        except FileNotFoundError:
            print(f"❌ Archivo no encontrado: {self.ruta_archivo}")
        except Exception as e:
            print(f"⚠️ Error al enviar mensajes: {e}")
