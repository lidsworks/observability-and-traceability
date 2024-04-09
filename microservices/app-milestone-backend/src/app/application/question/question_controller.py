from venv import logger
from flask import Blueprint, jsonify
from app.domain.question.question_repository import QuestionRepository
from app.application.question.question_service import generative_ai_question
import json
from datetime import datetime
import random
import time

question_bp = Blueprint('question', __name__)


def str_time_prop(start, end, time_format, prop):
    """
    Calcula un tiempo basado en una proporción de un rango de tiempo especificado.

    Parámetros:
    start (str): La hora de inicio en el formato especificado.
    end (str): La hora de finalización en el formato especificado.
    time_format (str): El formato de las horas de entrada.
    prop (float): La proporción de tiempo entre el inicio y el fin para calcular.

    Retorna:
    str: El tiempo calculado basado en la proporción del rango de tiempo.
    """
    start_time = time.mktime(time.strptime(start, time_format))
    end_time = time.mktime(time.strptime(end, time_format))

    prop_time = start_time + prop * (end_time - start_time)

    return time.strftime(time_format, time.localtime(prop_time))

@question_bp.route('/questions', methods=['GET'])
def list_questions():
    """
    A route that lists questions using the question repository and returns them as JSON.
    """
    # Obtener preguntas de la base de datos
    questions = QuestionRepository.list_questions()
    return jsonify(questions)

@question_bp.route('/question/<question_date>', methods=['GET'])
def get_question(question_date):
    """
    Route to get a question by specific date.
    
    Args:
        question_date (str): The date of the question in the format dd-mm-yyyy.
        
    Returns:
        JSON: A JSON object containing the question details.
    """
    try:
        datetime.strptime(question_date, '%d-%m-%Y')
    except ValueError:
        logger.error('La fecha debe tener el formato dd-mm-yyyy')
        return jsonify({'error': 'La fecha debe tener el formato dd-mm-yyyy'}), 400

    try:
        respuesta = json.loads(generative_ai_question(question_date=question_date))
    except Exception as e:
        logger.error(f'Error al procesar el json de la pregunta: {e}')
        return jsonify({'error': 'Error al procesar el json de la pregunta'}), 500

    try:
        # Guardar la pregunta en la base de datos
        QuestionRepository.create_question(
            fecha=respuesta['fecha'],
            titular=respuesta['titular'],
            hecho=respuesta['hecho'],
            tipo=respuesta['tipo'],
            tags=str(respuesta['tags'])
        )
    except Exception as e:
        logger.error(f'Error al guardar la pregunta en la base de datos: {e}')

    return jsonify(respuesta)


@question_bp.route('/question/generate/random', methods=['GET'])
@question_bp.route('/question/generate/random/<int:number>', methods=['GET'])
def random_generate(number=1):
    """
    Route to generate a random question.

    Returns:
        JSON: A JSON object containing the question details.
    """
    questions = []
    retorno = None

    for i in range(number):
        # Generar una fecha aleatoria
        random_date = str_time_prop(
            "01-01-1900", "31-12-2023", '%d-%m-%Y', random.random())

        # Obtener una pregunta aleatoria
        try:
            questions.append(json.loads(generative_ai_question(
                question_date=random_date)))
        except Exception as e:
            logger.error(f'Error al procesar el json de la pregunta: {e}')

    # Guardar las preguntas en la base de datos
    try:
        logger.debug(f'Guardando las pregunta en la base de datos...')
        retorno = QuestionRepository.create_questions(questions)
    except Exception as e:
        logger.error(f'Error al guardar la pregunta en la base de datos: {e}')
    
    return jsonify({
        'openia': questions,
        'count_openia': len(questions),
        'message': 'Preguntas generadas con exito'
    }), 200


@question_bp.route('/question/random', methods=['GET'])
def get_random_question():
    """
    Route to get a random question from the database.
    """
    return jsonify(QuestionRepository.get_random_question())
