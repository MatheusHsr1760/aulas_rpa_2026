import logging

# Configuração do módulo de logging (arquivo + formato padronizado)
logging.basicConfig(
    filename="execucao_bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

# Adiciona um handler para exibir os logs também no console/terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)
logging.getLogger().addHandler(console_handler)


def processar_arquivo(caminho: str) -> None:
    """Abre um arquivo CSV/texto, grava logs de cada linha e trata exceções."""
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                conteudo = linha.strip()
                if conteudo:
                    logging.info(f"Linha lida: {conteudo}")
    except FileNotFoundError:
        logging.error(f"Arquivo não encontrado no caminho: {caminho}")
    finally:
        logging.info("Tentativa de processamento concluída.")


if __name__ == "__main__":
    processar_arquivo("dados.csv")
    