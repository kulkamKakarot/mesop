import os

from flask import send_file
from werkzeug.security import safe_join

from optic.utils.runfiles import get_runfile_location

from .flags import port
from .server import app


def get_path(path: str):
  safe_path = safe_join("optic/optic/web/src/app/prod/web_package", path)
  assert safe_path
  return get_runfile_location(safe_path)


@app.route("/")
def serve_root():
  return send_file(get_path("index.html"))


@app.route("/<path:path>")
def serve_file(path: str):
  if is_file_path(path):
    return send_file(get_path(path))
  else:
    return send_file(get_path("index.html"))


def run():
  app.run(host="0.0.0.0", port=port(), use_reloader=False)


def is_file_path(path: str) -> bool:
  _, last_segment = os.path.split(path)
  return "." in last_segment


if __name__ == "__main__":
  run()
