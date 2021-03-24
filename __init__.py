# -*-encoding:utf-8-*-
import json
from Block import Block
  
total_votes = [0,0,0]

def set_total_votes(candidate):
    global total_votes
    total_votes[candidate] += 1
    
def clean_votes():
    global total_votes
    total_votes = [0,0,0]
    
def get_votes_from(candidate):
    return total_votes[candidate]

def is_chain_valid():
    if blocks.__len__() != 1:
        count = 1
        while count < blocks.__len__():
            if blocks[count].get_previous_hash() != blocks[count-1].get_hash():
                return False
            count += 1
    return True

def vote():
    print("Select the candidate")
    print("1 - Jonh")
    print("2 - Joseph")
    print("3 - Mary")
    
    c = int(input())
    if c == 1:
        set_total_votes(0)
    elif c == 2:
        set_total_votes(1)
    else:
        set_total_votes(2)
        
    print("Vote computed!")
    
def count():
    if genesis.get_data().__len__() == 0:
        genesis.set_data(json.dumps({"c1": get_votes_from(0), "c2": get_votes_from(1), "c3": get_votes_from(2)}))
    else:
        new_block = Block(blocks.__getitem__(blocks.__len__() - 1).get_hash())
        new_block.set_data(json.dumps({"c1": get_votes_from(0), "c2": get_votes_from(1), "c3": get_votes_from(2)}))
        blocks.append(new_block)
        clean_votes()
 
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
  
def terminate():
    exit(0)   
    
def invalid_option():
    print("Invalid Option")   
    
def show_options():
    print("1 - Vote")
    print("2 - Count")
    print("3 - Close")
    print("9 - Print hashes")
    print("0 - Exit")    
     
def switch_menu():
    while True:
        show_options()
        op = input()
        
        switcher = {
            "1": vote,
            "2": count,
            "3": close,
            "9": print_hashes,
            "0": terminate
        }  
        
        switcher.get(op, invalid_option)()

if __name__ == '__main__':
    genesis = Block(0)
    blocks = [genesis]
    switch_menu()
    
