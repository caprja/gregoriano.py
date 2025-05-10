import streamlit as st

# Funzione che calcola il giorno della settimana dal 1752 in poi

def giorno_della_settimana(D, M, Y):
    # Validazione base
    if Y < 1582:
        raise ValueError("Il Calendario Gregoriano venne introdotto nel 1582")
    if M < 1 or M > 12:
        raise ValueError("Mese non valido")
    if D < 1 or D > 31:
        raise ValueError("Giorno non valido")
    # Controllo giorni per mese
    if M == 2:
        bis = (Y % 4 == 0)
        if D > (29 if bis else 28):
            raise ValueError("Giorno non valido per Febbraio")
    elif M in (4, 6, 9, 11):
        if D > 30:
            raise ValueError("Giorno non valido per questo mese")
    # Assegnazione nome mese e valore n
    if M == 1:
        m_name, n = 'Gennaio', 0 if Y % 4 == 0 else 1
    elif M == 2:
        m_name, n = 'Febbraio', 3 if Y % 4 == 0 else 4
    elif M == 3:
        m_name, n = 'Marzo', 4
    elif M == 4:
        m_name, n = 'Aprile', 0
    elif M == 5:
        m_name, n = 'Maggio', 2
    elif M == 6:
        m_name, n = 'Giugno', 5
    elif M == 7:
        m_name, n = 'Luglio', 0
    elif M == 8:
        m_name, n = 'Agosto', 3
    elif M == 9:
        m_name, n = 'Settembre', 6
    elif M == 10:
        m_name, n = 'Ottobre', 1
    elif M == 11:
        m_name, n = 'Novembre', 4
    else:
        m_name, n = 'Dicembre', 6
    # Calcolo S in base ai 400 anni
    y_mod = (Y - 1700) % 400
    if y_mod <= 99:
        S = 4
    elif y_mod <= 199:
        S = 2
    elif y_mod <= 299:
        S = 0
    else:
        S = -1

    # Funzione ausiliaria per ultimi due cifre dell'anno
    def Y1(num, digs=2):
        return abs(num) % (10**digs)

    # Calcolo giorno (0=Sabato, …)
    z = (Y1(Y) + (Y1(Y) // 4) + n + D + S) % 7
    giorni = {
        0: 'Sabato',   1: 'Domenica', 2: 'Lunedi',
        3: 'Martedì',  4: 'Mercoledì', 5: 'Giovedì',
        6: 'Venerdì'
    }
    giorno_str = giorni[z]

    # Costruzione frase finale
    if Y < 2025:
        pref = 'era '
    elif Y == 2025:
        pref = 'è '
    else:
        pref = 'sarà '
    return f"Il giorno {D} di {m_name} del {Y} {pref}{giorno_str}"

# Interfaccia Streamlit
st.title("Calcola Giorno della Settimana")
st.write("Inserisci giorno, mese e anno per ottenere il giorno della settimana corrispondente.")

col1, col2, col3 = st.columns(3)
with col1:
    giorno = st.number_input("Giorno", min_value=1, max_value=31, value=1)
with col2:
    mese = st.number_input("Mese", min_value=1, max_value=12, value=1)
with col3:
    anno = st.number_input("Anno", min_value=1582, max_value=9999, value=2025)

if st.button("Calcola"):
    try:
        risultato = giorno_della_settimana(giorno, mese, anno)
        st.success(risultato)
    except ValueError as e:
        st.error(f"Errore: {e}")
# streamlit run app.py
