from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route("/",methods=["GET"])
def home():
    with open("todo.csv",encoding="utf-8") as csv_file:
        todos = csv_file.read().split("\n")
        if "" in todos:
            todos.remove("")
    return render_template("index.html",todos=todos)

@app.route("/add" ,methods=['GET',"POST"])
def add_task():
    new_task = request.form["new_task"]
    with open("todo.csv","a",encoding="UTF-8") as csv_file:
            csv_file.write(f"\n{new_task}")
    return redirect( url_for("home"))

@app.route("/delete/<task_title>" ,methods=["GET","DELETE"])
def delete(task_title):
    with open("todo.csv",encoding="utf-8") as csv_file:
        all_tasks = csv_file.read().split("\n")
    if task_title in all_tasks or "" in all_tasks:
        all_tasks.remove(task_title)
        if "" in all_tasks:
            all_tasks.remove("")
        with open("todo.csv","w",newline= "", encoding="utf-8") as csv_file:
            for task in all_tasks:
                csv_file.writelines(f"{task}\n")
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)