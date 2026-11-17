"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'

# Example 1
def test_nested_if_account_access():
    """Check account access using nested conditions."""

    cases = [
        (True, True, 'Access granted'),
        (True, False, 'Verify your account'),
        (False, False, 'Create an account'),
    ]

    for has_account, is_verified, expected in cases:
        if has_account:
            if is_verified:
                message = 'Access granted'
            else:
                message = 'Verify your account'
        else:
            message = 'Create an account'

        assert message == expected

