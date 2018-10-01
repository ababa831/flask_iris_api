# Iris classification API demo

A simple ML RESTful API demo by [Flask](http://flask.pocoo.org/)

## Usage

1. git clone the repository
2. Run `apy_demp.py`, and the API server will start
3. Post API requests by curl command (as shown in below example)

```bash
$ curl http://0.0.0.0:5000/predict -X POST -H 'Content-Type:application/json' -d '{"X_pred":[6.5,2.8,4.6,1.5]}'
{
  "Content-Type": "application/json", 
  "is_succeeded": true, 
  "y_pred": [
    "versicolor"
  ]
}
$ curl http://0.0.0.0:5000/predict -X POST -H 'Content-Type:application/json' -d '{"X_pred":[6.3,2.8,5.1,1.5]}'
{
  "Content-Type": "application/json", 
  "is_succeeded": true, 
  "y_pred": [
    "virginica"
  ]
}
$ curl http://0.0.0.0:5000/predict -X POST -H 'Content-Type:application/json' -d '{"X_pred":[4.6,3.4,1.4,0.3]}'
{
  "Content-Type": "application/json", 
  "is_succeeded": true, 
  "y_pred": [
    "setosa"
  ]
}
```

## References

- [ナード戦隊データマン's article](http://datanerd.hateblo.jp/entry/2017/09/01/212021)
- [yukkyo's article](https://qiita.com/yukkyo/items/1464c42324f15d7b8223)