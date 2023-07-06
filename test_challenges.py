import pytest
import os
import csv
import math

import challenges


def clean_up_file_if_exists(filepath: str):
    try:
        os.remove(filepath)
    except OSError:
        pass


@pytest.fixture(autouse=True)
def run_around_tests():
    clean_up_file_if_exists("test1.txt")
    clean_up_file_if_exists("test2.txt")
    clean_up_file_if_exists("test3.txt")
    yield
    clean_up_file_if_exists("test1.txt")
    clean_up_file_if_exists("test2.txt")
    clean_up_file_if_exists("test3.txt")


@pytest.mark.parametrize(
    "filepath, file_content, word, expected_count",
    [
        ("test1.txt", "Hi", "hello", 0),
        ("test2.txt", "The wheels on the bus go round and round", "round", 2),
        (
            "test3.txt",
            "The Antikythera mechanism is believed to be the earliest known mechanical analog computer",
            "the",
            2,
        ),
    ],
)
def test_count_instances_of_word_in_file(
    filepath: str, file_content: str, word: str, expected_count: int
) -> None:
    with open(filepath, "w") as file:
        file.write(file_content)
    count = challenges.count_instances_of_word_in_file(filepath, word)
    assert (
        count == expected_count
    ), f'Expected there to be {expected_count} instances of the word "{word}" in the text "{file_content}"'


@pytest.mark.parametrize(
    "filepath, text",
    [
        ("test1.txt", "The wheels on the bus go round and round"),
        (
            "test2.txt",
            "The Antikythera mechanism is believed to be the earliest known mechanical analog computer",
        ),
    ],
)
def test_write_text_to_file(filepath: str, text: str) -> None:
    challenges.write_text_to_file(filepath, text)
    with open(filepath) as file:
        assert (
            file.read() == text
        ), f'Expected the file {filepath} to contain the exact text "{text}"'


@pytest.mark.parametrize(
    "filepath, text, expected_text_after_adding_t",
    [
        ("test1.txt", "None", "None"),
        ("test2.txt", "Apple", "Atpple"),
        ("test3.txt", "Congraulations", "Congratulations"),
    ],
)
def test_write_t_after_first_a(
    filepath: str, text: str, expected_text_after_adding_t: str
) -> None:
    with open(filepath, "w") as file:
        file.write(text)
    challenges.write_t_after_first_a(filepath)
    with open(filepath) as file:
        assert (
            file.read() == expected_text_after_adding_t
        ), f'Expected the file {filepath} to contain the exact text "{expected_text_after_adding_t}"'


@pytest.mark.parametrize(
    "filepath, data, expected_file_content",
    [
        (
            "test1.txt",
            [
                {"name": "Alice", "city": "London"},
                {"name": "Bob", "city": "Houston"},
                {"name": "Charlie", "city": "Kuala Lumpur"},
            ],
            "name,city\nAlice,London\nBob,Houston\nCharlie,Kuala Lumpur\n",
        ),
        (
            "test2.txt",
            [
                {"complete": 1, "in progress": 0, "not started": 5},
                {"complete": 4, "in progress": 1, "not started": 1},
            ],
            "complete,in progress,not started\n1,0,5\n4,1,1\n",
        ),
    ],
)
def test_record_data(
    filepath: str, data: list[dict], expected_file_content: str
) -> None:
    challenges.record_data(filepath, data)
    with open(filepath) as file:
        assert (
            file.read() == expected_file_content
        ), f'Expected the file {filepath} to contain the exact content "{expected_file_content}"'


