import json
from web3 import Web3
from dotenv import load_dotenv
import os



def mint_coins(file_path):
    # Set up account details
    decimals = 18
    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    private_key = os.getenv("PRIVATE_KEY")
    sepolia_rpc_url = os.getenv("SEPOLIA_RPC_URL")
    owner_address = os.getenv("PUBLIC_ADDRESS")

    # Connect to the Ethereum network
    infura_url = sepolia_rpc_url  # Replace with your Infura URL
    web3 = Web3(Web3.HTTPProvider(infura_url))

    # Check connection
    if not web3.is_connected():
        msg = "Failed to connect to Ethereum network"
        print(msg)
        return msg


    # Set up contract details
    contract_address = os.getenv("CONTRACT_ADDRESS") # Replace with your contract's address
    with open("../build/contracts/Handraise.json") as f:
        contract_abi = json.load(f)["abi"]
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Set up account details

    with open(file_path, "r") as file:
        data = json.load(file)

    # Prepare recipients and amounts
    recipients = [entry["address"] for entry in data.values()]
    amounts = [entry["points"]*(10**decimals) for entry in data.values()]

    # Build transaction
    nonce = web3.eth.get_transaction_count(owner_address)
    transaction = contract.functions.mintBatch(recipients, amounts).build_transaction({
        "chainId": 11155111,  # Sepolia Testnet chain ID (update for your network)
        "gas": 3000000,  # Adjust gas limit based on your contract
        "gasPrice": web3.to_wei("20", "gwei"),  # Adjust gas price
        "nonce": nonce,
    })

    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(transaction, private_key)

    # Send the transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    send_msg = f"Transaction sent! TX Hash: {web3.to_hex(tx_hash)}"
    print(send_msg)

    # Wait for confirmation
    tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    confirm_msg = f"Transaction confirmed in block {tx_receipt['blockNumber']}"
    print(confirm_msg)

    msg = f"{send_msg}\n\n{confirm_msg}"

    return msg

