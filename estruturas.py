#Menu em Python
# Estruturas de Dados e Ordenação
# Pilha, Fila e Fila Circular + Bubble, Selection e Insertion Sort
# Todas as estruturas usam o MESMO vetor: "dados"

# ---------------------------------------------------------------
# Variáveis globais (vetor único e controles de cada estrutura)
# ---------------------------------------------------------------
dados = []        # vetor usado por pilha, fila e fila circular
tipo = None       # "pilha", "fila" ou "circular" (None = nada criado)
tamanho = 0       # capacidade do vetor

topo = -1         # controle da pilha
inicio = 0        # controle da fila e da fila circular
fim = 0           # controle da fila (próxima posição livre)
qtd = 0           # controle da fila circular (número de elementos)

LARGURA = 36


# ---------------------------------------------------------------
# Funções auxiliares de interface
# ---------------------------------------------------------------
def mostrar_menu(titulo, opcoes):
    print("*" * (LARGURA + 2))
    print("| " + titulo.ljust(LARGURA - 2) + " |")
    print("|" + "-" * LARGURA + "|")
    for linha in opcoes:
        print("| " + linha.ljust(LARGURA - 2) + " |")
    print("*" * (LARGURA + 2))


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def estrutura_existe(esperado):
    if tipo != esperado:
        print(f"Crie primeiro a estrutura '{esperado}' (opção 1 deste menu).")
        return False
    return True


# ---------------------------------------------------------------
# PILHA
# ---------------------------------------------------------------
def pilha_init():
    global dados, tipo, tamanho, topo
    n = ler_inteiro("Tamanho da pilha: ")
    if n <= 0:
        print("O tamanho deve ser maior que zero.")
        return
    dados = [None] * n
    tipo = "pilha"
    tamanho = n
    topo = -1
    print(f"Pilha criada com capacidade {n}.")


def pilha_push(valor):
    global topo
    if topo == tamanho - 1:
        print("Pilha cheia (overflow).")
        return
    topo += 1
    dados[topo] = valor
    print(f"{valor} empilhado.")


def pilha_pop():
    global topo
    if topo == -1:
        print("Pilha vazia (underflow).")
        return
    valor = dados[topo]
    dados[topo] = None
    topo -= 1
    print(f"Valor extraído: {valor}")


def pilha_show():
    print("\nVetor dados completo:", dados)
    print("Pilha (base -> topo):", dados[:topo + 1])
    print("topo =", topo)


# ---------------------------------------------------------------
# FILA (linear)
# ---------------------------------------------------------------
def fila_init():
    global dados, tipo, tamanho, inicio, fim
    n = ler_inteiro("Tamanho da fila: ")
    if n <= 0:
        print("O tamanho deve ser maior que zero.")
        return
    dados = [None] * n
    tipo = "fila"
    tamanho = n
    inicio = 0
    fim = 0
    print(f"Fila criada com capacidade {n}.")


def fila_enqueue(valor):
    global fim
    if fim == tamanho:
        print("Fila cheia.")
        return
    dados[fim] = valor
    fim += 1
    print(f"{valor} enfileirado.")


def fila_dequeue():
    global inicio
    if inicio == fim:
        print("Fila vazia.")
        return
    valor = dados[inicio]
    dados[inicio] = None
    inicio += 1
    print(f"Valor extraído: {valor}")


def fila_show():
    print("\nVetor dados completo:", dados)
    print("Fila (início -> fim):", dados[inicio:fim])
    print(f"início = {inicio}, fim = {fim}")


# ---------------------------------------------------------------
# FILA CIRCULAR
# ---------------------------------------------------------------
def circular_init():
    global dados, tipo, tamanho, inicio, qtd
    n = ler_inteiro("Tamanho da fila circular: ")
    if n <= 0:
        print("O tamanho deve ser maior que zero.")
        return
    dados = [None] * n
    tipo = "circular"
    tamanho = n
    inicio = 0
    qtd = 0
    print(f"Fila circular criada com capacidade {n}.")


def circular_enqueue(valor):
    global qtd
    if qtd == tamanho:
        print("Fila circular cheia.")
        return
    pos = (inicio + qtd) % tamanho
    dados[pos] = valor
    qtd += 1
    print(f"{valor} enfileirado na posição {pos}.")


def circular_dequeue():
    global inicio, qtd
    if qtd == 0:
        print("Fila circular vazia.")
        return
    valor = dados[inicio]
    dados[inicio] = None
    inicio = (inicio + 1) % tamanho
    qtd -= 1
    print(f"Valor extraído: {valor}")


def circular_elementos():
    return [dados[(inicio + i) % tamanho] for i in range(qtd)]


def circular_show():
    print("\nVetor dados completo:", dados)
    print("Fila circular (início -> fim):", circular_elementos())
    print(f"início = {inicio}, quantidade = {qtd}")


# ---------------------------------------------------------------
# ALGORITMOS DE ORDENAÇÃO (atuam no vetor "dados")
# ---------------------------------------------------------------
def bubble_sort(v, ini, fim_excl):
    n = fim_excl - ini
    for i in range(n - 1):
        trocou = False
        for j in range(ini, fim_excl - 1 - i):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]
                trocou = True
        if not trocou:
            break


