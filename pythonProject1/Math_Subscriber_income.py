def sub_money_(subscribers, lowest_cost, highest_cost, exp_losses):
    lowest_one_month_value = subscribers * lowest_cost
    print(f'Lowest cost for the month = {lowest_one_month_value:,}')
    highest_one_month_value = subscribers * highest_cost
    print(f"Highest cost for the month = {highest_one_month_value:,}")
    lowest_year_inc = lowest_one_month_value * 12
    print(f'Lowest cost for the year = {lowest_year_inc:,}')
    highest_year_inc = highest_one_month_value * 12
    print(f"Highest cost for the year = {highest_one_month_value:,}")
    rng_of_year_inc = lowest_year_inc + highest_year_inc
    print(f"Yearly Range = {rng_of_year_inc:,}")
    yearly_avg = rng_of_year_inc / 2
    print(f'Average for the year = {yearly_avg:,}')
    losses_year = yearly_avg - exp_losses
    print(f'Losses for the year = {losses_year:,}')


print(f'{sub_money_(34000000, 10, 15, 3000000000)}')

if __name__ == '__main__':
    print('Hi PyCharm')
