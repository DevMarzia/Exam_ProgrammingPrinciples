import os
import json


class Virgilio:
    class CantoNotFoundError(Exception):
        pass

    def __init__(self, directory):
        self.directory = directory  # attributo di istanza

    # ----------- Esercizio 1 -----------
    def read_canto_lines(self, canto_number, strip_lines=False, num_lines=None):

        # ----------- Esercizio 15 -----------
        if not isinstance(canto_number, int):
            raise TypeError(f"canto_number deve essere un numero intero")

    # ----------- Esercizio 16 -----------
        if not (1 <= canto_number <= 34):
            raise Virgilio.CantoNotFoundError(
                'canto_number deve essere tra 1 e 34')

        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")

    # ----------- Esercizio 17 -----------
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

    # ----------- Esercizio 14 ----------- num_lines
            if num_lines is not None:
                lines = lines[:num_lines]

        except Exception:
            return f"Errore durante l'apertura del file '{file_path}'"

    # ----------- Esercizio 13 ----------- strip_lines
        if strip_lines == True:
            list_stripped = []
            for versi in lines:
                new_lines = versi.strip()
                list_stripped.append(new_lines)
            return list_stripped
        else:
            return lines

    # ----------- Esercizio 2 -----------
    def count_verses(self, canto_number):
        verses = self.read_canto_lines(canto_number)
        count = len(verses)
        return f"Nel canto {canto_number} il numero dei versi è: {count}, il tipo di dato è {type(count)}"

    # ----------- Esercizio 3 -----------
    def count_tercets(self, canto_number):
        tercets = self.read_canto_lines(canto_number)
        floor_division = len(tercets)//3
        return f"Le terzine nel canto {canto_number} sono {floor_division}, il tipo di dato è {type(floor_division)}"

    # ----------- Esercizio 4 -----------
    def count_word(self, canto_number, word):
        canto = self.read_canto_lines(canto_number)
        text = "".join(canto).lower()
        # print("Verifico testo con join applicato", text)
        lower_word = word
        word_count = text.count(lower_word)
        return f"Il numero di volte che la parola '{request_word}' compare è {word_count} volte, nel canto {canto_number}, il suo tipo di dato è {type(word_count)}"

    # ----------- Esercizio 5 -----------
    def get_verse_with_word(self, canto_number, word, strip_lines=True):
        canto = self.read_canto_lines(canto_number, strip_lines)
        i = 1
        for i, vers in enumerate(canto):
            if vers.find(word) != -1:
                i += 1
                # vers.strip()
                return f"La parola '{word}' è nel verso {i}: {vers}"
        return f"La parola '{word}' non si trova in nessun verso del canto {canto_number}"

    # ----------- Esercizio 6 -----------
    def get_verses_with_word(self, canto_number, word):
        canto = self.read_canto_lines(canto_number)
        word_lower = word
        calculate_verses = [vers.strip()
                            for vers in canto if word_lower in vers]
        return f"I versi in cui si trova la parola '{word}' sono:\n{calculate_verses}.\nIl tipo di dato è: {type(calculate_verses)}"

    # ----------- Esercizio 7 -----------
    def get_longest_verse(self, canto_number):
        canto = self.read_canto_lines(canto_number)
        longest_verses = max(canto, key=len)
        return f"Il verso più lungo nel canto {canto_number} è:\n '{longest_verses}', il suo tipo di dato è {type(longest_verses)}"

    # ----------- Esercizio 8 -----------
    def get_longest_canto(self):
        dict = {"canto_number": 0, "canto_len": 0}

        # Itera su tutti i Canti
        for canto_number in range(1, 35):
            num_verses = len(self.read_canto_lines(
                canto_number))  # Conta i versi del Canto

            # Aggiorna il risultato se troviamo un Canto con più versi
            if num_verses > dict["canto_len"]:
                dict["canto_number"] = canto_number
                dict["canto_len"] = num_verses
        return f"Il canto con il maggior numero di versi è {dict}"

    # ----------- Esercizio 9 -----------
    def count_words(self, canto_number, words):
        canto = self.read_canto_lines(canto_number)
        # Rimuove la punteggiatura e converte il testo in una lista di parole
        text = "".join(canto)

        word_counts = {}

        for word in words:
            word_counts[word] = text.count(word)

    # ----------- Esercizio 18 -----------
        # serializzazione
        try:
            with open(r'C:\Users\marzi\Desktop\exam_pp\canti\word_counts.json', 'w') as file:
                json.dump(word_counts, file)
                print("Serializzazione avvenuta con succeso!")
        except Exception:
            print("Qualcosa nella serializzazione è andato storto, Riprova!")
        # Restituisce il dizionario con i risultati
        return f"Ecco a te il conteggio di tutte le parole, del canto n {canto_number}:\n{word_counts}\nil tipo di dato è {type(word_counts)}"

    # ----------- Esercizio 10 -----------
    def get_hell_verses(self):
        total_verses = []
        for canto_number in range(1, 35):
            canto = self.read_canto_lines(canto_number)
            total_verses.extend(canto)
        return f'Ecco a te i tutti i versi dell\'Inferno:\n{total_verses}'

    # ----------- Esercizio 11 -----------
    def count_hell_verses(self):
        number_total = 0
        for canto_number in range(1, 35):
            canto = self.read_canto_lines(canto_number)
            number_total += len(canto)
        return number_total

    # ----------- Esercizio 12 -----------
    def get_hell_verse_men_lean(self, strip_lines=True):
        total_length = 0

        # Calcola la lunghezza totale di tutti i versi
        for canto_number in range(1, 35):
            canto = self.read_canto_lines(canto_number, strip_lines)
            # Rimuovi spazi inizio/fine e somma le lunghezze
            for verso in canto:
                total_length += len(verso)  # (verso.strip())

        # Ottengo il numero totale di versi
        total_verses = self.count_hell_verses()
        # Calcola la lunghezza media, evitando divisioni per zero
        calculate = total_length / total_verses
        return f"La lunghezza media di tutti i versi dell'inferno è '{calculate:.2f}', ed il suo tipo di dato è {type(calculate)}"


