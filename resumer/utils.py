import os

def get_file_vars(file:str) -> dict[str, str]:
    """
    a simple parser for variables
    defined within the given `file` parameter.
    A simple implementation of a dotfile parser
    without setting the variables as env variables.

    :param file str: The file containing such variables
    """
    assert os.path.exists(file), "File does not exist"

    with open(file, "r") as file:
        lines = file.readlines()

    variables: dict[str, str] = {}

    for line in lines:
        line = line.strip()

        if len(line) == 0:
            continue

        if line[0] == "#":
            # allowing for comments within such file
            continue

        key, val = line.split("=", maxsplit=1)
        key = key.strip()
        val = val.strip()

        # supporting environment variables
        val = os.path.expandvars(val)

        variables[key] = val

    return variables
