from flask import Blueprint, render_template, request
from app.utils.game_logic import find_nash_equilibria

games_bp = Blueprint('games', __name__)

@games_bp.route('/solve-game', methods=['POST'])
def solve_game():
    payoff_matrix = request.json['payoff_matrix']
    equilibria = find_nash_equilibria(payoff_matrix)
    return {"equilibria": equilibria}