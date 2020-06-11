import sys
import getopt # to parse the command line variables

def get_start_and_end_dates():
    start_date = None
    end_date = None

    argv = sys.argv[1:] #skip the first element and print out the rest of arg

    try:
        #opts, args = getopt.getopt(argv,"s:e:")  # s: s with colon required us to pass in a value hs: h does not require value
        opts, args = getopt.getopt(argv, "s:e:", ['start_date=', 'end_date=']) # long form with using --
        print(opts)
    except getopt.GetoptError as error:
        print(error)
        opts = []

    for opt, arg in opts: #go through each tuple
        if opt in ['-s', '--start_date']:
            start_date = arg
        elif opt in ['-e', '--end_date']:
            end_date = arg

    print('start_date: {}'.format(start_date))
    print('end_date: {}'.format(end_date))

get_start_and_end_dates()

# put below command line in the terminal
# argvgetopt.py --start_date=2000-1-1 --end_date=2010-1-1
# argvgetopt.py -s 2000-1-1 -e 2010-1-1