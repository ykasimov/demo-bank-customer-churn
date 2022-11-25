import argparse
import sys
from pathlib import Path
import dvclive



src_path = Path(__file__).parent.parent.resolve()
sys.path.append(str(src_path))
from mlem.api import load
import gto
import joblib
import dvc.api
import git
from utils.load_params import load_params
import json
# repo = "."
# # repo="https://github.com/ykasimov/demo-bank-customer-churn"
# revision = gto.api.find_versions_in_stage(repo=repo, name="randomforest-model", stage="dev")[0].ref
# with dvc.api.open("model/clf-model", repo=repo, rev=revision, mode="rb") as f:
#     model = joblib.load(f)
# print()
# # gto.api.GitRegistry.
# print(model)

def compare(model_path: str, compare_to: str):
    new_model = joblib.load(model_path)
    repo = "."
    # repo="https://github.com/ykasimov/demo-bank-customer-churn"
    revision = gto.api.find_versions_in_stage(repo=repo, name=compare_to, stage="prod")[0].ref
    with dvc.api.open(model_path, repo=repo, rev=revision, mode="rb") as f:
        prev_model = joblib.load(f)

    ### your comparison code here
    best_model = new_model
    # gto.api.register(git.Repo.refs)
    # gto.api.assign()
    metrics = {"old_model_metrics": {"acc": 0.8, "f1": 0.83},
                "new_model_metrics": {"acc": 0.86, "f1": 0.88}}
    with open("comparison_metrics.json", "w") as f:
        json.dump(metrics, f)

if __name__=="__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    params = load_params(params_path=args.config)
    model_path = "model/clf-model"
    compare(model_path=model_path, compare_to="anavo-model")