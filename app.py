from flask import Flask, request, jsonify
from consulta import buscar_localizacao
import traceback

app = Flask(__name__)

def build_response(text, end_session=True):
    return {
        "version":"1.0",
        "response":{
            "outputSpeech": {"type": "SSML", 
                             "ssml":f"<speak>{text} <break time='2s'/> Deseja buscar outro material? </speak>"},
            "shouldEndSession": end_session
        }
    }

@app.route('/alexa', methods=['POST'])
def alexa_webhook():
    payload = request.get_json(force=True, silent=True)

    if not payload or 'request' not in payload:
        return jsonify(build_response("Requisição inválida.")), 400
    
    r_type = payload['request']['type']

    if r_type == 'LaunchRequest':
        msg = "Olá! Diga o nome do material que deseja localizar."
        return jsonify(build_response(msg, end_session=False))
    
    if r_type == 'IntentRequest':
        intent_name = payload['request']['intent']['name']

        if intent_name == 'ConsultaMaterialIntent':
            slots = payload['request']['intent']['slots']
            material = slots.get('material', {}).get('value')

            if not material:
                return jsonify(build_response(
                    "Não entendi o material. Pode repetir?", end_session=False))
                
            try:
                resposta = buscar_localizacao(material)
                #resposta += " Deseja buscar outro material?"
                return jsonify(build_response(resposta, end_session=False))
            except Exception as e:
                print(traceback.format_exc())
                return jsonify(build_response(
                    "Ocorreu um erro ao buscar o material.", end_session=False))

        return jsonify(build_response("Desculpe, não entendi o pedido.", end_session=False))

    return jsonify(build_response("Requisição não suportada.", end_session=True))      

if __name__ == "__main__":
    # debug=True opcional para desenvolvimento
    app.run(port=5000, debug=True)

