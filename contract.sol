pragma solidity ^0.5.5;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/math/SafeMath.sol";

/**

*/
contract EthBNB {
    /** address of property owner
    */
    using SafeMath for uint256;
    address payable public bnb_owner;
    address public payer;
    string bnb;
    address last_to_deposit;
    uint256 last_deposit_amount;
    uint256 fee;
    uint256 public balance;
    address last_to_withdraw;
    uint256 last_withdraw_amount;
    address contract_owner;

    function pay(address payable recipient) public payable {
        require(recipient == bnb_owner, "wrong account");
        require(msg.value == fee,"wrong amount paid");
        if (last_to_deposit !=msg.sender) {
            last_to_deposit = msg.sender; 
        }
        last_deposit_amount = msg.value;
        balance = address(this).balance + fee;
    }
    function withdraw(uint amount, address payable recipient) public {
        require(balance == amount || balance > amount, "insufficient funds");
        require(recipient == bnb_owner, "not owner of property");
        if (last_to_withdraw != recipient) {
            last_to_withdraw = recipient;
        }
        last_withdraw_amount = amount;
        balance = address(this).balance - amount;

        return msg.sender.transfer(amount);
    }
    function refund (uint256 amount, address refundee) public payable {
        require (amount == fee, "not equal");
        require (refundee == payer, "not payer");
        if (amount != fee) {
            amount = fee;
        }
        last_withdraw_amount = amount;
        last_to_withdraw = refundee;
        balance = address(this).balance - amount;
    }
    function take_cut(address recipient, uint cut) public payable{
        require (recipient == contract_owner, "not owner of contract");
        require (cut == balance/10, "cut too big");
        balance = address(this).balance;
        cut = balance/10;
    }
    function() external payable {}
}
    









