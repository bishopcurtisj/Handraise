# Handraise

## Requirements

The python scripts require the following packages:
- web3
- pandas
- dotenv

They can be installed with:
```bash
pip install pandas web3 dotenv
```
```bash
conda install pandas web3 dotenv
```

The required NPM packages are:
- @truffle/hdwallet-provider
- dotenv

They can be installed with:
```bash
npm install @truffle/hdwallet-provider dotenv
```

All of the code will require a .env file in the root directory, example contents of this file can be found [here](#example-env-file)

## Usage

From the directory that main.py is in run 
```
python main.py
```
Then choose the relevant menu options by entering the associated number.

```
$ python main.py

1. Mint Coins
2. Update Grades
3. Read Events
4. Exit
Enter your choice:

```

**1. Mint Coins**
Reads the students.csv file and mints coins equal to earned points to each student address in the file.

**2. Update Grades**
Reads token burning events and then updates student grades in canvas according to the tokens burned by each student.

**3. Read Events**
Reads token burning events then prints student a-numbers and tokens burned, primarily for testing.

In order to deploy the smart contract follow the instructions in this [file](truffle_deployment_instructions.md)

## File Organization

### python scripts/

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

**Migrations/:** 
Contains js script for deploying smart contract

**Contracts/Handraise.sol:** 
Creates a smart contract that mints coins to students according to class participation credit.
When the tokens are transferred back to the smart contract the tokens are burned and an event is emitted.
Any eth that is sent to the contract is stored and an event is emitted. For the longevity of the contract we suggest 
offering extra credit for extra sepolia eth.



## Example .env file

PRIVATE_KEY=your_private_key\
SEPOLIA_RPC_URL=https://sepolia.infura.io/v3/your_project_id \
PUBLIC_ADDRESS=your_public_addresss\
CANVAS_URL=https://yourcanvasinstance.instructure.com/api/v1
CANVAS_ACCESS_TOKEN=your_canvas_access_token\
COURSE_ID=1234\
ASSIGNMENT_ID=5678\
CONTRACT_ADDRESS=your_contract_address
