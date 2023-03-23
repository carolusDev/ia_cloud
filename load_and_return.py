import joblib

def load_model(model_path):
    """
    Fonction qui charge un modèle sauvegardé avec joblib
    
    Parameters:
    ----------
    model_path : str
        Chemin vers le fichier contenant le modèle sauvegardé
    
    Returns:
    -------
    model : object
        Objet modèle chargé
    """
    model = joblib.load(model_path)
    return model

