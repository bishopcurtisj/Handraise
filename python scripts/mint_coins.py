import json
from web3 import Web3

def mint_coins(file_path):
    # Connect to the Ethereum network
    infura_url = "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura URL
    web3 = Web3(Web3.HTTPProvider(infura_url))

    # Check connection
    if not web3.isConnected():
        print("Failed to connect to Ethereum network")
        exit()

    # Set up contract details
    contract_address = "DEPLOYED_CONTRACT_ADDRESS"  # Replace with your contract's address
    contract_abi = json.loads("""[YOUR_CONTRACT_ABI_HERE]""")  # Replace with your contract's ABI
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Set up account details
    owner_address = "YOUR_WALLET_ADDRESS"  # Replace with your wallet address
    private_key = "YOUR_PRIVATE_KEY"  # Replace with your private key

    with open(file_path, "r") as file:
        data = json.load(file)

    # Prepare recipients and amounts
    recipients = [entry["address"] for entry in data.values()]
    amounts = [entry["points"] for entry in data.values()]

    # Build transaction
    nonce = web3.eth.getTransactionCount(owner_address)
    transaction = contract.functions.mintBatch(recipients, amounts).buildTransaction({
        "chainId": 5,  # Goerli Testnet chain ID (update for your network)
        "gas": 3000000,  # Adjust gas limit based on your contract
        "gasPrice": web3.toWei("20", "gwei"),  # Adjust gas price
        "nonce": nonce,
    })

    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(transaction, private_key)

    # Send the transaction
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Transaction sent! TX Hash: {web3.toHex(tx_hash)}")

    # Wait for confirmation
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print(f"Transaction confirmed! Block: {tx_receipt.blockNumber}")
