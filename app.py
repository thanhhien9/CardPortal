from flask import Flask, send_from_directory
import subprocess
import os
import sys

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
    if getattr(sys, 'frozen', False):
        LOCAL_DIR = os.path.dirname(sys.executable)
    else:
        LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))
    LOCAL_CODE_DIR = os.path.join(LOCAL_DIR, "lastest_code")
    task_file = os.path.join(LOCAL_CODE_DIR, mapping[task])

    try:
        #Gọi file python bằng subprocess
        # result = subprocess.check_output(["python", task_file], text=True, encoding="utf-8", errors="replace")
        result = subprocess.check_output([sys.executable, task_file], text=True, encoding="utf-8", errors="replace")

        return f"Kết quả {task}:\n{result}"
    except Exception as e:
        return 'Error: ' + str(e), 500
if __name__ == '__main__':
    # app.run(port=5000, debug=True)
    app.run(port=5000, debug=False, use_reloader=False)
