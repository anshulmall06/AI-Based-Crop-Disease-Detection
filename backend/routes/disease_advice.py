
def get_local_advice(disease: str) -> str:
    name = disease.replace("___", " - ").replace("_", " ").strip()
    key = name.lower()

    advice = {
        "early blight": {
            "description": "Early blight is a fungal disease that commonly affects tomato and potato leaves.",
            "symptoms": "Brown spots, often with concentric rings, appear on older leaves. Yellowing may develop around affected areas.",
            "causes": "The disease is associated with the fungus Alternaria solani and can spread through infected plant material and splashing water.",
            "treatment": "Remove badly affected leaves and dispose of them away from the crop. Avoid wetting foliage. Use only locally approved fungicides according to their product labels.",
            "prevention": "Rotate crops, maintain proper plant spacing, remove crop debris, and water near the soil rather than over the leaves.",
        },
        "late blight": {
            "description": "Late blight is a serious disease of potato and tomato plants.",
            "symptoms": "Water-soaked or dark patches may appear on leaves. White fungal-like growth may develop under humid conditions.",
            "causes": "It is caused by Phytophthora infestans and spreads rapidly in cool, humid, wet conditions.",
            "treatment": "Remove and safely dispose of infected plant material. Seek local agricultural guidance promptly because this disease can spread quickly. Use only approved treatments according to their labels.",
            "prevention": "Use healthy planting material, avoid overhead irrigation, provide good air circulation, and monitor crops regularly.",
        },
        "bacterial spot": {
            "description": "Bacterial spot affects crops such as tomato and pepper.",
            "symptoms": "Small dark, water-soaked spots may develop on leaves and fruit. Leaves can turn yellow and fall.",
            "causes": "The disease is caused by bacterial pathogens and can spread through infected seeds, plant material, rain, and handling wet plants.",
            "treatment": "Remove severely affected plant parts where practical. Avoid handling plants when wet. Ask a local agricultural expert about suitable locally approved management options.",
            "prevention": "Use certified disease-free seeds or seedlings, rotate crops, remove plant debris, and avoid overhead watering.",
        },
        "powdery mildew": {
            "description": "Powdery mildew is a fungal disease that affects leaves and other green plant parts.",
            "symptoms": "White or grey powder-like patches appear on the leaf surface. Leaves may become distorted or dry.",
            "causes": "The disease is associated with powdery mildew fungi and can spread through airborne spores.",
            "treatment": "Remove badly affected leaves where practical. Improve airflow and ask an agricultural expert about approved treatments for the crop.",
            "prevention": "Maintain suitable spacing, avoid excessive nitrogen fertilization, and inspect plants regularly.",
        },
        "leaf mold": {
            "description": "Leaf mold is a fungal disease commonly associated with tomato plants grown in humid conditions.",
            "symptoms": "Pale yellow patches may appear on the upper leaf surface, with olive or greyish growth underneath.",
            "causes": "High humidity, poor ventilation, and prolonged leaf wetness encourage disease development.",
            "treatment": "Remove badly affected leaves, improve ventilation, and avoid wetting foliage. Use only approved treatments when recommended locally.",
            "prevention": "Maintain airflow, avoid overcrowding, and manage humidity and irrigation carefully.",
        },
        "septoria": {
            "description": "Septoria leaf spot is a fungal disease commonly found on tomato plants.",
            "symptoms": "Small circular spots with dark edges and pale centres appear on leaves, often starting on older leaves.",
            "causes": "The fungus can survive on infected crop debris and spread through splashing water.",
            "treatment": "Remove affected lower leaves and dispose of crop debris safely. Avoid overhead watering.",
            "prevention": "Rotate crops, use clean planting material, mulch soil where suitable, and keep foliage dry.",
        },
        "cercospora": {
            "description": "Cercospora leaf spot is a fungal disease affecting several crops, including maize.",
            "symptoms": "Small lesions may develop and expand into elongated grey or brown spots.",
            "causes": "The disease spreads through fungal spores, particularly in warm and humid conditions.",
            "treatment": "Remove infected crop debris after harvest and seek local advice about approved disease management.",
            "prevention": "Rotate crops, use resistant varieties where available, and maintain good field hygiene.",
        },
        "common rust": {
            "description": "Common rust is a fungal disease of maize.",
            "symptoms": "Small reddish-brown raised pustules appear on both sides of leaves.",
            "causes": "The disease is caused by a rust fungus and spreads through airborne spores.",
            "treatment": "Monitor disease development and consult local agricultural guidance about resistant varieties and approved treatments.",
            "prevention": "Grow resistant varieties where available and monitor the crop during humid weather.",
        },
        "northern leaf blight": {
            "description": "Northern leaf blight is a fungal disease affecting maize.",
            "symptoms": "Long, cigar-shaped grey-green or brown lesions develop on leaves.",
            "causes": "The disease spreads through fungal spores and infected crop residues.",
            "treatment": "Manage infected residues and consult local agricultural experts about suitable control measures.",
            "prevention": "Use resistant varieties, rotate crops, and maintain field sanitation.",
        },
        "black rot": {
            "description": "Black rot is a fungal disease that can affect crops such as grape and apple.",
            "symptoms": "Brown or black lesions may develop on leaves and fruit. Infected fruit may shrivel.",
            "causes": "The disease spreads from infected plant debris and fungal spores, especially in wet conditions.",
            "treatment": "Remove infected fruit and plant debris where practical. Seek crop-specific local advice for approved treatments.",
            "prevention": "Prune for good airflow, remove mummified fruit, and monitor plants during wet weather.",
        },
        "esca": {
            "description": "Esca is a complex grapevine disease associated with wood-inhabiting fungi.",
            "symptoms": "Leaves may show striped discoloration, drying, or scorched areas. Symptoms can vary between vines.",
            "causes": "The disease is associated with fungal infections in grapevine wood.",
            "treatment": "Prune and manage affected vines with guidance from a viticulture expert. There is no simple universal cure.",
            "prevention": "Use healthy planting material, protect pruning wounds where recommended, and remove severely affected wood appropriately.",
        },
        "scab": {
            "description": "Apple scab is a fungal disease affecting apple leaves and fruit.",
            "symptoms": "Olive-green to dark scabby spots develop on leaves and fruit.",
            "causes": "The fungus overwinters in infected fallen leaves and spreads through spores during wet weather.",
            "treatment": "Remove fallen infected leaves and seek local advice about approved crop protection options.",
            "prevention": "Plant resistant varieties where possible, prune for airflow, and remove infected leaf litter.",
        },
        "citrus greening": {
            "description": "Citrus greening, also called Huanglongbing, is a serious bacterial disease of citrus.",
            "symptoms": "Leaves may show uneven yellow mottling. Fruit can become misshapen, remain green, or taste bitter.",
            "causes": "The disease is associated with bacteria spread by the Asian citrus psyllid.",
            "treatment": "There is no established cure for an infected tree. Contact a local agricultural or plant-health authority for diagnosis and management guidance.",
            "prevention": "Use certified disease-free nursery plants and monitor and manage psyllid populations using locally approved methods.",
        },
        "spider mites": {
            "description": "Spider mites are tiny pests that feed on plant cells.",
            "symptoms": "Leaves may develop fine pale speckles, bronzing, or webbing and can eventually dry out.",
            "causes": "Mite populations can increase rapidly in hot and dry conditions.",
            "treatment": "Inspect the undersides of leaves and seek local advice about suitable mite-management options. Avoid unnecessary broad-spectrum pesticide use.",
            "prevention": "Monitor plants regularly, maintain suitable growing conditions, and conserve beneficial insects.",
        },
        "healthy": {
            "description": "The image was classified as a healthy leaf.",
            "symptoms": "No disease symptoms were identified by this classification result.",
            "causes": "No visible disease pattern was identified in the submitted image.",
            "treatment": "No disease-specific treatment is indicated by this result.",
            "prevention": "Continue regular monitoring, proper irrigation, balanced nutrition, and good field hygiene.",
        },
    }

    selected = next(
        (value for keyword, value in advice.items() if keyword in key),
        None
    )

    if selected is None:
        selected = {
            "description": f"The model classified the submitted leaf as: {name}.",
            "symptoms": "The exact symptoms depend on the crop and disease. Compare the result with the visible leaf symptoms.",
            "causes": "Possible causes vary by disease and may include fungal, bacterial, viral, or pest-related factors.",
            "treatment": "Remove severely damaged plant material where appropriate. Confirm the diagnosis with a local agricultural expert before applying any treatment.",
            "prevention": "Use healthy planting material, maintain proper spacing, avoid unnecessary leaf wetness, remove crop debris, and monitor the crop regularly.",
        }

    return (
        "LOCAL DISEASE ADVICE (offline fallback)\n\n"
        f"Disease: {name}\n\n"
        f"Description: {selected['description']}\n\n"
        f"Symptoms: {selected['symptoms']}\n\n"
        f"Causes: {selected['causes']}\n\n"
        f"Treatment: {selected['treatment']}\n\n"
        f"Prevention: {selected['prevention']}\n\n"
        "Farmer Tips: Monitor the crop regularly. Confirm uncertain diagnoses with a local agriculture expert. Always follow the label and local guidance for any crop protection product."
    )
