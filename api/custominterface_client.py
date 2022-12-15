import pandas as pd
import requests

from mlem.api import apply_remote
from mlem.runtime.client import HTTPClient


def main():
    r = requests.post("http://localhost:8080/predict", json={
        "data": {
            "values": [
                {
                    "": "0",
                    "Geography": "France",
                    "CreditScore": "5",
                    "Age": "25",
                    "Tenure": "2",
                    "Balance": "10",
                    "NumOfProducts": "0",
                    "HasCrCard": "0",
                    "IsActiveMember": "0",
                    "EstimatedSalary": "233"
                }
            ],
            "metadata": {"add": 10}
        },

    }, )

    print(r.json())

    client = HTTPClient()

    res = client.predict(pd.DataFrame([
        {
            "": 0,
            "Geography": "France",
            "CreditScore": 5,
            "Age": 25,
            "Tenure": 2,
            "Balance": 10.0,
            "NumOfProducts": 0,
            "HasCrCard": 0,
            "IsActiveMember": 0,
            "EstimatedSalary": 233.0
        }
    ]))

    print(res)



if __name__ == '__main__':
    main()
