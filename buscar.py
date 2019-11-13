def busca(x):
    data2 =open('')
    string_de_busca = str(x)
    string_split = string_de_busca.split()
    for lines in data2.readlines():
        linha_sem_character_barra_n = lines.replace('\n', '')
        elementos_na_linha = linha_sem_character_barra_n.split(';')
        if string_split == elementos_na_linha:
            print(elementos_na_linha)
            return elementos_na_linha
    data2.close()


#buscar(334342727)

