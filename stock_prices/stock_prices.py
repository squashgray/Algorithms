#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price = prices[0]
  max_profit_so_far = 0
  for price in prices:
    if price < current_min_price:
      current_min_price = price
    elif ((price - current_min_price) > max_profit_so_far):
      max_profit_so_far = price - current_min_price
  return max_profit_so_far


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))