# Handraise

## Usage
From the directory that main.py is in run 
```
python main.py
```
Then choose the relevant menu options by entering the associated number.

## File Organization

**main.py:** 
Contains the CLI menu for functionalities

**read_events.py:** 
Reads events emitted by the contract when tokens are sent back to the contract. 

**canvas_script.py:** 
Updates student grades based on amount of Handraise burned.

**mint_coins.py:** 
Tells the smart contract to mint coins and send them to addresses based on the contents of the students.csv file.

**students.csv:** 
File that contains student information and grades. The one in this repo is an example.
The columns are: [name,a_number,address,points]

**Contracts/:**  
Contains solidity code for smart contract

**Scripts/:** 
Contains js script for deploying smart contract

**Contracts/Handraise.sol:** 
Creates a smart contract that mints coins to students according to class participation credit.
When the tokens are transferred back to the smart contract the tokens are burned and an event is emitted.
Any eth that is sent to the contract is stored and an event is emitted. For the longevity of the contract we suggest 
offering extra credit for extra sepolia eth.
