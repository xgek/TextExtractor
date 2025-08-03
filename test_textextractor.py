# test_textextractor.py
"""
Tests for TextExtractor module.
"""

import unittest
from textextractor import TextExtractor

class TestTextExtractor(unittest.TestCase):
    """Test cases for TextExtractor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TextExtractor()
        self.assertIsInstance(instance, TextExtractor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TextExtractor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
