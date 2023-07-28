import subprocess

def update_packages():
    try:
        # Ejecutar el comando de actualización de paquetes según la distribución de Linux
        # En este ejemplo, se utiliza 'apt' para sistemas basados en Debian (como Ubuntu)
        # Puedes modificar este comando según la distribución que estés usando.
        subprocess.run(['yum', 'update'], check=True)
        subprocess.run(['yum', 'upgrade', '-y'], check=True)
        print("Los paquetes se han actualizado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al actualizar paquetes: {e}")

if __name__ == "__main__":
    update_packages()