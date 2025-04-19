# Author: _________
# Generate random alleles for height 'genes' and create a histogram
# BC Honor Code Pledge: This is my own original work and
# I did not use the internet for help (except for looking up individual python functions)
import numpy as np
heights = [] #store height of each plant
num_plants = 500

def count_elements(seq):  
    '''
    You do not have to modify this function.
    Generates a frequency table given a list of numbers 
            Parameters:
                    seq: list of integers or floats
            Returns:
                    hist: a dictionary
    '''
    hist = dict()
    for height in seq:
        hist[height]=hist.get(height,0)+1
    return hist

def ascii_histogram(seq) -> None:  #create a histogram from a list of numbers
    '''
    You do not have to modify this function.
    It creates a horizontal frequency-table/histogram plot
    Code borrowed from https://realpython.com/python-histograms/"""
    '''
    counted = count_elements(seq) #generate frequency table  (dictionary)
    for key in sorted(counted):   # want the heights sorted from smallest to largest
        print('{0:5d} {1}'.format(key, '+' * counted[key])) #prints out asterisk for each plant

def generate_height_distr(default_height, min_val,max_val,num_plants):
    '''Generate the plants' heights using random sampling and
    return the list of heights.
            Parameters:
                    default_height: the height that the plant would be without the genes influencing height
                    minVal: the minimum effect of the gene on height (eg, -1 inch)
                    maxVal: the maximum effect of the gene on height (eg, + 1 inch)
                    num_plants
            Returns:
                heights: a list of heights (where the length of list is num_plants)
    For each plant, generate a list of outcomes of the genes (20 genes would be reasonable
    for this project). Use np.random.randint(min, max, size) to generate the contribution
    from each gene.  (Size will be the number of genes that you choose, such as 20.)
    To calculate the net effect of all 20 genes, calculate the sum of this list.

    The actual height of each plant will be the default height, plus this sum of the effect
    of the genes. Return a list of heights of each plant.
    '''
    p=[]
    for plant in range(0,num_plants):
        plants=np.random.randint(min_val,max_val,20)
        add=sum(plants)
        p.append(add+default_height)
    return p   #erase this sample code

#This is the main program. You do not have to modify this.
heights = generate_height_distr(50,-1,1,400)#input min height contribution, max contribution, number of plants
ascii_histogram(heights)
