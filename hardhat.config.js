require("@nomicfoundation/hardhat-toolbox");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.20",
  networks: {
    ganache: {
      url: "http://127.0.0.1:8545",
      accounts: ["0xc15979e52dd149f179ee7776c3c51feb060f5f4d6a67250a6ba039009424834e"], // Add Ganache's pre-funded account private key
    },
  },
};
