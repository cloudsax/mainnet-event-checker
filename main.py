import sys
from core.engine import run_validator
from colorama import Fore, Style

def main():
    print(f"{Fore.CYAN}--- Rewards Validation Engine v2.0.4 ---{Style.RESET_ALL}")
    wallet = "0x..." # User input simulation
    result = run_validator(wallet)
    
    if result['eligible']:
        print(f"{Fore.GREEN}[SUCCESS] Allocation found! Check README for claim link.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
