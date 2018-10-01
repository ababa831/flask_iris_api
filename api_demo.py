from sklearn.externals import joblib
import flask
import numpy as np

# Settings
MODEL_PATH = "./models/iris_pretrained_svc.pkl"
iris_dict = {"0": "setosa", "1": "versicolor", "2": "virginica"}

# Initialize App
app = flask.Flask(__name__)
model = None


def load_model():
    """
    Load a pretrained iris classification model from MODEL_PATH
    """
    global model
    print("Loading a pretrained model.")
    model = joblib.load(MODEL_PATH)
    print("Finish loading the model.")


@app.route("/predict", methods=["post"])
def predict():
    res = {"is_succeeded": False, "Content-Type": "application/json"}

    # Ensure an feature was properly uploaded
    if flask.request.method == "POST":
        # Get feature from json
        X_pred_list = flask.request.get_json().get("X_pred")
        print(X_pred_list)
        if X_pred_list:
            X_pred_np = np.array(X_pred_list).reshape(1, -1)
            y_pred = model.predict(X_pred_np)
            res["y_pred"] = [iris_dict[str(y)] for y in y_pred]
            res["is_succeeded"] = True

    return flask.jsonify(res)


def main():
    load_model()
    print("Starting Flask api server...")
    app.run(debug=True)


if __name__ == '__main__':
    main()