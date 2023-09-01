import json
from web3 import Web3

#Import local Ganache URL (you can download Ganache here: https://trufflesuite.com/ganache/index.html )
ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

abi = json.loads('')
address = web3.toChecksumAddress("")

contract = web3.eth.contract(address=address, abi=abi)