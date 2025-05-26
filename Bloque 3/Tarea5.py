def saludo(lang):
    if lang == "es":
        return("HOLA")
    elif lang == "fr":
        return("Bonjour")
    else:
        return("HELLO")

print(saludo("en"), "Glenn")

print(saludo ("es"), "Sally")

print(saludo ("fr"),"Michael")