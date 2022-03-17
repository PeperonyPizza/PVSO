import numpy as np


def vote_acumulator(img):
    rho_res = 1;
    theta_res = 1;
    height, width = img.shape  # velkost obrazka - vyska sirka
    diag_len = np.ceil(np.sqrt(height * height + width * width))  # pythagorova veta dostanem diagonalnu dlzku
    # urcenie priestoru
    print(diag_len)
      
    rhos = np.arange(-diag_len , diag_len + 1, rho_res)
    thetas = np.deg2rad(np.arange(-90, 90, theta_res))
    print(rhos,thetas)
    acc = np.zeros((2 * int(diag_len), len(thetas)), dtype=np.uint64)
    y_idx, x_idx = np.nonzero(img)  # najdeme vsetky nenulove pixely (taktiez sa vyuziva dalej pre hladanie vrcholov)
    # ohodnotenie akumulatora
    for i in range(len(x_idx)):
        x = x_idx[i]
        y = y_idx[i]

        for j in range(len(thetas)):
            rho = int((x * np.cos(thetas[j]) +
                       y * np.sin(thetas[j])) + diag_len)
            acc[rho, j] += 1

        print(rho) 
    return acc, rhos, thetas
