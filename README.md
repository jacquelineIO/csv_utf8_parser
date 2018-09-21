# Jacqueline McKinney Software Engineering Problem Submittal

## Solution 

In my solution, I didn't completely solve the problem as requested. 
The program is able to accept input from `stdin`, direct output to `stdout`, and 
errors to `stderr`. The output to `stdout` is in the requested nomalized CSV format.

However, the issue I ran into was in trying to read the broken UTF-8 CSV file from `stdin`. I've take some notes on to how to resolve this issue, but was not able to complete this in the alloted 4 hours.


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
git clone <insert>
cd <folder>
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