import socket
from dilithium_py.ml_dsa import ML_DSA_44

def server_program():
    # Create a socket connection:
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    
    # Receive message, signature and public key:
    message = conn.recv(1024)
    print("Message: " + str(message))
    signature = conn.recv(2420)
    pk = conn.recv(2048)

    #Check the signature and send response:
    if ML_DSA_44.verify(pk, message, signature):
        print("Signature is valid")
    else:
        print("Signature is invalid")

    # Close connection
    conn.close()

if __name__ == '__main__':
    server_program()