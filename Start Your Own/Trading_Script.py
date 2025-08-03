"""Wrapper for the shared trading script using local data directory."""

from pathlib import Path
import sys

# Allow importing the shared module from the repository root
sys.path.append(str(Path(__file__).resolve().parents[1]))

from trading_script import main


if __name__ == "__main__":
    cash = 100
    chatgpt_portfolio = [
        {"ticker": "QSI", "shares": 9, "stop_loss": 0.90, "buy_price": 1.48, "cost_basis": 13.32},
        {"ticker": "FDMT", "shares": 3, "stop_loss": 5.00, "buy_price": 6.39, "cost_basis": 19.17},
        {"ticker": "ALT", "shares": 3, "stop_loss": 2.50, "buy_price": 3.68, "cost_basis": 11.04},
        {"ticker": "GLUE", "shares": 3, "stop_loss": 3.50, "buy_price": 4.79, "cost_basis": 14.37},
        {"ticker": "TXMD", "shares": 6, "stop_loss": 0.80, "buy_price": 1.11, "cost_basis": 6.66},
    ]

    data_dir = Path(__file__).resolve().parent
    main(chatgpt_portfolio, cash, data_dir)

