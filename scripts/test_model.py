from sklearn.linear_model import LinearRegression
import pickle
import pandas as pd
 
df = pd.read_csv('/home/user02/Projects/mlops_2_3/datasets/data_test.csv', header=None)
df.columns = ['id', 'counts']
 
model = LinearRegression()
with open('/home/user02/Projects/mlops_2_3/models/data.pickle', 'rb') as f:
    model = pickle.load(f)
 
score = model.score(df['id'].values.reshape(-1,1), df['counts'])
print("score=", score)