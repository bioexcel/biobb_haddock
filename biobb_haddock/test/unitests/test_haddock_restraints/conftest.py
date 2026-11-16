# type: ignore
import shutil
import stat

import pytest

# Mimics a Python warning printed on stderr when the tool starts, e.g. a BiopythonWarning
FAKE_WARNING = "/fake/site-packages/Bio/__init__.py:138: BiopythonWarning: fake warning printed on stderr"


@pytest.fixture
def fake_warning():
    return FAKE_WARNING


@pytest.fixture
def noisy_properties(tmp_path):
    """Return a function giving the properties to run a block with its binary wrapped in a script that
    prints FAKE_WARNING on stderr first, and with an absolute err_log_path so the test can read the error log."""
    def make(binary):
        real_binary = shutil.which(binary)
        assert real_binary, f"{binary} not found in PATH"
        script = tmp_path / f"noisy_{binary}"
        script.write_text(f'#!/bin/sh\nprintf "%s\\n  warnings.warn(\\n" "{FAKE_WARNING}" >&2\nexec "{real_binary}" "$@"\n')
        script.chmod(script.stat().st_mode | stat.S_IXUSR)
        return {'binary_path': str(script), 'err_log_path': str(tmp_path / "log.err")}
    return make
