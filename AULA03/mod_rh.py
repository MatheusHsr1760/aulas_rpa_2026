def cadastrar_colaborador(nome: str, cargo: str, salario: float) -> dict:
    """Cria e retorna um dicionario estruturado com os dados do colaborador."""
    colaborador = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }
    return colaborador


def exibir_colaboradores(lista_colaboradores: list) -> None:
    """Percorre a lista de colaboradores e imprime os dados formatados."""
    if not lista_colaboradores:
        print("\nNenhum colaborador cadastrado.")
        return

    print("\n--- LISTA DE COLABORADORES ---")
    for index, colab in enumerate(lista_colaboradores, start=1):
        print(
            f"{index}. Nome: {colab['nome']} | "
            f"Cargo: {colab['cargo']} | "
            f"Salário: R$ {colab['salario']:.2f}"
        )
    print("-" * 30)
    