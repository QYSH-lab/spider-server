from flask import Flask, render_template

app = Flask(__name__)

# Главная страница
@app.route("/")
def home():
    return render_template("robot.html")

# Страница управления
@app.route("/control")
def control():
    return render_template("control.html")

# Обработка команд движения
@app.route("/move/<cmd>")
def move(cmd):
    # Пока просто печатаем команду в консоль
    print(f"Команда для робота: {cmd}")
    return f"Команда {cmd} получена"

if __name__ == "__main__":
    # host=0.0.0.0 чтобы был доступ с телефона
    app.run(host="0.0.0.0", port=5000)
