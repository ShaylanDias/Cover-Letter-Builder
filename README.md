# Cover-Letter-Builder
Script for using a command line tool to fill in a generic cover letter with information relevant to each position when mass applying to jobs

In your template use the following tags:

{date} - For today's date

{company} - For the company you are applying to

{role} - The position you are applying to

{location} - The location of the position

Commandline Arguments:
-c \[Company\]
-r \[Role\]
-l \[Location\]

Example Script Call:
python3 parser.py -c Test.inc -r Developer -l Sunnyvale, CA
