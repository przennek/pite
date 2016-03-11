To calculate integral:
1. Create a textfile with suffix '.dat'.

2. Enter your polynomial as follows:
    > ax^0 + bx^1 + ... + nx^m
(notice)
you only enter a, b, ..., n factors
the power is raising incrementaly
    > So if you want to enter 1 + x + 2x^2 it would look like:
    > 1 1 2

3. In the beginning of line enter your integral calculation range ex. 2 to 4
    > Our example from above would look like:
    > 2 4 1 1 2


General information:
Demo.py runs the script so user can calculate integrals.
PerformanceTest.py runs the test against scipy.integrate module.