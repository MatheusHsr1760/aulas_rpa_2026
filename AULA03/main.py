from mod_rh import cadastrar_colaborador, exibir_colaboradores


def main():
    colaboradores = []

    while True:
        print("\n=== MENU RH ===")
        print("1 - Cadastrar Colaborador")
        print("2 - Listar Colaboradores")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = input("Digite o nome: ").strip()
            cargo = input("Digite o cargo: ").strip()
            try:
                salario = float(input("Digite o salário: "))
                novo_colab = cadastrar_colaborador(nome, cargo, salario)
                colaboradores.append(novo_colab)
                print(f"Colaborador {nome} cadastrado com sucesso!")
            except ValueError:
                print("Erro: Salário inválido. Digite um valor numérico.")

        elif opcao == "2":
            exibir_colaboradores(colaboradores)

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()