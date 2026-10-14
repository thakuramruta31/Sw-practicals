# Running and Evaluating the Login UI Tests

## Prerequisites

- Python 3 installed and available in the VS Code terminal.
- Google Chrome installed.
- `login.html` and `test_login.py` in the same folder.

The tests use Selenium 4's Selenium Manager to locate or download a compatible ChromeDriver automatically, so a separate manual ChromeDriver setup is normally not needed.

## Install

Open the VS Code terminal in the `Experiment_10` folder and run:

```powershell
python -m pip install selenium pytest
```

## Execute

Run all tests from the same folder:

```powershell
python -m pytest -v
```

Pytest discovers `test_login.py` automatically. The tests open the local `login.html` file in Chrome and close the browser after each test, including when an assertion fails.

## Evaluate Test Accuracy

- Check that the tests use the IDs in `login.html`: `username`, `password`, `loginButton`, and `message`.
- Confirm the expected messages exactly match the webpage: `Login successful!` for `student` / `pass123`, and `Invalid username or password.` for invalid credentials.
- Run the tests and confirm all three pass against the current page.
- Check that the controls-visibility test verifies all three required controls.
- As a simple negative check of the tests themselves, temporarily change an expected message or an element ID in the test and confirm the relevant test fails; then restore it.

The provided cases cover the requested valid login, invalid login, and visible controls. They do not test empty-field validation, browser compatibility beyond Chrome, or security properties because those are outside the stated practical requirements.
