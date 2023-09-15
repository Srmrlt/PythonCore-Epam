from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    result = (selector(data))
    for f in filters:
        result = f(result)
    return result


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def select_columns(dictionaries: DataType) -> DataType:
        return [{column: dictionary[column] for column in columns} for dictionary in dictionaries]

    return select_columns


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    def field_filter_finder(dictionaries: DataType) -> DataType:
        return [dictionary for dictionary in dictionaries for value in values if value == dictionary[column]]

    return field_filter_finder


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()
