from FilaFilmes import filaFilmes

def testar_fila_vazia():
    return filaFilmes.empty()
def testar_adicionar_filme(filme):
     filaFilmes.put(filme)
     return filaFilmes.qsize()
def testar_listar_filmes():
    filmes = []
    tamanho_fila = filaFilmes.qsize()
    
    for _ in range(tamanho_fila):
       filme = filaFilmes.get()
       filmes.append(filme)
       filaFilmes.put(filme)  # Reinsere o filme na fila
    
       return filmes
def testar_pesquisar_filme(titulo):
    resultados = []
    tamanho_fila = filaFilmes.qsize()
    
    for _ in range(tamanho_fila):
        filme = filaFilmes.get()
        if titulo.lower() in filme['titulo'].lower():
           resultados.append(filme)
        filaFilmes.put(filme)  # Reinsere o filme na fila
    
    return resultados