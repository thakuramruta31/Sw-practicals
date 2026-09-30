import pytest

from validators import is_valid_email


@pytest.mark.parametrize(
    "email",
    [
        "user@example.com",
        "first.last+tag@sub.example.org",
    ],
)
def test_is_valid_email_accepts_normal_addresses(email):
    assert is_valid_email(email) is True


@pytest.mark.parametrize(
    "email",
    [
        "a@b.c",
        "x@domain.",
        "x@.domain",
        "user@domain..com",
    ],
)
def test_is_valid_email_accepts_boundary_and_permissive_edges(email):
    assert is_valid_email(email) is True


@pytest.mark.parametrize(
    "email",
    [None, 123, 1.5, True, [], {}, ()],
)
def test_is_valid_email_rejects_non_string_inputs(email):
    assert is_valid_email(email) is False


@pytest.mark.parametrize(
    "email",
    [
        "",
        "username",
        "example.com",
        "@example.com",
        "@",
        "user@",
        "user@example",
        "user@@example.com",
        "user@example.com@other.org",
    ],
)
def test_is_valid_email_rejects_invalid_strings(email):
    assert is_valid_email(email) is False


# Additional manual test
def test_email_with_spaces():
    assert is_valid_email("user name@example.com") is False