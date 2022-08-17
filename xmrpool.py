class xmrpool:

    def __init__(self,stats,worker,payments):
        self.stats = stats
        self.worker = worker
        self.payments = payments

    def get_balance(self):
        return self.stats['balance']

    def get_payments(self):
        return self.payments

    def get_workers(self):
        return self.worker

    def get_list_workers(self):
        print("workers: ")
        for value in self.worker:
            print("worker id: " + value['workerId']+ " hashrate: " + value['hashrate']  + " hashes: " + value['hashes'] + " last share: " + value['lastShare'] + " expired: "+value['expired'])

    def get_list_payments(self):
        print("payments: ")
        for pays in self.payments:
            print(pays)

