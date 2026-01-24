from sklearn.model_selection import train_test_split
import uuid
import numpy as np

def add_identifiers(df):

    df["unique_id"] = [uuid.uuid4().hex for x in range(len(df))]
      
    #split into train and test
    train_ids, test_ids = train_test_split(df["unique_id"], test_size = 0.1, random_state = 10)

    #create the split map to be used later
    train_set = set(train_ids)

    df["which_set"] = np.where(df["unique_id"].isin(train_set), "train", "test")
    df.drop(columns = ["unique_id"], inplace = True)

    return df