from backend.app import create_app

app = create_app()


if __name__ == "__main__":
    if not app.config.get("SECRET_KEY"):
        raise RuntimeError("Set FLASK_SECRET_KEY in the environment before starting the server.")
    app.run(host="127.0.0.1", port=5000, debug=False)
