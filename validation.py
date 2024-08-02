from config import (
    NUMBER_OF_SLOTS, DEFAULT_SLOT_SIZE, MIN_PULL_CYCLES, MAX_PULL_CYCLES,
    SLOT_SYMBOLS
)


def validate_configurations() -> None:
    """Validate configuration parameters."""

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

    # Validate SLOT_SYMBOLS
    for i, symbol in enumerate(SLOT_SYMBOLS):
        if len(symbol) > 1:
            errors.append(f"Symbol at index {i} ({symbol}) is not a single Unicode character.")

    if errors:
        error_message = "\n".join(errors) + "\n\nPlease update config.py to correct these issues."
        raise ValueError(error_message)
