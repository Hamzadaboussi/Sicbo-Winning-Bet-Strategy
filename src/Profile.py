class Profile:
    def __init__(self, balance, base_bet_price):
        self.balance = balance
        self.base_bet_price = base_bet_price
        self.profit_balance =0
        self.initial_balance=balance

    def win(self, occurrence):
        self.balance += occurrence * self.base_bet_price * 2
        self.gain_profits()

    def win_number(self, occurrence,dice,result):
        bonus = 1
        if f"{dice}-{dice}-{dice}" in result:
            bonus =3
            print(occurrence * self.base_bet_price * 2 *bonus)
            print(bonus)
        elif f"{dice}-{dice}" in result:
            bonus =2
            print(occurrence * self.base_bet_price * 2 * bonus)
            print(bonus)
        self.balance += occurrence * self.base_bet_price * 2 *bonus
        self.gain_profits()
    def gain_profits(self):
        if (self.balance > self.initial_balance):
            self.profit_balance += (self.balance - self.initial_balance)
            self.balance = self.initial_balance

    def bet(self, occurrence):
        self.balance -= occurrence * self.base_bet_price


    def big_loss(self, occurrence):
        if not self.check_you_can_bet(occurrence):
            if self.profit_balance > self.initial_balance:
                self.profit_balance -= self.initial_balance-self.balance
                self.balance = self.initial_balance
            # elif self.profit_balance ==0:
            #     print("no money to bet your balance =",self.balance,"the bet price =",occurrence * self.base_bet_price,"and your profits =",self.profit_balance)
            else:
                self.balance += self.profit_balance
                self.profit_balance = 0
            return True
        return False




    def get_profit_balance(self):
        return self.profit_balance

    def get_balance(self):
        return self.balance

    def check_you_can_bet(self,occurrence):
        if self.balance > (occurrence*2) * self.base_bet_price :
            return True
        else:return False


    def check_total_lost(self):
        if self.balance<=0 and self.profit_balance==0 :
            #print("you lost all your money")
            return True
        else:return False
