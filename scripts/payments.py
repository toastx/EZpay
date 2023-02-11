from db import userDict,keypairDict,databse
from time import sleep
from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer
from solana.publickey import PublicKey
user = userDict['domain']


def topUpGas(user):
    print("choose top up method:")
    print('1: UPI')
    print("2: Card")
    print("3: NetBanking")

    ans = int(input())

    if ans == 1:
        print("QR:")
        print("UpiId:xxxxxxxxxx@upi")
        val = int(input("Amount:"))
        chk = int(input("press 1 after paying"))
        if chk == 1:
            sleep (2)
            for i in databse:
                if i['domain'] == user:
                    i['gasFeeBalance'] = val
                    print("gas top up complete")
                    break
    




def paySol(recipientName,amount):
    client: Client = Client("https://api.devnet.solana.com")
    sender = keypairDict['sol']
    print(sender)
    transaction = Transaction().add(transfer(TransferParams(
        from_pubkey= sender.public_key,
        to_pubkey=PublicKey(recipientName),
        lamports= amount*1000000000)
    ))

    client.send_transaction(transaction, sender)
    print(transaction.signature)


