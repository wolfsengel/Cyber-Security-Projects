import hashlib
import magic
import os

# Determina la extensión del archivo
def get_extension(filename):
    return os.path.splitext(filename)[1]

# Calcula el hash MD5 del archivo
def calculate_md5(filename):
    md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
    return md5.hexdigest()

# Analiza el archivo para determinar si es sospechoso o no
def analyze_file(filename):
    try:
        # Obtiene la información del tipo de archivo
        file_type = magic.from_file(filename)

        # Verifica si el archivo es un archivo ejecutable o un script
        if 'executable' in file_type or 'script' in file_type:
            print("El archivo es un ejecutable o un script")

            # Calcula el hash MD5 del archivo
            md5 = calculate_md5(filename)
            print(f"MD5 hash: {md5}")

        else:
            print("El archivo no es un ejecutable o un script")
            
        # Verifica si el archivo tiene una extensión sospechosa
        extension = get_extension(filename)
        if extension in ['.exe', '.bat', '.vbs']:
            print(f"La extensión {extension} es sospechosa")

    except Exception as e:
        print(f"Error al analizar el archivo: {e}")


if __name__ == "__main__":
    # Ingresa el nombre del archivo que deseas analizar
    filename = input("Ingrese el nombre del archivo que desea analizar: ")

    # Analiza el archivo
    analyze_file(filename)
