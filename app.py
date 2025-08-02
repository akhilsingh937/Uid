import os
import requests
import schedule
import time
from flask import Flask, request, render_template_string

app = Flask(__name__)

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Messenger Group Extractor</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background: url('https://i.ibb.co/G47gnsMH/1745140321925.png') no-repeat center center fixed;
            background-size: cover;
            color: white;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 90%;
            max-width: 400px;
            margin: 100px auto;
            padding: 20px;
            background: rgba(0, 0, 0, 0.8);
            border-radius: 15px;
            border: 2px solid #00ffff;
            box-shadow: 0px 0px 15px rgba(0, 255, 255, 0.4);
        }
        h2 {
            margin-bottom: 20px;
            font-size: 24px;
            text-transform: uppercase;
            color: #00ffff;
        }
        input {
            width: 90%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #00ffff;
            background: black;
            color: white;
            border-radius: 5px;
            text-align: center;
        }
        button {
            width: 100%;
            padding: 12px;
            background: blue;
            color: white;
            font-weight: bold;
            border: 2px solid white;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 10px;
            transition: 0.3s;
        }
        button:hover {
            background: darkblue;
            transform: scale(1.05);
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            background: black;
            border: 2px solid #00ffff;
            border-radius: 10px;
            color: white;
        }
        .group-box {
            background: #111;
            padding: 12px;
            margin: 12px 0;
            border-radius: 10px;
            border: 1px solid #00ffff;
        }
        .uid-box {
            background: #000;
            margin-top: 10px;
            padding: 8px;
            border-radius: 6px;
            border: 1px solid #ffffff;
            font-size: 14px;
        }
        .small-button {
            display: inline-block;
            width: 48%;
            padding: 10px;
            margin: 5px 1%;
            background: green;
            color: white;
            border: 1px solid white;
            border-radius: 8px;
            text-decoration: none;
            font-size: 14px;
        }
        .small-button:hover {
            background: darkgreen;
        }
        .messenger {
            background: #0084FF;
        }
        .messenger:hover {
            background: #005bb5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>❣️😂𝐓𝐎𝐊𝐄𝐍 𝐃𝐀𝐀𝐋 𝐊𝐄 𝐔𝐈𝐃 𝐍𝐈𝐊𝐀𝐋𝐎 𝐁𝐄𝐓𝐈𝐂𝐇𝐎𝐃𝐃 😂❣️</h2>
        <form method="POST">
            <input type="text" name="token" placeholder="😂𝐁𝐒𝐃𝐊 𝐓𝐎𝐊𝐄𝐍 𝐃𝐀𝐀𝐋😂" required>
            <button type="submit">😂𝐁𝐒𝐃𝐊 𝐒𝐔𝐁𝐌𝐈𝐓 𝐊𝐀𝐑😂</button>
        </form>

        

        

        <!-- Buttons Section -->
        <div style="margin-top: 15px;">
            <a href="https://wa.me/+917543864229" target="_blank" class="small-button">WhatsApp</a>
            <a href="https://www.facebook.com/profile.php?id=100064267823693" target="_blank" class="small-button messenger">Messenger</a>
        </div>

        <div class="result">❣️❣️ 𝐓𝐇𝐄'𝐖 𝐓𝐇𝐄 𝐔𝐍𝐒𝐓𝐎𝐏𝐏𝐀𝐁𝐋𝐄 𝐋𝐄𝐆𝐄𝐍𝐃 𝐁𝐎'𝐈𝐈 𝐏𝐑𝐈𝐍𝐂𝐄 𝐃𝐎𝐍𝐄 𝐇𝐄𝐑𝐄❣️❣️</div>
    </div>
</body>
</html>
