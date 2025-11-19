def draw_stairs(pic, x0, y0, step_w, step_h, n_steps, col):
    # @param pic: Picture   immagine su cui disegnare
    # @param x0: int        x di partenza
    # @param y0: int        y di partenza
    # @param step_w: int    larghezza di ciascun gradino
    # @param step_h: int    altezza di ciascun gradino
    # @param n_steps: int   numero di gradini
    # @param col: Color     colore della scaletta
    for i in range(n_steps):
        # --- segmento orizzontale ---
        addLine(pic, x0, y0, x0 + step_w, y0, col)
        
        # aggiorno posizione
        x0 = x0 + step_w
        
        # --- segmento verticale ---
        addLine(pic, x0, y0, x0, y0 - step_h, col)
        
        # aggiorno posizione
        y0 = y0 - step_h

pict = makePicture(pickAFile())
draw_stairs(pict, 100, 200, 300, 400, 500, orange)
repaint(pict)