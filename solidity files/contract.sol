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
    uint256 public balance;
    address last_to_withdraw;
    uint256 last_withdraw_amount;
    address contract_owner;
    uint fee;
    mapping(address => uint) public lockTime;
    mapping(address => uint) public balances;


    function pay(address payable recipient, uint amount) public payable {
        require(recipient == bnb_owner, "wrong account");
        require(amount == fee,"wrong amount paid");
        if (last_to_deposit !=msg.sender) {
            last_to_deposit = msg.sender; 
        }
        last_deposit_amount = msg.value;
        balance = address(this).balance + fee;
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
    function buy_property(address payable recipient, uint amount) public payable {
        require (recipient == bnb_owner, "not owner");
        if (last_to_deposit != msg.sender){
            last_to_deposit = msg.sender;
        }
        last_deposit_amount = msg.value;
        balance = address(this).balance + amount;
    }
    function increaseLockTime(uint _secondsToIncrease) public {

        // the add function below is from safemath and will take care of uint overflow
        // if a call to add causes an error an error will be thrown and the call to the function will fail
         lockTime[msg.sender] = lockTime[msg.sender].add(_secondsToIncrease);

    }

      

    function withdraw() public {

        // check that the sender has ether deposited in this contract in the mapping and the balance is >0
        require(balances[msg.sender] > 0, "insufficient funds");

        // check that the now time is > the time saved in the lock time mapping
        require(block.timestamp > lockTime[msg.sender], "lock time has not expired");
      

        // update the balance
        balances[msg.sender] = 0;
    }
    function() external payable {}
}

/**     unneeded delete if needed
function withdraw_timelocked(uint amount, address payable recipient) public {
        require(balance == amount || balance > amount, "insufficient funds");
        require(recipient == bnb_owner, "not owner of property");
        if (last_to_withdraw != recipient) {
            last_to_withdraw = recipient;
        }
        last_withdraw_amount = amount;
        balance = address(this).balance - amount;

        return msg.sender.transfer(amount);
    }
    **/


    









