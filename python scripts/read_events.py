from web3 import Web3
import pandas as pd
import json

def read_events():
    # Infura or other provider URL
    INFURA_URL = "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura URL
    web3 = Web3(Web3.HTTPProvider(INFURA_URL))

    # Check connection
    if not web3.isConnected():
        print("Failed to connect to Ethereum network")
        exit()

    # Contract details
    CONTRACT_ADDRESS = "YOUR_CONTRACT_ADDRESS"  # Replace with your contract's address
    CONTRACT_ABI = json.loads("""[YOUR_CONTRACT_ABI_HERE]""")  # Replace with your contract's ABI

    # Initialize contract
    contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

    # Event signature for TokensBurned(address indexed sender, uint256 amount)
    event_signature_hash = web3.keccak(text="TokensBurned(address,uint256)").hex()

    # Define block range to scan
    START_BLOCK = 0  # Replace with the block number where your contract was deployed
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
        decoded_event = contract.events.TokensBurned().processLog(log)
        sender = decoded_event["args"]["sender"]
        amount = decoded_event["args"]["amount"]
        block_number = decoded_event["blockNumber"]

        # Append to the list
        events_data.append({
            "Sender": sender,
            "Amount Burned": web3.fromWei(amount, "ether"),  # Convert to Ether if applicable
            "Block Number": block_number
        })

    # Save events to CSV
    df = pd.DataFrame(events_data)
    df.to_csv("tokens_burned_events.csv", index=False)

    print(f"TokensBurned events saved to 'tokens_burned_events.csv'.")
