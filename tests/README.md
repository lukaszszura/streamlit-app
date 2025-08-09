# Testing

Simple tests for the Digital Wellness App.

## Test Files

- `run_all_tests.py` - Run all tests
- `test_unit.py` - Basic functionality  
- `test_integration.py` - System integration
- `test_security.py` - Security checks
- `test_user.py` - User experience

## How to Run

```bash
python tests/run_all_tests.py
```

## What Tests Check

- Data files exist and load correctly
- App components work together
- Security and file access
- User experience functionality

## If Tests Fail

1. Check data files exist in `data/` folder
2. Run the main notebook first to generate files
3. Install dependencies: `pip install pandas numpy scikit-learn`
