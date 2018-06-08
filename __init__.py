# -*-encoding:utf-8-*-

from Block import Block


def is_valid_block(block):
    for b in blocks:
        pass


if __name__ == '__main__':
    genesis = Block(0)
    blocks = [genesis]
    total_c1 = 0
    total_c2 = 0
    total_c3 = 0
    while True:
        name = input("Digite seu nome\n")
        print("1 - Votar")
        print("2 - Contabilizar")
        print("3 - Fechar urna")
        print("0 - Sair")
        op = input()
        if op == "1":
            print("Selecione o candidato")
            print("1 - Joao")
            print("2 - Jose")
            print("3 - Maria")
            c = int(input())
            if c == 1:
                total_c1 += 1
            elif c == 2:
                total_c2 += 1
            else:
                total_c3 += 1
            print("Voto salvo com sucesso!")
        elif op == "3":
            new_block = Block(blocks.__getitem__(blocks.__len__()-1))
            new_block.set_data({"c1": total_c1, "c2": total_c2, "c3": total_c3})
        elif op == "2":
            for index, block in enumerate(blocks):
                if block.get_previous_hash() != 0:
                    pass
        elif op == "0":
            exit(0)
