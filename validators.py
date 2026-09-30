def is_valid_email(email):
    if not isinstance(email, str):
        return False

    if " " in email:
        return False

    if "@" not in email:
        return False

    parts = email.split("@")

    if len(parts) != 2:
        return False

    username, domain = parts

    if not username or not domain:
        return False

    if "." not in domain:
        return False

    return True