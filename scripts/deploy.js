const hre = require("hardhat");

async function main() {
  const initialSupply = 10; // 1 million tokens

  // Deploy the contract
  const Handraise = await hre.ethers.getContractFactory("Handraise");
  const handraise = await Handraise.deploy(initialSupply);

  await handraise.deployed();

  console.log(`MyToken deployed to: ${handraise.address}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
