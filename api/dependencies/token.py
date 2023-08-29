import jwt
import datetime
import secrets

SECRET_KEY = secrets.token_hex(32)

def generate_jwt_token(payload):
    # Defina o tempo de expiração do token, por exemplo, 1 hora a partir do momento atual.
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=240)
    
    # Crie o payload do token com os dados do usuário
    token_payload = {
        'exp': expiration,
        **payload  # Aqui você pode adicionar outras informações sobre o usuário, como ID, nome, etc.
    }
    
    # Gere o token utilizando a função jwt.encode()
    token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')
    
    return token