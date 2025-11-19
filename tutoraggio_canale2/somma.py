def somma_pari(seq):
    # @param seq: Sequenza int
    somma = 0
    for n in seq:
        if n % 2 == 0:
           somma = somma + n
    print somma

seq = [1, 10, 63, 40, 2, 11, 3, 44, 21]
somma_pari(seq)