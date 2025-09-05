[![Python application](https://github.com/nahallacman/LeetCode/actions/workflows/python-app.yml/badge.svg)](https://github.com/nahallacman/LeetCode/actions/workflows/python-app.yml)

# What Is This?
A repo for me to brush off my python skills and attempt some Leet Code problems as practice.

# What Have I Done?
## Framework
I made it so all of the tests could be run in bulk at the same time by selecting a different debug option in Visual Studio Code. There are two options:
* Run the selected file
* Run all tests

Just pick one in the Visual Studio Code debugger and hit f5 to start debugging. Note that you will need the python plugin to run this.

## CI/CD
To ensure that I don't break anything and that my current problem I am working on passes, I wrote a little CI/CD using GitHub Actions to run all of the tests and display the final test results at the end.

## Problems
Each problem is in it's own folder with a Problem_### format where ### matches the Leet Code problem.

For example, problem_001 corresponds to https://leetcode.com/problems/two-sum/description/?language=Python

Each problem needs two files, the `problem.py` file, and the `test_inputs.json` file. To add a new problem, copy the `problem_template` folder, rename `template` to the problem number, and edit the `test_inputs.json` to match the test cases and test function you wish to call.

Note: there are some problems in this repo that are not actually LeetCode problems, but I will try to keep their numbers outside of the range of LeetCode problems.