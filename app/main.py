from datetime import datetime

total = 0

# Lista para armazenar as receitas temporariamente
receitas = []

#Lista para armazenar as despesas temporariamente
despesas = []

def adicionar_receita(valor, categoria, data=None):
    """Função para adicionar uma nova receita."""
    global total
    
    
    if data is None:
        data = datetime.now().strftime('%Y-%m-%d') #Data atual como padrão
    
    # Estrutura da receita usando um dicionário
    receita = {
        "valor":  valor,
        "categoria": categoria,
        "data": data
    }
    
    # Adiciona a receita à lista de receitas
    receitas.append(receita)
    total += receita["valor"]
    print("Receita adicionada com sucesso!")
    print(f"Total: {total}")
    

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


def adicionar_despesa(valor, categoria, data=None):
    global total
    
    if data is None:
        data = datetime.now().strftime('%Y-%m-%d')
    
    despesa = {
        "valor": valor,
        "categoria": categoria,
        "data": data
    }
    
    if despesa["valor"] > total:
        print(f"Infelizmente você não possuí saldo suficiente para adicionar está despesa: {despesa['categoria']}")
        return
    else:
        despesas.append(despesa)
        total -= despesa["valor"]
        print(f"Despesa adicionada com sucesso!")


def listar_despesas():
    print("\nLista de despesas:")
    for idx, despesa in enumerate(despesas, start=1):
        print(f"{idx}. Valor: {despesa['valor']} | Categoria: {despesa['categoria']} | Data: {despesa['data']}")
    print()

def remover_despesa():
    listar_despesas()
    try:
        index = int(input("Digite o número da receita que deseja remover: ")) - 1
        if 0 <= index < len(despesas):
            despesas.pop(index)
            print("Despesa removida com sucesso.")
            listar_despesas()
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")


if __name__ == '__main__':
    print(f'Receita total: {total}')
    adicionar_receita(500, "Salário")
    adicionar_receita(200, "Freelance", "2023-10-15")
    listar_receitas()
    
    print("----------------------------------")
    
    adicionar_despesa(150, "Mercado")
    adicionar_despesa(70, "Conta d'agua", "2023-11-07")
    adicionar_despesa(700, "Parcela do Carro", "2023-11-21")
    listar_despesas()
    
    print(f'Receita total: {total}')
    
    #remover_receita()
    #remover_despesa()