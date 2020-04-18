from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)
db = client.dbsparta




@app.route('/write') 
def write():
    return render_template('write.html')


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/save', methods=['POST'])
def post_save():
    category = request.form['category']
    title = request.form['title']
    code = request.form['code']
    memo = request.form['memo']
    print(code)
    collection = {
        'category': category,
        'title': title,
        'code': code,
        'memo': memo
    }
    db.collections.insert_one(collection)
    return jsonify({'result': 'success', 'msg': '저장이 완료되었습니다!'})


@app.route('/collections', methods=['GET'])
def get_collections():
    collections = list(db.collections.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'collections': collections})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
