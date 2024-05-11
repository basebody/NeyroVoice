import g4f

from elevenlabs.client import ElevenLabs
from elevenlabs import Voice, VoiceSettings, save

API_KEYS = ['ff143c1b7c7f7db2f735b814ecfb565f' , '66643a9a8963218b753b34e1f6890607', 'd72e79ef0c3d1534d4ced7eeb36a567f']

def create_response(prompt):

    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": prompt}]
    )

    return response

def text_to_voice(text, current_api):

    client = ElevenLabs(api_key=API_KEYS[current_api])

    audio = client.generate(
        text=text,
        voice='Max - Clear & Professional',
        model='eleven_multilingual_v2'
    )

    save(audio=audio, filename='output.mp3')

def voice_to_text(path):
    pass

#print(text_to_voice(create_response(''), 0))