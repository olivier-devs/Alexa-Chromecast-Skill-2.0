from lambda_function.lang.language import Key
'''
To add another language create a file using the code below, without the hyphen (-).
Use the same keys in the LANGUAGE dictionary and update the spoken values.
    ar-SA: Arabic (SA)
    de-DE: German (DE)
    en-AU: English (AU)
    en-CA: English (CA)
    en-GB: English (UK)
    en-IN: English (IN)
    en-US: English (US)
    es-ES: Spanish (ES)
    es-MX: Spanish (MX)
    es-US: Spanish (US)
    fr-CA: French (CA)
    fr-FR: French (FR)
    hi-IN: Hindi (IN)
    it-IT: Italian (IT)
    ja-JP: Japanese (JP)
    pt-BR: Portuguese (BR)
'''

LANGUAGE = {
    Key.CardTitle: 'Alexa Chromecast Controller',
    #TODO
    Key.Help: '''
    Bienvenue sur Alexa Chromecast controller. Ce skill vous permet de contrôler vos Chromecasts de différentes pièces.
    Un appareil Alexa, peut être configuré pour contrôler une Chromecast dans une pièce particulière.
    Ensuite, vous dire quelque chose comme: "Alexa, demande à Chromecast de jouer, ou: Alexa, demande à Chromecast de mettre pause.
    Vous pouvez contrôler un pièce particulière en disant: Alexa, demande à Chromecast de jouer dans la pièce média.
    ''',
    Key.Ok: 'Ok',
    Key.Goodbye: 'Au revoir!',
    Key.ErrorGeneral: 'Désolé, je n\'ai pas réussi à effectuer ce que vous avez demandé. Veuillez réessayer.',

    # Set the room
    #TODO
    Key.SetTheRoom: 'J\'ai besoin d\'attribuer la pièce de la Chromcast à cet appareil Alexa pour pouvor la contrôler. ' +
                  'Merci d\'attribuer la Chromecast de la pièce en disant: attribue pièce to média.',
    #TODO
    Key.ShortSetTheRoom: 'Merci d\'attribuer la Chromecast de la pièce en disant: attribue pièce to média.',
    Key.ControlRoom: 'Ok, la Chromecast de la pièce {room} est maintenant controlable.',

    # Set Volume
    Key.SetVolume: 'Ok, modification du volume à {volume}.',
    Key.IncreaseVolume: 'Ok, augmentation du volume.',
    Key.DecreaseVolume: 'Ok, di;inution du volume.',

    # Subtitles
    Key.SubtitlesOff: 'Ok, suppression des sous-titres.',
    Key.SubtitlesOn: 'Ok, activation des sous-titres.',

    # SNS Publish
    Key.LogErrorSnsPublish: 'L\'envoi de la commande à la Chromecast a échoué.',
    Key.ErrorSnsPublish: 'Désolé, une erreur a été recontré lors de l\'envoi de la commande à la Chromecast. ',

    # Switch Audio
    Key.SwitchAudio: 'Ok, modification de l\'audio.',

    # QualityIntent
    Key.ChangeQuality: 'Ok, modification de la qualité du média vers {quality}.',
    Key.IncreaseQuality: 'Ok, augmentation de la qualité du média.',
    Key.DecreaseQuality: 'Ok, diminution de la qualité du média.',
    Key.ErrorChangeQuality: 'Désolé je n\'ai pas réussi à modifier la qualité. Veuillez réessayer.',

    Key.ErrorEpisodeParams: 'Je ne peux pas faire ça. Merci de spécifier une saison ou un épisode.',
    Key.ErrorSetVolumeRange: 'Désolé, le volume doit être compris entre 0 et 10. Veuillez réessayer.',

    # Play Media Types
    Key.Playing: 'Lecture en cours.',
    Key.Finding: 'Recherche en cours.',
    Key.Shuffling: 'Mélange en cours.',

    Key.InRoom: 'dans la pièce {room}',
    Key.OnApp: 'sur l\'applicatoon {app}',

    # Play music
    Key.PlayTitle: '{play} {title}',
    Key.PlaySongsByArtist: '{play} la chanson de {artist}',
    Key.PlaySong: '{play} la chanson {title}',
    Key.PlaySongsByAlbum: '{play} l\'album {album}',

    # Play photos
    Key.PlayPhotosByDate: '{play} les photos depuis le mois de {month} {year}',
    Key.PlayPhotosByEvent: '{play} les photos de {title} {year}',
    Key.PlayPhotosByTitle: '{play} les photos de {title}',
    Key.PlayPhotosByYear: '{play} les photos de l\'année {year}',

    # Play media
    Key.PlayPlaylist: '{play} la playlist {title}',
    Key.PlayMovie: '{play} le film {title}',
    Key.PlayShow: '{play} la série {show}',
    Key.PlayEpisode: '{play} l\'épisode {title} de la série {show}',
    Key.PlayEpisodeNumber: '{play} l\'épisode {episode} de la saison {season} de la série {show}',
    Key.PlaySeason: '{play} la saison {season} de la série {show}',

    # Speech to pronounce definitions like "1080p"
    Key.Speak1080p: 'mille quatre vingt p',
    Key.Speak720p: 'sept cents vingt p',
    Key.Speak480p: 'quatre cents quatre vingt p',

    # List of months based on Amazon Month slot type
    Key.ListMonths: ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août',
                     'septembre', 'octobre', 'novembre', 'décembre']

}
