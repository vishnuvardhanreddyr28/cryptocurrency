# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 11:49:05 2020

@author: ADMIN
"""


from datetime import datetime
import hashlib
import json



class transaction:
    def __init__(self,from_address,to_address,amount):
        self.sender=from_address
        self.recipent=to_address
        self.amount=amount
        
        
        
class Block:
    def __init__(self,transaction_details=transaction("Genesis","",0),previous_hash=" "):
        self.index=0
        self.timestamp=datetime.now()
        self.transactionlist=transaction_details
        self.previous_hash=previous_hash
        self.minier_reward=0
        self.hash=self.calculate_hash()
        
    def calculate_hash(self):
        block_string=json.dumps({"index":str(self.index),"timestamp":str(self.timestamp),\
                                 "transaction_sender":self.transactionlist.sender,"previoushash":\
                                     str(self.previous_hash)},sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def mine_block(self,difficulty):
            while(self.hash[:difficulty] != str('').zfill(difficulty)):
                self.index += 1
                self.hash=self.calculate_hash()
    
    def print_block(self):
        print( "Block values are :")
        print(self.index)
        print(self.timestamp)
        print(self.transactionlist.sender,self.transactionlist.recipent,\
              self.transactionlist.amount)
        print(self.hash)
        print(self.miner_reward)
        
        
class Block_chain:
    def __init__(self):
        self.chain=[]
        self.chain.append(self.create_genesis_block())
        self.difficulty=3
        self.reward=1
    
    def create_genesis_block(self):
        return Block()
    
    def get_last_block(self):
        return self.chain[-1]
    
    def add_block(self,transaction_details):
        new_block=Block(transaction_details)
        new_block.previous_hash=self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        new_block.miner_reward=1
        print("Block sucessfully mined")
        new_block.print_block()
        self.chain.append(new_block)
        
    def isChainValid(self):
        for i in range(1,len(self.chain)):
            previous_block=self.chain[i-1]
            current_block=self.chain[i]
            if(current_block.hash != current_block.calculate_hash()):
                print("invalid block")
                return False
            if(current_block.previous_hash != previous_block.hash):
                print("invalid chain")
                return False
            if(current_block.timestamp<previous_block.timestamp):
                print("invalid block")
                return False
        return True
    
    

        
        
        
t=transaction('a','b',200)
print("First block added")
b=Block_chain()
b.add_block(t)
print("Second block added")
t=transaction('b','a',200)
b.add_block(t)
print(b.isChainValid())

        
    
        

        
    

    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
            
        
    
   
        
