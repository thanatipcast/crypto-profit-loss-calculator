import sys

def read_transactions(file_name):
    transactions = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            parts = line.strip().split()
            transaction = (parts[0], parts[1], float(parts[2]), float(parts[3]))
            transactions.append(transaction)
    return transactions

def fifo_profit_loss(transactions):
    buys = {}
    profit_loss = 0.0

    for transaction in transactions:
        action, coin, price, amount = transaction
        if action == 'B':
            if coin not in buys:
                buys[coin] = []
            buys[coin].append((price, amount))
        elif action == 'S':
            if coin not in buys or len(buys[coin]) == 0:
                sys.exit("Error: Not enough coins to sell")
                

            remaining_amount = amount
            while remaining_amount > 0:
                buy_price, buy_amount = buys[coin][0]
                sell_amount = min(remaining_amount, buy_amount)
                profit_loss += (price - buy_price) * sell_amount

                if buy_amount == sell_amount:
                    buys[coin].pop(0)
                else:
                    buys[coin][0] = (buy_price, buy_amount - sell_amount)
                remaining_amount -= sell_amount

    return profit_loss

def main():
    file_name = "crypto_tax.txt"
    transactions = read_transactions(file_name)
    profit_loss = fifo_profit_loss(transactions)
    print('Total profit/loss:', profit_loss)

if __name__ == "__main__":
    main()
