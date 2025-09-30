from flask import Flask, render_template, request, jsonify
import os
from utils import subtitle, ocr
from pathlib import Path

app = Flask(__name__)
OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

# Global status
TASK_STATUS = {"state": "idle", "message": ""}
TASK_CANCELLED = False


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    global TASK_STATUS, TASK_CANCELLED
    TASK_CANCELLED = False
    TASK_STATUS = {"state": "running", "message": "Processing..."}

    save_path = request.form.get("save_path") or str(OUTPUT_DIR)
    os.makedirs(save_path, exist_ok=True)

    action = request.form.get("action")
    output_text = ""

    try:
        if TASK_CANCELLED:
            raise Exception("Task cancelled by user.")

        if action == "youtube":
            youtube_url = request.form.get("youtube_url")
            output_text = subtitle.transcribe_youtube(youtube_url, save_path)

        elif action == "upload_file":
            file = request.files.get("media_file")
            if file:
                file_path = os.path.join(save_path, file.filename)
                file.save(file_path)
                output_text = subtitle.transcribe_local(file_path, save_path)

        elif action == "ocr":
            file = request.files.get("image_file")
            if file:
                file_path = os.path.join(save_path, file.filename)
                file.save(file_path)
                output_text = ocr.extract_text(file_path, save_path)

        if TASK_CANCELLED:
            raise Exception("Task cancelled by user.")

        TASK_STATUS = {"state": "done", "message": "✅ Completed"}
        return jsonify({"success": True, "output": output_text})

    except Exception as e:
        if TASK_CANCELLED:
            TASK_STATUS = {"state": "cancelled", "message": "⛔ Cancelled"}
            return jsonify({"success": False, "error": "Cancelled by user"}), 400
        TASK_STATUS = {"state": "error", "message": f"❌ Error: {e}"}
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/cancel", methods=["POST"])
def cancel():
    global TASK_CANCELLED, TASK_STATUS
    TASK_CANCELLED = True
    TASK_STATUS = {"state": "cancelled", "message": "⛔ Cancelled"}
    return jsonify({"success": True})


@app.route("/status")
def status():
    return jsonify(TASK_STATUS)


if __name__ == "__main__":
    app.run(debug=True)







# from flask import Flask, render_template, request, jsonify
# import os
# from utils import subtitle, ocr
# from pathlib import Path

# app = Flask(__name__)
# OUTPUT_DIR = Path("output")
# OUTPUT_DIR.mkdir(exist_ok=True)

# # Global status
# TASK_STATUS = {"state": "idle", "message": ""}

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/process", methods=["POST"])
# def process():
#     global TASK_STATUS
#     TASK_STATUS = {"state": "running", "message": "Processing..."}
#     save_path = request.form.get("save_path") or str(OUTPUT_DIR)
#     os.makedirs(save_path, exist_ok=True)

#     action = request.form.get("action")
#     output_text = ""

#     try:
#         if action == "youtube":
#             youtube_url = request.form.get("youtube_url")
#             output_text = subtitle.transcribe_youtube(youtube_url, save_path)

#         elif action == "upload_file":
#             file = request.files.get("media_file")
#             if file:
#                 file_path = os.path.join(save_path, file.filename)
#                 file.save(file_path)
#                 output_text = subtitle.transcribe_local(file_path, save_path)

#         elif action == "ocr":
#             file = request.files.get("image_file")
#             if file:
#                 file_path = os.path.join(save_path, file.filename)
#                 file.save(file_path)
#                 output_text = ocr.extract_text(file_path, save_path)

#         TASK_STATUS = {"state": "done", "message": "✅ Completed"}
#         return jsonify({"success": True, "output": output_text})

#     except Exception as e:
#         TASK_STATUS = {"state": "error", "message": f"❌ Error: {e}"}
#         return jsonify({"success": False, "error": str(e)}), 500

# @app.route("/status")
# def status():
#     return jsonify(TASK_STATUS)


# if __name__ == "__main__":
#     app.run(debug=True)















# from flask import Flask, render_template, request, redirect, url_for
# import os
# from utils import subtitle, ocr

# app = Flask(__name__)
# OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")

# @app.route("/", methods=["GET", "POST"])
# def index():
#     output_text = ""
#     if request.method == "POST":
#         action = request.form.get("action")
#         save_path = request.form.get("save_path") or OUTPUT_DIR

#         os.makedirs(save_path, exist_ok=True)

#         if action == "youtube":
#             youtube_url = request.form.get("youtube_url")
#             output_text = subtitle.transcribe_youtube(youtube_url, save_path)

#         elif action == "upload_file":
#             file = request.files.get("media_file")
#             if file:
#                 file_path = os.path.join(OUTPUT_DIR, file.filename)
#                 file.save(file_path)
#                 output_text = subtitle.transcribe_local(file_path, save_path)

#         elif action == "ocr":
#             file = request.files.get("image_file")
#             if file:
#                 file_path = os.path.join(OUTPUT_DIR, file.filename)
#                 file.save(file_path)
#                 output_text = ocr.extract_text(file_path, save_path)

#     return render_template("index.html", output_text=output_text)


# if __name__ == "__main__":
#     app.run(debug=True)
