"""Smoke test: the package must import cleanly on a bare install."""
import exit_yield_referee


def test_package_imports():
    assert exit_yield_referee.__doc__ or True  # presence of the module is the contract


def test_package_has_version():
    import importlib.metadata

    assert importlib.metadata.version("exit-yield-referee")
