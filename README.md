
# 🏆 Club Recommendation System

A web application that recommends top-rated clubs based on selected skills using **Streamlit** for the frontend and **Flask** for a REST API backend. The system merges club skillsets and rating datasets to offer personalized recommendations.

---

## 🚀 Features

- 🔍 Skill-based club recommendation engine.
- 🎨 Interactive user interface with Streamlit.
- 🌐 Flask-based REST API for external usage (e.g., Postman).
- 📊 Dynamic dataset merging and sorting based on rating.
- 🖼️ Club images and ratings shown in a visually appealing card layout.

---

## 📁 Project Structure

```
📦 Club-Recommendation-System
├── Dataset/
│   ├── Club_Skills_Dataset_Extended.xlsx
│   └── Ratings_dataset.xlsx
├── app.py
├── README.md
```

---

## 📦 Dependencies

Make sure you have the following libraries installed:

```bash
pip install pandas streamlit flask openpyxl
```

---

## 🧠 How It Works

1. **Data Loading & Preprocessing**:
   - Loads skill and rating data from Excel files.
   - Strips and renames columns to ensure clean merges.

2. **Recommendation Logic**:
   - Filters clubs based on selected skill.
   - Sorts them by rating and returns top 5.

3. **Flask API**:
   - Accepts a `POST` request with a skill.
   - Returns JSON response with recommended clubs.

4. **Streamlit UI**:
   - User selects a skill via dropdown.
   - Recommendations are shown as cards with images and ratings.

---

## 🌐 Flask API Endpoint

### `POST /predict`

**Request Body**:
```json
{
  "skill": "Python"
}
```

**Response**:
```json
{
  "recommended_clubs": [
    {
      "Club Name": "Tech Enthusiasts",
      "image_url": "https://example.com/image.jpg",
      "Rating": 4.8
    },
    ...
  ]
}
```

> The Flask API runs in a background thread on port `5000`.

---

## 📺 Streamlit Web Interface

To launch the UI:
-To view the live 
```bash
ahas2711-clubrecommandation-app-nx54uh.streamlit.app
```

-To run on your own System

```bash
streamlit run app.py
```

You can then use the interactive UI to:

- Select a skill.
- Click **Get Recommendations**.
- View top clubs with matching skills and their ratings.

---

## 📌 Notes

- Ensure the `Dataset` folder contains the required Excel files.
- The image URLs must be accessible online to be rendered correctly in Streamlit.
- Flask and Streamlit run together via multithreading.

---

## 🛠️ Future Enhancements

- ✅ Add filtering by multiple skills.
- 📈 Include sorting/filtering by other metrics (e.g., popularity).
- 💬 Add feedback submission for users.

---

## 🧑‍💻 Author

**Sahas Nagar**  
Computer Engineering, MIT  
[Portfolio](https://sahas2711.github.io/Sahas_Portfolio/)

---

## 📄 License

MIT License - feel free to use and modify.
