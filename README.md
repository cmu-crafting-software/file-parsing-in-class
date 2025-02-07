## January 22 in class exercise

1. Open repository in codespaces
2. Create a branch of this repository. Use your first name as the name of the branch.  You may use the UI, or this command `git checkout -b YOUR_NAME`
3. Create a new file, `solution.py`, in the root directory of this repository that you will use to write your code.
4. Write a python function that reads in `presidents.json` in the root of this repository and computes the average age of each of the people in the file.
3. Edit `presidents.json` to add a new president. Rerun your function to make sure it prints the age of the new president. 
4. Edit the presidents.json file to add a new column for state of birth.
5. Write a python function that reads in your new `presidents.json` and prints out all of the presidents sorted by state.
6. **Stretch goal 1:** Write a python function that finds all json files in the repository directory or any subdirectory. Compute the average age of all of the people listed in any of these files.
7. **Stretch goal 2:** Write a python function that finds all json **or csv** files in the repository directory or any subdirectory. **Remove duplicates**, and compute the average age of all of the people listed in any of these files. 

### Resources
* [Working with dates in Python](https://docs.python.org/3/library/datetime.html)
* [Python `json` module](https://docs.python.org/3/library/json.html)
* [Python `io` module for working with Files and streams](https://docs.python.org/3/library/io.html)
* [Python `os.path` module](https://docs.python.org/3/library/os.path.html)

