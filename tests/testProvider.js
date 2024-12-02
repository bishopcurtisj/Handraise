require('dotenv').config();
const HDWalletProvider = require("@truffle/hdwallet-provider");

const provider = new HDWalletProvider(
    process.env.PRIVATE_KEY,
    process.env.SEPOLIA_RPC_URL
);

console.log("Provider initialized:", provider);