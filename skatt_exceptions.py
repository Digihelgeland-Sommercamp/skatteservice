import werkzeug

class ItemNotFound(werkzeug.exceptions.HTTPException):
    code = 500
    description = "Item not found"