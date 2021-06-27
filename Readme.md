# Hahow Backend Engineer 徵才小專案
這是一個簡單的API server，提供`GET /heroes`和`GET /heroes/<hero_id>`兩個endpoint，會透過hahow提供的api獲取對應資料，並回傳給client。

## Get Started
### Install requirements

```
pipenv install
pipenv shell

or 

pip instll requirements.txt
```
### 設定環境變數
```
export FLASK_APP=flaskr
```
### 啟動 local server
```
flask run
```

<br>
<br>

## 專案架構

### 程式架構
參考[MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)邏輯。<br>
`flaskr/`：主要程式碼，包含API routing, error handling, controllers等主程式碼
* `views/`：api routing邏輯
* `thirdparty/`：第三方API 的utility function
* `tests/`：相關api測試（目前只有針對api endpoint撰寫，third party尚未實現）
* `error_handler.py`：錯誤Response的wrapper
* `thread.py`：包含`class ThreadRequest`，用來執行concurrent requests

### Thirdparty Library
這個專案大部分使用python或flask框架提供的library，如  [requests](https://github.com/psf/requests)
, [flask-restful](https://github.com/flask-restful/flask-restful)、實現retry機制使用的[retrying](https://github.com/rholder/retrying)、以及程式碼品質分析(linting)的[isort](https://github.com/PyCQA/isort), [flake8](https://github.com/PyCQA/flake8) 和[black](https://github.com/psf/black)。

<br>
<br>


## 專案特色
### Retry 機制
**問題**：由於第三方API不穩定性，使得api endpoint 頻繁回傳Invalid Response。
**解方**：針對最不穩定的`get_profile_by_id`，加入max_retry=2的機制，成功將錯誤次數降到原本的1/3。

### Multithreading優化
**問題**：針對Authenticated request，需要回傳額外的profile data。然而由於該資料需要根據每個id一個一個去打第三方API，導致速度太慢。
**解方**：針對authenticated的`/heros`做multithread的優化，成功提升速度兩倍以上。

其他更多詳細內容與測試過程，可參考 [這份Google doc](https://docs.google.com/document/d/1nbh4kq1npun7aMx5vGXpVpnB1h1jlmDtj1qKLwgzzzs/edit?usp=sharing)

## 其他
### 註解原則
原則上，程式碼應該透過函式命名、標註回傳型態等方式，讓其他人一目瞭然，而避免用過多的註解去敘述功能。然而若是遇到有些狀況，例如為了handle某些特殊情況而加的`if-else`、或是因應功能需求產生的額外API call，可能就會需要加上comment，敘述這段程式碼做的事情以及原因。
