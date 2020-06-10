# Purpose: record progress and problems...
# levels: notset (0), debug (10), info(20), warning (30), error (40), critical (50)
import logging

# Create and configure logger
LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename = 'loggingexample.log',
                    level=logging.DEBUG, # set the logging level: debug (10), info(20), warning (30), error (40), critical (50)
                    format = LOG_FORMAT)
logger = logging.getLogger()
#Test the logger
logger.info("1. Our first message.")
print(logger.level)
logger.debug('2. This is a harmless debug mesage.')
print(logger.level)
logger.info('3. Just some useful info.')
print(logger.level)
logger.warning('4. I\'m sorry, but I can\'t do that, Dave.')
print(logger.level)
logger.error('5. Did you just try to divid by zero?')
print(logger.level)
logger.critical('6. The entire internet is down!!')
print(logger.level)

