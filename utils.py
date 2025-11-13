def mood_to_playlist(mood: str):
    playlists = {
        "happy": ["Happy Song 1", "Happy Song 2"],
        "sad": ["Sad Song 1", "Sad Song 2"],
        "angry": ["Calm Song 1", "Relaxing Song 2"],
        "neutral": ["Chill Song 1", "Chill Song 2"]
    }
    return playlists.get(mood, ["Default Song 1", "Default Song 2"])
