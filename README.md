# Lesson 9 Independent Challenges

## Challenge 1: `count_instances_of_word_in_file` (15 points)

| Function parameter(s)                                                     | Function return(s)                                            |
|---------------------------------------------------------------------------|---------------------------------------------------------------|
| `filepath`, a path to a file to analyse, and `word`, a word to search for | The number of occurrences of the given word in the given file |

Given a path to a file, read the contents of the file and count the number of occurrences of a given word. The count should be done on a case-insensitive basis. Only standalone instances of the word should be counted. For example, if the word being searched for is "nan", the sequence of characters "nan" in the word "banana" won't count as an instance of the word for our purposes.

## Challenge 2: `write_text_to_file` (10 points)

| Function parameter(s)                                                    | Function return(s) |
|--------------------------------------------------------------------------|--------------------|
| `filepath`, a path to a file to write to, and `text`, some text to write | None               |

Given a path to a file, write some given text to the file. The file should be overwritten if it already exists.

## Challenge 3: `write_t_after_first_a` (15 points)

| Function parameter(s)                    | Function return(s) |
|------------------------------------------|--------------------|
| `filepath`, a path to a file to write to | None               |

Given a path to a file, modify the contents so that a letter `t` is added after the first instance of the letter `a` (case-insensitive for the `a`, although the added `t` should always be lowercase). If there is no `a`, the file should be left unchanged.

## Challenge 4: `record_data` (10 points)

| Function parameter(s)                                                    | Function return(s) |
|--------------------------------------------------------------------------|--------------------|
| `filepath`, a path to a file to write to, and `data`, some data to write | None               |

Given a path to a file, write some data (given in the form of a list of dictionaries) to the file in CSV format. The file should be overwritten if it already exists. You may assume that each dictionary in the data has the same keys as all the other dictionaries, and that there is at least one dictionary in the data.

## Challenge 5: `find_fastest_runner_using_csv` (15 points)

| Function parameter(s)                   | Function return(s)                         |
|-----------------------------------------|--------------------------------------------|
| `filepath`, a path to a file to analyse | The name of the fastest runner in the file |

Given a path to a CSV file, find and return the name of the fastest runner in the file using the standard library `csv` module. You may assume that there are no ties for fastest runner. The headings in the CSV file will be "name" and "finish_time".

## Challenge 6: `find_fastest_runner_using_pandas` (15 points)

| Function parameter(s)                   | Function return(s)                         |
|-----------------------------------------|--------------------------------------------|
| `filepath`, a path to a file to analyse | The name of the fastest runner in the file |

Given a path to a CSV file, find and return the name of the fastest runner in the file using the third-party `pandas` package. You may assume that there are no ties for fastest runner. The headings in the CSV file will be "name" and "finish_time".

## Challenge 7: `find_mean_finish_time_using_csv` (10 points)

| Function parameter(s)                   | Function return(s)                                  |
|-----------------------------------------|-----------------------------------------------------|
| `filepath`, a path to a file to analyse | The mean finish time of all the runners in the file |

Given a path to a CSV file, find and return mean finish time of all the runners in the file using the standard library `csv` module. You may assume that there is at least one runner. The headings in the CSV file will be "name" and "finish_time".

## Challenge 8: `find_mean_finish_time_using_pandas` (10 points)

| Function parameter(s)                   | Function return(s)                                  |
|-----------------------------------------|-----------------------------------------------------|
| `filepath`, a path to a file to analyse | The mean finish time of all the runners in the file |

Given a path to a CSV file, find and return mean finish time of all the runners in the file using the third-party `pandas` package. You may assume that there is at least one runner. The headings in the CSV file will be "name" and "finish_time".
