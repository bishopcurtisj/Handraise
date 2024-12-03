from web3 import Web3
import pandas as pd
import json
from dotenv import load_dotenv
import os



def read_events():

    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    sepolia_rpc_url = os.getenv("SEPOLIA_RPC_URL")
    # Infura or other provider URL
    INFURA_URL = sepolia_rpc_url  # Replace with your Infura URL
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))

    # Check connection
    if not web3.is_connected():
        print("Failed to connect to Ethereum network")
        exit()

    # Contract details
    CONTRACT_ADDRESS = os.getenv("CONTRACT_ADDRESS") # Replace with your contract's address
    with open("../build/contracts/Handraise.json") as f:
            CONTRACT_ABI = json.load(f)["abi"]
    # Initialize contract
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

    # Event signature for TokensBurned(address indexed sender, uint256 amount)
    event_signature_hash = web3.keccak(text="TokensBurned(address,uint256)").hex()
    event_signature_hash = "0x" + event_signature_hash
    # Define block range to scan
    START_BLOCK = 7_100_000  # Replace with the block number where your contract was deployed
    END_BLOCK = web3.eth.block_number  # Get the latest block number

    # List to store event data
    events_data = []

    # Fetch all TokensBurned events
    print(f"Fetching TokensBurned events from block {START_BLOCK} to {END_BLOCK}...")
    logs = web3.eth.get_logs({
        "fromBlock": START_BLOCK,
        "toBlock": END_BLOCK,
        "address": CONTRACT_ADDRESS,
        "topics": [event_signature_hash]
    })

    for log in logs:
        # Decode the log data
        decoded_event = contract.events.TokensBurned().process_log(log)
        sender = decoded_event["args"]["sender"]
        amount = decoded_event["args"]["amount"]
        block_number = decoded_event["blockNumber"]

        # Append to the list
        events_data.append({
            "Sender": sender,
            "Amount Burned": web3.from_wei(amount, "ether"),  # Convert to Ether if applicable
            "Block Number": block_number
        })

    # Save events to CSV
    df = pd.DataFrame(events_data)
    df.to_csv("tokens_burned_events.csv", index=False)

    print(f"TokensBurned events saved to 'tokens_burned_events.csv'.")


def test_grades(students):
    
    events = pd.read_csv("tokens_burned_events.csv")

    for student in students.keys():
        if students[student]['address'] in events['Sender'].values:
            ## get the index of the value
            index = events[events['Sender'] == students[student]['address']].index[0]
            grade = events['Amount Burned'][index]
            user_id = student
            print(user_id, grade)
        else:
            print(f"User {student} did not burn any tokens")
