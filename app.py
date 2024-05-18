from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from datetime import datetime
import json
import random
import re

# --------------------------------------- CLAN ---------------------------------------!
with open('clanpass.txt', 'r') as file:
    passwords = json.load(file)
# -----------------------FOREVER--------------!
SCRIPTIEZ_LEADER = passwords['forever']
def update_leader_password(new_password):
    try:
        with open('clanpass.txt', 'r+') as file:
            data = json.load(file)
            data['forever'] = new_password
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    except Exception as e:
        print("An error occurred while updating the leader password:", e)
# -----------------------FOREVER-END-------------!
# -----------------------AUTOMOTIVE--------------!
AUTO_LEADER = passwords['auto']
def update_leader_password(new_password):
    try:
        with open('clanpass.txt', 'r+') as file:
            data = json.load(file)
            data['auto'] = new_password
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()
    except Exception as e:
        print("An error occurred while updating the leader password:", e)
# -----------------------AUTOMOTIVE-END-------------!

# -----------------------------------------------------------------------------------------!

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

clans = {}
groups = {}
clan_messages = {}
group_messages = {}
messages = []
scriptiez_messages= []
auto_messages= []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)
@app.route('/changelog')
def changelog():
    return render_template('changelog.html')
@app.route('/donation')
def donation():
    mail = 'mailto:scriptiez.in@gmail.com'
    return render_template('donation.html', mail=mail)
@app.route('/clan')
def clan():
    return render_template('clan.html',clans=clans)
@app.route('/game')
def game():
    return render_template('game.html')
@app.route('/snake')
def snake():
    return render_template('snake.html')
@app.route('/car')
def car():
    return render_template('car.html')
@app.route('/flappy')
def flappy():
    return render_template('flappy.html')
@app.route('/chess')
def chess():
    return render_template('chess.html')
@app.route('/cricket')
def cricket():
    return render_template('cricket.html')

#----------------------------------------IMAGE SYSTEM---------------------------------------!
def fetch_meme():
    try:
        # Generate a random key between 0 and 3859
        random_key = random.randint(0, 4999)

        # Read the dictionary from the file
        with open('data/meme.txt', 'r') as file:
            meme_urls = eval(file.read())

        # Get the URL corresponding to the random key
        meme_url = meme_urls.get(random_key)

        return meme_url
        
    except (IOError, SyntaxError) as e:
        print("Error reading meme file:", e)
        return None
    
def fetch_funny():
    try:
        # Generate a random key between 0 and 3859
        random_key = random.randint(0, 4999)

        # Read the dictionary from the file
        with open('data/funny.txt', 'r') as file:
            funny_urls = eval(file.read())

        # Get the URL corresponding to the random key
        funny_url = funny_urls.get(random_key)

        return funny_url
        
    except (IOError, SyntaxError) as e:
        print("Error reading meme file:", e)
        return None
    
def fetch_earth():
    try:
        # Generate a random key between 0 and 3859
        random_key = random.randint(0, 4999)

        # Read the dictionary from the file
        with open('data/earth.txt', 'r') as file:
            earth_urls = eval(file.read())

        # Get the URL corresponding to the random key
        earth_url = earth_urls.get(random_key)

        return earth_url
        
    except (IOError, SyntaxError) as e:
        print("Error reading meme file:", e)
        return None
    
def fetch_q():
    try:
        # Generate a random key between 0 and 3859
        random_key = random.randint(0, 4999)

        # Read the dictionary from the file
        with open('data/quotes.txt', 'r') as file:
            q_urls = eval(file.read())

        # Get the URL corresponding to the random key
        q_url = q_urls.get(random_key)

        return q_url
        
    except (IOError, SyntaxError) as e:
        print("Error reading meme file:", e)
        return None
    
def fetch_space():
    try:
        # Generate a random key between 0 and 3859
        random_key = random.randint(0, 4999)

        # Read the dictionary from the file
        with open('data/space.txt', 'r') as file:
            space_urls = eval(file.read())

        # Get the URL corresponding to the random key
        space_url = space_urls.get(random_key)

        return space_url
        
    except (IOError, SyntaxError) as e:
        print("Error reading meme file:", e)
        return None
    
