from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
next_id = 1


@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    global next_id

    task_name = request.form.get("task", "").strip()

    if task_name:
        tasks.append({
            "id": next_id,
            "name": task_name
        })
        next_id += 1

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    global tasks

    tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)