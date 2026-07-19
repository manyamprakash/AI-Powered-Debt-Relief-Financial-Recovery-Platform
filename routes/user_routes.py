from flask import Blueprint, request, jsonify
from database import db
from models import User


user_bp = Blueprint(
    "users",
    __name__
)


# CREATE USER
@user_bp.route("/users", methods=["POST"])
def create_user():

    data = request.json

    user = User(
        name=data["name"],
        email=data["email"],
        password=data["password"],
        phone=data.get("phone")
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully",
        "user": user.to_dict()
    }), 201



# GET ALL USERS
@user_bp.route("/users", methods=["GET"])
def get_users():

    users = User.query.all()

    return jsonify([
        user.to_dict()
        for user in users
    ])




# GET SINGLE USER
@user_bp.route("/users/<int:id>", methods=["GET"])
def get_user(id):

    user = User.query.get(id)

    if not user:
        return jsonify({
            "message":"User not found"
        }),404


    return jsonify(
        user.to_dict()
    )




# UPDATE USER
@user_bp.route("/users/<int:id>", methods=["PUT"])
def update_user(id):

    user = User.query.get(id)

    if not user:
        return jsonify({
            "message":"User not found"
        }),404


    data=request.json


    user.name=data.get(
        "name",
        user.name
    )

    user.phone=data.get(
        "phone",
        user.phone
    )


    db.session.commit()


    return jsonify({
        "message":"User updated successfully",
        "user":user.to_dict()
    })




# DELETE USER
@user_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):

    user=User.query.get(id)


    if not user:
        return jsonify({
            "message":"User not found"
        }),404


    db.session.delete(user)

    db.session.commit()


    return jsonify({
        "message":"User deleted successfully"
    })