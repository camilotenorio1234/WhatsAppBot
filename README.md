# 📲 WhatsAppBot

**WhatsAppBot** es un bot automatizado que envía mensajes a través de WhatsApp Web utilizando `pyautogui` y `webbrowser`.  
Este proyecto permite automatizar el envío de textos a contactos específicos.

## 📂 Estructura del Proyecto





## 🔧 Instalación y Configuración

Este proyecto está desarrollado en **Python 3.7**. Antes de ejecutarlo, instala las dependencias necesarias con:

```sh
pip install -r requirements.txt
```
🚀 Uso
Asegúrate de haber iniciado sesión en WhatsApp Web.
Ejecuta el script principal para iniciar el bot:
```sh
python src/main.py
```
El bot abrirá WhatsApp Web, seleccionará el número del contacto y enviará los mensajes almacenados en guion_sherk2.txt.

⚙️ Configuración de Contactos y Países
El archivo whatsapp_bot.py contiene las siguientes configuraciones:

Lista de contactos:
Modifica la función obtener_numeros_whatsapp() para agregar los números de contacto.


```sh
def obtener_numeros_whatsapp(self) -> dict:
    """
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

```
Lista de códigos de país:
Modifica la función obtener_codigos_pais() para agregar nuevos países.
```sh
def obtener_codigos_pais(self) -> dict:
    return {
        "Colombia": 57,
        "España": 34,
        "Estados Unidos": 1,
        "México": 52,
        "Argentina": 54,
        "Brasil": 55
    }
```
✅ Resultados de Pruebas Unitarias
El proyecto cuenta con pruebas automatizadas ejecutadas con pytest.
A continuación, los resultados:
```sh
PS C:\Users\JuanC\OneDrive\Escritorio\codigos python\codigo en desarrollo\whatsapp_bot> pytest src/test_main.py  
========================================================================
platform win32 -- Python 3.7.16, pytest-7.4.4, pluggy-1.2.0
collected 22 items
src\test_main.py ...................... [100%]
========================================================================
22 passed in 0.08s
```
```sh
PS C:\Users\JuanC\OneDrive\Escritorio\codigos python\codigo en desarrollo\whatsapp_bot> pytest -v
========================================================================
platform win32 -- Python 3.7.16, pytest-7.4.4, pluggy-1.2.0
collected 22 items

src/test_main.py::test_obtener_codigo_pais[Colombia-57] PASSED  [  4%]
src/test_main.py::test_obtener_codigo_pais[España-34] PASSED     [  9%]
src/test_main.py::test_obtener_codigo_pais[Estados Unidos-1] PASSED [13%]
src/test_main.py::test_generar_numero_completo PASSED            [ 54%]
src/test_main.py::test_generar_numero_completo_error PASSED      [ 59%]
src/test_main.py::test_archivo_mensajes_existe PASSED            [ 68%]
src/test_main.py::test_obtener_numeros_whatsapp PASSED           [ 72%]
========================================================================
22 passed in 0.15s
```
🛠️ Mejoras Futuras
📌 Soporte para múltiples mensajes por contacto.
📌 Interfaz gráfica (GUI) para configurar los envíos.
📌 Logs detallados para registrar la actividad del bot.



