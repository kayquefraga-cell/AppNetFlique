from FilaFilmes import filaFilmes

def gerenciar_filme(filme):
    filaFilmes.put(filme)
def listar_filmes():
    filmes = []
    tamanho_fila = filaFilmes.qsize()
    
    for _ in range(tamanho_fila):
        filme = filaFilmes.get()
        filmes.append(filme)
        filaFilmes.put(filme)  # Reinsere o filme na fila
    
    return filmes