import socket
from dilithium_py.ml_dsa import ML_DSA_44

def client_program():
    # Create a socket connection:
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host, port))

    # Message:
    message = b"Alooooooooooooooooooooo"

    # Sign the message:
    pk, sk = ML_DSA_44.keygen()
    signature = ML_DSA_44.sign(sk, message)
    
    # Send message, signature, and public key:
    client_socket.send(message)
    client_socket.send(signature)
    client_socket.send(pk)

    # Close the connection:
    client_socket.close()

if __name__ == '__main__':
    client_program()