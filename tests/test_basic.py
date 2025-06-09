import pytest
import os
from dotenv import load_dotenv

def test_environment_variables():
    """Test if required environment variables are set"""
    load_dotenv()
    # Check if we're in CI environment
    if os.getenv('CI'):
        # In CI, we should have the secret set
        assert os.getenv('GOOGLE_API_KEY') is not None, "GOOGLE_API_KEY not found in CI environment"
    else:
        # In local environment, check .env file
        assert os.path.exists('.env'), ".env file not found"
        assert os.getenv('GOOGLE_API_KEY') is not None, "GOOGLE_API_KEY not found in .env file"

def test_requirements_file():
    """Test if requirements.txt exists"""
    assert os.path.exists('requirements.txt'), "requirements.txt file not found"

def test_src_directory():
    """Test if src directory exists"""
    assert os.path.exists('src'), "src directory not found" 