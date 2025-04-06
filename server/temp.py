labels={'American_Bollworm_on_Cotton': 0,
 'Anthracnose_on_Cotton': 1,
 'Apple___Apple_scab': 2,
 'Apple___Black_rot': 3,
 'Apple___Cedar_apple_rust': 4,
 'Apple___healthy': 5,
 'Army_worm': 6,
 'Becterial_Blight_in_Rice': 7,
 'Blueberry___healthy': 8,
 'Brownspot': 9,
 'Cherry_(including_sour)___Powdery_mildew': 10,
 'Cherry_(including_sour)___healthy': 11,
 'Common_Rust': 12,
 'Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot': 13,
 'Corn_(maize)___Common_rust_': 14,
 'Corn_(maize)___Northern_Leaf_Blight': 15,
 'Corn_(maize)___healthy': 16,
 'Cotton_Aphid': 17,
 'Flag_Smut': 18,
 'Grape___Black_rot': 19,
 'Grape___Esca_(Black_Measles)': 20,
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 21,
 'Grape___healthy': 22,
 'Gray_Leaf_Spot': 23,
 'Healthy_Maize': 24,
 'Healthy_Wheat': 25,
 'Healthy_cotton': 26,
 'Leaf_Curl': 27,
 'Leaf_smut': 28,
 'Mosaic_sugarcane': 29,
 'Orange___Haunglongbing_(Citrus_greening)': 30,
 'Peach___Bacterial_spot': 31,
 'Peach___healthy': 32,
 'Pepper,_bell___Bacterial_spot': 33,
 'Pepper,_bell___healthy': 34,
 'Potato___Early_blight': 35,
 'Potato___Late_blight': 36,
 'Potato___healthy': 37,
 'Raspberry___healthy': 38,
 'RedRot_sugarcane': 39,
 'RedRust_sugarcane': 40,
 'Rice_Blast': 41,
 'Soybean___healthy': 42,
 'Squash___Powdery_mildew': 43,
 'Strawberry___Leaf_scorch': 44,
 'Strawberry___healthy': 45,
 'Sugarcane_Healthy': 46,
 'Tomato___Bacterial_spot': 47,
 'Tomato___Early_blight': 48,
 'Tomato___Late_blight': 49,
 'Tomato___Leaf_Mold': 50,
 'Tomato___Septoria_leaf_spot': 51,
 'Tomato___Spider_mites_Two-spotted_spider_mite': 52,
 'Tomato___Target_Spot': 53,
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 54,
 'Tomato___Tomato_mosaic_virus': 55,
 'Tomato___healthy': 56,
 'Tungro': 57,
 'Wheat_Brown_leaf_Rust': 58,
 'Wheat_Stem_fly': 59,
 'Wheat___Yellow_Rust': 60,
 'Wheat_aphid': 61,
 'Wheat_black_rust': 62,
 'Wheat_leaf_blight': 63,
 'Wheat_mite': 64,
 'Wheat_powdery_mildew': 65,
 'Wheat_scab': 66,
 'Wilt': 67,
 'Yellow_Rust_Sugarcane': 68,
 'bacterial_blight_in_Cotton': 69,
 'bollrot_on_Cotton': 70,
 'bollworm_on_Cotton': 71,
 'cotton_mealy_bug': 72,
 'cotton_whitefly': 73,
 'maize_ear_rot': 74,
 'maize_fall_armyworm': 75,
 'maize_stem_borer': 76,
 'pink_bollworm_in_cotton': 77,
 'red_cotton_bug': 78,
 'thirps_on__cotton': 79}

def getData(result):
    label_name = list(labels.keys())[list(labels.values()).index(result)]
    parts = str(label_name).split('___')  # Most names use '___' to separate crop and disease

    if len(parts) == 2:
        crop, disease = parts
    elif "healthy" in label_name.lower():
        crop = label_name.replace("___healthy", "").replace("_", " ")
        disease = "Healthy"
    else:
        # Fallback for any irregular cases
        crop = "Unknown"
        disease = label_name.replace("_", " ")

    return [crop.strip().replace("_", " "), disease.strip().replace("_", " ")]

if __name__=="__main__":
    print(getData(0))
