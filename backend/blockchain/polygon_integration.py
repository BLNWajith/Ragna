from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.exceptions import TransactionNotFound

polygon_rpc_url = "https://polygon-mainnet.infura.io"
private_key = "deal trash wish crater erode post network insect tumble exchange easily salad"

w3 = Web3(Web3.HTTPProvider(polygon_rpc_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
account = w3.eth.account.from_key(private_key)

token_address = "YOUR_ERC20_TOKEN_ADDRESS_ON_ETHEREUM"

token_abi = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
]

token_contract = w3.eth.contract(address=token_address, abi=token_abi)
bridge_contract_address = "YOUR_POLYGON_BRIDGE_CONTRACT_ADDRESS"
approve_tx = token_contract.functions.approve(bridge_contract_address, amount_to_transfer).buildTransaction( # type: ignore
    {
        "from": account.address,
        "gas": 200000,
        "nonce": w3.eth.getTransactionCount(account.address)
    }
)

signed_approve_tx = w3.eth.account.sign_transaction(approve_tx, private_key=private_key)
approve_tx_hash = w3.eth.sendRawTransaction(signed_approve_tx.rawTransaction)
w3.eth.waitForTransactionReceipt(approve_tx_hash)
deposit_tx = bridge_contract.functions.deposit(amount_to_transfer).buildTransaction( # type: ignore
    {
        "from": account.address,
        "gas": 200000,
        "nonce": w3.eth.getTransactionCount(account.address)
    }
)

signed_deposit_tx = w3.eth.account.sign_transaction(deposit_tx, private_key=private_key)
deposit_tx_hash = w3.eth.sendRawTransaction(signed_deposit_tx.rawTransaction)
try:
    w3.eth.waitForTransactionReceipt(deposit_tx_hash)
    print("Tokens deposited successfully!")
except TransactionNotFound:
    print("Deposit transaction not found. Please check the transaction hash.")
