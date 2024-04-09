from app.domain.question.question_model import Question
from app import db
from venv import logger
from sqlalchemy import func, desc, and_, text
from datetime import datetime
from app.infraestructure.system_logs import Logs


class QuestionRepository:
    @staticmethod
    def list_questions():
        return Question.query.all()

    @staticmethod
    def create_question(fecha, titular, hecho, tipo, tags):
        fecha_normalizada = datetime.strptime(fecha, '%d-%m-%Y').date(),

        question = Question(fecha_normalizada, titular, hecho, tipo, tags)
        db.session.add(question)
        db.session.commit()

        return question

    @staticmethod
    def create_questions(questions):
        logger.info(f'Creando {len(questions)} preguntas...')

        questions_to_add = []
        
        for question in questions:
            questions_to_add.append(Question(
                datetime.strptime(question['fecha'], '%d-%m-%Y').date(),
                question['titular'],
                question['hecho'],
                question['tipo'],
                question['tags']
            ))

        try:
            db.session.add_all(questions_to_add)
            db.session.commit()
        except Exception as e:
            logger.error(f'Error al insertar algunas preguntas: {e}')
            db.session.rollback()
            questions_to_add = [q for q in questions_to_add if q not in db.session]
            db.session.add_all(questions_to_add)
            db.session.commit()
        return questions_to_add

    @staticmethod
    def list_question_by_fecha(fecha):
        return Question.query \
            .filter_by(fecha=fecha) \
            .order_by(Question.start.desc()) \
            .first()
    
    @staticmethod
    def get_random_question():
        return db.session.query(Question).order_by(func.random()).first()

    @staticmethod
    def list_fechas():
        return db.session.query(Question.fecha).distinct().all()

    @staticmethod
    def list_questions_test(fecha):
        query = text(f"""
            SELECT * FROM question
            WHERE fecha IN :fecha
            ORDER BY fecha DESC
        """)

        result = db.engine.execute(query, fecha=fecha)
        rows = result.fetchall()
        return [Question(*row) for row in rows]
