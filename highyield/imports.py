#import modules
from importlib.resources import files
import pandas as pd

#load RR.csv
def load_rr():
    # read text from highyield/data/RR.csv
    # split string into list of strings
    rr = files("/highyield/data").joinpath("RR.csv").read_text().split(sep="\n")

    #convert list of strings to df
    rr = pd.DataFrame(data=rr)
    return rr