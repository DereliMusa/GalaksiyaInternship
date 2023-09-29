import joblib as jb
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Modelimizin çalışması için gerekli olan özelliklerin girilmesi
class Features(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

xgb_model = jb.load('PretrainedModel/xgb_model.joblib')
lgb_model = jb.load('PretrainedModel/lgb_model.joblib')
cat_model = jb.load('PretrainedModel/cb_model.joblib')

app = FastAPI()

# fast.api ile gelen isteklerin karşılanacağı fonksiyonlar oluşturacağız
# bu fonksiyonlar decorator ile belirtilecek

@app.get("/")
def read_data():
    return {"message": "Connection available"}

# Modelimimizin çalışması için gerekli olan özelliklerin girilmesi
# ve modelden dönen sonucun gösterilmesi

@app.post("/predict", status_code=200)
def predict_diabetes(features: Features):
    prediction_xgb = xgb_model.predict([[features.Pregnancies,
                                               features.Glucose,
                                               features.BloodPressure,
                                               features.SkinThickness,
                                               features.Insulin,
                                               features.BMI,
                                               features.DiabetesPedigreeFunction,
                                               features.Age]])
    prediction_lgb = lgb_model.predict([[features.Pregnancies,
                                                features.Glucose,
                                                features.BloodPressure,
                                                features.SkinThickness,
                                                features.Insulin,
                                                features.BMI,
                                                features.DiabetesPedigreeFunction,
                                                features.Age]])
    prediction_cat = cat_model.predict([[features.Pregnancies,
                                                features.Glucose,
                                                features.BloodPressure,
                                                features.SkinThickness,
                                                features.Insulin,
                                                features.BMI,
                                                features.DiabetesPedigreeFunction,
                                                features.Age]])
    
    if(prediction_xgb[0] == 1):
        prediction_xgb = "Diabetes"
    else:
        prediction_xgb = "No Diabetes"
    
    if(prediction_lgb[0] == 1):
        prediction_lgb = "Diabetes"
    else:
        prediction_lgb = "No Diabetes"

    if(prediction_cat[0] == 1):
        prediction_cat = "Diabetes"
    else:
        prediction_cat = "No Diabetes"

    
    return {"prediction_xgb": prediction_xgb,"prediction_lgb": prediction_lgb,"prediction_cat": prediction_cat}

if __name__ == "__main__":
    uvicorn.run("api:app", host='127.0.0.1', port=8000)

