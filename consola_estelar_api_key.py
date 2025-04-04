
import time
import random
import os
import pyttsx3
import openai
from datetime import datetime

# 💡 Aquí puedes poner tu clave directamente para pruebas (NO subir a GitHub con esto)
openai.api_key = "sk-proj-..."

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def log_event(event):
    with open("bitacora_nave.log", "a") as log:
        log.write(f"[{datetime.now()}] {event}\n")

def ia_responder(pregunta):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres una IA a bordo de una nave estelar. Puedes responder preguntas o ejecutar comandos como 'revisa los sistemas', 'haz un escaneo', 'inicia despegue' o 'autodestruir'."},
                {"role": "user", "content": pregunta}
            ],
            max_tokens=150,
            temperature=0.8
        )
        return respuesta.choices[0].message["content"].strip()
    except Exception as e:
        return f"[ERROR] No se pudo contactar con la IA: {str(e)}"

def ejecutar_comando_ia(respuesta):
    r = respuesta.lower()
    if "revisa los sistemas" in r or "estado de los sistemas" in r:
        status()
    elif "escaneo" in r or "escanear" in r:
        scan()
    elif "despegue" in r or "lanzamiento" in r:
        launch()
    elif "autodestruir" in r or "autodestrucción" in r:
        self_destruct()

def show_intro():
    clear()
    typewriter("""╔══════════════════════════════════════╗
║  COMANDO ESTELAR - CONSOLA DE MANDO  ║
╚══════════════════════════════════════╝
    """, delay=0.02)
    typewriter("Inicializando sistemas...", 0.03)
    time.sleep(1)
    typewriter("IA de vuelo en línea", 0.03)
    speak("Bienvenida, Comandante Matilda. Todos los sistemas están listos.")
    log_event("Sistema iniciado por la comandante Matilda.")

def status():
    clear()
    speak("Mostrando estado de los sistemas.")
    typewriter("📡 Escaneando sistemas...")
    time.sleep(1)
    systems = {
        "Motor de curvatura": "Operativo",
        "Escudos deflectores": "100%",
        "Armas de plasma": "Listas",
        "Nivel de energía": f"{random.randint(80, 100)}%",
        "Oxígeno": "Estable"
    }
    for k, v in systems.items():
        typewriter(f"{k}: {v}", 0.03)
    log_event("Comando 'status' ejecutado.")
    input("\nPresiona ENTER para volver...")

def scan():
    clear()
    speak("Iniciando escaneo del espacio exterior.")
    typewriter("🔍 Escaneando área espacial...")
    time.sleep(2)
    eventos = [
        "Se detecta energía oscura en el sector 7G.",
        "Radiación solar intensa en el cuadrante 3.",
        "Objeto no identificado en trayectoria de colisión.",
        "Zona segura para navegación detectada.",
        "Ninguna anomalía espacial relevante."
    ]
    evento = random.choice(eventos)
    typewriter(evento, 0.04)
    speak(evento)
    log_event(f"Comando 'scan' ejecutado. Resultado: {evento}")
    input("\nPresiona ENTER para volver...")

def launch():
    clear()
    speak("Iniciando secuencia de despegue.")
    typewriter("🚀 Preparando secuencia de lanzamiento...", 0.03)
    for i in range(5, 0, -1):
        typewriter(f"{i}...", 0.5)
    typewriter("¡Despegue exitoso! La nave ha entrado en modo crucero.", 0.03)
    speak("Despegue exitoso. Ahora estamos en modo crucero.")
    log_event("Comando 'launch' ejecutado.")
    input("\nPresiona ENTER para volver...")

def self_destruct():
    clear()
    speak("Advertencia. Activando secuencia de autodestrucción.")
    typewriter("⚠️ ACTIVANDO SECUENCIA DE AUTODESTRUCCIÓN ⚠️", 0.05)
    for i in range(10, 0, -1):
        typewriter(f"Autodestrucción en: {i}", 0.3)
    mensaje = "¡BOOM! ... Simulación completada ;)"
    typewriter(f"💥 {mensaje}", 0.05)
    speak(mensaje)
    log_event("Comando 'self-destruct' ejecutado (simulado).")
    input("\nPresiona ENTER para volver...")

def ia_chat():
    clear()
    speak("IA lista para asistencia.")
    typewriter("🤖 Puedes hacerme una pregunta o pedirme una acción, comandante.\n", 0.04)
    pregunta = input("Tu pregunta> ")
    respuesta = ia_responder(pregunta)
    typewriter(f"IA: {respuesta}", 0.04)
    speak(respuesta)
    log_event(f"IA consultada. Pregunta: {pregunta} | Respuesta: {respuesta}")
    ejecutar_comando_ia(respuesta)
    input("\nPresiona ENTER para volver...")

def main():
    show_intro()
    while True:
        clear()
        print("""╔═════════════════════════════╗
║     CONSOLA DE COMANDOS     ║
╚═════════════════════════════╝
1. status         - Estado de sistemas
2. scan           - Escanear área espacial
3. launch         - Iniciar despegue
4. self-destruct  - Activar autodestrucción
5. ia             - Consultar a la IA de la nave
6. exit           - Salir
        """)
        cmd = input("Comando> ").strip().lower()
        if cmd == "status" or cmd == "1":
            status()
        elif cmd == "scan" or cmd == "2":
            scan()
        elif cmd == "launch" or cmd == "3":
            launch()
        elif cmd == "self-destruct" or cmd == "4":
            self_destruct()
        elif cmd == "ia" or cmd == "5":
            ia_chat()
        elif cmd == "exit" or cmd == "6":
            speak("Cerrando consola. Hasta pronto, Comandante Matilda.")
            typewriter("Cerrando consola. Buen viaje, comandante Matilda.", 0.03)
            log_event("Consola cerrada por la comandante.")
            break
        else:
            speak("Comando no reconocido.")
            print("Comando no reconocido.")
            time.sleep(1)

if __name__ == "__main__":
    main()
