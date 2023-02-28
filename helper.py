def convert_input_file(file_path: str) -> list[list[str]]:
    """Converts txt file into a grid-like structure

    Parameters
    ----------
    file_path : str
        File path to input file

    Returns
    -------
    list[list[str]]
        Grid-like list of list
    """
    with open(file_path, "r") as f:
        rows = f.read().splitlines()
        input_from_txt = [[*row] for row in rows]

        return input_from_txt
