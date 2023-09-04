import assemblyai as aai
import constants 

aai.settings.api_keys = constants.API_KEY

transcriber = aai.Transcriber()
transcript = transcriber.transcribe("What-wonderful-orld.m4a")
print(transcript.text)
