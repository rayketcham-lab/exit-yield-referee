"""Smoke test: the package must import cleanly on a bare install."""
import importlib.metadata

import exit_yield_referee


def test_package_imports():
    assert exit_yield_referee is not None  # presence of the module is the contract


def test_package_has_version():
    assert importlib.metadata.version("exit-yield-referee")
