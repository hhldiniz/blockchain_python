# -*-encoding:utf-8-*-
import json
from Block import Block
  
total_votes = [0,0,0]
election = {}

def init_election():
    global election
    candidates = load_candidates()
    
    for key in candidates:
        election[key] = { 'name': candidates[key], 'votes': 0 }  
            
def set_election(vote):
    global election
    election[vote]['votes'] += 1 
    
def clean_votes():
    init_election()

def is_chain_valid():
    if blocks.__len__() != 1:
        count = 1
        while count < blocks.__len__():
            if blocks[count].get_previous_hash() != blocks[count-1].get_hash():
                return False
            count += 1
    return True

def load_candidates():
    with open('candidates.json', 'r') as candidates:
        json_data = json.load(candidates)
    
    return json_data 
 
def print_candidates():
    for key in election:
        print(key,"-",election[key]['name'])
    
def vote():
    print("Select a candidate")
    print_candidates()
    
    c = input()
    set_election(c)
        
    print("Vote computed!")
    
def count():
    if genesis.get_data().__len__() == 0:
        genesis.set_data(json.dumps(election))
    else:
        new_block = Block(blocks.__getitem__(blocks.__len__() - 1).get_hash())
        new_block.set_data(json.dumps(election))
        blocks.append(new_block)
        clean_votes()
 
def print_result():
    for key in election:
        print(election[key]['name'],"votes:",election[key]['votes'])
    
def close():
    if is_chain_valid():
        for block in blocks:
            data = json.loads(block.get_data())
            print_result()
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
    init_election()
    switch_menu()
    
