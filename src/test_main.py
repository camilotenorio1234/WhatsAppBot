import pytest
from whatsapp_bot import WhatsAppBot



# 🔹 Prueba para verificar que los códigos de país sean correctos
@pytest.mark.parametrize("pais, esperado", [
    ("Colombia", 57),
    ("España", 34),
    ("Estados Unidos", 1),
    ("Bangladesh", 880),
    ("Brasil", 55),
    ("Argentina", 54),
    ("México", 52),
    ("Japón", 81),
    ("China", 86),
    ("Francia", 33),
    ("Rusia", 7),
])
def test_obtener_codigo_pais(pais, esperado):
    bot = WhatsAppBot("Colombia", "mio", "data/guion_sherk2.txt")
    assert bot.obtener_codigos_pais()[pais] == esperado


# 🔹 Prueba para validar la generación de un número completo
def test_generar_numero_completo():
    bot = WhatsAppBot("Colombia", "mio", "data/guion_sherk2.txt")
    numero_completo = bot.generar_numero_completo()
    assert numero_completo == "573155781585"  # Código de Colombia + número del contacto "mio"


# 🔹 Prueba para verificar el manejo de errores al generar números inválidos
def test_generar_numero_completo_error():
    bot = WhatsAppBot("PaísInexistente", "mio", "data/guion_sherk2.txt")
    with pytest.raises(ValueError):
        bot.generar_numero_completo()


# 🔹 Prueba para asegurar que el bot maneja números inexistentes correctamente
def test_generar_numero_completo_numero_invalido():
    bot = WhatsAppBot("Colombia", "contacto_no_existe", "data/guion_sherk2.txt")
    with pytest.raises(ValueError):
        bot.generar_numero_completo()


# 🔹 Prueba para verificar si el archivo de mensajes existe antes de enviar
def test_archivo_mensajes_existe():
    bot = WhatsAppBot("Colombia", "mio", "data/guion_sherk2.txt")
    try:
        with open(bot.ruta_archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        assert len(contenido) > 0  # El archivo debe tener contenido
    except FileNotFoundError:
        pytest.fail("❌ El archivo de mensajes no existe")


# 🔹 Prueba para verificar que el diccionario de números de WhatsApp tenga contenido
def test_obtener_numeros_whatsapp():
    bot = WhatsAppBot("Colombia", "mio", "data/guion_sherk2.txt")
    numeros = bot.obtener_numeros_whatsapp()
    assert isinstance(numeros, dict) and len(numeros) > 0


# 🔹 Prueba para asegurar que se devuelven los contactos correctos
@pytest.mark.parametrize("contacto, esperado", [
    ("mio", 0000000000),
    ("amigo1", 1111111111),
    ("amigo2", 2222222222),
    ("amigo3", 3333333333),
    ("amigo4", 4444444444),
    ("amigo5", 9999999999),  # ⚠️ Número de ejemplo no válido
])

def test_obtener_numeros_whatsapp_contactos(contacto, esperado):
    bot = WhatsAppBot("Colombia", "mio", "data/guion_sherk2.txt")
    assert bot.obtener_numeros_whatsapp()[contacto] == esperado
