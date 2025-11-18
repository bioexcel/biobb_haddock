"""
Disclaimer
This code was obtained from the HADDOCK3 repository:
https://github.com/haddocking/haddock3/blob/main/src/haddock/gear/config.py
"""
import toml
import os
import re
from pathlib import Path

# the re.ASCII parameter makes sure non-ascii chars are rejected in the \w key

# Captures the main headers.
# https://regex101.com/r/9urqti/1
_main_header_re = re.compile(r"^ *\[(\w+)\]", re.ASCII)

# regex by @sverhoeven
# Matches ['<name>.<digit>']
_main_quoted_header_re = re.compile(r"^ *\[\'(\w+)\.\d+\'\]", re.ASCII)

# Captures sub-headers
# https://regex101.com/r/6OpJJ8/1
# thanks https://stackoverflow.com/questions/39158902
_sub_header_re = re.compile(r"^ *\[(\w+)((?:\.\w+)+)\]", re.ASCII)

# regex by @sverhoeven
_sub_quoted_header_re = re.compile(
    r"^ *\[\'(\w+)\.\d+\'((?:\.\w+)+)\]",
    re.ASCII,
)

# Captures parameter uppercase boolean
_uppercase_bool_re = re.compile(r"(_?\w+((_?\w+?)+)?\s*=\s*)(True|False)", re.ASCII)


def load(fpath: str) -> dict[str, dict[str, dict[str, str]]]:
    """
    Load an HADDOCK3 configuration file to a dictionary.

    Accepts HADDOCK3 ``cfg`` files or pure ``toml`` files.

    Parameters
    ----------
    fpath : str or :external:py:class:`pathlib.Path`
        Path to user configuration file.

    Returns
    -------
    dictionary
        Representing the user configuration file where first level of
        keys are the module names. Step keys will have a numeric
        suffix, for example: ``module.1``.

    .. see-also::
        * :py:func:`loads`
    """
    try:
        return loads(Path(fpath).read_text())
    except Exception as err:
        raise Exception(
            "Something is wrong with the config file."
        ) from err  # noqa: E501


def loads(cfg_str: str) -> dict[str, dict[str, dict[str, str]]]:
    """
    Read a string representing a config file to a dictionary.

    Config strings are converted to toml-compatible format and finally
    read by the toml library.

    All headers (dictionary keys) will be suffixed by an integer
    starting at ``1``. For example: ``topoaa.1``. If the key is
    repeated, ``2`` is appended, and so forth. Even if specific
    integers are provided by the user, the suffix integers will be
    normalized.

    Parameters
    ----------
    cfg_str : str
        The string representing the config file. Accepted formats are
        the HADDOCK3 config file or pure `toml` syntax.

    Returns
    -------
    all_configs : dict
        A dictionary holding all the configuration file steps:

        - 'raw_input': Original input file as provided by user.
        - 'cleaned_input': Regex cleaned input file.
        - 'loaded_cleaned_input': Dict of toml loaded cleaned input.
        - 'final_cfg': The config in the form of a dictionary. In which
          the order of the keys matters as it defines the order of the
          steps in the workflow.
    """
    new_lines: list[str] = []
    cfg_lines = cfg_str.split(os.linesep)
    counter: dict[str, int] = {}

    # this for-loop normalizes all headers regardless of their input format.
    for line in cfg_lines:
        if group := _main_header_re.match(line):
            name = group[1]
            counter.setdefault(name, 0)
            counter[name] += 1
            count = counter[name]
            new_line = f"['{name}.{count}']"

        elif group := _main_quoted_header_re.match(line):
            name = group[1]
            counter.setdefault(name, 0)
            counter[name] += 1
            count = counter[name]
            new_line = f"['{name}.{count}']"

        elif group := _sub_header_re.match(line):
            name = group[1]
            count = counter[name]  # name should be already defined here
            new_line = f"['{name}.{count}'{group[2]}]"

        elif group := _sub_quoted_header_re.match(line):
            name = group[1]
            count = counter[name]  # name should be already defined here
            new_line = f"['{name}.{count}'{group[2]}]"

        elif group := _uppercase_bool_re.match(line):
            param = group[1]  # Catches 'param = '
            uppercase_bool = group[4]
            new_line = f"{param}{uppercase_bool.lower()}"  # Lowercase bool

        else:
            new_line = line

        new_lines.append(new_line)

    # Re-build workflow configuration file
    cfg = os.linesep.join(new_lines)

    try:
        cfg_dict = toml.loads(cfg)  # Try to load it with the toml library
    except Exception as err:
        print(cfg)
        raise Exception(
            "Some thing is wrong with the config file: " f"{str(err)}"
        ) from err

    return cfg_dict


def save(cfg_dict: dict, path: str) -> None:
    """
    Write a dictionary to a HADDOCK3 config file.

    Write the HADDOCK3 parameter dictionary to a `.cfg` file. There is
    also the option to write in pure TOML format. Both are compatible with
    HADDOCK3.

    Parameters
    ----------
    cfg_dict : dict
        The dictionary containing the parameters.

    path : str or pathlib.Path
        File name where to save the configuration file.

    """

    with open(path, "w") as fout:
        toml.dump(cfg_dict, fout)
