// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract Handraise is ERC20 {
    address public owner;

    // Event to log when tokens are sent to the contract and burned
    event TokensBurned(address indexed sender, uint256 amount);

    // Event to log details of minting
    event TokensMinted(address indexed recipient, uint256 amount, string reason);

    // Event to log batch minting details
    event TokensMintedBatch(address[] recipients, uint256[] amounts);

    event ReceivedETH(address indexed sender, uint256 amount);


    constructor(
        string memory name,
        string memory symbol,
        uint8 decimals,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        owner = msg.sender;
        _mint(msg.sender, initialSupply * (10 ** decimals));
    }

    // Function to accept ETH transfers and store it
    receive() external payable {
        emit ReceivedETH(msg.sender, msg.value);
    }

     // Function to handle token transfers to the contract
    function burnTokensOnReceive(address from, uint256 amount) private {
        _burn(from, amount);
        emit TokensBurned(from, amount);
    }

    // Override the ERC20 _update function to burn tokens sent to the contract
    function _update(
        address from,
        address to,
        uint256 amount
    ) internal override {
        if (to == address(this)) {
            burnTokensOnReceive(from, amount);
        } else {
            super._update(from, to, amount);
        }
    }

    // Function to withdraw ETH from the contract
    function withdrawETH(uint256 amount, address payable to) external {
        require(msg.sender == owner, "Only the owner can withdraw ETH");
        require(address(this).balance >= amount, "Insufficient ETH balance");
        to.transfer(amount);
    }

    // Helper function to check the contract's ETH balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to mint new tokens
    function mint(address to, uint256 amount, string calldata reason) external {
        require(msg.sender == owner, "Only the owner can mint tokens");
        _mint(to, amount);
        emit TokensMinted(to, amount, reason);
    }


    // Function to mint tokens in batch
    function mintBatch(address[] calldata recipients, uint256[] calldata amounts) external {
        require(msg.sender == owner, "Only the owner can mint tokens");
        require(recipients.length == amounts.length, "Mismatched arrays");

        for (uint256 i = 0; i < recipients.length; i++) {
            _mint(recipients[i], amounts[i]);
        }

        emit TokensMintedBatch(recipients, amounts);
    }

    // Burn tokens manually
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }
}


