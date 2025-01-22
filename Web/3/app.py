from flask import Flask, render_template_string, request, jsonify
import os

app = Flask(__name__)

FLAG = "flag{unsupported_file_type_reveals_secrets}"
SUPPORTED_TYPES = [".png", ".jpg", ".pdf", ".exe", ".txt"]

# HTML template with working obfuscated JavaScript
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>File Upload Challenge</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            text-align: center;
        }
        .upload-container {
            border: 2px dashed #ccc;
            padding: 20px;
            margin: 20px 0;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            margin: 10px;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>File Upload Challenge</h1>
    <div class="upload-container">
        <input type="file" id="fileInput" accept=".png,.jpg,.pdf,.exe,.txt">
        <br><br>
        <button onclick="checkFileType()">Upload File</button>
    </div>
    <script>
    (function(){
        const _0x2ae8=['log','error','fetch','/upload','files','status','form-data','catch','file','message','flag','json','File\x20type\x20not\x20supported','then'];
        window['checkFileType']=function(){
            const _0x4e=document['getElementById']('fileInput');
            const _0x4f=_0x4e[_0x2ae8[4]][0];
            if(!_0x4f){
                alert('Please\x20select\x20a\x20file');
                return;
            }
            const _0x50=new FormData();
            _0x50['append'](_0x2ae8[8],_0x4f);
            fetch(_0x2ae8[3],{
                'method':'POST',
                'body':_0x50
            })[_0x2ae8[13]](_0x51=>_0x51[_0x2ae8[11]]())[_0x2ae8[13]](_0x51=>{
                if(_0x51[_0x2ae8[5]]==='error'&&_0x51[_0x2ae8[10]]){
                    console[_0x2ae8[0]]('Found\x20flag:',_0x51[_0x2ae8[10]]);
                }
                alert(_0x51[_0x2ae8[9]]);
            })[_0x2ae8[7]](_0x51=>{
                console[_0x2ae8[1]]('Error:',_0x51);
                alert('An\x20error\x20occurred');
            });
        };
    })();
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file provided'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No file selected'})
    
    _, ext = os.path.splitext(file.filename.lower())
    if ext in SUPPORTED_TYPES:
        return jsonify({'status': 'success', 'message': 'File type supported'})
    else:
        return jsonify({
            'status': 'error',
            'message': 'File type not supported',
            'flag': FLAG
        })

if __name__ == '__main__':
    app.run(debug=True)