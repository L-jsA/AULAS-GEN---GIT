def main():
    # Lista de nomes que eu gosto
    nomes_que_eu_gosto = ["Thomson", "Thompson", "Haddock", "Snowy"]

    # Iterador interno começa em 0
    iterador_interno = 0

    # Laço for percorre cada nome na lista
    for nome in nomes_que_eu_gosto:
        print("Iterador interno:", iterador_interno, "- Gosto deste nome", nome)
        iterador_interno += 1  # adiciona 1 ao iterador

# Fim do programa
if __name__ == "__main__":
    main()