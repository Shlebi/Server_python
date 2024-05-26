import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Конфигурация подключения к базе данных PostgreSQL из переменной окружения
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://myuser:mypassword@localhost:5432/mydatabase')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(50))
    material = db.Column(db.String(50))
    quantity = db.Column(db.String(50))

    def __init__(self, name, type, material, quantity):
        self.name = name
        self.type = type
        self.material = material
        self.quantity = quantity

# Попробуем создать все таблицы
with app.app_context():
    db.create_all()

@app.route('/add_tool', methods=['POST'])
def add_tool():
    name = request.form['name']
    type = request.form['type']
    material = request.form['material']
    quantity = request.form['quantity']
    tool = Tool(name, type, material, quantity)

    db.session.add(tool)
    db.session.commit()
    return {"session": "Tool added successfully"}

@app.route('/get_tool/<int:id>')
def get_tool(id):
    tool = Tool.query.get(id)
    if tool:
        return jsonify({
            'id': tool.id,
            'name': tool.name,
            'type': tool.type,
            'material': tool.material,
            'quantity': tool.quantity
        })
    else:
        return {'error': 'Tool not found'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
