
from fastapi import FastAPI,UploadFile,File
import pandas as pd
from io import StringIO
app=FastAPI()
@app.post('/ab_test/')
async def run_abtest(file: UploadFile = File(...)):
    contents = await file.read()
    csv_str= contents.decode("utf-8")
    df=pd.read_csv(StringIO(csv_str))
    
    import numpy as np
    from scipy.stats import norm
    df_clean=df.drop_duplicates(subset='user_id',keep='first')
    conversion_rates=df_clean.groupby('group')['converted'].agg(['mean','count','sum'])
    pt=conversion_rates.loc['treatment','mean']
    pc=conversion_rates.loc['control','mean']
    diff = pt-pc
    n_control = conversion_rates.loc['control','count']
    x_control = conversion_rates.loc['control','sum']
    n_treatment = conversion_rates.loc['treatment','count']
    x_treatment = conversion_rates.loc['treatment','sum']
    pooled=(x_control+x_treatment)/(n_treatment+n_control)
    SE=np.sqrt(pooled*(1-pooled)*(1/n_control+1/n_treatment))
    z_score = diff/SE
    p_value=2*(1- norm.cdf(abs(z_score)))

    result= {
        "Control conversion rate ":round(pc,5),
        "Treatment conversion rate":round(pt,5),
        "Difference":round(diff,5),
        "Pooled conversion rate":round(pooled,5),
        "Standard Error":round(SE,5),
        "Z-score":round(z_score,5),
        "P value":round(p_value,5)}
    
    return result

