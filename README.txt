We have 2 + 1 assignment, +1 is totally optional, as we said in the lecture.

The first one is about content based recommender system. The dataset you will be used can be found at the Homework_RecSys.ipynb notebook. If there is a problem with notebook, or if there is a ambigious explanation about this assignment, you can always	make contact with Enes Sadi Uysal.

The second one is about anomaly detection. The dataset you will be used can be found at main directory with "kdd.csv" name. The task is building a model that can distinguish anomaly (probe) and normal. Train, validation and test variables are defined in notebook. Please report your auc-roc and macro average f1 scores. If there is a problem with notebook, or if there is a ambigious explanation about this assignment, you can always make contact with Şafak Bilici.


The third and totally optional assignment was stated in the lecture. You can find all datasets at optional_assignment_datasets folder. If you are planning to play with this optional assignment you can report your accuracy, f1 and g-mean scores. G-mean is defined as:

```
from imblearn.metrics import sensitivity_score, specificity_score

def gmean(y_true, y_pred):
    return np.sqrt(sensitivity_score(y_true, y_pred) * specificity_score(y_true,y_pred))
```
