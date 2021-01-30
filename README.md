# Printing usage report with Python
A Python program which parses a file containing information about the printing usage of a number of users and outputs summary information.

## Specifications
1. It should be invoked as: `python printing_summary.py option printing_usage_file`
2. The program checks that argument *printing_usage_file* exists, is a file and is readable. If not, it prints an error message to the standard output and exit.
3. File *printing_usage_file* can have any arbitrary name. It must be a file of text with the following format:
    - The file consists of an arbitrary number of lines (including, possibly, zero lines).
    - Each line must contain three fields separated by commas.
    - The three fields are: *filename*, *size in bytes*, *username*.
    - The filename field is a string of characters of arbitrary (yet reasonably limited) length. Acceptable characters include: lower and upper case letters, digits, underscore, dot, space.
    - The *size in bytes* field is an integer limited between 1 and 67,108,864.
    - The *username* field is a string of characters of arbitrary (yet reasonably limited) length. Acceptable characters include: lower and upper case letters, digits, underscore,
dot.
    The following example should be regarded as the reference specification for the format of file *printing_usage_file*:
      ```
      article.pdf,1550008,massimo.piccardi
      USP 32547 Assignment S2012.docx,36024,MarkThomas
      article.ps,10000000,massimo.piccardi
      article.pdf,205000,massimo.piccardi
      Recipes.html,239250,schmidt1974
      ```

4. This program can be invoked with option: `-a`. In this case, it must print each unique username in the order in which it first appears in the file: 
   ```
   Printing users:
   <first user in appearance order>
   <second user in appearance order>
   …
   <last user in appearance order>
   ```
   Command line:
   ```
   printing_summary.py -a printing_usage_file
   ```
   Output:
   ```
   Printing users:
   massimo.piccardi
   MarkThomas
   schmidt1974
   ```
   If the file is empty:
   ```
   No printing users
   ```

5. This program can be invoked with option: `-f`. In this case, it must only print the following string:
   ```
   Total number of files printed: <number of files printed>
   ```
   Command line:
   ```
   printing_summary.py –f printing_usage_file
   ```
   Output:
   ```
   Total number of files printed: 5
   ```
   If the file is empty:
   ```
   Total number of files printed: 0
   ```
6. This program can be invoked with option: `-s`. In this case, it must only print the following string:
   ```
   Total number of bytes printed: <number of bytes printed>
   ```
   Command line: 
   ```
   printing_summary.py –s printing_usage_file
   ```
   Output:
   ```
   Total number of bytes printed: 12030282
   ```
   If the file is empty:
   ```
   Total number of bytes printed: 0
   ```
7. This program can be invoked with option: `-u username`. In this case, it must print:
   ```
   User username:
   Total number of files printed: <number of files printed for user username>
   Total number of bytes printed: <number of bytes printed for user username>
   Largest file printed: <number of bytes of the largest file printed for user username>
   ```
   Command line:
   ```
   printing_summary.py –u massimo.piccardi printing_usage_file
   ```
   Output:
   ```
   User massimo.piccardi:
   Total number of files printed: 3
   Total number of bytes printed: 11755008
   Largest file printed: 10000000
   ```
   If the username is not present in the file:
   ```
   User <username> not found
   ```
8. This program can be invoked with option: `-v`. In this case, it must only print the author's name and date of completion. Please note that argument argument_file is still required.
9. No options can be used simultaneously. This means that the program can only be invoked with one of the options at a time.
10. If this program is invoked with any other syntax than those specified above, it must print a message to the standard output and exit.
    Examples of incorrect syntax:
    ```
    printing_summary.py -Z argument_file
    printing_summary.py -u
    ```
