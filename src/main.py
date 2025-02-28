from whatsapp_bot import WhatsAppBot

if __name__ == "__main__":
    # Configuración del envío
    pais_destino = "Colombia"
    contacto_destino = "mio"
    ruta_mensajes = r'codigo en desarrollo\WhatsAppBot\data\guion_sherk2.txt'

    try:
        bot = WhatsAppBot(pais_destino, contacto_destino, ruta_mensajes)
        bot.enviar_mensajes()
    except ValueError as e:
        print(f"⚡ {e}")
