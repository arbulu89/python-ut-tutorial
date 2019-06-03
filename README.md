[![Build Status](https://travis-ci.org/arbulu89/python-ut-tutorial.svg?branch=master)](https://travis-ci.org/arbulu89/python-ut-tutorial)
[![Maintainability](https://api.codeclimate.com/v1/badges/ec92d2849689b3cf8954/maintainability)](https://codeclimate.com/github/arbulu89/python-ut-tutorial/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ec92d2849689b3cf8954/test_coverage)](https://codeclimate.com/github/arbulu89/python-ut-tutorial/test_coverage)

# Python Unit Test tutorial

This project shows some tips and good practices about how to create correct Unit Test in Python.

Unit testing is an essential part of creating a good code so this part must not be avoided in any project.
Usually the unit tests are done by the same author of the code under test, as he has the best idea
about what the code should do.

A project with 100% unit tested code shows that the authors really care about the code quality and
they invest time on that. However, **unit tested code doesn't mean that the code is out bugs or bad
design/architecture.**

Here some benefits of unit testing the code of our projects:

- Avoid any basic syntax error as the code at least is executed.
- The author gives a second look to the code in a deeper way. This can help to fix some undesired
behaviours.
- Test the code without other dependencies as the 3rd party packages are mocked.
- Enable regression tests. This is extremely helpful to avoid breaking the code in future changes.
- In helps to test the code in different language versions (py2 and py3 for example).
- Enable automation to improve the project Pull Request reviews and approvals.
- Unit testing forces the author of the project to split the code in smaller methods/functions
structuring better the code (**a method that cannot be unit tested is not a good piece of code**).
- If extra collaborators are adding new code to the project, unit testing helps to have a more
mature contributions.

## This project

This project will use the next tools:
- **[pytest](https://docs.pytest.org/en/latest/)**: Really popular python test runner.
- **[coverage.py](https://coverage.readthedocs.io/en/v4.5.x/)**: Tool for measuring code coverage in Python programs.
- **[tox](https://tox.readthedocs.io/en/latest/)**: Tool to automate and standardize testing in Python.
Besides, tox creates new virtual environments every execution, so the test are executed in clean environments.
- **[travis](https://travis-ci.org/)**: Tool used to configure continuous integration of the tests.

## How to run

To run the tests basically run:

```
sudo pip install tox
cd python-ut-tutorial
sudo tox
```

## Recommendations

Here some personal recommendations to structure the code and the unit tests:

- The unit tests should be stored in a folder named tests in the root path of the project folder:
[tests](./tests).
- The test files must be named like *_test.py.
- The project should have one test file for each main code file.
- Always try to follow the linting rules even in the test code as it helps for future changes and
readability.
- Create a new test for each method code path. For example, if a method raises an exception in a not desired
behaviour, we should have one test for the correct path and other to the piece of code that is executed
when the exception is raised. **(This is a personal preference, other developers prefer to have one
test for each method)**.
- Give meaningful names to the test *mocked* variables. As a test might have several mocked methods,
having meaningful names will help to make the test easy to understand.
- The test method must be named like test_*method_under_test*.
- Add additional information to the test names. If several tests are created for each method, add a
meaningful information to the test name (avoid using indexes in the name like *test_my_method1* please!).
- If the test has a lot of lines, adding a comment line above the method under test to identify it might
be helpful.
- The test should only test the method under test. If this method depends in other methods, **those
must be mocked**. Try to avoid dependencies between methods.
- Patch the methods to mock them as much as you can. This is the best way to avoid issues in the next
test as patching process of the method/module will be reverted after the test execution.
- If the code under test is a class, create a new instance in the setup to have a fresh object to
work with.
- Try to always test the logging outputs. It helps to review the logging messages and reach more
code paths.

## Linting the code

Linting the code is other essential part of creating a good project. Here a brief description of *linting*
([source](https://en.wikipedia.org/wiki/Lint_%28software%29)):

```
Lint, or a linter, is a tool that analyzes source code to flag programming errors, bugs, stylistic
errors, and suspicious constructs
```

We should always have a linter package installed in our code editor. This will help us to fix
some potential errors and have cleaner code.

The most popular code style guide for Python is the **[PEP8 style guide](https://www.python.org/dev/peps/pep-0008/)**.
It is always recommended to have a look and learn some basics and good practices.

## License

See the [LICENSE](LICENSE) file for license rights and limitations.

## Author

Xabier Arbulu Insausti (arbulu89@gmail.com or xarbulu@suse.com)

## Reviewers

*Pull request* preferred reviewers for this project:
- Xabier Arbulu Insausti (arbulu89@gmail.com or xarbulu@suse.com)
