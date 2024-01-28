import pandas as pd
from src.repository import read_and_clean_excel
from src.Graph import showGraph

from src.Profile import Profile
from src.Validators import save_data, bet, validate_type

data = read_and_clean_excel(4)
repeated_data = pd.DataFrame(columns=['time', 'case', 'betprice', 'result', 'bet', 'balance', 'profits'])

current_case = None
bet_price = 1
count = 0

my_profile = Profile(1500, 10)

for index, row in data.iterrows():
    case, time, result = row['case'], row['time'], row['result']

    if case == current_case:
        count += 1
    else:
        current_case = case
        count = 0

    if count >= 4:
        if not my_profile.big_loss(bet_price):
            my_profile.bet(bet_price)
            if bet(case, validate_type(result).value).value == "win":
                my_profile.win(bet_price)
                count = 0
                bet_price = 1

            else:
                bet_price *= 3

            repeated_data = save_data(time, case, bet_price, result, repeated_data, my_profile)

            if not my_profile.check_total_lost:
                break
        elif not my_profile.check_total_lost:
            break
        else:
            bet_price = 1

showGraph(repeated_data)
