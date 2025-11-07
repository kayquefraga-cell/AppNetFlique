from FilaFilmes import filaFilmes

def pesquisar_filme(titulo):
    resultados = []
    tamanho_fila = filaFilmes.qsize()
    
    for _ in range(tamanho_fila):
        filme = filaFilmes.get()
        if titulo.lower() in filme['titulo'].lower():
            resultados.append(filme)
        filaFilmes.put(filme)  # Reinsere o filme na fila
    
    return resultados