
import re


def get_local_advice(disease: str, confidence=None):

    # Normalize disease name
    disease_name = re.sub(r"[_\s]+", " ", disease).strip()
    key = disease_name.lower()

    advice_database = {

        # TOMATO EARLY BLIGHT
        "tomato early blight": {
            "description": "Tomato Early Blight is a fungal disease caused by Alternaria solani. It commonly affects leaves, stems and sometimes fruits. The disease usually begins on older leaves and can reduce plant health and fruit production if not managed properly.",

            "symptoms": "Dark brown circular spots with characteristic concentric rings may develop on older leaves. Yellow areas often surround the spots. As the disease progresses, affected leaves may turn yellow, dry and fall prematurely.",

            "causes": "The disease is caused by Alternaria solani. It can spread through infected crop debris, contaminated seeds and spores carried by wind or splashing water. Warm temperatures, humidity and prolonged leaf wetness encourage infection.",

            "treatment": "Remove severely infected leaves and safely dispose of infected plant material. Avoid working with wet plants because this can spread spores. Use only locally approved fungicides according to product labels and agricultural expert recommendations.",

            "prevention": "Practice crop rotation, maintain proper plant spacing, remove infected crop debris and avoid overhead irrigation. Use healthy seeds and maintain balanced plant nutrition.",

            "tips": "Inspect older leaves regularly because early blight often appears there first. Early identification and proper field management can help reduce disease spread."
        },


        # TOMATO LATE BLIGHT
        "tomato late blight": {
            "description": "Tomato Late Blight is a destructive disease caused by the oomycete pathogen Phytophthora infestans. It affects tomato leaves, stems and fruits and can spread rapidly during cool, humid and wet weather. Severe infections can damage the entire plant and cause significant crop losses.",

            "symptoms": "The disease initially produces irregular, water-soaked, pale green or dark brown patches on leaves. These patches may enlarge rapidly and turn brown or black. Under humid conditions, white cotton-like growth may appear around the edges of infected areas on the underside of leaves. Dark lesions may also develop on stems, while fruits can develop large, firm, brown or greasy-looking patches.",

            "causes": "The disease is caused by Phytophthora infestans. It spreads through airborne spores, infected plant material and splashing rainwater. Cool temperatures, high humidity, frequent rainfall and prolonged leaf wetness create favorable conditions for infection.",

            "treatment": "Remove and safely dispose of infected leaves, stems and fruits where appropriate. Avoid handling wet plants because moisture can encourage disease spread. Consult a local agricultural expert promptly about suitable disease management. Use only locally registered fungicides according to their product labels.",

            "prevention": "Use healthy seedlings, maintain proper spacing and ensure good air circulation. Avoid overhead irrigation and prolonged leaf wetness. Remove infected crop residues, manage volunteer tomato and potato plants, and inspect crops regularly, especially during humid weather.",

            "tips": "Inspect tomato plants frequently for water-soaked patches and rapidly spreading dark lesions. Late blight can progress quickly under favorable weather conditions, so early identification and timely management are essential. Seek expert confirmation if symptoms are uncertain."
        },


        # POTATO EARLY BLIGHT
        "potato early blight": {
            "description": "Potato Early Blight is a fungal disease caused by Alternaria solani. It mainly affects potato leaves but can also affect stems and tubers. The disease is more common under warm conditions and can reduce the plant's ability to produce healthy tubers.",

            "symptoms": "Small dark brown spots generally appear on older leaves. These spots may develop concentric rings resembling a target pattern and are often surrounded by yellow areas. Severely affected leaves gradually turn yellow, dry and fall.",

            "causes": "The disease is caused by Alternaria solani. The fungus survives in infected plant debris and can spread through wind, rain splash and contaminated plant material. Warm weather, moisture and plant stress can encourage disease development.",

            "treatment": "Remove severely affected leaves and dispose of infected plant debris safely. Maintain proper irrigation and avoid unnecessary leaf wetness. Consult a local agricultural expert about suitable fungicide management and use only locally approved products according to their labels.",

            "prevention": "Use healthy seed potatoes, practice crop rotation and maintain proper spacing between plants. Remove infected crop residues, control weeds and maintain balanced soil nutrition. Avoid excessive irrigation.",

            "tips": "Regularly inspect older potato leaves for brown spots with concentric rings. Early detection and timely management can help protect healthy foliage and reduce crop damage."
        },


        # POTATO LATE BLIGHT
        "potato late blight": {
            "description": "Potato Late Blight is a destructive disease caused by Phytophthora infestans. It primarily affects potato leaves, stems and tubers. The disease can spread rapidly under cool and humid weather conditions and may cause significant crop losses if not managed early.",

            "symptoms": "Initial symptoms include irregular, water-soaked, pale green or dark brown patches on leaves. Under moist conditions, white cotton-like growth may develop around the edges of infected areas on the underside of leaves. Infected leaves gradually turn brown, wilt and decay. Dark or discolored lesions may also develop on potato tubers.",

            "causes": "The disease is caused by Phytophthora infestans, a pathogen that spreads through infected plant material, airborne spores and splashing rainwater. Cool temperatures, high humidity and prolonged leaf wetness favor disease development.",

            "treatment": "Immediately remove and safely dispose of infected plant parts where appropriate. Avoid moving infected plant material between fields. Consult a local agricultural expert about suitable disease management. Use only locally registered and approved products according to their labels.",

            "prevention": "Plant certified disease-free seed potatoes, maintain proper spacing and ensure good field drainage. Avoid excessive irrigation and prolonged leaf wetness. Remove volunteer potato plants and infected crop residues. Monitor crops regularly.",

            "tips": "Inspect potato plants frequently, especially during cool and humid weather. Early identification and timely management are important because late blight can spread quickly. Seek agricultural expert confirmation if symptoms are uncertain."
        },


        # TOMATO HEALTHY
        "tomato healthy": {
            "description": "The AI-based crop disease detection system has classified the submitted tomato leaf image as Healthy. The image does not show prominent visual symptoms associated with the tomato diseases included in the model's classification categories. This indicates that the leaf appears healthy at the time of image analysis.",

            "symptoms": "The leaf appears generally green and structurally healthy, without obvious disease-associated spots, lesions, yellowing, wilting or visible fungal growth in the submitted image.",

            "causes": "No specific disease-causing pathogen has been identified by the model prediction. The healthy classification indicates that the visible leaf features most closely match the healthy tomato category in the trained dataset.",

            "treatment": "No disease-specific treatment is indicated based on this prediction. Continue normal crop maintenance, provide balanced nutrients and maintain an appropriate watering schedule. Avoid unnecessary pesticide or fungicide applications.",

            "prevention": "Maintain proper plant spacing, provide adequate sunlight and air circulation, use healthy planting material and remove dead plant debris. Monitor irrigation and maintain good field hygiene to reduce the risk of future infections.",

            "tips": "Continue inspecting tomato leaves, stems and fruits regularly. A healthy prediction applies only to the submitted image and does not guarantee that the entire plant or crop is free from disease. If new symptoms appear, capture another clear image and seek expert advice when necessary."
        },


        # POTATO HEALTHY
        "potato healthy": {
            "description": "The AI-based crop disease detection system has classified the submitted potato leaf image as Healthy. No prominent visual symptoms associated with the potato diseases included in the model's classification categories were identified in the submitted image.",

            "symptoms": "The leaf appears generally green and healthy, without obvious dark lesions, concentric spots, unusual yellowing, wilting or visible signs of infection.",

            "causes": "No specific disease-causing pathogen has been identified by the model prediction. The image features most closely match the healthy potato category in the trained dataset.",

            "treatment": "No disease-specific treatment is indicated based on this prediction. Continue regular crop maintenance, provide balanced nutrients and follow an appropriate irrigation schedule. Avoid unnecessary chemical applications.",

            "prevention": "Use healthy seed potatoes, maintain proper plant spacing, ensure good drainage and remove infected crop debris. Practice crop rotation and maintain proper field hygiene.",

            "tips": "Inspect potato leaves and stems regularly throughout the growing season. This prediction applies only to the submitted image and does not guarantee that the entire plant or field is disease-free."
        },


        # PEPPER BELL HEALTHY
        "pepper bell healthy": {
            "description": "The AI-based crop disease detection system has classified the submitted bell pepper leaf image as Healthy. No prominent visual symptoms associated with the bell pepper diseases included in the model's classification categories were identified.",

            "symptoms": "The leaf appears generally green and healthy, without obvious bacterial spots, unusual discoloration, lesions, wilting or visible fungal growth.",

            "causes": "No specific disease-causing pathogen has been identified by the model prediction. The image features most closely match the healthy bell pepper category in the trained dataset.",

            "treatment": "No disease-specific treatment is indicated based on this prediction. Continue normal crop maintenance, maintain balanced soil nutrition and provide an appropriate watering schedule.",

            "prevention": "Use healthy planting material, maintain proper plant spacing and air circulation, remove infected plant debris and avoid excessive moisture on leaves. Maintain good field hygiene.",

            "tips": "Inspect leaves, stems and fruits regularly. A healthy prediction applies only to the submitted image and does not guarantee that the entire plant is disease-free."
        }

    }


    # Get disease-specific advice
    data = advice_database.get(key)


    if data:

        description = data["description"]
        symptoms = data["symptoms"]
        causes = data["causes"]
        treatment = data["treatment"]
        prevention = data["prevention"]
        tips = data["tips"]

    else:

        description = f"{disease_name} was identified as the closest matching category by the crop disease prediction model."

        symptoms = "Visible symptoms may vary depending on the crop and disease. The submitted image should be examined carefully for disease-specific signs."

        causes = "The exact cause depends on the identified disease. Further confirmation may be necessary."

        treatment = "Consult a local agricultural expert for disease-specific treatment. Use only locally approved crop protection products according to their labels."

        prevention = "Use healthy planting material, maintain proper spacing, ensure good field hygiene and monitor crops regularly."

        tips = "Confirm uncertain predictions with an agricultural expert before applying any crop protection product."


    # Prediction confidence
    confidence_text = (
        f"\nPrediction Confidence: {confidence}%"
        if confidence is not None else ""
    )


    # Generate final report
    return f"""
==================================================
       AI-BASED CROP DISEASE ANALYSIS REPORT
==================================================

Predicted Disease: {disease_name}{confidence_text}

--------------------------------------------------
1. DISEASE DESCRIPTION
--------------------------------------------------
{description}

--------------------------------------------------
2. SYMPTOMS
--------------------------------------------------
{symptoms}

--------------------------------------------------
3. POSSIBLE CAUSES
--------------------------------------------------
{causes}

--------------------------------------------------
4. RECOMMENDED TREATMENT
--------------------------------------------------
{treatment}

--------------------------------------------------
5. PREVENTION MEASURES
--------------------------------------------------
{prevention}


==================================================
Generated By: AI Crop Disease Detection System
==================================================


"""
