# Daily Python snippets

This is a series I published regularly on Twitter with short Python snippets to learn about various Python functions. 

Snippets were published as images, but here they are stored in .py files. **In each file I added original Tweet as docstring with short explanation.** The repository will be updated as I continue with the series. 

Enjoy!

## Standard library

1. [How to use `argparse` to pass args to your script](standard_library/01_argparsing.py)
2. [Using `logging` instead of print - logging level](standard_library/02_logging_level.py)
3. [Creating paths with `pathlib`](standard_library/03_pathlib_path_creation.py)
4. [Saving logs to .log file using `logging`](standard_library/04_logging_filesave.py)
5. [List files in subdirectories recursively using `pathlib`](standard_library/08_list_recursively_format.py)
6. [Define what types you use in function definition using `typing`](standard_library/09_using_typing.py)
7. [Create one hot encoded vector in plain Python](standard_library/12_one_hot_encoding.py)
8. [Make directory using `pathlib`](standard_library/16_pathlib_mkdir.py)
9. [Use product to generate unique pairs/trios/etc. from multiple sets](standard_library/17_itertools_product.py)
10. [Using any vs. all](standard_library/22_any_all.py)
11. [Type vs. isinstance for checking the type in Python](standard_library/23_type_vs_isinstance.py)
12. [How to use subparsers from `argparse`](standard_library/25_subparsers.py)
13. [Check if file name matches a pattern using `re`](standard_library/26_re.py)
14. [What bare asterisk * means in Python](standard_library/27_bare_asterisk.py)
15. [How to write custom decorator](standard_library/28_custom_decorator.py)
16. [How to add 2 args to your script but allow only one at a time with `argparse`](standard_library/31_mutually_exclusive_groups.py)
17. [Simple dict vs. OrderedDict](standard_library/36_ordered_dict.py)
18. [How to use chain to concatenate lists faster](standard_library/37_chain_vs_list_sum.py)

## Soundfile

1. [Reading .wav audio file to numpy array](soundfile/05_reading_audio.py)

## PyTorch

1. [Creating Dataset from Pandas DataFrame](pytorch/06_pandas_torch_dataset.py)
2. [Create one hot encoded vector](pytorch/12_one_hot_encoding.py)
3. [Find bottlenecks in your code using profiler](pytorch/21_torch_profiler.py)
4. [How to write custom context manager - example for PyTorch](pytorch/29_custom_contextmanager.py)
5. [Define our own differentiable functions using autograd](pytorch/38_torch_autograd.py)

## NumPy

1. [NumPy pad modes explained](numpy/07_np_pad_modes.py)
2. [Matrix multiplication - 2 ways](numpy/10_matrix_multiplication.py)
3. [6 ways to create a dummy numpy array](numpy/11_dummy_arrays.py)
4. [Create one hot encoded vector](numpy/12_one_hot_encoding.py)
5. [Epsilon aka really small value in numpy](numpy/24_numpy_eps.py)
6. [Create read-only, un-writeable numpy array](numpy/30_unwriteable_np_array.py)
7. [Create and remove artificial dimensions - expand_dims and squeeze](numpy/33_numpy_squeeze_and_expand.py)
8. [Extract unique rows from array](numpy/39_array_unique_rows.py)
9. [Difference between nan and inf + explanation](numpy/40_infinity_vs_nan.py)

## Matplotlib

1. [Quickly improve the looks of the plot using styling](matplotlib/13_matplotlib_style.py)

## Pandas

1. [Difference between .loc and .iloc](pandas/14_pandas_loc_vs_iloc.py)
2. [Count unique values in column](pandas/15_pandas_value_counts.py)
3. [Example how to use groupby - create summary with respect to categorical variable](pandas/19_pandas_groupby.py)
4. [Convert DataFrame to Latex table](pandas/20_pandas_latex.py)
5. [Using apply and lambda to quickly transform the columns](pandas/35_pandas_apply_with_lambda.py)

## Tqdm

1. [Add progress bar to your for loops](tqdm/18_tqdm.py)
2. [Progress bar and range in one function - trange](tqdm/32_tqdm_trange.py)
3. [Add description to progress bar](tqdm/34_tqdm_description.py)
