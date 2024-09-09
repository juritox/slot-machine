"""
This module provides validation functions for the Slot Machine game configuration.

It includes functions to validate various game settings and ensure they meet
the required criteria for the game to function correctly.
"""

from config import (
    NUMBER_OF_SLOTS, DEFAULT_SLOT_SIZE, MIN_PULL_CYCLES, MAX_PULL_CYCLES,
    SLOT_SYMBOLS, SLOT_NUMBERS, JACKPOT_WINNING_SYMBOL, JACKPOT_WINNING_NUMBER,
    PULL_COST, WIN_PRIZE
)


def validate_configurations() -> None:
    """
    Validate configuration parameters.

    This function checks various configuration settings to ensure they meet
    the required criteria for the game to function correctly.

    Raises:
        ValueError: If any configuration setting is invalid.
    """
    errors: list[str] = []

    if NUMBER_OF_SLOTS < 2:
        errors.append("NUMBER_OF_SLOTS must be at least 2.")
    if DEFAULT_SLOT_SIZE != 20:
        errors.append("DEFAULT_SLOT_SIZE must be set to 20.")
    if MIN_PULL_CYCLES < 1:
        errors.append("MIN_PULL_CYCLES must be at least 1.")
    if MAX_PULL_CYCLES > 100:
        errors.append("MAX_PULL_CYCLES must not be greater than 100.")
    if MIN_PULL_CYCLES > MAX_PULL_CYCLES:
        errors.append("MIN_PULL_CYCLES must not be greater than MAX_PULL_CYCLES.")
    if WIN_PRIZE < PULL_COST * 2:
        errors.append("WIN_PRIZE must be at least twice as big as PULL_COST.")

    # Validate SLOT_SYMBOLS
    for i, symbol in enumerate(SLOT_SYMBOLS):
        if len(symbol) > 1:
            errors.append(f"Symbol at index {i} ({symbol}) is not a single Unicode character.")

    # Validate JACKPOT_WINNING_SYMBOL and JACKPOT_WINNING_NUMBER
    if JACKPOT_WINNING_SYMBOL not in SLOT_SYMBOLS:
        errors.append(f"Jackpot symbol {JACKPOT_WINNING_SYMBOL} is not included in slot symbols: {SLOT_SYMBOLS}.")
    if JACKPOT_WINNING_NUMBER not in SLOT_NUMBERS:
        errors.append(f"Jackpot number {JACKPOT_WINNING_NUMBER} is not included in slot numbers: {SLOT_NUMBERS}.")

    if errors:
        error_message = "\n".join(errors) + "\n\nPlease update config.py to correct these issues."
        raise ValueError(error_message)
