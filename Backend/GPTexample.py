from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 페이지 생성
@app.route('/pages', methods=['POST'])
def create_page():
    data = request.json
    conn = sqlite3.connect('diary.db')
    c = conn.cursor()
    c.execute("INSERT INTO pages (date, gratitude, regret, study, exercise) VALUES (?, ?, ?, ?, ?)",
              (data['date'], data['gratitude'], data['regret'], data['study'], data['exercise']))
    conn.commit()
    page_id = c.lastrowid
    conn.close()
    return jsonify({"id": page_id, "message": "페이지 생성 완료"}), 201

# 특정 날짜 페이지 읽기
@app.route('/pages/<date>', methods=['GET'])
def get_page(date):
    conn = sqlite3.connect('diary.db')
    c = conn.cursor()
    c.execute("SELECT * FROM pages WHERE date = ?", (date,))
    page = c.fetchone()
    conn.close()
    if page:
        return jsonify({"id": page[0], "date": page[1], "gratitude": page[2], "regret": page[3], "study": page[4], "exercise": page[5]})
    else:
        return jsonify({"message": "페이지를 찾을 수 없음"}), 404

# 페이지 수정
@app.route('/pages/<id>', methods=['PUT'])
def update_page(id):
    data = request.json
    conn = sqlite3.connect('diary.db')
    c = conn.cursor()
    c.execute("UPDATE pages SET gratitude = ?, regret = ?, study = ?, exercise = ? WHERE id = ?",
              (data['gratitude'], data['regret'], data['study'], data['exercise'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "페이지 수정 완료"})

# 페이지 삭제
@app.route('/pages/<id>', methods=['DELETE'])
def delete_page(id):
    conn = sqlite3.connect('diary.db')
    c = conn.cursor()
    c.execute("DELETE FROM pages WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "페이지 삭제 완료"})

if __name__ == '__main__':
    app.run(debug=True)
