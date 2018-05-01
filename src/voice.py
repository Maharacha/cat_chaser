import pygame
from google.cloud import texttospeech

def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='sv-SE',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100)

    response = client.synthesize_speech(input_text, voice, audio_config)

    pygame.mixer.pre_init(22000, -16, 2, 2048)
    pygame.mixer.init()
    p = pygame.mixer.Sound(response.audio_content)
    p.play()
    while pygame.mixer.get_busy():
        pass
    '''
    # The response's audio_content is binary.
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')
    '''

if __name__ == '__main__':
    synthesize_text('Jag är en apa, mjau!')