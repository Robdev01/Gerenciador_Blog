from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados fictícios para simular um banco de dados de posts
posts = []


# Página inicial do blog - lista de posts
@app.route('/')
def index():
    return render_template('index.html', posts=posts)


# Página para visualizar um post específico
@app.route('/post/<int:id>')
def ver_post(id):
    post = next((post for post in posts if post['id'] == id), None)
    if post:
        return render_template('post.html', post=post)
    return 'Post não encontrado', 404


# Página para criar um novo post
@app.route('/criar_post', methods=['GET', 'POST'])
def criar_post():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo']
        novo_post = {"id": len(posts) + 1, "titulo": titulo, "conteudo": conteudo}
        posts.append(novo_post)
        return redirect(url_for('index'))
    return render_template('criar_post.html')


# Página para editar um post existente
@app.route('/editar_post/<int:id>', methods=['GET', 'POST'])
def editar_post(id):
    post = next((post for post in posts if post['id'] == id), None)
    if request.method == 'POST':
        post['titulo'] = request.form['titulo']
        post['conteudo'] = request.form['conteudo']
        return redirect(url_for('index'))
    return render_template('editar_post.html', post=post)


# Rota para excluir um post
@app.route('/excluir_post/<int:id>')
def excluir_post(id):
    global posts
    posts = [post for post in posts if post['id'] != id]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
