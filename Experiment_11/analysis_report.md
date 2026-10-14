Root Cause
The accumulation statement subtracts each price instead of adding it. Starting from zero, the loop calculates 0 - 100 - 200 - 300, which produces -600.

Faulty Statement
In app.py:6:


Minimum Correction
Change subtraction to addition:


Verification
Run the test from the Experiment_11 folder:


The test should pass with calculate_total([100, 200, 300]) returning 600.

Evidence and Assumptions
Evidence: The build log reports expected 600 and actual -600. The test supplies [100, 200, 300] and expects 600 in test_app.py:4-8. The implementation uses total -= price in its loop.

Assumption: The intended behavior is to sum the prices. That is supported by the test’s expected result, but should be confirmed if the function is meant to do anything other than calculate a total.