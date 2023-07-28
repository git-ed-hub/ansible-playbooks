import subprocess
import os

def update_packages():
    try:
        # Ejecutar el comando de actualización de paquetes 

        
        subprocess.run(['yum', 'install', '-y', 'httpd'], check=True)
        os.system("cp -r /home/andy/palm1/* /var/www/html")
        subprocess.run(['systemctl', 'start', 'httpd'],check=True)
        subprocess.run(['systemctl', 'enable', 'httpd'],check=True)
        subprocess.run(['firewall-cmd', '--zone=public', '--add-service=http', '--permanent'],check=True)
        subprocess.run(['firewall-cmd', '--reload'],check=True)






        print("Los paquetes se han actualizado correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al actualizar paquetes: {e}")

if __name__ == "__main__":
    update_packages()