# valorizzo attributo
virgilio = Virgilio(r"C:\Users\marzi\Desktop\exam_pp\canti")
# print("risultato:" , virgilio.directory)

print('\n----------- Esercizio 1 -----------')
# scelgo il canto
# int(input("Scrivi il numero del canto che vuoi leggere (da 1 a 34): "))
canto_number = 2
request_word = 'nel'.lower()  # input("\nQuale parola/lettera vuoi cercare?: ")

# legge le righe del canto
canto_lines = virgilio.read_canto_lines(canto_number)
print(
    f"Ecco a te il canto n {canto_number}:\n{canto_lines}\ne il suo tipo di dato è {type(canto_lines)}")


print('\n----------- Esercizio 2 -----------')
# conta i versi del canto
verse_count = virgilio.count_verses(canto_number)
print(verse_count)

print('\n----------- Esercizio 3 -----------')
# calcola le terzine nel canto
total_tercets = virgilio.count_tercets(canto_number)
print(total_tercets)

print('\n----------- Esercizio 4 -----------')
# conta quante volte è presente una parola
number_word = virgilio.count_word(canto_number, request_word)
print(number_word)

print('\n----------- Esercizio 5 -----------')
# trova il verso tramite la parola cercata
find_vers = virgilio.get_verse_with_word(canto_number, request_word)
print(find_vers)

print('\n----------- Esercizio 6 -----------')
# crea lista dei versi contenenti la lettera/parola cercata
list_verses = virgilio.get_verses_with_word(canto_number, request_word)
print(list_verses)

print('\n----------- Esercizio 7 -----------')
# trova il verso più lungo
long_vers = virgilio.get_longest_verse(canto_number)
print(long_vers)

print('\n----------- Esercizio 8 -----------')
# restituisce il canto come un dizionario
dict_ = virgilio.get_longest_canto()
print(dict_)

print('\n----------- Esercizio 9 -----------')
# restituisce un dizionario con il conteggio di tutte le parole da noi richieste
total_words = virgilio.count_words(
    canto_number, ['Nel', 'nel', 'vidi', 'vorrei'])
print(total_words)

print('\n----------- Esercizio 10 -----------')
# Lista con tutti i versi dell'inferno
all_verses = virgilio.get_hell_verses()
print(all_verses)

print('\n----------- Esercizio 11 -----------')
# Numero totale dei versi presenti nell'Inferno
number_verses = virgilio.count_hell_verses()
print(f"\nI versi totali dell\'Inferno sono:")
print(number_verses)
print(f'e il tipo di dato è:{type(number_verses)}')

print('\n----------- Esercizio 12 -----------')
# Ottengo il valore numerico che rappresenta la lunghezza media dei versi dell'inferno
media = virgilio.get_hell_verse_men_lean()
print(media)



