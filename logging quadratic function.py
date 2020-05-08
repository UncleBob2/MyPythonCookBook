# Purpose: record progress and problems...
# levels: notset (0), debug (10), info(20), warning (30), error (40), critical (50)
import logging
import math

# Create and configure logger
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename = 'logquadraticerrors.log',
                    level=logging.DEBUG, # set the logging level: debug (10), info(20), warning (30), error (40), critical (50)
                    format = LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

def quadratic_formula(a,b,c):
    """Return the solutions to the equation ax^2 + bx + c =0. """
    logger.info("quadratic_formula({0}, {1}, {2})".format(a,b,c))

    # Compute the discriminat
    logger.debug("# Compute the discrimant")
    disc = b**2 - 4*a*c

    # Compute the two roots
    logger.debug("# compute first root")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    logger.debug("# computer second root")
    root2 = (-b - math.sqrt(disc))/ (2*a)

    # Return the roots
    logger.debug("# Return the roots")
    return(root1, root2)

roots = quadratic_formula(1,0,1)
print(roots)


