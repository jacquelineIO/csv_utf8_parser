import sys
import csv
from datetime import datetime
from pytz import timezone
import datetime

def print_err(message):
    print(message, file=sys.stderr)

eastern = timezone('US/Eastern')
pacific = timezone('US/Pacific')
infmt = '%m/%d/%y %H:%M:%S %p'
outfmt = '%Y-%m-%dT%H:%M:SS.%f'
#ISO 8601 format, YYYY-MM-DDTHH:MM:SS.mmmmmm or, if microsecond is 0, YYYY-MM-DDTHH:MM:SS

# Read from STDIN and decode to UTF-8
data = sys.stdin.buffer.read()
utf8_decode = data.decode("utf-8", 'replace')
#utf8_decode = data.decode("utf-8", 'backslashreplace')
csv_data = utf8_decode

# Process csv_data with DictReader
csv_reader = csv.DictReader(csv_data.splitlines())
header = csv_reader.fieldnames
csv_writer = csv.DictWriter(sys.stdout, fieldnames=header)

# Timestamp,Address,ZIP,FullName,FooDuration,BarDuration,TotalDuration,Notes
csv_writer.writeheader()
for row in csv_reader:
    outrow = {}
    try:
        # * The Timestamp column should be formatted in ISO-8601 format.
        # * The Timestamp column should be assumed to be in US/Pacific time;
        #   please convert it to US/Eastern.
        # 4/1/11 11:00:00 AM
        dt = datetime.datetime.strptime(row['Timestamp'], '%m/%d/%y %H:%M:%S %p')
        loc_dt = pacific.localize(dt)
        eastern_dt = loc_dt.astimezone(eastern)
        outrow['Timestamp'] =  eastern_dt.isoformat()

        # * The Address column should be passed through as is, except for
        #   Unicode validation. Please note there are commas in the Address
        #   field; your CSV parsing will need to take that into account. Commas
        #   will only be present inside a quoted string.
        outrow['Address'] = row['Address']

        # * All ZIP codes should be formatted as 5 digits. If there are less
        #   than 5 digits, assume 0 as the prefix.
        outrow['ZIP'] = '{:05d}'.format(int(row['ZIP']))

        # * All name columns should be converted to uppercase. There will be
        #   non-English names.
        outrow['FullName'] = row['FullName'].upper()

        # * The columns `FooDuration` and `BarDuration` are in HH:MM:SS.MS
        #   format (where MS is milliseconds); please convert them to a floating
        #   point seconds format.
        #   double seconds = milliseconds / 1000.0;
        split_date = row['FooDuration'].split('.')
        fd_dt = datetime.datetime.strptime(split_date[0], '%H:%M:%S')
        milli_sec = int(split_date[1])
        fd_dt = fd_dt + datetime.timedelta(milliseconds=milli_sec)
        outrow['FooDuration'] = "{}.{}".format(fd_dt.strftime('%H:%M:%S'), int(milli_sec))

        # * The columns `FooDuration` and `BarDuration` are in HH:MM:SS.MS
        #   format (where MS is milliseconds); please convert them to a floating
        #   point seconds format.
        split_date = row['BarDuration'].split('.')
        bd_dt = datetime.datetime.strptime(split_date[0], '%H:%M:%S')
        milli_sec = int(split_date[1])
        bd_dt = bd_dt + datetime.timedelta(milliseconds=milli_sec)
        outrow['BarDuration'] = "{}.{}".format(bd_dt.strftime('%H:%M:%S'), int(milli_sec))

        # * The column "TotalDuration" is filled with garbage data. For each
        #   row, please replace the value of TotalDuration with the sum of
        #   FooDuration and BarDuration.
        td_dt = fd_dt + datetime.timedelta(hours=bd_dt.hour, minutes=bd_dt.minute, seconds=bd_dt.second, microseconds=bd_dt.microsecond)
        milli_sec = td_dt.microsecond / 1000.0
        outrow['TotalDuration'] = "{}.{}".format(td_dt.strftime('%H:%M:%S'), int(milli_sec))


        # * The column "Notes" is free form text input by end-users; please do
        #   not perform any transformations on this column. If there are invalid
        #   UTF-8 characters, please replace them with the Unicode Replacement
        #   Character.
        outrow['Notes'] = row['Notes']
        
        #csv_writer.writerow(row)
        csv_writer.writerow(outrow)
    except ValueError as err:
        print_err(err)
