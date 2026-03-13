# traduccion-a-braille-STL
actividad de tecnicas de modelado de software para decimas en el parcial
# Iteración 1: Traducción simple a Braille

# Diccionario básico de equivalencias (simplificado)
braille_dict = {
    "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑",
    "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
    "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕",
    "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
    "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽", "z": "⠵",
    " ": " "  # espacio
}

# Entrada del usuario
    frase = input("Ingresa una frase en español: ").lower()

# Traducción
traduccion = "".join([braille_dict.get(letra, "?") for letra in frase])

    print("Traducción a Braille:", traduccion)

# Iteración 2: Guardar traducción en archivo

    frase = input("Ingresa una frase en español: ").lower()
    traduccion = "".join([braille_dict.get(letra, "?") for letra in frase])

print("Traducción a Braille:", traduccion)

# Guardar en archivo
with open("traduccion_braille.txt", "w", encoding="utf-8") as f:
    f.write(traduccion)

    print("La traducción se ha guardado en 'traduccion_braille.txt'")


