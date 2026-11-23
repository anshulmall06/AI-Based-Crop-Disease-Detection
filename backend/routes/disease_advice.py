
def get_local_advice(disease: str, confidence=None):

    disease_name = disease.replace("___", " - ").replace("_", " ")
    key = disease_name.lower()

    advice_database = {

        "tomato - early blight": {
            "description": "Early blight is a fungal disease that commonly affects tomato leaves, stems and fruits.",
            "symptoms": "Brown spots with concentric rings, yellowing leaves and drying of older leaves.",
            "causes": "It is associated with the fungus Alternaria solani and spreads through infected plant material and splashing water.",
            "treatment": "Remove badly affected leaves and dispose of them away from the crop. Use only locally approved fungicides according to their product labels.",
            "prevention": "Rotate crops, maintain proper plant spacing, remove crop debris and avoid overhead irrigation.",
            "tips": "Monitor the crop regularly and consult an agricultural expert if symptoms spread."
        },

        "potato - late blight": {
            "description": "Late blight is a serious disease affecting potato and tomato plants.",
            "symptoms": "Water-soaked or dark patches may appear on leaves. White fungal-like growth may develop under humid conditions.",
            "causes": "It is caused by Phytophthora infestans and spreads rapidly in cool, humid and wet conditions.",
            "treatment": "Remove and safely dispose of infected plant material. Seek local agricultural guidance promptly because this disease can spread quickly. Use only approved treatments according to their labels.",
            "prevention": "Use healthy planting material, avoid overhead irrigation, provide good air circulation and monitor crops regularly.",
            "tips": "Monitor crops regularly. Confirm uncertain diagnoses with a local agriculture expert."
        },

        "tomato - healthy": {
            "description": "No visible disease has been identified in the tomato leaf.",
            "symptoms": "The leaf appears healthy based on the prediction.",
            "causes": "No disease symptoms were identified by the model.",
            "treatment": "No disease-specific treatment is currently indicated.",
            "prevention": "Maintain proper irrigation, crop spacing and field hygiene.",
            "tips": "Continue monitoring the crop because a model prediction cannot guarantee that the entire plant is disease-free."
        },

        "potato - healthy": {
            "description": "No visible disease has been identified in the potato leaf.",
            "symptoms": "The leaf appears healthy based on the prediction.",
            "causes": "No disease symptoms were identified by the model.",
            "treatment": "No disease-specific treatment is currently indicated.",
            "prevention": "Use healthy planting material and maintain proper field hygiene.",
            "tips": "Inspect plants regularly and monitor for any new symptoms."
        }
    }

    data = advice_database.get(key)

    if data:
        description = data["description"]
        symptoms = data["symptoms"]
        causes = data["causes"]
        treatment = data["treatment"]
        prevention = data["prevention"]
        tips = data["tips"]

    else:
        description = f"{disease_name} was detected by the crop disease prediction model."
        symptoms = "Symptoms may vary depending on the disease and crop."
        causes = "The cause depends on the specific disease. Further confirmation may be required."
        treatment = "Remove severely affected plant material where appropriate. Consult a local agricultural expert for disease-specific treatment."
        prevention = "Maintain field hygiene, use healthy planting material, provide proper spacing and monitor crops regularly."
        tips = "Confirm the diagnosis with a local agriculture expert before applying any crop protection product."

    confidence_text = (
        f"\nPrediction Confidence: {confidence}%"
        if confidence is not None else ""
    )

    return f"""
LOCAL DISEASE ADVICE (offline fallback)

Disease: {disease_name}{confidence_text}

Description: {description}

Symptoms: {symptoms}

Causes: {causes}

Treatment: {treatment}

Prevention: {prevention}

Farmer Tips: {tips}

Note: This is locally stored guidance, not a live AI-generated diagnosis.
Confirm uncertain results with an agricultural expert.
"""
