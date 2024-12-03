# Step 1: Prepare Your Development Environment

Ensure you have the necessary tools and software:

1. Install Node.js: Ensure Node.js and npm (Node Package Manager) are installed.
Download from [Node.js](https://nodejs.org/).

2. Install Truffle: This framework simplifies the deployment process.
```bash
    npm install -g truffle
```

# Step 2: Compile the Smart Contract

1. Save your Solidity contract (e.g., ERC20Token.sol) in the appropriate directory, typically under a contracts folder.
2. Compile the contract:
    If using Truffle:
        Place your file in the contracts/ folder.
        Run ```truffle compile``` to generate the ABI and bytecode.

## Step 3: Deploy the Smart Contract

You need an Ethereum wallet (like MetaMask) and some ETH (testnet ETH for testnets).

1. Update the migration file in the migrations/ folder  (2_deploy_handraise.js is the file that should be updated)
2. Configure truffle-config.js with your network settings (e.g., Infura URL and private key).
3. Run the deployment:
```bash
    truffle migrate --network <network_name>
```

# Step 5: Verify Deployment

1. Use the token's address to verify on Etherscan (for public networks).
2. Test the token functions (transfer, approve, etc.) using tools like:
    - Hardhat console
    - Remix IDE
    - Web3.js or ethers.js scripts
