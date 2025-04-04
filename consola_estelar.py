
import time
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_intro():
    clear()
    typewriter("""    ╔══════════════════════════════════════╗
    ║  COMANDO ESTELAR - CONSOLA DE MANDO  ║
    ╚══════════════════════════════════════╝
    """, delay=0.02)
    typewriter("Inicializando sistemas...", 0.03)
    time.sleep(1)
    typewriter("Cargando módulos de navegación... OK", 0.03)
    typewriter("Sistemas de defensa... OK", 0.03)
    typewriter("IA de combate: Online", 0.03)
    typewriter("Bienvenida, Comandante Matilda.\n", 0.04)

def status():
    clear()
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
    input("\nPresiona ENTER para volver...")

def scan():
    clear()
    typewriter("🔍 Escaneando área espacial...")
    time.sleep(2)
    eventos = [
        "Ninguna anomalía detectada.",
        "Se detectó una señal desconocida en el cuadrante 4.",
        "Restos de una nave destruida flotan cerca.",
        "Un agujero de gusano inestable se encuentra a 12.000 km.",
        "Una nave no identificada se aproxima lentamente..."
    ]
    typewriter(random.choice(eventos), 0.04)
    input("\nPresiona ENTER para volver...")

def launch():
    clear()
    typewriter("🚀 Preparando secuencia de lanzamiento...", 0.03)
    for i in range(5, 0, -1):
        typewriter(f"{i}...", 0.5)
    typewriter("¡Despegue exitoso! La nave ha entrado en modo crucero.", 0.03)
    input("\nPresiona ENTER para volver...")

def self_destruct():
    clear()
    typewriter("⚠️ ACTIVANDO SECUENCIA DE AUTODESTRUCCIÓN ⚠️", 0.05)
    for i in range(10, 0, -1):
        typewriter(f"Autodestrucción en: {i}", 0.3)
    typewriter("💥 ¡BOOM! ... No era más que una simulación ;)", 0.05)
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
5. exit           - Salir
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
        elif cmd == "exit" or cmd == "5":
            typewriter("Cerrando consola. Buen viaje, comandante Matilda.", 0.03)
            break
        else:
            print("Comando no reconocido.")
            time.sleep(1)

if __name__ == "__main__":
    main()
