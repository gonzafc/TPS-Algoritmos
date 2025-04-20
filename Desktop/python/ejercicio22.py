def usar_la_fuerza(mochila, i=0):
    if i >= len(mochila):
        return ("No hay sable de luz en la mochila") 

    if mochila[i] == "sable de luz":
        return ("Se sacaron", i + 1, "objetos hasta encontrar el sable de luz")

    # Si el objeto no es un sable de luz, lo sacamos y se repite el proceso
    return usar_la_fuerza(mochila, i + 1)

#ejemploss

mochila_con_sable = ["remedios", "agua", "papas fritas", "sable de luz", "coca"]
resultado_con = usar_la_fuerza(mochila_con_sable)
print(resultado_con)

mochila_sin_sable = ["chisitos", "agua", "casco de clon", "llaves de la nave"]
resultado_sin = usar_la_fuerza(mochila_sin_sable)
print(resultado_sin)