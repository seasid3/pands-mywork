# how to use a configuration file
# author: Orla Woods

import config as cfg

password = cfg.gmail["password"]

print(password)

# so you would save this file to github but you keep the config.py file on your laptop only so you 
# keep your sensitive info on your laptop only and not on github
# sensitive info into config file