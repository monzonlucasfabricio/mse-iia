#!/bin/bash

# Instalar virtualenv usando pip3
python3 -m venv .venv

# Crear el entorno virtual llamado .venv
# Activar el entorno virtual
source .venv/bin/activate

# Instalar ipykernel dentro del entorno virtual
pip3 install ipykernel

# # Desactivar el entorno virtual
deactivate

echo "El entorno virtual ha sido configurado, y las dependencias y ipykernel han sido instaladas."