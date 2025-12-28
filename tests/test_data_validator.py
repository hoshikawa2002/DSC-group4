"""Tests for data validation utilities."""

import pytest
from utils.data_validator import (
    validate_smiles,
    validate_numeric_value,
    check_dataset_completeness,
)


class TestValidateSmiles:
    """Tests for SMILES validation."""

    def test_valid_smiles(self):
        """Test valid SMILES strings."""
        assert validate_smiles("CCO")  # Ethanol
        assert validate_smiles("c1ccccc1")  # Benzene
        assert validate_smiles("CC(=O)O")  # Acetic acid

    def test_invalid_smiles(self):
        """Test invalid SMILES strings."""
        assert not validate_smiles("")
        assert not validate_smiles(None)
        assert not validate_smiles(123)

    def test_smiles_with_special_chars(self):
        """Test SMILES with brackets and charges."""
        assert validate_smiles("[Na+]")
        assert validate_smiles("C[C@H](O)C")


class TestValidateNumericValue:
    """Tests for numeric value validation."""

    def test_valid_values(self):
        """Test valid numeric values."""
        assert validate_numeric_value(5.0)
        assert validate_numeric_value(0)
        assert validate_numeric_value(-10.5)

    def test_range_validation(self):
        """Test range validation."""
        assert validate_numeric_value(5.0, min_val=0, max_val=10)
        assert not validate_numeric_value(-1, min_val=0, max_val=10)
        assert not validate_numeric_value(11, min_val=0, max_val=10)

    def test_invalid_values(self):
        """Test invalid values."""
        assert not validate_numeric_value("not a number")
        assert not validate_numeric_value(None)


class TestCheckDatasetCompleteness:
    """Tests for dataset completeness checking."""

    def test_complete_dataset(self):
        """Test complete dataset."""
        data = {"smiles": "CCO", "target": 5.0}
        is_complete, missing = check_dataset_completeness(data)
        assert is_complete
        assert len(missing) == 0

    def test_incomplete_dataset(self):
        """Test incomplete dataset."""
        data = {"smiles": "CCO"}
        is_complete, missing = check_dataset_completeness(data)
        assert not is_complete
        assert "target" in missing

    def test_empty_dataset(self):
        """Test empty dataset."""
        data = {}
        is_complete, missing = check_dataset_completeness(data)
        assert not is_complete
        assert len(missing) == 2
