from flask import Blueprint, request, jsonify
from app.utils.openai_service import analyze_intent, generate_chat_response
from app.utils.email_service import send_email
from app.utils.weather_service import get_weather
from app.models.search_history import SearchHistory
from app.models.user import User
from app.extensions import db
from datetime import datetime

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    user_id = data.get('userId')

    if not user_message or not user_id:
        return jsonify({"error": "Message and userId are required"}), 400

    try:
        print("Analyzing intent...")
        analysis = analyze_intent(user_message)
        print(f"Intent analysis: {analysis}")

        action_response = {}
        ai_response = ''

        if analysis['action'] == 'send_email' and analysis['confidence'] > 0.7 and analysis['data'].get('to'):
            print("Sending email...")
            action_response = send_email(
                analysis['data'].get('to'),
                analysis['data'].get('subject', 'No Subject'),
                analysis['data'].get('body', 'No Content')
            )
            ai_response = (
                f"I've sent an email to {analysis['data'].get('to')} with subject \"{analysis['data'].get('subject', 'No Subject')}\"."
                if action_response['success']
                else f"I couldn't send the email: {action_response.get('error')}"
            )

        elif analysis['action'] == 'get_weather' and analysis['confidence'] > 0.7 and analysis['data'].get('location'):
            print("Getting weather...")
            action_response = get_weather(analysis['data'].get('location'))
            ai_response = (
                action_response['message']
                if action_response['success']
                else f"I couldn't get the weather for {analysis['data'].get('location')}: {action_response.get('error')}"
            )

        else:
            print("Generating chat response...")
            ai_response = generate_chat_response(user_message)

        print("Recording chat history...")

        # Vérification de l'utilisateur avec la bonne convention de nommage
        user = User.query.filter_by(user_id=user_id).first()  # Changé de userId à user_id
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Enregistrement avec la bonne convention de nommage
        new_history = SearchHistory(
            user_id=user_id,  # Changé de userId à user_id
            query=user_message,
            result=ai_response,
            created_at=datetime.utcnow()  # Ajout explicite du timestamp
        )
        
        db.session.add(new_history)
        db.session.commit()
        print(f"Chat history recorded for user {user_id}")

        return jsonify({
            "message": ai_response,
            "action": analysis['action'],
            "action_detail": action_response
        })

    except Exception as e:
        db.session.rollback()
        print(f"Error processing message: {str(e)}", exc_info=True)
        return jsonify({"error": f"Error processing your message: {str(e)}"}), 500