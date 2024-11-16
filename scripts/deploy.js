const hre = require("hardhat");

async function main() {
  const initialSupply = 100000; // 1 million tokens

  // Deploy the contract
  const Handraise = await hre.ethers.getContractFactory("Handraise");
  console.log("Contract factory created");

  const handraise = await Handraise.deploy(10);
  console.log("Deployment transaction:", handraise.deployTransaction);


  await handraise.deployed();

  console.log(`MyToken deployed to: ${handraise.address}`);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