@pytest.mark.parametrize(
    "filepath, data, expected_fastest_runner",
    [
        ("test1.txt", [{"name": "Alice", "finish_time": 11.56}], "Alice"),
        (
            "test2.txt",
            [
                {"name": "Alice", "finish_time": 11.56},
                {"name": "Bob", "finish_time": 10.99},
                {"name": "Charlie", "finish_time": 17.02},
            ],
            "Bob",
        ),
        (
            "test3.txt",
            [
                {"name": "David", "finish_time": 14.2},
                {"name": "Eve", "finish_time": 13.7},
                {"name": "Frank", "finish_time": 14.4},
            ],
            "Eve",
        ),
    ],
)
def test_find_fastest_runner_using_csv(
    filepath: str, data: list[dict], expected_fastest_runner: str
) -> None:
    with open(filepath, "w") as file:
        spreadsheet = csv.DictWriter(file, fieldnames=["name", "finish_time"])
        spreadsheet.writeheader()
        spreadsheet.writerows(data)
    fastest_runner = challenges.find_fastest_runner_using_csv(filepath)
    assert (
        fastest_runner == expected_fastest_runner
    ), f"Expected the fastest runner to be {expected_fastest_runner}"


@pytest.mark.parametrize(
    "filepath, data, expected_fastest_runner",
    [
        ("test1.txt", [{"name": "Alice", "finish_time": 11.56}], "Alice"),
        (
            "test2.txt",
            [
                {"name": "Alice", "finish_time": 11.56},
                {"name": "Bob", "finish_time": 10.99},
                {"name": "Charlie", "finish_time": 17.02},
            ],
            "Bob",
        ),
        (
            "test3.txt",
            [
                {"name": "David", "finish_time": 14.2},
                {"name": "Eve", "finish_time": 13.7},
                {"name": "Frank", "finish_time": 14.4},
            ],
            "Eve",
        ),
    ],
)
def test_find_fastest_runner_using_pandas(
    filepath: str, data: list[dict], expected_fastest_runner: str
) -> None:
    with open(filepath, "w") as file:
        spreadsheet = csv.DictWriter(file, fieldnames=["name", "finish_time"])
        spreadsheet.writeheader()
        spreadsheet.writerows(data)
    fastest_runner = challenges.find_fastest_runner_using_pandas(filepath)
    assert (
        fastest_runner == expected_fastest_runner
    ), f"Expected the fastest runner to be {expected_fastest_runner}"


@pytest.mark.parametrize(
    "filepath, data, expected_mean_finish_time",
    [
        ("test1.txt", [{"name": "Alice", "finish_time": 11.56}], 11.56),
        (
            "test2.txt",
            [
                {"name": "Alice", "finish_time": 11.56},
                {"name": "Bob", "finish_time": 10.99},
                {"name": "Charlie", "finish_time": 17.02},
            ],
            13.19,
        ),
    ],
)
def test_find_mean_finish_time_using_csv(
    filepath: str, data: list[dict], expected_mean_finish_time: float
) -> None:
    with open(filepath, "w") as file:
        spreadsheet = csv.DictWriter(file, fieldnames=["name", "finish_time"])
        spreadsheet.writeheader()
        spreadsheet.writerows(data)
    mean_finish_time = challenges.find_mean_finish_time_using_csv(filepath)
    assert math.isclose(
        mean_finish_time, expected_mean_finish_time
    ), f"Expected the mean finish time to be {expected_mean_finish_time}"


@pytest.mark.parametrize(
    "filepath, data, expected_mean_finish_time",
    [
        ("test1.txt", [{"name": "Alice", "finish_time": 11.56}], 11.56),
        (
            "test2.txt",
            [
                {"name": "Alice", "finish_time": 11.56},
                {"name": "Bob", "finish_time": 10.99},
                {"name": "Charlie", "finish_time": 17.02},
            ],
            13.19,
        ),
    ],
)
def test_find_mean_finish_time_using_pandas(
    filepath: str, data: list[dict], expected_mean_finish_time: float
) -> None:
    with open(filepath, "w") as file:
        spreadsheet = csv.DictWriter(file, fieldnames=["name", "finish_time"])
        spreadsheet.writeheader()
        spreadsheet.writerows(data)
    mean_finish_time = challenges.find_mean_finish_time_using_pandas(filepath)
    assert math.isclose(
        mean_finish_time, expected_mean_finish_time
    ), f"Expected the mean finish time to be {expected_mean_finish_time}"
