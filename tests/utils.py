from typing import Any

from hypothesis import (Verbosity,
                        find,
                        settings)
from hypothesis.searchstrategy import SearchStrategy


def example(strategy: SearchStrategy) -> Any:
    return find(specifier=strategy,
                condition=lambda x: True,
                settings=settings(max_shrinks=0,
                                  max_iterations=10_000,
                                  database=None,
                                  verbosity=Verbosity.quiet))


def is_positive_integer(value: Any) -> bool:
    return isinstance(value, int) and value > 0


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and value
