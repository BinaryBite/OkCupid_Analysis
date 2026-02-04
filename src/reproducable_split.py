from sklearn.model_selection import train_test_split
import numpy as np

def add_identifiers(df):

    df.reset_index()
      
    #split into train and test
    train_ids, test_ids = train_test_split(df.index, test_size = 0.1, random_state = 42)

    #create the split map to be used later
    train_set = set(train_ids)

    df["which_set"] = np.where(df.index.isin(train_set), "train", "test")

    return df