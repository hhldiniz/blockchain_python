# -*-encoding:utf-8-*-
import json
from Block import Block
  
def is_chain_valid():
    if blocks.__len__() != 1:
        count = 1
        while count < blocks.__len__():
            if blocks[count].get_previous_hash() != blocks[count-1].get_hash():
                return False
            count += 1
    return True

def vote(total_votes):
    print("Select the candidate")
    print("1 - Jonh")
    print("2 - Joseph")
    print("3 - Mary")
    
    c = int(input())
    if c == 1:
        total_votes[0] += 1
    elif c == 2:
        total_votes[1] += 1
    else:
        total_votes[2] += 1
        
    print("Vote computed!")
    return total_votes
    
def count(total_votes):
    if genesis.get_data().__len__() == 0:
        genesis.set_data(json.dumps({"c1": total_votes[0], "c2": total_votes[1], "c3": total_votes[2]}))
    else:
        new_block = Block(blocks.__getitem__(blocks.__len__() - 1).get_hash())
        new_block.set_data(json.dumps({"c1": total_votes[0], "c2": total_votes[1], "c3": total_votes[2]}))
        blocks.append(new_block)
        total_votes = [0,0,0]
        
    return total_votes
 
def close():
    if is_chain_valid():
        t1 = 0
        t2 = 0
        t3 = 0
        for block in blocks:
            data = json.loads(block.get_data())
            t1 += data["c1"]
            t2 += data["c2"]
            t3 += data["c3"]
        print(f"#1 candidate: {t1}")
        print(f"#2 candidate: {t2}")
        print(f"#3 candidate: {t3}")
    else:
        print("Invalid Blockchain!")
        
def print_hashes():
    for block in blocks:
        print(f"Actual Hash : {block.get_hash()} -> Previous Hash: {block.get_previous_hash()}")   
        
def menu():
    total_votes = [0,0,0]
     
    while True:
        print("1 - Vote")
        print("2 - Count")
        print("3 - Close")
        print("9 - Print hashes")
        print("0 - Exit")
        op = input()
        if op == "1":
            total_votes = vote(total_votes)
        elif op == "2":
            total_votes = count(total_votes)
        elif op == "3":
            close()
        elif op == "9":
            print_hashes()
        elif op == "0":
            exit(0)

if __name__ == '__main__':
    genesis = Block(0)
    blocks = [genesis]
    menu()
    
