print('projeto de Vitória Karpovas Chisman - 32008554')
print('')
print('')
print('bem vindo ao Virtual Escape Room')
input('aperte enter para começar')
print('')
print('')
print('a história é a seguinte:')
print('a quarentena acabou!')
print('você vai finalmente sair de casa em meses')
print('mas você não sabe onde estão o seu celular, carteira, chave do carro, óculos de sol, garrafa de água e maquiagem')
print('para poder sair, você precisa achar os objetos')
print('a única coisa que você sabe é que cada objeto está em um cômodo diferente da casa')
print('você então tenta encontrá-los relembrando o que você fez recentemente')
input('aperte enter para continuar')
print('')
print('')
print('as regras são:')
print('você precisa responder a pergunta que será feita em cada cômodo')
print('em cada cômodo você terá 3 opções')
print('cada opção corresponde a um número')
print('você só precisa digitar 1, 2 ou 3 na resposta')
input('aperte enter para continuar')
print('')
print('')
print('cada objeto te da uma pontuação diferente')
print('objetos essenciais (celular e carteira) te dão 4 pontos')
print('chave do carro e maquiagem te dão 3 pontos')
print('e garrafa de água e óculos de sol te dão 2 pontos')
print('para ganhar o jogo, você precisa de 10 pontos e ter achado pelo menos um dos objetos essenciais')
print('nos cômodos com objetos essenciais, você terá duas chances para procurar')
print('mas na segunda chance você ganha apenas 2 pontos')
print('preparado? digite "sim" para começar e "não" para sair!')
r=str(input())
while r!= 'nao' and r!= 'não' and r!='sim':
    print('resposta inválida, digite novamente')
    r=str(input())
j=1
if r=='nao' or r=='não' and j==1:
    print('tem certeza que deseja sair?')
    print('digite "sim" ou "não"')
    c=str(input())
    while c!= 'nao' and c!= 'não' and c!='sim':
        print('resposta inválida, digite novamente')
        c=str(input())
    if c=='não' or c=='nao':
        r='sim'
    elif c=='sim':
        r='não'
