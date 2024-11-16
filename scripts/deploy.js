const hre = require("hardhat");

async function main() {
  // Get the contract factory
  const Handraise = await hre.ethers.getContractFactory("Handraise");
  console.log("Contract factory created");

  // Deploy the contract
  const handraise = await Handraise.deploy(1000000); // Pass initial supply if needed
  console.log("Deployment transaction:", handraise.deployTransaction.hash);

  // Wait for the contract to be deployed
  await handraise.deployed();
  console.log("Contract deployed to:", handraise.address);
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
