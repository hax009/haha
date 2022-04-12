import numpy as np
from itertools import combinations

def get_index(n, k):
    """
    Helper function to get all combinations
    :param n: Objects
    :param k: Sample(s)
    :return:
    """
    return combinations([i for i in range(n)], k)

def est_pdf(p: list):
    """
    Calculate the est_pdf
    :param p: list of probabilities of investing success
    :return: est_pdf
    """
    result = np.zeros(len(p))
    for k in range(len(p)):
        if k == 0:
            company_combination_prob = np.array(p)
            company_combination_prob = 1 - company_combination_prob
            result[k] = company_combination_prob.prod()
            continue
        company_combinations = get_index(len(p), k)
        #p = [0.4,0.5,0.1]
        #ex: i = 2, return indexes = [[1,1,0],[0,1,1],[1,0,1]]
        for company_combination in company_combinations:
                company_combination_prob = np.array(p)
                company_combination_prob = 1 - company_combination_prob
                company_combination_prob[list(company_combination)] = 1 - company_combination_prob[list(company_combination)]
                result[k] += company_combination_prob.prod()
    return result

if __name__ == '__main__':
    p = [0.34537093, 0.75580255, 0.61383029, 0.06516869, 0.46175061, 0.57079639, 0.03297377, 0.88347158, 0.91001774, 0.09064271]
    print(est_pdf(p))