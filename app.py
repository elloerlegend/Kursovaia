from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
import os
from flask import session


app = Flask(__name__)
db = SQLAlchemy()
# Подключаем SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///museum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ABC123'  # Используй уникальный ключ для безопасности

db = SQLAlchemy(app)

# Настроим Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Указываем страницу для перенаправления, если пользователь не авторизован

# Модели таблиц
class Hall(db.Model):  #Залы
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    exhibits = db.relationship('Exhibit', backref='hall', lazy=True)


class Exhibit(db.Model): #Добавляем экспонатов
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    species = db.Column(db.String(100))
    hall_id = db.Column(db.Integer, db.ForeignKey('hall.id'))


class Event(db.Model):  # Добавляем таблицу событий
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)  # Название события
    description = db.Column(db.String(200), nullable=False)  # Описание
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Дата события
    location = db.Column(db.String(100), nullable=False)  # Место проведения

    def __repr__(self):
        return f'<Event {self.title}>'



class User(db.Model, UserMixin):  # Добавляем UserMixin для Flask-Login
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

    # Обязательные методы для Flask-Login
    def is_active(self):
        return True  # Пользователь активен (если хотите добавить проверку, можно вернуть False для неактивных пользователей)

    def get_id(self):
        return str(self.id)  # Возвращает ID пользователя как строку

    def is_authenticated(self):
        return True  # Если пользователь аутентифицирован (можно изменить логику, если необходимо)

    def is_anonymous(self):
        return False  # Если пользователь не анонимный


# Модель для отзывов
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)  # Содержание отзыва
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)  # Связь с мероприятием
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Связь с пользователем

    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    event = db.relationship('Event', backref=db.backref('reviews', lazy=True))

    def __repr__(self):
        return f'<Review {self.content}>'

# Модель для истории посещений
class VisitHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)  # Связь с мероприятием
    date_visited = db.Column(db.DateTime, default=datetime.utcnow)  # Дата посещения

    user = db.relationship('User', backref=db.backref('visits', lazy=True))
    event = db.relationship('Event', backref=db.backref('visits', lazy=True))

    def __repr__(self):
        return f'<VisitHistory {self.date_visited}>'

# Инициализация базы данных
with app.app_context():
    db.create_all()


# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin/reviews')
def manage_reviews():
    # Получаем все отзывы из базы данных
    reviews = Review.query.all()  #
    return render_template('admin_panel.html', reviews=reviews)

@app.route('/admin')
@login_required
def admin_panel():
    # Проверяем, что пользователь — администратор
    if current_user.username != 'admin' or current_user.email != 'admin@gmail.com':
        abort(403)  # Запрещаем доступ, если это не администратор
    return render_template('admin_panel.html')


# Страница с экспонатами
@app.route('/exhibits')
def exhibits():
    exhibits = Exhibit.query.all()
    return render_template('exhibits.html', exhibits=exhibits)

@app.route('/delete_review/<int:review_id>', methods=['POST'])
def delete_review(review_id):
    # Логика для удаления отзыва из базы данных
    review = Review.query.get(review_id)
    if review:
        db.session.delete(review)
        db.session.commit()
    return redirect(url_for('manage_reviews'))  # После удаления перенаправляем на страницу управления отзывами

# Страница для добавления экспоната
@app.route('/add_exhibit', methods=['GET', 'POST'])
def add_exhibit():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        species = request.form['species']
        hall_id = request.form['hall_id']

        new_exhibit = Exhibit(name=name, description=description, species=species, hall_id=hall_id)
        db.session.add(new_exhibit)
        db.session.commit()
        return redirect(url_for('exhibits'))

    halls = Hall.query.all()
    return render_template('add_exhibit.html', halls=halls)


# Страница со списком мероприятий
@app.route('/events')
def events():
    events = Event.query.order_by(Event.date).all()  # Получаем все события
    return render_template('events.html', events=events)



# Страница добавления мероприятия
@app.route('/add_event', methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        date = datetime.strptime(request.form['date'], '%Y-%m-%dT%H:%M')
        location = request.form['location']

        new_event = Event(title=title, description=description, date=date, location=location)
        db.session.add(new_event)
        db.session.commit()
        return redirect(url_for('events'))

    return render_template('add_event.html')

# Оставить отзыв о мероприятии
@app.route('/add_review/<int:event_id>', methods=['POST'])
@login_required
def add_review(event_id):
    content = request.form['content']
    event = Event.query.get(event_id)

    # Создаем новый отзыв
    review = Review(content=content, event_id=event.id, user_id=current_user.id)
    db.session.add(review)
    db.session.commit()

    flash('Ваш отзыв был оставлен!', 'success')
    return redirect(url_for('profile'))

# Страница регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)  # Хешируем пароль

        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Регистрация прошла успешно!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')



# Страница входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Ищем пользователя по email
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):  # Проверка пароля
            login_user(user)  # Вход пользователя
            flash('Вы успешно вошли в систему!', 'success')
            return redirect(url_for('profile'))  # Перенаправление на профиль или главную страницу
        else:
            flash('Неверный email или пароль', 'danger')  # Ошибка при входе

    return render_template('login.html')

@app.route('/profile')
@login_required
def profile():
    # Получаем список экспонатов из базы данных
    exhibits = Exhibit.query.all()  # Проверка на модель

    # Получаем список событий и проверяем, записан ли пользователь
    events = Event.query.all()
    for event in events:
        event.is_registered = VisitHistory.query.filter_by(
            user_id=current_user.id,
            event_id=event.id
        ).first() is not None

    # Получаем историю посещений
    visit_history = VisitHistory.query.filter_by(user_id=current_user.id).all()

    # Передаем данные в шаблон
    return render_template(
        'profile.html',
        user=current_user,
        exhibits=exhibits,  # Проверка передачи модели
        events=events,
        visit_history=visit_history
    )


@app.route('/register_event/<int:event_id>', methods=['POST'])
@login_required
def register_event(event_id):
    event = Event.query.get(event_id)

    if not event:
        flash('Событие не найдено!', 'danger')
        return redirect(url_for('profile'))

    # Проверяем, не записан ли пользователь уже
    existing_registration = VisitHistory.query.filter_by(user_id=current_user.id, event_id=event_id).first()
    if existing_registration:
        flash('Вы уже записаны на это событие!', 'warning')
    else:
        # Добавляем запись в историю посещений
        new_visit = VisitHistory(user_id=current_user.id, event_id=event_id, date_visited=datetime.utcnow())
        db.session.add(new_visit)
        db.session.commit()
        flash('Вы успешно записались на событие!', 'success')

    return redirect(url_for('profile'))


# Страница выхода
@app.route('/logout')
def logout():
    logout_user()
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('index'))


# Инициализация текущего пользователя для Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
