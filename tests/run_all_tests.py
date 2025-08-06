"""
Test Runner - Digital Wellness Dashboard
Run all tests and show results
"""

import sys
import os
import time
from datetime import datetime

# Add current directory to path  
sys.path.append(os.path.dirname(__file__))

def run_all_tests():
    """Run all tests and show results"""
    
    start_time = time.time()
    
    # Import test modules
    try:
        from test_unit import run_all_unit_tests
        from test_integration import run_all_integration_tests  
        from test_security import run_all_security_tests
        from test_user import run_all_user_tests
    except ImportError as e:
        print(f"ERROR: Cannot import tests: {e}")
        return False
    
    # Test information
    tests = [
        {"name": "Unit Tests", "function": run_all_unit_tests, "count": 3},
        {"name": "Integration Tests", "function": run_all_integration_tests, "count": 3},
        {"name": "Security Tests", "function": run_all_security_tests, "count": 3},
        {"name": "User Tests", "function": run_all_user_tests, "count": 3}
    ]
    
    results = []
    passed = 0
    
    # Run each test (silently)
    for test in tests:
        try:
            # Suppress output by redirecting stdout temporarily
            import io
            import contextlib
            
            f = io.StringIO()
            with contextlib.redirect_stdout(f):
                result = test["function"]()
            
            if result:
                passed += 1
                results.append({"name": test["name"], "status": "PASSED", "count": test["count"]})
            else:
                results.append({"name": test["name"], "status": "FAILED", "count": 0})
        except:
            results.append({"name": test["name"], "status": "ERROR", "count": 0})
    
    end_time = time.time()
    total_time = end_time - start_time
    
    
    # SUMMARY REPORT
    print("=" * 50)
    print("TEST SUMMARY REPORT")
    print("=" * 50)
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Time taken: {total_time:.1f} seconds")
    print()
    
    # RESULTS TABLE
    print("TEST RESULTS:")
    print("+" + "-" * 48 + "+")
    print("| Test Category      | Status  | Tests Passed |")
    print("+" + "-" * 48 + "+")
    
    total_tests = 0
    passed_tests = 0
    
    for result in results:
        category = result["name"].ljust(18)
        status = result["status"].ljust(7)
        if result["status"] == "PASSED":
            test_info = f"{result['count']}/{result['count']}"
            passed_tests += result["count"]
        else:
            test_info = f"0/{result['count']}"
        test_info = test_info.ljust(12)
        total_tests += result["count"]
        
        print(f"| {category} | {status} | {test_info} |")
    
    print("+" + "-" * 48 + "+")
    print()
    
    # SUMMARY STATISTICS
    print("SUMMARY:")
    print("+" + "-" * 30 + "+")
    print("| Metric           | Value   |")
    print("+" + "-" * 30 + "+")
    print(f"| Categories Passed| {passed}/{len(tests)}     |")
    print(f"| Total Tests      | {passed_tests}/{total_tests}     |")
    print(f"| Success Rate     | {(passed/len(tests)*100):.0f}%     |")
    print(f"| Time Taken       | {total_time:.1f}s    |")
    print("+" + "-" * 30 + "+")
    print()
    
    # FINAL STATUS
    if passed == len(tests):
        print("🎉 ALL TESTS PASSED!")
        
    else:
        print(f"⚠️  {passed}/{len(tests)} TEST CATEGORIES PASSED")
        print("   Some tests need attention")
    
    return passed == len(tests)

if __name__ == '__main__':
    run_all_tests()
