# FactSniffer

Ladies and gentlemen, welcome to the age of misinformation! A time where every outlander idea, no matter how, finds its audience.🤪

Who need facts when you can simply denny reality? 
Nowadays social media has given everyone the power to share their "alternative truths". 📣 
Who cares about evidence when you have a strong opinion, right?
Misinformation can lead to real-world consequences, influencing elections, fueling pandemics and it doesn't stop there; fake news turns people into racists, homophobes.

Fear not, dear friends! We've got FactSniffer, your trustly machine learning algorithm that fight against fake news. Think of it as your personal digital detective.🔍

Let's dive into how FactSniffer works!
I curated data from three diverse datasets:

- 📰 News dataset from Kaggle
- 🦠 Covid news dataset
- 🕵️‍♂️ Scraped data from Politifact's webpage

To better understand Politifact's fact-checking process, I created an interactive dashboard on Tableau. Check it out here: [Fact-checking analysis in Politifact Dashboard](https://public.tableau.com/app/profile/lydia2817/viz/Fact-chekinganalysisinPolitiffact/Dashboard1?publish=yes). You can use the dashboard to compare who lied more between Trump and Biden.

Additionally, I conducted polarity analysis using TextBlob to gauge the sentiment across various statements.



## Project Structure
- `app.py`: Streamlit application for real-time fake news detection.
- `train.py`: Script for training the fake news detection model.
- `requirements.txt`: List of dependencies required to run the project.
- `data/`: Directory containing the datasets used for training and evaluation.
- `packages.txt`: Requirement to process image to text and use streamlit app.

## Instructions to Run the Code and Reproduce the Results

### Step 1: Set Up the Environment
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/FactSniffer.git
   cd FactSniffer
2. **Create and activate the Conda environment::**
      ```sh
   conda create --name FactSniffer python=3.9
   conda activate FactSniffer
3. **Install the required packages:::**
      ```sh
   pip install -r requirements.txt


### Step 2: Trsain the Model
1. **Run the training script:**
   ```sh
   gpython train.py
### Step 2: Run the streamlit application
1. **Launch the streamlit app:**
   ```sh
   gstreamlit run app.py


## Link to my Deployed App:
https://fakene.streamlit.app

### Want to see a demo?

Watch our demo video on YouTube:

[![FactSniffer Demo Video](https://img.youtube.com/vi/rFD8hLvLg9E/0.jpg)](https://www.youtube.com/watch?v=rFD8hLvLg9E)

Click the image above to view the demo.