while r=='sim':
    if j>1:
        print('')
        print('')
        print('preparado? digite "sim" para recomeçar e "não" para sair!')
        r=str(input())
        while r!= 'nao' and r!= 'não' and r!='sim':
            print('resposta inválida, digite novamente')
            r=str(input())
        if r=='não' or r=='nao':
            break
    z=0
    b=0
    print('')
    print('')
    print('vamos começar')
    print('')
    print('')
    print('você começa a sua busca na sala de estar')
    print('você sabe que a sua carteira está aqui')
    print('você lembra que jogou sua bolsa na mesa')
    print('depois disso, você deitou no sofá')
    print('e depois arrumou o armário em baixo da TV')
    print('mas você não se lembra se a carteira estava na bolsa que você estava carregando ou no seu bolso do casaco')
    print('você então sabe que ela está na mesa (1), sofá (2) ou armário (3)') 
    tentativas=1
    while (tentativas<3):
        a=str(input('onde você procura? '))
        if a=='2':
            print('EBA! você encontrou a carteira, então segue para procurar o resto')
            b=1
            if tentativas==1:
                z=z+4
                print('você tem', z, 'pontos')
                tentativas=4
            if tentativas==2:
                z=z+2
                print('você tem', z, 'pontos')
                tentativas=4
        elif a=='1' or a=='3':
            if tentativas<2:
                print('POXA... você não achou de primeira, mas como esse item é essencial você decide dar mais uma olhada')
                tentativas=tentativas+1
            else:
                print('POXA... você não achou de novo, mas como só tem mais um lugar possível você segue para procurar o resto')
                print('você tem', z, 'pontos')
                tentativas=tentativas+1
        else:
            print('resposta inválida, digite novamente')
    input('aperte enter para continuar')
    print('')
    print('')
    print('você agora está na varanda e sabe que seu óculos de sol ficou aqui')
    print('você lembra que estava fazendo churrasco alguns dias atras')
    print('depois você lembra de ter tirado uma soneca na poltrona')
    print('e por fim você arrumou a caixa de brinquedos da sua filha')
    print('o que você não lembra é quando você tirou o óculos (ou quando ele caiu do seu rosto)')
    print('você tem certeza que ele está nos objetos de churrasco (1), ou na poltrona (2) ou na caixa de brinquedos (3)')
    t=0
    while t==0:
        a=str(input('onde você procura? '))
        if a=='3':
            print('EBA! você encontrou o óculos, então vai em direção á cozinha')
            z=z+2
            print('você tem', z, 'pontos')
            t=1
        elif a=='1' or a=='2':
            print('POXA... você não achou o óculos e percebe que está quase atrasada então deixa ele. afinal, você está indo para um lugar fechado, não vai precisar dele')
            print('você tem', z, 'pontos')
            t=1
        else:
            print('resposta inválida, digite novamente')
    input('aperte enter para continuar')
    print('')
    print('')
    print('agora que você está na cozinha, lembra que deixou a chave do carro aqui')
    print('você lembra que da ultima vez que saiu de carro, quando voltou veio fazer um sanduiche e estava bem distraida')
    print('você pegou a manteiga na geladeira (1), uma faca na gaveta (2) e depois colocou tudo na pia (3) para lavar')
    print('então sabe que a chave precisa estar em um dos três lugares')
    t=0
    while t==0:
        a=str(input('onde você procura? '))
        if a=='1':
            print('EBA! você encontrou a chave!')
            z=z+3
            print('você tem', z, 'pontos')
            t=1
        elif a=='2' or a=='3':
            print('POXA... você não achou a chave do carro então decide ir a pé para não perder mais tempo procurando')
            print('você tem', z, 'pontos')
            t=1
        else:
            print('resposta inválida, digite novamente')
    input('aperte enter para continuar')
    print('')
    print('')
    print('agora você vai para o banheiro procurar sua maquiagem')
    print('você se lembra que da ultima vez que usou maquiagem, deixou do lado da pia')
    print('mas depois percebe que sua filha de 4 anos entrou e bagunçou todo o banheiro')
    print('percebe que ela jogou varias coisas na banheira e outras no chão')
    print('você vê uma caixa na banheira (1), outra do lado da pia (2) e outra no chão (3), todas onde o batom que você quer pode estar')
    t=0
    while t==0:
        a=str(input('em qual das três caixas você procura? '))
        if a=='3':
            print('EBA! você conseguiu achar seu batom no meio de tanta bagunça, então segue sua busca em outros cômodos')
            z=z+3
            print('você tem', z, 'pontos')
            t=1
        elif a=='1' or a=='2':
            print('POXA... você não achou o batom que queria mas não quer perder mais tempo com isso então decide usar outro batom e segue sua busca')
            print('você tem', z, 'pontos')
            t=1
        else:
            print('resposta inválida, digite novamente')
    input('aperte enter para continuar')
    print('')
    print('')
    print('você então vai para o quarto da sua filha procurar sua garafa de água')
    print('você lembra de ter deixado a garrafa do lado da cama dela antes dela dormir')
    print('mas sabe que ela é bagunceira e gosta de esconder suas coisas no armário e na pilha de roupas sujas no chão')
    print('você sabe então que precisa procurar na pilha de roupas (1), no armário (2) ou na cama (3)')
    t=0
    while t==0:
        a=str(input('onde você procura? '))
        if a=='1':
            print('EBA! você encontrou a garrafa e corre para o seu quarto para procurar o seu celular')
            z=z+2
            print('você tem', z, 'pontos')
            t=1
        elif a=='2' or a=='3':
            print('POXA... você não achou a garrafa e está suuuuper atrasada então deixa a garrafa e vai procurar seu celular')
            print('você tem', z, 'pontos')
            t=1
        else:
            print('resposta inválida, digite novamente')
    input('aperte enter para continuar')
    print('')
    print('')
    print('você está finalmente procurando o último objeto')
    print('você lembra que seu celular estava carregando na escrivaninha (1)')
    print('você também lembra de ter usado ele enquanto estava deitada na cama (2)')
    print('e se lembra de ter arrumado a prateleira (3) enquanto segurava o celular')
    print('o que você não lembra é qual dos três aconteceu por último')
    tentativas=1
    while (tentativas<3):
        a=str(input('onde você procura? '))
        if a=='3':
            print('EBA! você encontrou o celular e está finalmente pronta para aproveitar o fim da quarentena e sair de casa!')
            b=b+1
            if tentativas==1:
                z=z+4
                print('você tem', z, 'pontos')
                tentativas=4
            if tentativas==2:
                z=z+2
                print('você tem', z, 'pontos')
                tentativas=4
        elif a=='1' or a=='2':
            if tentativas<2:
                print('POXA... você procurou no lugar errado, mas como esse item é essencial você decide dar mais uma olhada')
            else:
                print('POXA... você procurou no lugar errado de novo, mas só sobrou um lugar para ele estar')
                print('portanto está pronta para aproveitar o fim da quarentena e sair de casa!')
                print('você tem', z, 'pontos')
            tentativas=tentativas+1
        else:
            print('resposta inválida, digite novamente')
    input('aperte enter para continuar')
    print('')
    print('')
    if z>=10 and b>=1:
        print('você conseguiu', z,'pontos e achou', b,'dos 2 objetos essenciais')
        print('parabéns, você ganhou o jogo!!!')
        print('aproveite o fim da quarentena')
    elif z>=10 and b==0:
        print('não foi dessa vez... você alcançou', z,'pontos mas não achou nenhum objeto essencial')
        print('você perdeu')
    elif z<10 and b>=1:
        print('não foi dessa vez... você achou', b,'dos 2 objetos essenciais, mas tem apenas', z,'pontos')
        print('você perdeu')
    elif z<10 and b==0:
        print('não foi dessa vez... você não achou nenhum dos 2 objetos essenciais, e tem apenas', z,'pontos')
        print('você perdeu')
    print('')
    print('')
    print('você quer jogar de novo?')
    print('digite "sim" para continuar e "não" para sair do jogo')
    r=str(input())
    while r!= 'nao' and r!= 'não' and r!='sim':
        print('resposta inválida, digite novamente')
        r=str(input())
    if r=='sim':
        j=j+1
if r=='não' or r=='nao':
    print('obrigada por jogar! espero que tenha gostado')
