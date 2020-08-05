# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 02:35:01 2020

@author: JOhn Ketterer
"""
import pandas as pd
import pickle

# chunks were taken from regex of POS tags located on google colab
chunks1 = pickle.load( open('chunks_1.pickle', "rb" ) )
chunks2 = pickle.load( open('chunks_2.pickle', "rb" ) )
chunks3 = pickle.load( open('chunks_3.pickle', "rb" ) )
chunks4 = pickle.load( open('chunks_4.pickle', "rb" ) )

# Sample size is 10% and will be labeled accordingly
# perhaps a sample of a sample can be used depends on NN model
print('Length:', len(chunks1), 'Sample Size:', len(chunks1) * .10)
print('Length:', len(chunks2), 'Sample Size:', len(chunks2) * .10) 
print('Length:', len(chunks3), 'Sample Size:', len(chunks3) * .10)
print('Length:', len(chunks4), 'Sample Size:', len(chunks4) * .10)

def training_set(chunks):
    '''creates a dataframe that easily parsed with the chunks data '''
    df = pd.DataFrame(chunks)    
    df.fillna('X', inplace = True)
    
    train = []
    for row in df.values:
        phrase = ''
        for tup in row:
            # needs a space at the end for seperation
            phrase += tup[0] + ' '
        phrase = ''.join(phrase)
        # could use padding tages but encoder method will provide during 
        # tokenizing/embeddings; X can replace paddding for now
        train.append( phrase.replace('X', '').strip())

    df['phrase'] = train

    # only returns 10% of each dataframe to be used 
    return df.phrase.sample(frac = 0.1)

# one training corpus with 10% of each POS regex identification
training = pd.concat([training_set(chunks1),
                      training_set(chunks2), 
                      training_set(chunks3),
                      training_set(chunks4)], 
                        ignore_index = True )

training.to_csv('train_skills.csv')
print("'train_skills.csv' has been created")
