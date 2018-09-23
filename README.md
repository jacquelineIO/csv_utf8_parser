# Jacqueline McKinney Software Engineering Problem Submittal

## Solution 

In my solution, I didn't completely solve the problem as requested. 
The program is able to accept input from `stdin`, direct output to `stdout`, and 
errors to `stderr`. The output to `stdout` is in the requested normalized CSV format.

However, the issue I ran into was in trying to read the broken UTF-8 CSV file from `stdin`. I've taken some notes on to how to resolve this issue, but was not able to complete this in the allotted 4 hours.

I also have one question as I'm re-reading the problem. The `FooDuration` and `BarDuration` columns are times (assumed to be in US/Pacific), but there weren't specfic instructions to convert to US/Eastern therefore, were left as is. 


## Environment Used

macOS High Sierra v10.13.16 was used to implement the solution.

## Prerequisites 

1. python 3
2. python [pytz] (https://pypi.org/project/pytz/) package for timezone support
3. cat
4. python env (optional)

## Setup and Run

### Setup env (this is optional)

Go to folder where you will be running the application

```
python3 -m venv env
source env/bin/activate
```

### Download repo from GitHub

```
git clone https://github.com/jacquelineflemming/csv_utf8_parser.git
cd csv_utf8_parser
pip install -r requirements.txt
```

### Run solution

```
cat sample.csv | python cli_process_csv.py > output.csv
```

### View CSV file in desired application 

```
vim output.csv
```

## Solution Part 2

I believe this part took me longer than 4 hours to solve. I would like to also include it in this GitHub. Please ignore if not allowed.

When decoding the broken CSV file into UTF-8 no replacement characters are used. It seems that the byte values were
translated to a valid UTF-8 character.

The solution in part 2 was to read everything in bytes from `stdin` and then use the python function `decode` to convert to UTF-8 and
I selected the errors option to `replace`.

### Run the part 2 solution

```
cat sample-with-broken-utf8.csv | python cli_process_csv2.py > output2.csv
```