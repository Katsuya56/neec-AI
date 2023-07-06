import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

# データの読み込み
data = pd.read_csv('train_all.csv')

# 不要な列の削除
data = data.drop(['id', 'tv', 'gameday', 'time'], axis=1)

# カテゴリ変数のエンコーディング
categorical_cols = ['stage', 'weather', 'home_team', 'away_team']
for col in categorical_cols:
    label_encoder = LabelEncoder()
    data[col] = label_encoder.fit_transform(data[col])

# 欠損値の処理（ここでは平均値で置き換える）
data = data.fillna(data.mean())

# 目的変数と特徴量の分割
X = data.drop('y', axis=1)
y = data['y']

# データの正規化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# データの分割（訓練データとテストデータ）
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 線形回帰モデルの構築と学習
model = LinearRegression()
model.fit(X_train, y_train)

# テストデータでの予測
y_pred = model.predict(X_test)

# 予測結果の評価
score = model.score(X_test, y_test)
print("R^2 Score:", score)
