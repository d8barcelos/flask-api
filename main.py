from flask import Flask, make_response, jsonify, request
from database import Carros

app = Flask(__name__)

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response (
        jsonify (
            message='Lista de carros',
            data=Carros
        )
    )

@app.route('/carros', methods=['POST'])
def create_car():
    car = request.json
    Carros.append(car)
    return make_response(
        jsonify(
            message='Carro cadastrado com sucesso!',
            car=car
        )
    )

@app.route('/carros/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    if car_id < len(Carros):
        deleted_car = Carros.pop(car_id)
        return make_response(
            jsonify(
                message='Carro removido com sucesso!',
                deleted_car=deleted_car
            )
        )
    else:
        return make_response(
            jsonify(
                message=f'Carro com ID {car_id} não encontrado!',
            ),
            404
        )

@app.route('/carros/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    if car_id < len(Carros):
        updated_car_data = request.json
        Carros[car_id].update(updated_car_data)
        return make_response(
            jsonify(
                message='Carro atualizado com sucesso!',
                updated_car=Carros[car_id]
            )
        )
    else:
        return make_response(
            jsonify(
                message=f'Carro com ID {car_id} não encontrado!',
            ),
            404
        ) 

app.run()

