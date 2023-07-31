#Inicializar un repositorio de git automáticamente después de crear la plantilla y un entorno virtual

import subprocess
import os

MESSAGE_COLOR = "\x1b[34m" #"\x1b[34m" representa un código de escape ANSI para cambiar el color del texto a azul 
RESET_ALL = "\x1b[0m"  #establecer el color de la terminal de nuevo al valor predeterminado después de imprimir el mensaje con color.

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

# nombre_ambiente = "{{ cookiecutter.project_slug }}"

# subprocess.call(['conda', 'create', '--name', nombre_ambiente, ])

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")