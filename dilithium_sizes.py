from dilithium_py.dilithium import Dilithium2, Dilithium3, Dilithium5
import matplotlib.pyplot as plt
from numpy import arange

if __name__ == "__main__":
    x_axis = ['Public key', 'Secret key', 'Signature']

    pk, sk = Dilithium2.keygen()
    sig = Dilithium2.sign(sk, b"Signed by dilithium")
    y_axis2 = [len(pk), len(sk), len(sig)]

    pk, sk = Dilithium3.keygen()
    sig = Dilithium3.sign(sk, b"Signed by dilithium")
    y_axis3 = [len(pk), len(sk), len(sig)]

    pk, sk= Dilithium5.keygen()
    sig = Dilithium5.sign(sk, b"Signed by dilithium")
    y_axis5 = [len(pk), len(sk), len(sig)]

    plt.figure(figsize=(10, 6))
    bar_width = 0.25
    indices = arange(len(x_axis))
    plt.bar(indices - bar_width, y_axis2, bar_width, color='blue', label='Dilithium2')
    plt.bar(indices, y_axis3, bar_width, color='green', label='Dilithium3')
    plt.bar(indices + bar_width, y_axis5, bar_width, color='orange', label='Dilithium5')
    plt.xticks(indices, x_axis)
    plt.legend()
    plt.title("Dilithium Sizes")
    plt.ylabel("Size (bytes)")
    plt.show()
    