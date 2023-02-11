from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from db import userDict
from time import sleep

def addSol():
    LAMPORT_PER_SOL = 1000000000

    client: Client = Client("https://api.devnet.solana.com")

    sender = userDict['keypairs']['sol']

    val = int(input("Enter sol you want to top up:"))
    sleep(2)
    airdrop = client.request_airdrop(sender.public_key, val * LAMPORT_PER_SOL)
    airdrop_signature = airdrop["result"]
    client.confirm_transaction(airdrop_signature)
    userDict['accountBalance']['sol'] = val
    print(f"{val} sol topped up")


