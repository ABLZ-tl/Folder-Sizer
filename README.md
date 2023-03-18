# Folder Size Calculator

This is a Python script that calculates the size of all folders in a given directory and generates an HTML report with the results. The folders are sorted by size in descending order, so you can easily identify the largest ones.

The script uses multiple processes to speed up the calculation process, and a progress bar is displayed to keep track of the progress. The results are saved in an HTML file that can be opened in any web browser. Additionally, an error log is generated in case of any exceptions.

## Usage

1. Clone or download this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the script by executing `python folder_size_calculator.py`.
4. Select the directory that you want to calculate the folder sizes for.
5. Wait for the script to finish calculating the sizes.
6. The results will be displayed in an HTML file called `tempfile.html` and will open in a new tab of your default web browser.

Note: Make sure that the `tempfile.html` and `error-log.txt` files are not open while running the script, as they will be overwritten.

## Dependencies

The script requires Python 3.x and the following packages:

- tkinter
- ttk
- multiprocessing
- webbrowser

These dependencies can be installed by running `pip install -r requirements.txt`.

## License

This script is licensed under the MIT License. See the `LICENSE` file for more details.
