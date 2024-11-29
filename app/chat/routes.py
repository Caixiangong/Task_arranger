from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app import database
from app.models.user import Messages
chat_bp = Blueprint('chat', __name__, template_folder='../templates')

@chat_bp.route('/chat', methods=['GET', 'POST'])
def chat():
    #if request.method == 'POST':
    #    time_now = datetime.now()
    #    formatted_time = time_now.strftime("%Y-%m-%d %H:%M:%S")
    #    sendtime = datetime.strptime(formatted_time, '%Y-%m-%d %H:%M:%S')
    #    chat_text = request.form['chat_text']
    #    chat = Messages(sendtime=sendtime, 
    #                text=chat_text)
    #    database.session.add(chat)
    #    database.session.commit()
    #chats = Messages.query.all()
    #if(chats):
    #    return render_template('chat.html', chats)
    return render_template('chat.html')