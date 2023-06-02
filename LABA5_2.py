from scipy import stats

pars = lambda k, m, n: len([i for i in range(n-1) if seq[i] == k and seq[i+1] == m])

def chi_squared_test(seq):
    n = len(seq)
    exp_freq = (n-1) / 4

    # Посчет количество битовых пар 00, 01, 10 и 11 в последовательности.
    freq_00 = pars(0, 0, n)
    freq_01 = pars(0, 1, n)
    freq_10 = pars(1, 0, n)
    freq_11 = pars(1, 1, n)

    # Ожидаемое количество битовых пар для равномерно 
    # распределенной последовательности той же длины.
    chi_square_stat = ((freq_00 - exp_freq)**2 + (freq_01 - exp_freq)**2 
                       + (freq_10 - exp_freq)**2 + (freq_11 - exp_freq)**2) / exp_freq
    
    # число степеней свободы
    # В данном случае имеются 4 категории битовых пар, 
    # поэтому число степеней свободы равно k = 4 - 1 = 3, 
    # где k - число степеней свободы.
    k = 3

    # уровень значимости alpha (0.05)
    alpha = 0.05

    # табличное значение критерия chi_squared
    chi_squared_table_value = 7.815

    # расчет p-value (вероятность получить для данной вероятностной модели 
    # распределения значений случайной величины такое же или более экстремальное
    #  значение статистики (среднего арифметического, медианы и др.), 
    # по сравнению с ранее наблюдаемым, при условии, что нулевая гипотеза верна.)
    p_value = 1 - stats.chi2.cdf(chi_square_stat, k)
    
    return p_value >= alpha, chi_square_stat, chi_squared_table_value

seq = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0]  # ваша генерируемая последовательность бит
is_random, chi_sq_stat, chi_sq_table_value = chi_squared_test(seq)

print(f'Генерируемая последовательность: {seq}')
print(f'Статистика chi-squared: {chi_sq_stat}')

if is_random:
    print('Генерируемая последовательность можно признать случайной')
else:
    print('Генерируемая последовательность скорее всего не случайная')