LearnMap AI
An Intelligent Learning Path Generator Powered by Jaseci & Python

LearnMap AI is an intelligent system that generates personalized learning roadmaps based on user goals, current skills, and desired career paths. It leverages a Jaseci knowledge graph to reason about learning nodes and automatically build structured, optimized learning journeys.

🌟 Key Features
✅ AI-Generated Learning Roadmaps

Automatically creates personalized learning paths based on user input.

✅ Jaseci Knowledge Graph Integration

Knowledge stored in nodes and edges enables structured reasoning.

✅ Modular Architecture

Clear separation of nodes, walkers, and driver logic.

✅ Command-Line Demo Runner

Run a full example with one command.

✅ Easy to Deploy

Simple Python + Jaseci environment.

📂 Project Structure
learnmap_ai/
│
├── src/
│   ├── driver.py          # Main entry point
│   ├── nodes.py           # Node definitions
│   ├── walkers.py         # Walker logic
│   ├── jac/               # Jac graph logic
│   ├── requirements.txt   # Python dependencies
│   └── README.md          # Developer docs
│
├── data/
│   └── sample.json        # Example data (optional)
│
└── README.md              # Main GitHub documentation

🛠️ Installation
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/learnmap_ai.git
cd learnmap_ai

2️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Requirements
pip install -r src/requirements.txt

🚀 Running the Project
Basic Run
python src/driver.py

🎥 Demo Video

Add your demo video link here once uploaded:

https://your-demo-link.com

🔧 Technologies Used

Python

Jaseci

Jac Language

Virtualenv

📜 License

MIT License EOQ
