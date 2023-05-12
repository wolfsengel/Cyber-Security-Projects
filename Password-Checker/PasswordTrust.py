import re

def password_strength(password):
    """Evalúa la fortaleza de una contraseña."""
    
    # Verificar longitud de la contraseña
    if len(password) < 8:
        return "La contraseña es demasiado corta."
    
    # Verificar caracteres especiales
    if not re.search("[^a-zA-Z0-9]", password):
        return "La contraseña debe contener al menos un caracter especial."
    
    # Verificar dígitos
    if not re.search("\d", password):
        return "La contraseña debe contener al menos un dígito."
    
    # Verificar letras mayúsculas y minúsculas
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        return "La contraseña debe contener al menos una letra mayúscula y una minúscula."
    
    # Verificar seguridad de la contraseña
    if re.search("(123|abc|qwerty)", password):
        return "La contraseña es demasiado común."
    
    return "La contraseña es segura."

# Ejemplo de uso
password = "MiContraseña123$"
print(password_strength(password))
