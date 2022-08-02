def num_coins(value_of_change_needed, coin_values = [1, 2, 5, 10, 20, 50, 100, 200]):
    coin_values_sorted = sorted(coin_values, reverse=True)
    num_coins_needed = 0
    
    for coin_value in coin_values_sorted:
        num_coins_needed += value_of_change_needed // coin_value
        value_of_change_needed %= coin_value
    return num_coins_needed

