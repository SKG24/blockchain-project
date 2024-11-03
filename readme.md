# Supply Chain Transparency Blockchain

This project implements a simple blockchain to track the journey of food products in a supply chain. It ensures transparency by allowing consumers to verify the origin and quality of their food.

## Project Overview

- **Objective**: To create a blockchain that records the journey of food products, allowing consumers to verify their source and quality.
- **Key Features**:
  - Add food product entries to the blockchain.
  - Each entry includes details such as product name, origin, timestamp, and previous entry hash.
  - Display the entire supply chain for a product.

## File Structure

- `supply_chain.py`: The main Python script that contains the blockchain implementation.

## How It Works

### Classes

1. **Block Class**:
   - Represents a single block in the blockchain.
   - Attributes:
     - `index`: Position of the block in the chain.
     - `previous_hash`: Hash of the previous block.
     - `timestamp`: Time when the block was created.
     - `data`: Information about the food product.
     - `hash`: Unique hash of the block, calculated using SHA-256.

   - **Methods**:
     - `calculate_hash()`: Generates a SHA-256 hash for the block based on its attributes.

2. **SupplyChain Class**:
   - Manages the chain of blocks.
   - Attributes:
     - `chain`: A list that holds all the blocks in the blockchain.

   - **Methods**:
     - `create_block(data)`: Creates a new block with the provided data and appends it to the chain.
     - `display_chain()`: Prints out the details of each block in the supply chain.

### Example Usage

You can run the `supply_chain.py` script to see how the blockchain works. Here’s how to do it:

1. **Install Python**: Make sure you have Python installed on your system.

2. **Clone the Repository**: If you have this code in a repository, clone it to your local machine.

3. **Navigate to the Directory**: Open your terminal or command prompt and navigate to the directory where `supply_chain.py` is located.

4. **Run the Script**:
   ```bash
   python supply_chain.py

**Expected Output**
Index: 1
Previous Hash: 0
Timestamp: 1700000000.0
Data: Genesis Block
Hash: 5e884898da28047151d0e56f8dc6292773603d0d4c1f1c1c1c1c1c1c1c1c1c1

Index: 2
Previous Hash: 5e884898da28047151d0e56f8dc6292773603d0d4c1f1c1c1c1c1c1c1c1c1
Timestamp: 1700000001.0
Data: Tomatoes from Farm A
Hash: 6dcd4ce23d88e2ee9568ba546c007c63a0c1c1c1c1c1c1c1c1c1c1c1c1c1

Index: 3
Previous Hash: 6dcd4ce23d88e2ee9568ba546c007c63a0c1c1c1c1c1c1c1c1c1c1c1c1c1
Timestamp: 1700000002.0
Data: Tomatoes processed at Factory B
Hash: 7d793037a76c3c4c9e3d62b50d3c7c3c8c8c8c8c8c8c8c8c8c8c8c8c8c8c8