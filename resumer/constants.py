from resumer.utils import get_file_vars


class Constants: ...


def get_constants_from_file(file: str) -> Constants:
    variables = get_file_vars(file)

    c = Constants()
    c.__dict__ |= variables

    return c
