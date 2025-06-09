import pytest
import os
from dotenv import load_dotenv

def test_environment_variables():
    """Test if required environment variables are set"""
    load_dotenv()
    assert os.getenv('GOOGLE_API_KEY') is not None, "GOOGLE_API_KEY not found in environment variables"

def test_requirements_file():
    """Test if requirements.txt exists"""
    assert os.path.exists('requirements.txt'), "requirements.txt file not found"

def test_src_directory():
    """Test if src directory exists"""
    assert os.path.exists('src'), "src directory not found" 