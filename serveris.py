from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
  return "Labrīt!"
@app.route('/sveiki')
def sveiki():
  return "Nav vairs nekāds rīts!"
@app.route('/sveiki/<vards>')
def sveikiPersona(vards):
  return f"Sveiki {vards}"
@app.route('/cik/<sk1>/<sk2>')
def reizinajums(sk1, sk2):
  return str(int(sk1)*int(sk2))

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
