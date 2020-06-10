import argparse2
from functools import reduce

def multipy(numbers):
    return reduce(lambda x,y: x*y, numbers)


parser = argparse2.ArgumentParser(description='Process some integers')
parser.add_argument('integer', nargs='+', type = int, metavar ='N',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest ='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default will find the max)')

parser.add_argument('--mult', dest ='accumulate', action='store_const',
                    const=multipy, default=max,
                    help='multiply the integers (default will find the max)')

args = parser.parse_args()
#print(args.accumulate(args.intergers))

