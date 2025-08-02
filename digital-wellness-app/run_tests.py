"""
Test runner that works from any directory
"""
import os
import sys

# Add the parent directory to the path so we can import the test modules
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, current_dir)

# Change to parent directory so relative paths work
os.chdir(parent_dir)

# Now import and run the tests
try:
    from tests.test_unit import run_all_unit_tests
    from tests.test_integration import run_all_integration_tests  
    from tests.test_security import run_all_security_tests
    from tests.test_user import run_all_user_tests
    
    print("DIGITAL WELLNESS DASHBOARD - TESTING")
    print("="*50)
    
    results = []
    
    print("Running Unit Tests...")
    print("-"*30)
    unit_result = run_all_unit_tests()
    results.append(("Unit Tests", unit_result))
    
    print("\nRunning Integration Tests...")
    print("-"*30)
    integration_result = run_all_integration_tests()
    results.append(("Integration Tests", integration_result))
    
    print("\nRunning Security Tests...")
    print("-"*30)
    security_result = run_all_security_tests()
    results.append(("Security Tests", security_result))
    
    print("\nRunning User Tests...")
    print("-"*30)
    user_result = run_all_user_tests()
    results.append(("User Tests", user_result))
    
    # Print summary
    print("\n" + "="*50)
    print("TEST SUMMARY")
    print("="*50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "PASSED" if result else "FAILED"
        emoji = "✅" if result else "❌"
        print(f"{emoji} {status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\nSUMMARY: {passed}/{total} test categories passed")
    success_rate = (passed / total) * 100 if total > 0 else 0
    print(f"Success Rate: {success_rate:.0f}%")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        print("   Project is ready for submission")
    else:
        print(f"\n⚠️  {total-passed}/{total} TEST CATEGORIES FAILED")
        print("   Some tests need attention")
        
except Exception as e:
    print(f"Error running tests: {e}")
    import traceback
    traceback.print_exc()
