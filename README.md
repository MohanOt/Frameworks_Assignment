# 📊 CORD-19 Metadata Analysis Setup & Execution

# 1. Clone your assignment repository from GitHub
git clone https://github.com/YOURUSERNAME/Frameworks_Assignment.git

# 2. Move into the project folder
cd Frameworks_Assignment

# 3. Create a virtual environment (this keeps dependencies isolated)
python3 -m venv venv

# 4. Activate the virtual environment
#    Use the correct command depending on your OS:
source venv/bin/activate         # macOS/Linux
# .\venv\Scripts\Activate.ps1    # Windows PowerShell

# 5. Install all required Python libraries
pip install pandas matplotlib seaborn wordcloud streamlit notebook

# 6. Download the dataset (metadata.csv) from Kaggle manually
#    Link: https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge
#    Place metadata.csv inside the Frameworks_Assignment folder

# 7. Run the Jupyter Notebook for data exploration & cleaning
jupyter notebook cord19_analysis.ipynb

#    Inside the notebook you will:
#    - Load and explore metadata.csv
#    - Clean missing values
#    - Convert dates and extract years
#    - Generate visualizations (publications per year, top journals, word cloud)

# 8. Run the Streamlit web app for interactive exploration
streamlit run app.py

#    If 'streamlit' command is not found, run it like this:
python -m streamlit run app.py

# 9. After finishing, deactivate the virtual environment
deactivate


# 📑 Notes:
# - Always activate the venv before running notebook or app
# - Use jupyter for analysis, streamlit for interactive app
# - Push your work to GitHub when done