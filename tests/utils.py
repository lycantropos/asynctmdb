import string
from typing import (Any,
                    Iterable,
                    Dict, List)

from hypothesis import (Verbosity,
                        find,
                        settings)
from hypothesis.searchstrategy import SearchStrategy


def example(strategy: SearchStrategy) -> Any:
    return find(specifier=strategy,
                condition=lambda x: True,
                settings=settings(max_shrinks=0,
                                  max_iterations=10000,
                                  database=None,
                                  verbosity=Verbosity.quiet))


def is_positive_integer(value: Any) -> bool:
    return isinstance(value, int) and value > 0


def is_non_negative_integer(value: Any) -> bool:
    return isinstance(value, int) and value >= 0


def is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and value


def is_non_empty_hex_string(value: Any) -> bool:
    return (is_non_empty_string(value) and
            all(character in string.hexdigits
                for character in value))


def is_valid_paginated_record(
        record: Dict[str, Any],
        paginated_record_keys: Iterable[str] = ('page',
                                                'total_pages',
                                                'total_results')) -> bool:
    if not isinstance(record, dict):
        return False
    if any(key not in record for key in paginated_record_keys):
        return False
    return (is_positive_integer(record['page']) and
            is_non_negative_integer(record['total_pages']) and
            is_non_negative_integer(record['total_results']))


def are_valid_results(results: List[Dict[str, Any]]) -> bool:
    return (isinstance(results, list) and
            all(isinstance(result, dict)
                for result in results))
