# Generate histograms and other analysis for survey results
import numpy as np

def count_elements(seq):  
    '''
    creates a dictionary that maps a list of items to the number of times
    they occur in the list.
    The 'keys' are the items and the 'values' are the counts.
            Parameters:
                    seq: list of integers or floats (or could be any list)
            Returns:
                    hist: a dictionary
    '''
    hist = dict()
    #You fill in this part
    for num in seq:
        hist[num]=hist.get(num,0)+1
    return hist

def ascii_histogram(seq) -> None:  #create a histogram from a list of numbers
    '''
    Creates a horizontal frequency-table/histogram plot using asterisks
    Code borrowed from https://realpython.com/python-histograms/"""
    '''
    counted = count_elements(seq) #generate frequency table  (dictionary)
    for key in sorted(counted):   # want the keys sorted from smallest to largest
        if key > 0:  #skips the nan
            print('{0:5f} {1}'.format(key, '+' * counted[key]))
 

survey_data = np.genfromtxt('StudentExercise.csv', delimiter=',', skip_header=1,autostrip=True)
#put code here to get the TV watching data
TV_list=[] #Your code here: should be a list of hours of TV watched per week
TV_array=survey_data[:,1]
for hrs in TV_array:
    try:
        TV_list.append(int(hrs))
    except:
        continue
#print(TV_list)
ascii_histogram(TV_list)
