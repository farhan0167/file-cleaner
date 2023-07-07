# File Cleaner

The script will allow you to remove files that are older or were last modified by more a specified number of days.

## Use Cases
### Cleaning PDF files such as curated resumes


You might have a directory where you save all your copies of resume, that you curated for a particular position. If you are applying to 100s of jobs
you might have atleast 50+ resume saved on your computer that you'll never use again. This script will allow you to remove files that are older than 
however many days you specify.

## Running the Script


1. To run the script, first clone the repository:
```bash
git clone https://github.com/farhan0167/file-cleaner
```
2. Copy the main.py script to the folder where you have all your resumes
3. Run the script. Lets say you want to delete pdf files older than 30 days:
```bash
python3 main.py --days 30
```
4. The previous command will mount on the directory where the script is, but lets say you want to delete files within a specific folder, i.e, Example_Folder:
```bash
python3 main.py --days 30 --target Example_Folder
```

** Note ** Remember this is a destructive action. Once deleted, you cannot recover these files