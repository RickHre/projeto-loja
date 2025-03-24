import os
from app import create_app

# Verifica o caminho absoluto para o template base.html
print(os.path.abspath("app/templates/base.html"))

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)