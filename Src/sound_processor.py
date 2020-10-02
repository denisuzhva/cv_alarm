import simpleaudio as sa


def one_shot():
    """
    play a siren one time
    """
    file_name = '../Sounds/'
    file_name += 'siren1.wav'
    wave_obj = sa.WaveObject.from_wave_file(file_name)
    play_obj = wave_obj.play()
    play_obj.stop()


def siren_loop(file_name):
    """
    main loop
    """
    pass
