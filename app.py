from flask import Flask, send_from_directory, Response
import subprocess
import os

app = Flask(__name__, static_folder='public')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/run/<task>', methods=['POST'])
def run_task(task):
    mapping = {
        "NAPAS_IBFT": "NAPAS_IBFT.py",
        "task2": "ThongTinPhatHanhThe.py"
    }
    if task not in mapping:
        return "Task không tồn tại", 400
    # task_file = os.path.join(os.getcwdb, mapping[task])
    task_file =  os.path.join(os.path.join(os.getcwd(), "latest_code"), mapping[task])
    try:
        #Gọi file python bằng subprocess
        result = subprocess.check_output(["python", task_file], text=True, encoding="utf-8", errors="replace")
        return f"Kết quả {task}:\n{result}"
    except Exception as e:
        return 'Error: ' + str(e), 500
if __name__ == '__main__':
    app.run(port=5000, debug=True)
