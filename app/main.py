from datetime import datetime

# Lista para armazenar as receitas temporariamente
receitas = []

def adicionar_receita(valor, categoria, data=None):
    """Função para adicionar uma nova receita."""
    if data is None:
        data = datetime.now().strftime('%Y-%m-%d') #Data atual como padrão
    
    # Estrutura da receita usando um dicionário
    receita = {
        "valor": valor,
        "categoria": categoria,
        "data": data
    }
    
    # Adiciona a receita à lista de receitas
    receitas.append(receita)
    print("Receita adicionada com sucesso!")

def listar_receitas():
    print("\nLista de Receitas:")
    for idx, receita in enumerate(receitas, start=1):
        print(f'{idx}. Valor: {receita['valor']} | Categoria: {receita['categoria']} | Data: {receita['data']}')
    print()
    
def remover_receita():
    listar_receitas()
    try:
        index = int(input("Digite o número da receita que deseja remover: ")) - 1
        if 0 <= index < len(receitas):
            receitas.pop(index)
            print("Receita removida com sucesso.")
            listar_receitas()
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if __name__ == '__main__':
    adicionar_receita(500, "Salário")
    adicionar_receita(200, "Freelance", "2023-10-15")
    listar_receitas()
    remover_receita()