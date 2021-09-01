from db import db

def get_room(room_id):
    try:
        result = db.session.execute(
            "SELECT * FROM rooms WHERE id=:id",
            { "id": room_id }
        )
        return result.fetchone()
    except:
        return None

def get_public_rooms():
    result = db.session.execute("SELECT * FROM rooms")
    return result.fetchall()

def get_rooms_by_user(user_id):
    result = db.session.execute(
        "SELECT * FROM rooms WHERE user_id=:user_id",
        { "user_id": user_id }
    )
    return result.fetchall()

def add_admin(user_id, room_id):
    try:
        db.session.execute(
            "INSERT INTO room_admins (user_id, room_id) "
            + "VALUES (:user_id, :room_id)",
            {
                "user_id": user_id,
                "room_id": room_id
            }
        )
        db.session.commit()
        return True
    except:
        return False

def create_room(name, description, user_id):
    try:
        db.session.execute(
            "INSERT INTO rooms (name, description, created_at, user_id) "
            + "VALUES (:name, :description, NOW(), :user_id)",
            {
                "name": name,
                "description": description,
                "user_id": user_id,
            }
        )
        db.session.commit()
    except:
        return False
    return True

def delete_room(room_id):
    try:
        db.session.execute(
            "DELETE FROM rooms WHERE id=:room_id",
            { "room_id": room_id }
        )
        db.session.commit()
        return True
    except:
        return False
