# Demonstrate logging
# Attributes you can put in the basicConifg
#  level
#  filename
#  filemode
#  format
#     %(name)s - %(levelname)s - %(message)s - %(asctime)s - %(lineno)d

import logging
logging.basicConfig(filename='./mainlog.log',
                    level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d") # what this is set at will dictate which below is output when run 
# the prog. so whatever is here, the output of below will be the level here and above (not lower). for format
# time is asctime. s is string. d is number. lineno is line number

# prog does stuff
logging.debug("we are doing stuff") # just like a print statement to check it's working
logging.info("this is for info")
logging.warning("ooooohh i am not certain about this")
logging.error("not good")
logging.critical("really bad")