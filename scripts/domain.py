from db import walletDict,keypairDict
from solana.keypair import Keypair
import base58


def naming():
    
    name = str(input("Enter a domain name you would like to own: "))
    name = name + ".mag"
    if name in walletDict:
        print("domain not available")
        name()
    print(name)
    return name


    
def addSol():
    print("Import new account or create new account")
    ans = int(input())
    if ans == 1:
        print("Enter private key")
        key = str(input())
        byte_array = base58.b58decode(key)
        keypair = Keypair.from_secret_key(bytes(byte_array))
        print(f'new wallet address : {keypair.public_key}')
        walletDict['sol'] = keypair.public_key
        keypairDict['sol'] = keypair
        print(keypairDict['sol'])

    else:
        keypair = Keypair.generate()
        walletDict["sol"] = keypair.public_key
        keypairDict['sol'] = keypair
    

def addBsc():
    bscAddy = str(input("Enter bsc20 address:"))
    walletDict["bsc20"] = bscAddy

def addErc():
    erc20Addy = str(input("Enter erc20 address:"))
    walletDict["erc20"] = erc20Addy

def addTrx():
    trc20Addy = str(input("Enter trc20 address:"))
    walletDict["trc20"] = trc20Addy






