# sign_easy
main aim :-
[YouTube Video]
↓
[Extract Audio → Transcribe to Text]
↓
[Text → Gloss → Sign Paths or Pose Data]
↓
▶️ Option A: Python → Web Avatar (SignLanguageAvatar3D)
▶️ Option B: Python → Pose2Sign → Animated keypoints

how to arrange these files in folder
Sign_easY/ ← this is your_project_folder/
├── main.py ← your main Python script
├── requirements.txt ← (optional)
├── models/ ← folder to store Vosk models
│ └── vosk-model-small-en-us-0.15/ ← extracted Vosk model folder
│ ├── am/
│ ├── conf/
│ ├── graph/
│ └── README
└── utils/
└── helper_functions.py ← (optional extra code)
