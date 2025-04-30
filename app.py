from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultat = None
    if request.method == 'POST':
        montant = float(request.form['montant'])
        source = request.form['source']
        cible = request.form['cible']

        taux_change = {
            ('EUR', 'DZD'): 145.0,
            ('DZD', 'EUR'): 1 / 145.0,
            ('USD', 'EUR'): 0.93,
            ('EUR', 'USD'): 1.08,
            ('USD', 'DZD'): 156.0,
            ('DZD', 'USD'): 1 / 156.0
        }

        if source == cible:
            resultat = f"Même devise choisie."
        elif (source, cible) in taux_change:
            resultat = f"{montant} {source} = {round(montant * taux_change[(source, cible)], 2)} {cible}"
        else:
            resultat = "Conversion non disponible."

    return render_template('index.html', resultat=resultat)

if __name__ == '__main__':
    app.run(debug=True)
