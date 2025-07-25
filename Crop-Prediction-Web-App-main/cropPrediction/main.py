# -*- coding: utf-8 -*-
"""
Spyder Editor

Written By : Komal Kumari
"""
import os
# os.chdir("C:/Program Files/Spyder")
os.chdir("C:/Desktop/Crop-Prediction-Web-App-main (1)/Crop-Prediction-Web-App-main/cropPrediction")

import pandas as pd

def predict(item):
    df = pd.read_csv("crop.csv")
    df.head(6)


    df.isnull().sum()
    df.info()

    df.tail()

    df['label'].value_counts()

    # using inplace = True.. will remove that row completely
    #x = df.drop('label', axis = 1, inplace = True)

    # 
    x = df.drop('label', axis = 1)
    # print(x)
    y = df['label']

    from sklearn.model_selection import train_test_split

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state = 1, test_size = 0.2)

    # print("Info of x_train")
    x_train.info()

    y_train.info()

    # Here we will develop 4 models, and the best out of them will be considered for use

    from sklearn.linear_model import LogisticRegression

    model = LogisticRegression()

    model.fit(x_train, y_train)

    y_pred1 = model.predict(x_test)

    from sklearn.metrics import accuracy_score

    logis_reg = accuracy_score(y_test, y_pred1)

    # print("Logistic Accuracy is " + str(logis_reg))

    from sklearn.tree import DecisionTreeClassifier
    model_2 = DecisionTreeClassifier()

    model_2.fit(x_train, y_train) 

    y_pred_2 = model_2.predict(x_test)

    dec_acc = accuracy_score(y_test, y_pred_2)

    # print("Decision Tree Accuracy is " + str(dec_acc))

    from sklearn.ensemble import RandomForestClassifier
    model_3 = DecisionTreeClassifier()

    model_3.fit(x_train, y_train)

    y_pred_3 = model_2.predict(x_test)

    random_fo_acc = accuracy_score(y_test, y_pred_3)

    # print("Random Forest Accuracy is " + str(random_fo_acc))

    # from tensorflow.keras.model import sequential

    import joblib

    filename = "crop prediction"

    # i have used the best models based on their accuracy score
    joblib.dump(model_3, 'crop prediction')

    app = joblib.load('crop prediction')

    # item = [[54 , 7 , 89 ,   22.874, 72.464, 6.9, 199.935536]]

    # print("Here goes our predicted crop")

    ans = (app.predict(item))
    return ans

# ------------------------------------------------------------------------------------
