import pandas as pd
import random

class OneHotEncoder:
    def __init__(self, categories):
        self.categories = categories
        self.one_hot_dict = {}
        for i, category in enumerate(categories):
            self.one_hot_dict[category] = [0] * i + [1] + [0] * (len(categories) - i - 1)
    
    def encode(self, lst):
        return [self.one_hot_dict[item] for item in lst]

class DataEncoder:
    def __init__(self, encoder):
        self.encoder = encoder
    
    def encode_data(self, lst):
        one_hot_lst = self.encoder.encode(lst)
        data = pd.DataFrame(one_hot_lst, columns=self.encoder.categories)
        return data

categories = ['robot', 'human']
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

encoder = OneHotEncoder(categories)
data_encoder = DataEncoder(encoder)

data = data_encoder.encode_data(lst)
data.head()
