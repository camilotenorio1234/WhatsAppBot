# WhatsAppBot 📲

## 🌍 Introduction | Introducción

WhatsAppBot is an automated bot that sends messages via WhatsApp Web using `pyautogui` and `webbrowser`. This project allows the automation of sending texts to specific contacts.

This README is available in both English and Spanish. Below, you will find two sections: one in English and another in Spanish, each containing the same detailed information about installation, usage, and testing.

<details>
  <summary>WhatsAppBot 📲 English</summary>

  # WhatsAppBot 📲

Automate WhatsApp messages using Python and WhatsApp Web.

## 📌 Description

WhatsAppBot is a bot that sends messages via WhatsApp Web using `pyautogui` and `webbrowser`. It allows automating text messages to specific contacts.

## 📁 Project Structure

```sh
WhatsAppBot/
├── data/
│   ├── script.txt                # File containing the messages to send
├── src/
│   ├── whatsapp_bot.py          # Main bot logic
│   ├── main.py                  # Executable script to start the bot
│   ├── test_main.py             # Unit tests for the project
├── requirements.txt             # Required dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Files and folders to ignore in the repository
```

# 🚀 Installation and Usage

## 📌 1. Clone the repository

```sh
git clone [https://github.com/your_user/WhatsAppBot.git](https://github.com/camilotenorio1234/WhatsAppBot-/tree/main)
cd WhatsAppBot
```

## 📌 2. Install dependencies

This project runs on **Python 3.7**. Before running it, install the required dependencies:

```sh
pip install -r requirements.txt
```

## 📌 3. Run the bot

Make sure you are logged into WhatsApp Web.
Run the main script to start the bot:

```sh
python src/main.py
```

The bot will open WhatsApp Web, select the contact number, and send the messages stored in `script.txt`.

## ⚙️ Contact and Country Code Configuration

Modify the function `get_whatsapp_numbers()` in `whatsapp_bot.py` to add contact numbers.

```sh
def get_whatsapp_numbers(self) -> dict:
    """
    📌 Add numbers to which messages will be sent.
    ⚠️ Example numbers have been provided to prevent misuse.
    """
    return {
        "me": 0000000000,
        "friend1": 1111111111,
        "friend2": 2222222222,
        "friend3": 3333333333,
        "friend4": 4444444444,
        "friend5": 9999999999  # ⚠️ Example number not valid
    }
```

Modify `get_country_codes()` to add new countries.

```sh
def get_country_codes(self) -> dict:
    return {
        "Colombia": 57,
        "Spain": 34,
        "United States": 1,
        "Mexico": 52,
        "Argentina": 54,
        "Brazil": 55
    }
```

## ✅ Unit Test Results

This project includes automated tests executed with pytest.
Below are the results:

```sh
pytest src/test_main.py
```

If you want more details:

```sh
pytest -v
```

</details>

---

WhatsAppBot es un bot automatizado que envía mensajes a través de WhatsApp Web utilizando `pyautogui` y `webbrowser`. Este proyecto permite automatizar el envío de textos a contactos específicos.

Este README está disponible en inglés y español. A continuación, encontrarás dos secciones: una en inglés y otra en español, cada una con la misma información detallada sobre instalación, uso y pruebas.

<details>
  <summary>WhatsAppBot 📲 Español</summary>

# WhatsAppBot 📲

Automatiza el envío de mensajes de WhatsApp utilizando Python y WhatsApp Web.

## 📌 Descripción

WhatsAppBot es un bot que envía mensajes a través de WhatsApp Web utilizando `pyautogui` y `webbrowser`. Permite automatizar el envío de textos a contactos específicos.

## 📁 Estructura del Proyecto

```sh
WhatsAppBot/
├── data/
│   ├── guion_sherk2.txt        # Archivo con los mensajes a enviar
├── src/
│   ├── whatsapp_bot.py         # Lógica principal del bot
│   ├── main.py                 # Archivo ejecutable para iniciar el bot
│   ├── test_main.py            # Pruebas unitarias del proyecto
├── requirements.txt            # Dependencias necesarias para la ejecución
├── README.md                   # Documentación del proyecto
├── .gitignore                   # Archivos y carpetas a ignorar en el repositorio
```

# 🚀 Instalación y Uso

## 📌 1. Clonar el repositorio

```sh
git clone [https://github.com/tu_usuario/WhatsAppBot.git](https://github.com/camilotenorio1234/WhatsAppBot-/tree/main)
cd WhatsAppBot
```

## 📌 2. Instalar dependencias

Este proyecto está desarrollado en **Python 3.7**. Antes de ejecutarlo, instala las dependencias necesarias con:

```sh
pip install -r requirements.txt
```

## 📌 3. Ejecutar el bot

Asegúrate de haber iniciado sesión en WhatsApp Web.
Ejecuta el script principal para iniciar el bot:

```sh
python src/main.py
```

El bot abrirá WhatsApp Web, seleccionará el número del contacto y enviará los mensajes almacenados en `guion_sherk2.txt`.

## ⚙️ Configuración de Contactos y Países

Modifica la función `obtener_numeros_whatsapp()` en `whatsapp_bot.py` para agregar los números de contacto.

Modifica `obtener_codigos_pais()` para agregar nuevos países.

## ✅ Resultados de Pruebas Unitarias

Este proyecto cuenta con pruebas automatizadas ejecutadas con pytest.

Para ejecutar las pruebas:

```sh
pytest src/test_main.py
```

Si quieres ver más detalles:

```sh
pytest -v
```

</details>