def fetch_fa():
    try:
        # Generate a random key between 0 and 3859
        random_key = random.randint(0, 4999)

        # Read the dictionary from the file
        with open('data/cats.txt', 'r') as file:
            fa_urls = eval(file.read())

        # Get the URL corresponding to the random key
        fa_url = fa_urls.get(random_key)

        return fa_url
        
    except (IOError, SyntaxError) as e:
        print("Error reading meme file:", e)
        return None

def fetch_dog():
    try:
        # Generate a random key between 0 and 3859
        random_key = random.randint(0, 4999)

        # Read the dictionary from the file
        with open('data/dog.txt', 'r') as file:
            dog_urls = eval(file.read())

        # Get the URL corresponding to the random key
        dog_url = dog_urls.get(random_key)

        return dog_url
        
    except (IOError, SyntaxError) as e:
        print("Error reading meme file:", e)
        return None

def fetch_na():
    try:
        # Generate a random key between 0 and 3859
        random_key = random.randint(0, 4999)

        # Read the dictionary from the file
        with open('data/anime.txt', 'r') as file:
            na_urls = eval(file.read())

        # Get the URL corresponding to the random key
        na_url = na_urls.get(random_key)

        return na_url
        
    except (IOError, SyntaxError) as e:
        print("Error reading meme file:", e)
        return None


@app.route('/image')                                                   #----------------------IMAGE INDEX-----------!
def image():
    static_image_url = url_for('static', filename='clicknext.jpg')
    return render_template('image.html', meme_url=static_image_url, funny_url=static_image_url, earth_url=static_image_url, q_url=static_image_url, space_url=static_image_url, fa_url=static_image_url, dog_url=static_image_url, na_url=static_image_url)

@app.route('/new_meme')
def new_meme():
    meme_url = fetch_meme()
    if meme_url:
        return jsonify({'meme_url': meme_url})
    else:
        return jsonify({'error': 'Failed to fetch meme'}) 

@app.route('/new_funny')
def new_funny():
    funny_url = fetch_funny()
    if funny_url:
        return jsonify({'funny_url': funny_url})
    else:
        return jsonify({'error': 'Failed to fetch meme'}) 
    
@app.route('/new_earth')
def new_earth():
    earth_url = fetch_earth()
    if earth_url:
        return jsonify({'earth_url': earth_url})
    else:
        return jsonify({'error': 'Failed to fetch meme'}) 
    
@app.route('/new_q')
def new_q():
    q_url = fetch_q()
    if q_url:
        return jsonify({'q_url': q_url})
    else:
        return jsonify({'error': 'Failed to fetch meme'}) 
    
@app.route('/new_space')
def new_space():
    space_url = fetch_space()
    if space_url:
        return jsonify({'space_url': space_url})
    else:
        return jsonify({'error': 'Failed to fetch meme'}) 
    
@app.route('/new_fa')
def new_fa():
    fa_url = fetch_fa()
    if fa_url:
        return jsonify({'fa_url': fa_url})
    else:
        return jsonify({'error': 'Failed to fetch meme'}) 
    
@app.route('/new_dog')
def new_dog():
    dog_url = fetch_dog()
    if dog_url:
        return jsonify({'dog_url': dog_url})
    else:
        return jsonify({'error': 'Failed to fetch meme'}) 
    
@app.route('/new_na')
def new_na():
    na_url = fetch_na()
    if na_url:
        return jsonify({'na_url': na_url})
    else:
        return jsonify({'error': 'Failed to fetch meme'}) 
#----------------------------------------IMAGE-END------------------------------------------!


# -------------------------------------------- SCRIPTIEZ clan----------------------------------!
@app.route('/clanscriptiez')
def clanscriptiez():
    return render_template('clanscriptiez.html')

@app.route('/scriptiez', methods=['POST'])
def scriptiezlogin():
    password = request.form['password']
    if password == SCRIPTIEZ_LEADER:
        session['scriptiez_user_type'] = 'Leader'
        return redirect('/scriptiez')
    else:
        session['scriptiez_user_type'] = 'Anonymous'
        return redirect('/scriptiez')

@app.route('/scriptiez')
def scriptiezclan():
    scriptiez_user_type = session['scriptiez_user_type']
    if scriptiez_user_type == 'Leader':
        heading = 'Welcome Leader!'
        command = 'Change_Password: /leader CURRENT_PASSWORD NEW_PASSWORD'
    elif scriptiez_user_type == 'Anonymous':
        heading = 'Welcome to "Forever"'
        command = ''
    return render_template('scriptiez.html', heading=heading, scriptiez_messages=scriptiez_messages, command=command)

