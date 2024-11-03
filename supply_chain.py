import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + self.previous_hash + str(self.timestamp) + self.data
        return hashlib.sha256(value.encode()).hexdigest()

class SupplyChain:
    def __init__(self):
        self.chain = []
        self.create_block(data="Genesis Block")  # Create the genesis block

    def create_block(self, data):
        index = len(self.chain) + 1
        timestamp = time.time()
        previous_hash = self.chain[-1].hash if self.chain else '0'
        block = Block(index, previous_hash, timestamp, data)
        self.chain.append(block)
        return block

    def display_chain(self):
        for block in self.chain:
            print(f'Index: {block.index}')
            print(f'Previous Hash: {block.previous_hash}')
            print(f'Timestamp: {block.timestamp}')
            print(f'Data: {block.data}')
            print(f'Hash: {block.hash}\n')

# Example usage
if __name__ == "__main__":
    supply_chain = SupplyChain()
    
    # Adding food product entries
    supply_chain.create_block(data="Tomatoes from Farm A")
    supply_chain.create_block(data="Tomatoes processed at Factory B")
    supply_chain.create_block(data="Tomatoes shipped to Store C")

    # Display the supply chain
    supply_chain.display_chain()