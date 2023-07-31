from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

posts = []


@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(post), 200


@app.route('/posts', methods=['POST'])
def create_post():
    if not request.json or not 'title' in request.json or not 'content' in request.json or not 'author' in request.json:
        return jsonify({'error': 'Bad Request, missing mandatory parameters'}), 400
    
    post = {
        'id': posts[-1]['id'] + 1 if posts else 1,
        'title': request.json['title'],
        'content': request.json['content'],
        'author': request.json['author'],
        'time': datetime.datetime.now()
    }

    posts.append(post)
    return jsonify(post), 201


@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return jsonify({'error': 'Post is no longer available.'}), 404
    
    post['time'] = datetime.datetime.now()

    post.update(
        title=request.json.get('title', post['title']),
        content=request.json.get('content', post['content']),
        author=request.json.get('author', post['author'])
    )
    return jsonify(post), 200


@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global posts
    posts = [post for post in posts if post['id'] != post_id]
    return jsonify({'success': True}), 200


if __name__ == '__main__':
    app.run(debug=True)
