# Importa la libreria necessaria
from youtube_transcript_api import YouTubeTranscriptApi

# Funzione per estrarre l'ID del video dall'URL di YouTube
def extract_video_id(url):
    # Cerca il parametro 'v=' nell'URL e prende il valore successivo
    if 'v=' in url:
        return url.split('v=')[1].split('&')[0]
    # Se l'URL è in formato abbreviato (youtu.be), prende l'ultima parte dell'URL
    elif 'youtu.be' in url:
        return url.split('/')[-1]
    else:
        return None

# Funzione principale per ottenere e salvare la trascrizione
def get_and_save_transcript(video_url, output_file='transcript.txt'):
    try:
        # Estrai l'ID del video dall'URL
        video_id = extract_video_id(video_url)
        if not video_id:
            raise ValueError("ID del video non valido o non trovato nell'URL")

        # Ottieni la trascrizione dal video in italiano
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['it'])

        # Formatta la trascrizione in un unico testo
        formatted_transcript = " ".join([entry['text'] for entry in transcript])

        # Salva la trascrizione in un file di testo
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(formatted_transcript)

        print(f"Trascrizione salvata con successo in {output_file}")

        # Stampa le prime righe della trascrizione come anteprima
        print("\nAnteprima della trascrizione:")
        print(formatted_transcript[:200] + "...")

    except Exception as e:
        print(f"Si è verificato un errore: {e}")

# Esempio di utilizzo
if __name__ == "__main__":
    video_url = input("Inserisci l'URL del video di YouTube: ")
    get_and_save_transcript(video_url)
