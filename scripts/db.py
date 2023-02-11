from localStoragePy import localStoragePy

ls = localStoragePy("database","json")

walletDict = {
        "sol":None,
        "bsc20":None,
        "erc20":None,
        "trc20":None,
        "btc":None
    }
    

poiDict = {
    "aadhar":str,
    "pancard":str
}

kycDict = {
    "firstName":str,
    "middleName":str,
    "lastName":str,
    "dob":str,
    "phoneNumber":str,
    "gender":str,
    "address":str,
    "occupation":str,
    "POI": poiDict
}
keypairDict={
    "sol":int,
    "bsc":int,
    "eth":int,
    "trx":int,
    "btc":int
}

accountBalanceDict = {
    'sol':0,
    'bnb':0,
    "btc":0,
    "eth":0,
    "trc":0
}

userDict = {
    'domain':str,
    'userName':str,
    'password':str,
    'KYCdata':kycDict,
    'walletAddresses':walletDict,
    'gasFeeBalance':int,
    'accountBalance':accountBalanceDict,
    'keypairs':keypairDict
}

databse = []

