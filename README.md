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


**Note** Remember this is a destructive action. Once deleted, you cannot recover these files
```bash
python3 main.py --days 30
```
The previous command will mount on the directory where the script is, but lets say you want to delete files within a specific folder, i.e, Example_Folder:
```bash
python3 main.py --days 30 --target 'Example Folder'
```

### Clean based on Search Term
You can now specify a search term or file name to look for when wiping out a directory.

```bash
python3 main.py --days 0 --target 'Example Folder' --search 'Example Search Term'
```

This action will look into the Example Directory for files that have Example Search Term name, and delete them if they are 0 days old.

### Arguments
```
  -h, --help       show this help message and exit
  --days DAYS      Number of days to look behind to consider a file outdated. Default value is 365 days
  --target TARGET  The directory to clean up. By default it will mount on current directory
  --search SEARCH  The search term to clean up. By default it will be None
```
**Note** Remember this is a destructive action. Once deleted, you cannot recover these files