from decimal import *

getcontext().prec = 78

BASE_EXP = 30
DECIMAL = 18

def coin_supply_base(expo):
    expo = expo + DECIMAL
    print("expo", expo)
    return Decimal(10**expo)

def max_int_size():
    #Max Integer accepted by solidity 2**256 - 1
    return Decimal(2**256 - 1)

def max_coin(expo):
    #fit
    m = max_int_size()
    c = coin_supply_base(expo)
    return m / c

def one_dollar():
    # cost amount to buy whole all coins for one one dollar
    mxc = max_coin(30)
    print("max_coin", mxc)

    div_by_one = Decimal(1) / mxc

    print("div_by_one", div_by_one)

    assert div_by_one * mxc == 1

    return div_by_one

def total_price_check(price):
    #cost to buy the max amount of coins
    mxc = max_coin(30)
    total_cost = mxc * Decimal(price)
    print('total_cost', total_cost)

    return total_cost

if __name__ == '__main__':
    one_dollar()
    total_price_check(10**-16)
