from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_study_plan(branch, goal, hours):
    plan = f"\n📚 Study Plan for {branch} student\n"
    plan += f"🎯 Goal: {goal}\n\n"

    if goal.lower() == "placement":
        plan += "Focus on:\n- DSA\n- Aptitude\n- Projects\n\n"
    elif goal.lower() == "higher studies":
        plan += "Focus on:\n- Core subjects\n- Research papers\n\n"
    else:
        plan += "Focus on:\n- Skill development\n\n"

    plan += f"⏱ Daily Plan ({hours} hrs/day):\n"
    plan += "- 40% Learning\n- 40% Practice\n- 20% Revision\n\n"

    plan += "💡 Suggested Resources:\n"
    plan += "- YouTube\n- Coursera\n- LeetCode\n"

    return plan

@app.route('/plan', methods=['POST'])
def plan():
    data = request.json
    result = generate_study_plan(data['branch'], data['goal'], data['hours'])
    return jsonify({"plan": result})

if __name__ == '__main__':
    app.run(debug=True)