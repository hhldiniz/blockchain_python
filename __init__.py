# -*-encoding:utf-8-*-

import json

from Block import Block


def is_chain_valid():
    for i, b in enumerate(blocks):
        if b.get_hash() != 0:
            if b.get_previous_hash() != blocks[i-1].get_hash():
                return False
    return True


if __name__ == '__main__':
    genesis = Block(0)
    blocks = [genesis]
    total_c1 = 0
    total_c2 = 0
    total_c3 = 0
    while True:
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
        elif op == "2":
            if blocks.__len__() == 1:
                genesis.set_data(json.dumps({"c1": total_c1, "c2": total_c2, "c3": total_c3}))
            new_block = Block(blocks.__getitem__(blocks.__len__() - 1))
            new_block.set_data(json.dumps({"c1": total_c1, "c2": total_c2, "c3": total_c3}))
            if is_chain_valid():
                blocks.append(new_block)
        elif op == "3":
            if is_chain_valid():
                t1 = 0
                t2 = 0
                t3 = 0
                for block in blocks:
                    data = json.loads(block.get_data())
                    t1 += data["c1"]
                    t2 += data["c2"]
                    t3 += data["c3"]
                print(f"Total do candidato 1: {t1}")
                print(f"Total do candidato 2: {t2}")
                print(f"Total do candidato 3: {t3}")
            else:
                print("Blockchain e invalida!")
        elif op == "0":
            exit(0)
