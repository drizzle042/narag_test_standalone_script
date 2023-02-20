import argparse


class CustomCMDParser(argparse.ArgumentParser):
    def _check_value(self, action, value):
        if action.choices is not None and value not in action.choices:
            args = {'value': value,
                    'choices': f'{action.choices[0]} - {action.choices[-1]}'}
            msg = ('invalid choice: %(value)r (choose from %(choices)s)')
            raise argparse.ArgumentError(action, msg % args)


parser = CustomCMDParser(
    prog = 'Document Reader',
    usage='%(prog)s [options]',
    description = 'Takes a document and prints first line or a specific line',
    epilog = 'Dedicated to Mr Ceril from Narag Energy Solutions'
)

parser.add_argument(
    '--version', 
    action='version', 
    version='%(prog)s 1.0'
)

parser.add_argument(
    "document",
    metavar='Document',
    help="Document to Read", 
    nargs=1,
    type=argparse.FileType('r')
)

parser.add_argument(
    "-l", "--line",
    help="Print Line From Document",
    choices=range(1, 1000000),
    default=0,
    nargs=1,
    type=int
)
 
# Read arguments from command line
args = parser.parse_args()

def main():
    document = args.document
    line_number = args.line

    if line_number == 0:
        line = document[0].read()
    else:
        line_number = line_number[0] - 1
        line = document[0].readlines()[line_number]

    return line


if __name__ == '__main__':
    print(main())
