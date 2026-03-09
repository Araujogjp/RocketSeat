perguntas = [['Seu animal gosta de bananas?', 'macaco']]

while True:
    print('Pense em um Animal!')
    acertou = False

    # resp.lower() -> Tranformar a string em minúsculo
    for p in perguntas:
        resp = input(f'{p[0]} s/n: ')
        if resp.lower() == 's':
            print(f'Você pensou no {p[1]}!')
            acertou = True
            break

    if not acertou:
        animal = input('Desisto! Em qual animal você pensou?: ')
        novaP = input('Qual pergunta você faria para diferenciar esse animal?: ')
        perguntas.append([novaP, animal])

    resp = input('Quer jogar novamente?: ')
    if resp.lower() != 's':
        break
