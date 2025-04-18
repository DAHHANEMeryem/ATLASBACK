from flask import Blueprint, request, jsonify
from app.models.search_history import SearchHistory
from app.extensions import db

history_bp = Blueprint('history', __name__)

@history_bp.route('/<string:user_id>', methods=['GET'])
def get_history(user_id):
    try:
        # Version robuste avec vérifications
        if not hasattr(SearchHistory, 'query'):
            raise AttributeError("SearchHistory n'a pas d'attribut query")
        
        # Construction progressive de la requête
        query = db.session.query(SearchHistory)
        query = query.filter(SearchHistory.user_id == user_id)
        query = query.order_by(SearchHistory.created_at.desc())
        
        history = query.all()
        
        if not history:
            return jsonify({"message": "Aucun historique trouvé"}), 404
            
        history_data = [{
            "id": h.id,
            "query": h.query,
            "result": h.result,
            "createdAt": h.created_at.isoformat()  # Format ISO standard
        } for h in history]

        return jsonify({
            "userId": user_id,
            "count": len(history_data),
            "history": history_data
        })

    except Exception as e:
        print(f"Erreur critique: {str(e)}")
        return jsonify({
            "error": "Erreur serveur",
            "details": str(e)
        }), 500