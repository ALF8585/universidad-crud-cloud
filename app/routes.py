from flask import Blueprint, render_template_string
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template_string("<h1>¡Universidad CRUD Cloud funcionando!</h1>")