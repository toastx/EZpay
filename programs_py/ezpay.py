from seahorse.prelude import *

declare_id('Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS')

class KYC(Account):
    owner: Pubkey
    cid : str

def init(owner: Signer, KYC = Empty[KYC]):
    KYC = KYC.init(payer=owner, seeds=["KYC",owner])
    KYC.owner = owner.key()

# def requestKYC():


# def approveKYC():


# def approvedKYC():



