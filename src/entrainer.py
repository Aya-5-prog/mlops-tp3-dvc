import os
import yaml
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

P = yaml.safe_load(open('params.yaml', encoding='utf-8'))['entrainement']
train = pd.read_csv('data/prepare/train.csv')
X, y = train.drop(columns='fraude'), train['fraude']
model = RandomForestClassifier(n_estimators=P['n_estimators'],
                               max_depth=P['max_depth'],
                               random_state=P['random_state'])
model.fit(X, y)
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/model.pkl')
print('entrainement : modele sauvegarde dans models/model.pkl')