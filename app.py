from flask import Flask, jsonify, request

app = Flask(__name__)

players_name = [
    {"Bat_on_position": 1, "name": "Rohit Sharma", "Jersey_no": 45, "nick_Name": "Hitman"},
    {"Bat_on_position": 2, "name": "Shubhman Gill", "Jersey_no": 45, "nick_Name": "Prince"},
    {"Bat_on_position": 3, "name": "Virat Kohli", "Jersey_no": 18, "nick_Name": "Chase Master"},
    {"Bat_on_position": 4, "name": "Shreyas Iyer", "Jersey_no": 41, "nick_Name": "Shreshth Iyer"},
    {"Bat_on_position": 5, "name": "KL Rahul", "Jersey_no": 1, "nick_Name": "Kllasic Rahul"},
    {"Bat_on_position": 6, "name": "Hardik Pandya ", "Jersey_no": 33, "nick_Name": "Kungfu Pandya"},
    {"Bat_on_position": 7, "name": "Ravindra Jadeja", "Jersey_no": 8, "nick_Name": "Sir Jadeja"},
    {"Bat_on_position": 8, "name": "Kuldeep Yadav", "Jersey_no": 23, "nick_Name": "China Man"},
    {"Bat_on_position": 9, "name": "Jasprit Bumrah", "Jersey_no": 93, "nick_Name": "Boom Boom"},
    {"Bat_on_position": 10, "name": "Mohammad Shami", "Jersey_no": 11, "nick_Name": "Sensational Shami"},
    {"Bat_on_position": 11, "name": "Mohammad Siraj", "Jersey_no": 73, "nick_Name": "Miya Bhai"},
]

# For get detail of all player in squad
@app.route('/players', methods=['GET'])
def get_players():
    return jsonify(players_name)

# To get a detail of specific player
@app.route('/player/<int:player_batting_position>', methods=(['GET']))
def get_player(player_batting_position):
    for player in players_name:
        if player['Bat_on_position'] == player_batting_position:
            return jsonify(player)
    return jsonify({'error': 'player position is invalid'})

# Join a player in squad
@app.route('/player_add', methods=['POST'])
def join_player():
    new_player = {'Bat_on_position': len(players_name) + 1, 'name': request.json['name'],
                  'Jersey_no': request.json['Jersey_no'], 'nick_Name': request.json['nick_Name']}
    players_name.append(new_player)
    return jsonify(new_player)

# Change the squad
@app.route('/player_change/<int:player_batting_position>', methods=(['PUT']))
def change_squad(player_batting_position):
    for player in players_name:
        if player['Bat_on_position'] == player_batting_position:
            player['name'] = request.json['name']
            player['Jersey_no'] = request.json['Jersey_no']
            player['nick_Name'] = request.json['nick_Name']
            return jsonify(player)
    return jsonify({'error': 'player position is invalid'})

# Remove the player from squad
@app.route('/player_remove/<int:player_batting_position>', methods=(['DELETE']))
def delete_player(player_batting_position):
    for player in players_name:
        if player['Bat_on_position'] == player_batting_position:
            players_name.remove(player)
            return jsonify({'data': 'player was removed from squad successfully'})
    return jsonify({'error': 'player position is invalid'})

if __name__ == '__main__':
    app.run(debug=True)

 