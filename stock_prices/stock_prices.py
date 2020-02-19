# !/usr/bin/python

import argparse

def find_max_profit(prices):
  initial_profit = prices[1] - prices[0]
  max_profit = initial_profit
  for i in range(0, len(prices)):
    for k in range(i + 1, len(prices)):
      profit = prices[k] - prices[i]
      if profit > max_profit:
        max_profit = profit
 
  return max_profit

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

print(find_max_profit([10, 7, 5, 8, 11, 9]))