

import sys

def main():
    if len(sys.argv) != 3 or sys.argv[1] != 'create':
        print("Usage: struct-maker create <project_name>")
        sys.exit(1)

    project_name = sys.argv[2]
    print(f"Creating project: {project_name}")
    # Implementar a lógica para criar a estrutura do projeto
