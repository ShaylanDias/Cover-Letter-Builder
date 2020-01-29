import argparse
from docx import Document
from datetime import date

def combine_str_args(args):
    if args:
        res = ''
        for arg in args:
            res += arg + ' '
        return res[: len(res) - 1] if len(res) > 1 else res
    else:
        return ''

parser = argparse.ArgumentParser(description='Add information')
parser.add_argument('-c', metavar='c', type=str, nargs='+',
                    help='company you are applying to with quotes around it')
parser.add_argument('-r', metavar='r', type=str, nargs='+',
                    help='role')
parser.add_argument('-l', metavar='l', type=str, nargs='+',
                    help='location')

parser.add_argument('-t', metavar='template', type=str, nargs='+',
                    help='filepath from this script to the cover letter template')

args = parser.parse_args()
company = combine_str_args(args.c)
role = combine_str_args(args.r)
location = combine_str_args(args.l)

today = date.today()
date = today.strftime("%B %d, %Y")

if not role or not company:
    raise ValueError("Need to input a company and role!")

document = Document('letter_templates/Cover-Letter-Template-Shaylan Dias.docx')

def replace_tag(run, tag, replacement):
    i = -1
    try:
        i = run.text.index(tag)
        run.text = run.text[:i] + replacement + run.text[i+len(tag):]  
        replace_tag(run, tag, replacement)
    except ValueError:
        return

for paragraph in document.paragraphs:
    for run in paragraph.runs:
        replace_tag(run, '{company}', company)
        replace_tag(run, '{role}', role)
        replace_tag(run, '{date}', date)
        if location:
            replace_tag(run, '{location}', location)
        else:
            replace_tag(run, '{location}', '')

document.save('generated_letters/' + company + '-' + role + '-Cover Letter.docx')

