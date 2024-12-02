const Handraise = artifacts.require("Handraise");

module.exports = function (deployer) {
    // Replace with your token details
    const name = "Handraise";
    const symbol = "HAND";
    const decimals = 18;
    const initialSupply = "1000000000000000000000"; // 1000 tokens (adjust as needed)

    deployer.deploy(Handraise, name, symbol, decimals, initialSupply);
};