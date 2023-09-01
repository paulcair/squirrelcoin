from web3 import Web3

#Import local Ganache URL (you can download Ganache here: https://trufflesuite.com/ganache/index.html )
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

#Check that server is connected and print the block
print(web3.isConnected())
print(web3.eth.blockNumber) 

#Import the ABI and address of a token called OMGToken as found on etherscan.io
#abi = json.loads('[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')
#address = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"

#Print ABI and address
#print(abi)
#print(address)

#Print the total supply
#print(totalSupply)

#Provide names for the Ganache based account numbers 
Jeff = "0x9f2faf1b200f9157Db3362fb129abe145190B725"
Alex = "0xB3845cB946D78A9fA90c1BE927178585D48A2AFE"
Grant = "0xCc565239b289f3b88BF0c5f2D337214964278acc"
Andrew = "0x8A1A76F2Fb4A818FfB6139f68a83f7588ec61b9A"
Paul = "0xfa4197Ec7cAAF4638997Ae97691c2679E1a8b68E"

#Provide private keys for the Ganache based accounts
Jeff_pk = "eb364a49d117deb16285b59a22478438c6aa10b6d90b64feb74c7afaf0056f9d"
Alex_pk = "6af8116efa3c805bd32debc018901ac15eaad521891f1ba55f81a527077d004a"
Grant_pk = "bb1a50f180bbfbea7e199b86a54a0b1ab9efa0ec262c8646f4f557bff6dc429b"
Andrew_pk = "35d8066b26d2003a428bdeb55b98609406978a1e83c981e90eb5e0c39a96f29e"
Paul_pk = "3cb94ac2e3c17a90ee238d2bb027bb440661a638d9d6ba098ddd2c23e02ca201"

#Ge the nonce
nonce = web3.eth.getTransactionCount(Alex)

#Build a transaction
tx = {
    'nonce': nonce,
    'to': Jeff,
    'value': web3.toWei(1,'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

#Sign a transaction
signed_tx = web3.eth.account.signTransaction(tx, Alex_pk)

#Send a transaction and assign a hash
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#Print transaction hash
print(web3.toHex(tx_hash))



