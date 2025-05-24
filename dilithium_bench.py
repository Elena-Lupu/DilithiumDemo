from dilithium_py.dilithium import Dilithium2, Dilithium3, Dilithium5
import cProfile
from time import time
from statistics import mean, median
import matplotlib.pyplot as plt
from numpy import arange


def profile_dilithium(Dilithium):
    pk, sk = Dilithium.keygen()
    m = b"Signed by dilithium"
    sig = Dilithium.sign(sk, m)
    check = Dilithium.verify(pk, m, sig)
    assert check

    gvars = {}
    lvars = {"Dilithium": Dilithium, "m": m, "pk": pk, "sk": sk, "sig": sig}

    cProfile.runctx(
        "[Dilithium.keygen() for _ in range(100)]", globals=gvars, locals=lvars, sort=1
    )
    cProfile.runctx(
        "[Dilithium.sign(sk, m) for _ in range(100)]",
        globals=gvars,
        locals=lvars,
        sort=1,
    )
    cProfile.runctx(
        "[Dilithium.verify(pk, m, sig) for _ in range(100)]",
        globals=gvars,
        locals=lvars,
        sort=1,
    )

def benchmark_dilithium(Dilithium, count):
    fails = 0
    keygen_times = []
    sign_times = []
    verify_times = []
    m = b"Signed by dilithium"

    for _ in range(count):
        t0 = time()
        pk, sk = Dilithium.keygen()
        keygen_times.append(time() - t0)

        t1 = time()
        sig = Dilithium.sign(sk, m)
        sign_times.append(time() - t1)

        t2 = time()
        verify = Dilithium.verify(pk, m, sig)
        verify_times.append(time() - t2)
        if not verify:
            fails += 1

    median_keygen_times = round(median(keygen_times), 3)
    average_sign_times = round(mean(sign_times), 3)
    median_sign_times = round(median(sign_times), 3)
    median_verify_times = round(median(verify_times), 3)
    return median_keygen_times, average_sign_times, median_sign_times, median_verify_times


if __name__ == "__main__":
    count = 1000
    x_axis = ['Median Keygen Times', 'Average Sign Times', 'Median Sign Times', 'Median Verify Times']

    median_keygen_times, average_sign_times, median_sign_times, median_verify_times = benchmark_dilithium(Dilithium2, count)
    y_axis2 = [median_keygen_times*1000, average_sign_times*1000, median_sign_times*1000, median_verify_times*1000]

    median_keygen_times, average_sign_times, median_sign_times, median_verify_times = benchmark_dilithium(Dilithium3, count)
    y_axis3 = [median_keygen_times*1000, average_sign_times*1000, median_sign_times*1000, median_verify_times*1000]

    median_keygen_times, average_sign_times, median_sign_times, median_verify_times = benchmark_dilithium(Dilithium5, count)
    y_axis5 = [median_keygen_times*1000, average_sign_times*1000, median_sign_times*1000, median_verify_times*1000]
    
    plt.figure(figsize=(10, 6))
    bar_width = 0.25
    indices = arange(len(x_axis))
    plt.bar(indices - bar_width, y_axis2, bar_width, color='blue', label='Dilithium2')
    plt.bar(indices, y_axis3, bar_width, color='green', label='Dilithium3')
    plt.bar(indices + bar_width, y_axis5, bar_width, color='orange', label='Dilithium5')
    plt.xticks(indices, x_axis)
    plt.legend()
    plt.title("Dilithium Benchmark Results")
    plt.xlabel("Operations")
    plt.ylabel("Time (ms)")
    plt.show()
