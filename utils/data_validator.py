"""Data validation utilities for molecular datasets."""


def validate_smiles(smiles: str) -> bool:
    """
    Validate SMILES string format.

    Args:
        smiles: SMILES string to validate

    Returns:
        True if valid, False otherwise
    """
    if not smiles or not isinstance(smiles, str):
        return False

    # Basic validation: check for valid characters
    valid_chars = set("CNOPSFClBrI0123456789[]()=#@+-\\/%")
    return all(c in valid_chars for c in smiles.replace(" ", ""))


def validate_numeric_value(value: float, min_val: float = None, max_val: float = None) -> bool:
    """
    Validate numeric value is within acceptable range.

    Args:
        value: Numeric value to validate
        min_val: Minimum acceptable value (optional)
        max_val: Maximum acceptable value (optional)

    Returns:
        True if valid, False otherwise
    """
    try:
        val = float(value)
        if min_val is not None and val < min_val:
            return False
        if max_val is not None and val > max_val:
            return False
        return True
    except (TypeError, ValueError):
        return False


def check_dataset_completeness(data: dict) -> tuple[bool, list[str]]:
    """
    Check if dataset has required fields.

    Args:
        data: Dictionary containing dataset information

    Returns:
        Tuple of (is_complete, missing_fields)
    """
    required_fields = ["smiles", "target"]
    missing = [field for field in required_fields if field not in data]
    return len(missing) == 0, missing
