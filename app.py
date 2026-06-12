from flask import Flask, request
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
api = Api(app, title="Student Credit Evaluation API", version="1.0")

class StudentResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pass_credits = db.Column(db.Integer, nullable=False)
    defer_credits = db.Column(db.Integer, nullable=False)
    fail_credits = db.Column(db.Integer, nullable=False)
    outcome = db.Column(db.String(50), nullable=False)

student_model = api.model("StudentResult", {
    "pass_credits": fields.Integer(required=True),
    "defer_credits": fields.Integer(required=True),
    "fail_credits": fields.Integer(required=True)
})

def evaluate_progression(pass_credits, defer_credits, fail_credits):
    total = pass_credits + defer_credits + fail_credits

    if total != 120:
        return "Invalid Total"

    if pass_credits == 120:
        return "Progress"
    elif pass_credits == 100:
        return "Progress - Module Trailer"
    elif fail_credits >= 80:
        return "Exclude"
    else:
        return "Do Not Progress - Module Retriever"

@api.route("/evaluate")
class EvaluateStudent(Resource):
    @api.expect(student_model)
    def post(self):
        data = request.json

        pass_credits = data["pass_credits"]
        defer_credits = data["defer_credits"]
        fail_credits = data["fail_credits"]

        outcome = evaluate_progression(pass_credits, defer_credits, fail_credits)

        result = StudentResult(
            pass_credits=pass_credits,
            defer_credits=defer_credits,
            fail_credits=fail_credits,
            outcome=outcome
        )

        db.session.add(result)
        db.session.commit()

        return {
            "pass_credits": pass_credits,
            "defer_credits": defer_credits,
            "fail_credits": fail_credits,
            "outcome": outcome
        }, 201

@api.route("/results")
class Results(Resource):
    def get(self):
        results = StudentResult.query.all()
        return [
            {
                "id": r.id,
                "pass_credits": r.pass_credits,
                "defer_credits": r.defer_credits,
                "fail_credits": r.fail_credits,
                "outcome": r.outcome
            }
            for r in results
        ]

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)