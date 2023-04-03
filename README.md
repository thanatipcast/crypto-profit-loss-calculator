# Crypto Profit/Loss Calculator

This program calculates the total profit or loss of cryptocurrency transactions using First In, First Out algorithm.

## Problem Description

The program reads transaction data from a file and calculates the total profit or loss based on the FIFO method. The transaction text file should look like this:
```
B BTC 680000.0 2.5 
B ETH 43000.0 12.0 
B BTC 690000.0 2.5 
S BTC 695000.0 3.0 
B ETH 43500.0 23.5 
S BTC 695000.0 1.0 
S ETH 45000.0 30.0 
```


Each line in the data file has 4 fields, as follows:

1. Transaction type: Buy or Sell, indicating each transaction
2. Cryptocurrency name: BTC, ETH
3. Price per coin: The price per coin for each buy or sell transaction
4. Amount: The amount of number of buy or sell

The program calculates the total profit or loss for all transactions of the same cryptocurrency and prints the result.

## How to Run

1. Include transaction text file in your directory and save it as any name.
2. Run the program with a command-line argument:

```bash
python crypto_calculator.py
```

