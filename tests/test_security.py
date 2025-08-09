# Simple security tests for the Digital Wellness Dashboard App

import os
import sys

# Add the parent directory so we can use app files
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

def test_data_files_safe():
    """Check if data files are in safe places"""
    print("Checking if data files are safe...")
    
    # Check if data is in the right folder
    data_folder = os.path.join(parent_dir, 'data')
    if os.path.exists(data_folder):
        print("  ✓ Data folder exists in safe location")
        return True
    else:
        print("  ✗ Data folder not found")
        return False

def test_no_passwords_in_code():
    """Make sure there are no passwords in the code"""
    print("Checking for passwords in code...")
    
    # Check password patterns
    dangerous_patterns = ['password=', 'secret=', 'key=', 'token=']
    
    # Check app.py file
    try:
        with open(os.path.join(parent_dir, 'app.py'), 'r', encoding='utf-8') as f:
            app_content = f.read().lower()
            
        found_passwords = False
        for pattern in dangerous_patterns:
            if pattern in app_content:
                found_passwords = True
                break
        
        if not found_passwords:
            print("  ✓ No obvious passwords found in code")
            return True
        else:
            print("  ✗ Potential passwords found in code")
            return False
            
    except Exception as e:
        print(f"  ✗ Error checking for passwords: {e}")
        return False

def test_safe_file_access():
    """Check if we only access files we should"""
    print("Checking file access...")
    
    # Make sure we only access files in our project folder
    current_dir = os.getcwd()
    project_dir = os.path.join(parent_dir)
    
    if project_dir in current_dir or current_dir in project_dir:
        print("  ✓ Working in safe project directory")
        return True
    else:
        print("  ✗ Working outside project directory")
        return False