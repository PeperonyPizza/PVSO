import numpy as np
import cv2
import acumulator
import peaks


def draw_hl(img, indicies, rhos, thetas):
    for i in range(len(indicies)):
        rho = rhos[indicies[i][0]]
        theta = thetas[indicies[i][1]]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)


def main():
    img = cv2.imread('stvorce.jpg')
    cv2.imshow("vstup", img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 1)
    canny = cv2.Canny(blur, 100, 200)
    cv2.imshow("canny", canny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    acc, rhos, thetas = acumulator.vote_acumulator(canny)
    indicies, acc = peaks.find_peaks(acc, 10, okolie=2)
    draw_hl(img, indicies, rhos, thetas)

    cv2.imshow("HT", img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
