from dilithium_py.ml_dsa import ML_DSA_44, ML_DSA_65, ML_DSA_87
import matplotlib.pyplot as plt
from numpy import arange

if __name__ == "__main__":
    x_axis = ['Public key', 'Secret key', 'Signature']

    pk, sk = ML_DSA_44.keygen()
    sig = ML_DSA_44.sign(sk, b"Signed by dilithium")
    y_axis2 = [len(pk), len(sk), len(sig)]

    pk, sk = ML_DSA_65.keygen()
    sig = ML_DSA_65.sign(sk, b"Signed by dilithium")
    y_axis3 = [len(pk), len(sk), len(sig)]

    pk, sk= ML_DSA_87.keygen()
    sig = ML_DSA_87.sign(sk, b"Signed by dilithium")
    y_axis5 = [len(pk), len(sk), len(sig)]

    plt.figure(figsize=(10, 6))
    bar_width = 0.25
    indices = arange(len(x_axis))
    plt.bar(indices - bar_width, y_axis2, bar_width, color='blue', label='ML_DSA_44')
    plt.bar(indices, y_axis3, bar_width, color='green', label='ML_DSA_65')
    plt.bar(indices + bar_width, y_axis5, bar_width, color='orange', label='ML_DSA_87')
    plt.xticks(indices, x_axis)
    plt.legend()
    plt.title("ML_DSA Sizes")
    plt.ylabel("Size (bytes)")
    plt.show()
    