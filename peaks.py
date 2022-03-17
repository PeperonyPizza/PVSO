import numpy as np


def find_peaks(acc, peaks, okolie=5):
    indicies = []
    acc_copy = np.copy(acc)
    for i in range(peaks):
        idx = np.argmax(acc_copy)  # najdeme maxima
        acc_idx = np.unravel_index(idx, acc_copy.shape)  # vypluje mi index - kde sa nachadza
        indicies.append(acc_idx)
        # ak sa hodnota idx_x a idx_y nachadza velmi blizko ku zvolenej tak ju vyber
        idx_y, idx_x = acc_idx

        if (idx_x - (okolie / 2)) < 0:
            min_x = 0
        else:
            min_x = idx_x - (okolie / 2)
        if (idx_x + (okolie / 2) + 1) > acc.shape[1]:
            max_x = acc.shape[1]
        else:
            max_x = idx_x + (okolie / 2) + 1
        if (idx_y - (okolie / 2)) < 0:
            min_y = 0
        else:
            min_y = idx_y - (okolie / 2)
        if ((idx_y + (okolie / 2) + 1) > acc.shape[0]):
            max_y = acc.shape[0]
        else:
            max_y = idx_y + (okolie / 2) + 1

        for x in range(int(min_x), int(max_x)):
            for y in range(int(min_y), int(max_y)):
                acc_copy[y, x] = 0

                if (x == min_x or x == (max_x - 1)):
                    acc[y, x] = 255
                if (y == min_y or y == (max_y - 1)):
                    acc[y, x] = 255

    return indicies, acc
