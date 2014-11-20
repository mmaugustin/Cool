@app.route('/<int:value>')
def counter(value):
    values = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
    return "<body bgcolor='orange'><h1>Number %s</h1></body>"% values.get(value,'Unkown')
