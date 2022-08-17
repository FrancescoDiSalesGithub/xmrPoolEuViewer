import requests
import xmrpool
import sys

if __name__ == '__main__':


    response = requests.get("https://web.xmrpool.eu:8119/stats_address?address="+sys.argv[1]+"&longpoll=false")
    data = response.json()

    xmrpoolobj = xmrpool.xmrpool(data['stats'],data['perWorkerStats'],data['payments'])

    balance = xmrpoolobj.get_balance()
    payments = xmrpoolobj.get_payments()

    print("balance: "+balance)
    print("payments: ")

    for pays in payments:
        print(pays)

    xmrpoolobj.get_list_workers()













