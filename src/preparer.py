import os
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split

P = yaml.safe_load(open('params.yaml', encoding='utf-8'))['preparation']
df = pd.read_csv('data/transactions.csv')
train, test = train_test_split(df, test_size=P['test_size'],
                               random_state=P['random_state'],
                               stratify=df['fraude'])
os.makedirs('data/prepare', exist_ok=True)
train.to_csv('data/prepare/train.csv', index=False)
test.to_csv('data/prepare/test.csv', index=False)
print(f"preparation : {len(train)} lignes train / {len(test)} lignes test")