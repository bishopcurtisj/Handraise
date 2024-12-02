require("dotenv").config();
const HDWalletProvider = require("@truffle/hdwallet-provider");

module.exports = {
    networks: {
        // Local development network
        development: {
            host: "127.0.0.1", // Localhost
            port: 7545,        // Ganache default port
            network_id: "*",   // Match any network ID
        },
        
        // Sepolia testnet
        sepolia: {
            provider: () =>
                new HDWalletProvider(
                    process.env.PRIVATE_KEY,
                    process.env.SEPOLIA_RPC_URL
                ),
            network_id: 11155111, // Sepolia network ID
            gas: 5500000,
            confirmations: 2,
            timeoutBlocks: 200,
            skipDryRun: true,
        },
        
    },
    // Configure Solidity compiler version
    compilers: {
        solc: {
            version: "0.8.20", // Update this to match your contract's Solidity version
            settings: {
                optimizer: {
                    enabled: true,
                    runs: 200,
                },
            },
        },
    },
    
    plugins: ["truffle-plugin-verify"],
};