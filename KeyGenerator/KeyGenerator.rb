# Generador de contraseñas seguras en Ruby

def generar_contrasena(longitud)
  caracteres = [('a'..'z'), ('A'..'Z'), (0..9)].map(&:to_a).flatten
  contrasena = ''
  longitud.times { contrasena += caracteres[rand(caracteres.length)] }
  contrasena
end

# Ejemplo de uso
puts generar_contrasena(8) # Genera una contraseña de 8 caracteres
puts generar_contrasena(12) # Genera una contraseña de 12 caracteres

#imprime la contraseña en un archivo de texto que tiene que crar en la misma carpeta
File.open("contrasena.txt", "w") do |f|
  f.write(generar_contrasena(12))
end