@app.route('/scriptiez_send_message', methods=['POST'])
def scriptiez_send_message():
    global SCRIPTIEZ_LEADER
    scriptiez_message = request.form['scriptiez_message']
    scriptiez_nam = scriptiez_message.split()
    scriptiez_user_type = session['scriptiez_user_type']
    if len(scriptiez_nam) > 0 and scriptiez_nam[0].lower().startswith("/clearall"):
        if scriptiez_user_type == 'Leader':
            # Clear all messages
            scriptiez_messages.clear()
        else:
            # Only the leader can clear all messages
            scriptiez_messages.append(('System', 'Only the leader can clear all messages.', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return redirect(url_for('scriptiezclan'))
    elif len(scriptiez_nam) > 0 and scriptiez_nam[0].lower().startswith("/p"):
        # Construct the HTML tag for the image
        scriptiez_message = f'<img src="{scriptiez_nam[1]}" style="max-width: 100%; height: auto;">'
        # Append the image tag to the group's message list
        scriptiez_name = session['scriptiez_user_type']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        scriptiez_messages.append((scriptiez_name, scriptiez_message, timestamp))
        return redirect(url_for('scriptiezclan'))
    elif len(scriptiez_nam) > 0 and scriptiez_nam[0].lower().startswith("/v"):
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com/shorts/|youtu\.?be/|youtube\.com/embed/)?([a-zA-Z0-9_-]{11})'
        youtube_link = re.search(youtube_regex, scriptiez_message[3:])
        if youtube_link:
            video_id = youtube_link.group(4)
            video_embed_tag = f'<iframe width="100%;" height="100%;" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
            # Set the message to the embedded video HTML tag
            scriptiez_message = video_embed_tag
        else:
            # If the message does not contain a valid YouTube link, display an error message
            scriptiez_message = 'Invalid YouTube link format.'

        # Set the sender name to Anonymous for video messages
        scriptiez_name = session['scriptiez_user_type']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        scriptiez_messages.append((scriptiez_name, scriptiez_message, timestamp))
        return redirect(url_for('scriptiezclan'))
    elif scriptiez_user_type == 'Leader':
        if len(scriptiez_nam) > 0 and scriptiez_nam[0].lower().startswith("/leader"):
            command_parts = scriptiez_nam
            if len(command_parts) == 3 and command_parts[1] == SCRIPTIEZ_LEADER:
                new_password = command_parts[2]
                update_leader_password(new_password)
                scriptiez_name = ''
                scriptiez_message = ''
                timestamp = ''
                with open('clanpass.txt', 'r') as file:
                    passwords = json.load(file)
                SCRIPTIEZ_LEADER = passwords['forever']
                scriptiez_messages.append((scriptiez_name, scriptiez_message, timestamp))
                return redirect(url_for('scriptiezclan'))
        elif len(scriptiez_nam) > 0 and scriptiez_nam[0].lower().startswith("/"):
            scriptiez_name = scriptiez_nam[0].replace('/','')
            scriptiez_message = scriptiez_message.replace(scriptiez_nam[0], '')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            scriptiez_messages.append((scriptiez_name, scriptiez_message, timestamp))
            return redirect(url_for('scriptiezclan'))
        else:
            scriptiez_name = 'Leader '
            scriptiez_message = scriptiez_message
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            scriptiez_messages.append((scriptiez_name, scriptiez_message, timestamp))
            return redirect(url_for('scriptiezclan'))

    else:
        if len(scriptiez_nam) > 0 and "/ADMINpassword123".lower() in scriptiez_nam[0].lower():
            scriptiez_name = 'ADMIN@admin: '
            scriptiez_message = scriptiez_message.replace(scriptiez_nam[0], '')
        elif len(scriptiez_nam) > 0 and scriptiez_nam[0].lower().startswith("/scriptiez"):
            scriptiez_name = 'Anonymous: '
            scriptiez_message = scriptiez_message.replace(scriptiez_nam[0], '')
        elif len(scriptiez_nam) > 0 and scriptiez_nam[0].lower().startswith("/leader"):
            scriptiez_name = 'Anonymous: '
            scriptiez_message = scriptiez_message.replace(scriptiez_nam[0], '')
        elif len(scriptiez_nam) > 0 and "@admin" in scriptiez_nam[0]:
            # Handle variations of '@admin' command
            scriptiez_name = 'Anonymous: '
            scriptiez_message = scriptiez_message.replace(scriptiez_nam[0], '')
        elif len(scriptiez_nam) > 0 and "@" in scriptiez_nam[0]:
            # Handle variations of '@' command
            scriptiez_name = 'Anonymous: '
            scriptiez_message = scriptiez_message.replace(scriptiez_nam[0], '')
        elif len(scriptiez_nam) > 0 and scriptiez_nam[0].startswith("/"):
            scriptiez_name = scriptiez_nam[0][1:] + ': '
            scriptiez_message = scriptiez_message.replace(scriptiez_nam[0], '')
        else:
            scriptiez_name = 'Anonymous: '
    
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        scriptiez_messages.append((scriptiez_name, scriptiez_message, timestamp))
        return redirect(url_for('scriptiezclan'))

# -----------------------------------------------------SCRIPTIEZ END ------------------------------------!

# -------------------------------------------- AUTOMOTIVE clan----------------------------------!
@app.route('/clanauto')
def clanauto():
    return render_template('clanauto.html')

@app.route('/auto', methods=['POST'])
def autologin():
    password = request.form['password']
    if password == AUTO_LEADER:
        session['auto_user_type'] = 'Leader'
        return redirect('/auto')
    else:
        session['auto_user_type'] = 'Anonymous'
        return redirect('/auto')

@app.route('/auto')
def autoclan():
    auto_user_type = session['auto_user_type']
    if auto_user_type == 'Leader':
        heading = 'Welcome Leader!'
        command = 'Change_Password: /leader CURRENT_PASSWORD NEW_PASSWORD'
    elif auto_user_type == 'Anonymous':
        heading = 'Welcome to "Automotive"'
        command = ''
    return render_template('auto.html', heading=heading, auto_messages=auto_messages, command=command)

@app.route('/auto_send_message', methods=['POST'])
def auto_send_message():
    global AUTO_LEADER
    auto_message = request.form['auto_message']
    auto_nam = auto_message.split()
    auto_user_type = session['auto_user_type']
    if len(auto_nam) > 0 and auto_nam[0].lower().startswith("/clearall"):
        if auto_user_type == 'Leader':
            # Clear all messages
            auto_messages.clear()
        else:
            # Only the leader can clear all messages
            auto_messages.append(('System', 'Only the leader can clear all messages.', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return redirect(url_for('autoclan'))
    if len(auto_nam) > 0 and auto_nam[0].lower().startswith("/p"):
        # Construct the HTML tag for the image
        auto_message = f'<img src="{auto_nam[1]}" style="max-width: 100%; height: auto;">'
        # Append the image tag to the group's message list
        auto_name = session['auto_user_type']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        auto_messages.append((auto_name, auto_message, timestamp))
        return redirect(url_for('autoclan'))
    elif len(auto_nam) > 0 and auto_nam[0].lower().startswith("/v"):
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com/shorts/|youtu\.?be/|youtube\.com/embed/)?([a-zA-Z0-9_-]{11})'
        youtube_link = re.search(youtube_regex, auto_message[3:])
        if youtube_link:
            video_id = youtube_link.group(4)
            video_embed_tag = f'<iframe width="100%;" height="100%;" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
            # Set the message to the embedded video HTML tag
            auto_message = video_embed_tag
        else:
            # If the message does not contain a valid YouTube link, display an error message
            auto_message = 'Invalid YouTube link format.'

        auto_name = session['auto_user_type']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        auto_messages.append((auto_name, auto_message, timestamp))
        return redirect(url_for('autoclan'))
    elif auto_user_type == 'Leader':
        if auto_message.startswith('/p '):
            # Extract the image URL from the message
            img_url = re.search(r'\bhttps?://\S+\b', auto_message[3:])
            if img_url:
                # If a valid URL is found, construct the HTML code to display the image
                auto_message = f'<img src="{img_url.group()}" style="max-width: 100%; height: auto;">'
            else:
                # If no valid URL is found, display an error message
                auto_message = 'Invalid image URL format.'
    
            # Set the sender name to Anonymous for image messages
            auto_name = 'Leader '
        if len(auto_nam) > 0 and auto_nam[0].lower().startswith("/leader"):
            command_parts = auto_nam
            if len(command_parts) == 3 and command_parts[1] == AUTO_LEADER:
                new_password = command_parts[2]
                update_leader_password(new_password)
                auto_name = ''
                auto_message = ''
                timestamp = ''
                with open('clanpass.txt', 'r') as file:
                    passwords = json.load(file)
                AUTO_LEADER = passwords['auto']
                auto_messages.append((auto_name, auto_message, timestamp))
                return redirect(url_for('autoclan'))
        elif len(auto_nam) > 0 and auto_nam[0].lower().startswith("/"):
            auto_name = auto_nam[0].replace('/','')
            auto_message = auto_message.replace(auto_nam[0], '')
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            auto_messages.append((auto_name, auto_message, timestamp))
            return redirect(url_for('autoclan'))
        else:
            auto_name = 'Leader '
            auto_message = auto_message
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            auto_messages.append((auto_name, auto_message, timestamp))
            return redirect(url_for('autoclan'))

    else:
        if auto_message.startswith('/p '):
            # Extract the image URL from the message
            img_url = re.search(r'\bhttps?://\S+\b', auto_message[3:])
            if img_url:
                # If a valid URL is found, construct the HTML code to display the image
                auto_message = f'<img src="{img_url.group()}" style="max-width: 100%; height: auto;">'
            else:
                # If no valid URL is found, display an error message
                auto_message = 'Invalid image URL format.'
    
            # Set the sender name to Anonymous for image messages
            auto_name = 'Anonymous '
        elif len(auto_nam) > 0 and "ADMINpassword123".lower() in auto_nam[0].lower():
            auto_name = 'ADMIN@admin: '
            auto_message = auto_message.replace(auto_nam[0], '')
        elif len(auto_nam) > 0 and auto_nam[0].lower().startswith("/auto"):
            auto_name = 'Anonymous: '
            auto_message = auto_message.replace(auto_nam[0], '')
        elif len(auto_nam) > 0 and auto_nam[0].lower().startswith("/leader"):
            auto_name = 'Anonymous: '
            auto_message = auto_message.replace(auto_nam[0], '')
        elif len(auto_nam) > 0 and "@admin" in auto_nam[0]:
            # Handle variations of '@admin' command
            auto_name = 'Anonymous: '
            auto_message = auto_message.replace(auto_nam[0], '')
        elif len(auto_nam) > 0 and "@" in auto_nam[0]:
            # Handle variations of '@' command
            auto_name = 'Anonymous: '
            auto_message = auto_message.replace(auto_nam[0], '')
        elif len(auto_nam) > 0 and auto_nam[0].startswith("/"):
            auto_name = auto_nam[0][1:] + ': '
            auto_message = auto_message.replace(auto_nam[0], '')
        else:
            auto_name = 'Anonymous: '
    
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        auto_messages.append((auto_name, auto_message, timestamp))
        return redirect(url_for('autoclan'))

# -----------------------------------------------------AUTOMOTIVE END ------------------------------------!




#-----------------------------------TEMPORARY CLAN--------------------------------------------!
@app.route('/login/<clan_name>', methods=['GET', 'POST'])
def login(clan_name):
    if request.method == 'POST':
        password = request.form['password']
        
        if clan_name in clans:
            if clans[clan_name] == password:
                session['clan_name'] = clan_name
                session['role'] = 'Leader'
                return redirect(url_for('clan_page', clan_name=clan_name))
            else:
                session['clan_name'] = clan_name
                session['role'] = 'Anonymous'
                return redirect(url_for('clan_page', clan_name=clan_name))
        else:
            return redirect(url_for('index'))
    
    return render_template('login.html', clan_name=clan_name)

@app.route('/<clan_name>')
def clan_page(clan_name):
    role = session.get('role', 'Anonymous')  # Default role is guest
    # Get messages for the current clan from the dictionary
    scriptiez_messages = clan_messages.get(clan_name, [])
    return render_template('clan_page.html', clan_name=clan_name, role=role, scriptiez_messages=scriptiez_messages)

@app.route('/create_clan', methods=['POST'])
def create_clan():
    clan_name = request.form['clan_name']
    leader_password = request.form['leader_password']
    
    if clan_name in clans:
        error_message = "Clan name already exists. Please choose a different name."
        error_message0=""
        return render_template('clan.html', error_message0=error_message0, error_message=error_message, clans = clans)
    
    # Store clan information in the dictionary
    clans[clan_name] = leader_password
    # Create an empty list for messages of the new clan
    clan_messages[clan_name] = []
    # Redirect to the clan page
    return redirect(url_for('login', clan_name=clan_name))


@app.route('/send_message/<clan_name>', methods=['POST'])
def clan_send_message(clan_name):
    global clan_messages
    message = request.form['message']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sender = session.get('role', 'Anonymous')
    if message.startswith('/clearall'):
        if sender == 'Leader':
            # Clear all messages
            clan_messages[clan_name].clear()
        else:
            # Only the leader can clear all messages
            clan_messages[clan_name].append(('System', 'Only the leader can clear all messages.', timestamp))
        return redirect(url_for('clan_page', clan_name=clan_name))
    # Check if the message starts with '/p'
    elif message.startswith('/p'):
        # Extract the image URL from the message
        img_url = message[3:].strip()
        # Format the HTML for displaying the image in the chatbox
        img_html = f'<img src="{img_url}" style="max-width: 100%; height: auto;">'
        # Append the image message to the clan's message list
        clan_messages[clan_name].append((sender, img_html, timestamp))
    elif message.startswith('/v'):
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com/shorts/|youtu\.?be/|youtube\.com/embed/)?([a-zA-Z0-9_-]{11})'
        youtube_link = re.search(youtube_regex, message[3:])
        if youtube_link:
            video_id = youtube_link.group(4)
            video_embed_tag = f'<iframe width="100%;" height="100%;" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
            # Set the message to the embedded video HTML tag
            img_html = video_embed_tag
        else:
            # If the message does not contain a valid YouTube link, display an error message
            img_html = 'Invalid YouTube link format.'
        # Set the sender name to Anonymous for video messages
        clan_messages[clan_name].append((sender, img_html, timestamp))
    else:
        # Append regular text message to the clan's message list
        clan_messages[clan_name].append((sender, message, timestamp))
    
    return redirect(url_for('clan_page', clan_name=clan_name))
# ------------------------------------------------------ TEMPORARY-END-----------!

#------------------------------------------GROUP-----------------------------------------------!
@app.route('/join_group', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        group_name = request.form['group_name']
        password = request.form['leader_password']
        name = request.form['name']
        
        if group_name == group_name:  # This condition is redundant, consider removing it
            if group_name in groups:
                if groups[group_name] == password:
                    session['group_name'] = group_name
                    session['role'] = name
                    return redirect(url_for('group_page', group_name=group_name))
            else:
                error = "Incorrect Credentials"
                return render_template('join.html', error = error)
        else:
            error = "Incorrect Credentials"
            return render_template('join.html', error = error)
    
    return render_template('join.html')


@app.route('/private/<group_name>')
def group_page(group_name):
    # Check if the user is joining the group for the first time
    if 'active_group' not in session or session['active_group'] != group_name:
        session['active_group'] = group_name
        # Send a notification message
        new_user_message = f"{session.get('role', 'Anonymous')} has joined the conversation."
        group_messages.setdefault(group_name, []).append(('System', new_user_message, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    
    role = session.get('role', 'Anonymous')  # Default role is guest
    # Use get method with a default value to handle KeyError
    group_messages_list = group_messages.get(group_name, [])
    return render_template('group_page.html', group_name=group_name, role=role, group_messages=group_messages_list)

@app.route('/leave')
def leave():
    group_name = request.args.get('group_name')
    if group_name:
        session.pop('active_group', None)  # Clear active group
    return redirect(url_for('index'))
@app.route('/create_group', methods=['POST'])
def create_group():
    group_name = request.form['group_name']
    leader_password = request.form['leader_password']
    
    if group_name in groups:
        error_message0 = "Group name already exists. Please choose a different name."
        error_message =""
        return render_template('clan.html', error_message0=error_message0, error_message=error_message, clans = clans)
    
    # Store clan information in the dictionary
    groups[group_name] = leader_password
    # Create an empty list for messages of the new clan
    group_messages[group_name] = []
    # Redirect to the clan page
    return redirect(url_for('clan'))


@app.route('/send_notification/private/<group_name>', methods=['POST'])
def group_send_notification(group_name):
    
    if request.form.get('notify'):
        # Construct the button message
        sender = session.get('role', 'Anonymous')
        button_message = '<button class="Audio"></button>'
        # Append the button message to the group's message list
        group_messages.setdefault(group_name, []).append(('🔔 Notification sent by: '+ sender, button_message, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return redirect(url_for('group_page', group_name=group_name))
    
    return redirect(url_for('group_page', group_name=group_name))

@app.route('/send_disturb/private/<group_name>', methods=['POST'])
def group_send_disturb(group_name):
    
    if request.form.get('clearall'):
        group_messages[group_name].clear()
        return redirect(url_for('group_page', group_name=group_name))
    
    return redirect(url_for('group_page', group_name=group_name))

@app.route('/send_message/private/<group_name>', methods=['POST'])
def group_send_message(group_name):
    message = request.form['message']
    nam = message.split()

    # Check if the message is an image command
    if len(nam) > 0 and nam[0].lower().startswith("/clearall"):
        group_messages[group_name].clear()
        return redirect(url_for('group_page', group_name=group_name))
    elif len(nam) > 0 and nam[0].lower().startswith("/p"):
        # Construct the HTML tag for the image
        image_tag = f'<img src="{nam[1]}" style="max-width: 100%; height: auto;">'
        # Append the image tag to the group's message list
        user = session.get('role', 'Anonymous')
        group_messages.setdefault(group_name, []).append((user, image_tag, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    elif len(nam) > 0 and nam[0].lower().startswith("/v"):
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com/shorts/|youtu\.?be/|youtube\.com/embed/)?([a-zA-Z0-9_-]{11})'
        youtube_link = re.search(youtube_regex, message[3:])
        if youtube_link:
            video_id = youtube_link.group(4)
            video_embed_tag = f'<iframe width="100%;" height="100%;" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
            # Set the message to the embedded video HTML tag
            image_tag = video_embed_tag
        else:
            # If the message does not contain a valid YouTube link, display an error message
            image_tag = 'Invalid YouTube link format.'
        # Set the sender name to Anonymous for video messages
        user = session.get('role', 'Anonymous')
        group_messages.setdefault(group_name, []).append((user, image_tag, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    else:
        # Append the message to the group's message list
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sender = session.get('role', 'Anonymous')
        group_messages.setdefault(group_name, []).append((sender, message, timestamp))
    
    return redirect(url_for('group_page', group_name=group_name))


#--------------------------------GROUP-END------------------------------------------------!

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    nam = message.split()
    
    if message.startswith("/9747vanish9786"):
        messages.clear()
        return redirect(url_for('index'))
    elif message.startswith('/p '):
        # Extract the image URL from the message
        img_url = re.search(r'\bhttps?://\S+\b', message[3:])
        if img_url:
            # If a valid URL is found, construct the HTML code to display the image
            message = f'<img src="{img_url.group()}" style="max-width: 100%; height: auto;">'
        else:
            # If no valid URL is found, display an error message
            message = 'Invalid image URL format.'

        # Set the sender name to Anonymous for image messages
        name = 'Anonymous: '
    elif message.startswith('/v '):
        youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)([^&?/\s]{11})'
        youtube_link = re.search(youtube_regex, message[3:])
        if youtube_link:
            video_id = youtube_link.group(4)  # Extract video ID from the link
            video_embed_tag = f'<iframe width="100%;" height="100%;" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
            # Set the message to the embedded video HTML tag
            message = video_embed_tag
        else:
            # If the message does not contain a valid YouTube link, display an error message
            message = 'Invalid YouTube link format.'

        # Set the sender name to Anonymous for video messages
        name = 'Anonymous: '
        
    elif len(nam) > 0 and "/ADMINpassword123".lower() in nam[0].lower():
        name = 'ADMIN@admin: '
        message = message.replace(nam[0], '')
    elif len(nam) > 0 and nam[0].lower().startswith("/scriptiez"):
        name = 'Anonymous: '
        message = message.replace(nam[0], '')
    elif len(nam) > 0 and nam[0].lower().startswith("/leader"):
        name = 'Anonymous: '
        message = message.replace(nam[0], '')
    elif len(nam) > 0 and "@admin" in nam[0]:
        # Handle variations of '@admin' command
        name = 'Anonymous: '
        message = message.replace(nam[0], '')
    elif len(nam) > 0 and "@" in nam[0]:
        # Handle variations of '@' command
        name = 'Anonymous: '
        message = message.replace(nam[0], '')
    elif len(nam) > 0 and nam[0].startswith("/"):
        name = nam[0][1:] + ': '
        message = message.replace(nam[0], '')
    else:
        name = 'Anonymous: '
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    messages.append((name, message, timestamp))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
