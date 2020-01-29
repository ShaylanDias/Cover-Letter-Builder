# Cover-Letter-Builder
Script for using a command line tool to fill in a generic cover letter with information relevant to each position when mass applying to jobs
\n

In your template use the following tags:\n
{date} - For today's date\n
{company} - For the company you are applying to\n
{role} - The position you are applying to\n
{location} - The location of the position\n
\n
Commandline Arguments:\n
-c \[Company\]\n
-r \[Role\]\n
-l \[Location\]\n
\n
Example Script Call:\n
python3 parser.py -c Test.inc -r Developer -l Sunnyvale, CA
