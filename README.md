# To-Do App

This project is a simple to-do list application with a graphical user interface (GUI). It allows users to add, edit, and complete tasks. The app is built using Python and the PySimpleGUI library.

## Features

- Add new tasks to the to-do list.
- Edit existing tasks.
- Mark tasks as complete and remove them from the list.
- Display the current date and time.
- Data persistence: The to-do list is stored in a text file (`todos.txt`) and is loaded every time the app is run.

## GUI Implementation

The GUI is created using the PySimpleGUI library, which provides an easy way to build user interfaces for Python applications. The layout consists of various elements, including a clock to display the current time, an input box to add new tasks, a list box to display the tasks, and buttons for editing, completing, and exiting the app.

## File Structure

- `gui.py`: This script contains the main application code and handles the GUI interaction.
- `functions.py`: This script contains helper functions for reading and writing to the `todos.txt` file.

## Requirements

The project requires the following dependencies:

- PySimpleGUI==4.60.5

You can install the required dependencies by running `pip install -r requirements.txt`.

## Usage

To use the to-do app:

1. Clone the repository or download the source code files.
2. Ensure that the `todos.txt` file exists in the same directory as the `gui.py` and `functions.py` files.
3. Run the `gui.py` script using Python: `python gui.py`.
4. The GUI window will open, displaying the current date and time, an input box, and the list of tasks.
5. Add new tasks by typing them into the input box and clicking the "Add" button.
6. Edit tasks by selecting them from the list and clicking the "Edit" button.
7. Mark tasks as complete by selecting them from the list and clicking the "Complete" button.
8. To exit the app, click the "Exit" button or close the window.

## Customization

You can customize the app by modifying the code in the `gui.py` and `functions.py` files. For example, you can change the layout, styling, or file path for storing the to-do list.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or new features to add, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [PySimpleGUI](https://pysimplegui.readthedocs.io/) - A Python library for building GUIs.

Feel free to customize the above template to include specific details about your to-do app, such as installation instructions, additional features, or any other relevant information.