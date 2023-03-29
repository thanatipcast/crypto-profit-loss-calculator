# Crypto Profit/Loss Calculator

This Python program calculates the total profit or loss of multiple cryptocurrency transactions using the First In, First Out (FIFO) method.

## Problem Description

The program reads transaction data from a file and calculates the total profit or loss based on the FIFO method. Each transaction has the following format:
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

1. Transaction type: B or S, representing a buy (B) or sell (S) transaction
2. Cryptocurrency name: e.g., BTC, ETH
3. Price per coin: The price of the cryptocurrency per coin for the buy or sell transaction
4. Amount: The number of coins involved in the buy or sell transaction

The program calculates the total profit or loss for all transactions of the same cryptocurrency and prints the result.

## How to Run

1. Save your transaction data in a text file, e.g., `crypto_tax.txt`.
2. Run the Python script with a command-line argument:

```bash
python crypto_calculator.py
```

