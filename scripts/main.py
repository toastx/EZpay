import domain
import payments
import db
import balance
wdict = {}

def main():
    print("888888888888    888888888888     888888888888          88         88        88")
    print("88                       88      88        88        88  88        88      88")
    print("88                      88       88        88       88    88        88    88")
    print("88888888              88         888888888888      88      88        88  88")
    print("88                  88           88               88 888888 88         88")
    print("88                88             88              88          88        88")
    print("888888888888    888888888888     88             88            88       88")

    print("*                                                                          *")
    print("-----------------------------------------------------------------------------")
    print("Welcome to EZpay CLI.....")
    
    name = domain.naming()
    print("Commands List:")
    print("addsol • Enter sol address")
    print("addbsc • Enter bsc address")
    print("addeth • Enter eth address")
    print("addtrx • Enter trx address")
    print("confirm • syncs your domain name and addresses")
    print("show • shows your addresses")
    while True:
        ans = str(input())
        if ans == "addsol":
            domain.addSol()
        elif ans =="addbsc":
            domain.addBsc()
        elif ans =="addeth":
            domain.addErc()
        elif ans =="addtrx":
            domain.addTrx()
        elif ans == "confirm":
            db.userDict['domain'] = name
            db.userDict['walletAddresses'] = domain.walletDict
            print(db.userDict['walletAddresses'])
            print(db.userDict['domain'])
            db.databse.append(db.userDict)
            


        elif ans == "show":
            for i in db.databse:
                if i['domain'] == name:
                    dict = i
            print(dict['accountBalance'])
        elif ans == 'topupsol':
            balance.addSol()    
        elif ans == 'topup':
            payments.topUpGas(name)  
        elif ans == "pay":
            addy = str(input("enter recipients address: "))  
            amount = int(input("enter amount in sol:"))
            payments.paySol(addy,amount)


main()