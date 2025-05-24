from dilithium_py.ml_dsa import ML_DSA_44, ML_DSA_65, ML_DSA_87
import cProfile
from time import time
from statistics import mean, median
import matplotlib.pyplot as plt
from numpy import arange


def profile_dilithium(ML_DSA):
    pk, sk = ML_DSA.keygen()
    m = b"Signed by dilithium"
    sig = ML_DSA.sign(sk, m)
    check = ML_DSA.verify(pk, m, sig)
    assert check

    gvars = {}
    lvars = {"ML_DSA": ML_DSA, "m": m, "pk": pk, "sk": sk, "sig": sig}

    cProfile.runctx(
        "[ML_DSA.keygen() for _ in range(100)]", globals=gvars, locals=lvars, sort=1
    )
    cProfile.runctx(
        "[ML_DSA.sign(sk, m) for _ in range(100)]",
        globals=gvars,
        locals=lvars,
        sort=1,
    )
    cProfile.runctx(
        "[ML_DSA.verify(pk, m, sig) for _ in range(100)]",
        globals=gvars,
        locals=lvars,
        sort=1,
    )

def benchmark_ML_DSA(ML_DSA, count):
    fails = 0
    keygen_times = []
    sign_times = []
    verify_times = []
    m = b"Signed by dilithium"

    for _ in range(count):
        t0 = time()
        pk, sk = ML_DSA.keygen()
        keygen_times.append(time() - t0)

        t1 = time()
        sig = ML_DSA.sign(sk, m)
        sign_times.append(time() - t1)

        t2 = time()
        verify = ML_DSA.verify(pk, m, sig)
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

    median_keygen_times, average_sign_times, median_sign_times, median_verify_times = benchmark_ML_DSA(ML_DSA_44, count)
    y_axis2 = [median_keygen_times*1000, average_sign_times*1000, median_sign_times*1000, median_verify_times*1000]

    median_keygen_times, average_sign_times, median_sign_times, median_verify_times = benchmark_ML_DSA(ML_DSA_65, count)
    y_axis3 = [median_keygen_times*1000, average_sign_times*1000, median_sign_times*1000, median_verify_times*1000]

    median_keygen_times, average_sign_times, median_sign_times, median_verify_times = benchmark_ML_DSA(ML_DSA_87, count)
    y_axis5 = [median_keygen_times*1000, average_sign_times*1000, median_sign_times*1000, median_verify_times*1000]
    
    plt.figure(figsize=(10, 6))
    bar_width = 0.25
    indices = arange(len(x_axis))
    plt.bar(indices - bar_width, y_axis2, bar_width, color='blue', label='ML_DSA_44')
    plt.bar(indices, y_axis3, bar_width, color='green', label='ML_DSA_65')
    plt.bar(indices + bar_width, y_axis5, bar_width, color='orange', label='ML_DSA_87')
    plt.xticks(indices, x_axis)
    plt.legend()
    plt.title("ML_DSA Benchmark Results")
    plt.xlabel("Operations")
    plt.ylabel("Time (ms)")
    plt.show()