def selection_sort(v, ini, fim_excl):
    for i in range(ini, fim_excl - 1):
        menor = i
        for j in range(i + 1, fim_excl):
            if v[j] < v[menor]:
                menor = j
        if menor != i:
            v[i], v[menor] = v[menor], v[i]


def insertion_sort(v, ini, fim_excl):
    for i in range(ini + 1, fim_excl):
        chave = v[i]
        j = i - 1
        while j >= ini and v[j] > chave:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave


def elementos_atuais():
    """Elementos da estrutura criada, na ordem lógica."""
    if tipo == "pilha":
        return dados[:topo + 1]
    if tipo == "fila":
        return dados[inicio:fim]
    return circular_elementos()


def intervalo_para_ordenar():
    """Devolve (ini, fim_excl): posições de 'dados' ocupadas pela estrutura."""
    global inicio
    if tipo == "pilha":
        return 0, topo + 1
    if tipo == "fila":
        return inicio, fim
    # Fila circular: os elementos podem "dar a volta" no vetor.
    # Antes de ordenar, reposicionamos tudo a partir do índice 0.
    itens = circular_elementos()
    for i in range(tamanho):
        dados[i] = None
    for i, valor in enumerate(itens):
        dados[i] = valor
    inicio = 0
    return 0, qtd


# ---------------------------------------------------------------
# MENUS
# ---------------------------------------------------------------
def menu_principal():
    while True:
        print("\n")
        mostrar_menu("Estruturas de Dados e Ordenação", [
            "1 - PILHA",
            "2 - FILA",
            "3 - FILA CIRCULAR",
            "4 - ORDENAR",
            "5 - SAIR",
        ])
        try:
            return int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inexistente")


def menu_estrutura(titulo):
    """Mostra o submenu de uma estrutura e devolve a opção escolhida."""
    print("\n")
    mostrar_menu(titulo, [
        "1 - Criar estrutura",
        "2 - Armazenar valor",
        "3 - Extrair valor",
        "4 - Imprimir conteúdo",
        "5 - Voltar ao menu anterior",
    ])
    try:
        return int(input("Digite a opção desejada: "))
    except ValueError:
        return 0


def pilha():
    while True:
        opt2 = menu_estrutura("Pilha")

        if opt2 == 5:
            print("Voltando ao menu anterior")
            return
        elif opt2 == 1:
            pilha_init()
        elif opt2 == 2:
            if estrutura_existe("pilha"):
                pilha_push(ler_inteiro("Valor a armazenar: "))
        elif opt2 == 3:
            if estrutura_existe("pilha"):
                pilha_pop()
        elif opt2 == 4:
            if estrutura_existe("pilha"):
                pilha_show()
        else:
            print("Opção inexistente")


def fila():
    while True:
        opt2 = menu_estrutura("Fila")

        if opt2 == 5:
            print("Voltando ao menu anterior")
            return
        elif opt2 == 1:
            fila_init()
        elif opt2 == 2:
            if estrutura_existe("fila"):
                fila_enqueue(ler_inteiro("Valor a armazenar: "))
        elif opt2 == 3:
            if estrutura_existe("fila"):
                fila_dequeue()
        elif opt2 == 4:
            if estrutura_existe("fila"):
                fila_show()
        else:
            print("Opção inexistente")


def fila_circular():
    while True:
        opt2 = menu_estrutura("Fila Circular")

        if opt2 == 5:
            print("Voltando ao menu anterior")
            return
        elif opt2 == 1:
            circular_init()
        elif opt2 == 2:
            if estrutura_existe("circular"):
                circular_enqueue(ler_inteiro("Valor a armazenar: "))
        elif opt2 == 3:
            if estrutura_existe("circular"):
                circular_dequeue()
        elif opt2 == 4:
            if estrutura_existe("circular"):
                circular_show()
        else:
            print("Opção inexistente")


def ordenar():
    if tipo is None:
        print("Nenhuma estrutura criada. Escolha primeiro PILHA, FILA ou "
              "FILA CIRCULAR no menu principal.")
        return

    while True:
        print("\n")
        mostrar_menu("Ordenar (estrutura: " + tipo + ")", [
            "1 - Bubble Sort",
            "2 - Selection Sort",
            "3 - Insertion Sort",
            "4 - Voltar ao menu anterior",
        ])
        try:
            opt3 = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inexistente")
            continue

        if opt3 == 4:
            print("Voltando ao menu anterior")
            return
        elif opt3 in (1, 2, 3):
            ini, fim_excl = intervalo_para_ordenar()
            if fim_excl - ini < 2:
                print("Há menos de 2 elementos; nada para ordenar.")
                continue
            print("Antes :", elementos_atuais())
            if opt3 == 1:
                bubble_sort(dados, ini, fim_excl)
                nome = "Bubble Sort"
            elif opt3 == 2:
                selection_sort(dados, ini, fim_excl)
                nome = "Selection Sort"
            else:
                insertion_sort(dados, ini, fim_excl)
                nome = "Insertion Sort"
            print("Depois:", elementos_atuais(), f"({nome}, ordem crescente)")
        else:
            print("Opção inexistente")


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
while True:
    opt1 = menu_principal()

    if opt1 == 5:
        break
    elif opt1 == 1:
        pilha()
    elif opt1 == 2:
        fila()
    elif opt1 == 3:
        fila_circular()
    elif opt1 == 4:
        ordenar()
    else:
        print("Opção inexistente")

print("Programa finalizado")
