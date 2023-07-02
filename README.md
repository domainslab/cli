#### AI-based domain generation

`python finder.py search 'an ai-powered mental health app for ADHD students'`
```
[ChatGPT] => Model gpt-4 is not available for provided API key. Reverting to gpt-3.5-turbo. Sign up for the GPT-4 wait list here: https://openai.com/waitlist/gpt-4-api
[ChatGPT] => Using prompt => You are a smart start up founder with a background in SEO optimization. Please come up with a 10 most catchy domain names using following top level domains .com, .ai, .io for an ai-powered mental
health app for ADHD students
[GoDaddy] => ❌ FocusAI.com is NOT available
[GoDaddy] => ✅ MindMender.ai is available
[GoDaddy] => ❌ BrainBoost.io is NOT available
[GoDaddy] => ✅ StudySmartAI.com is available
[GoDaddy] => ✅ ADHDHelper.ai is available
[GoDaddy] => ✅ NeuroNurture.io is available
[GoDaddy] => ❌ CognitiveCoach.com is NOT available
[GoDaddy] => ❌ BrainWave.ai is NOT available
[GoDaddy] => ❌ SmartStudy.io is NOT available
[GoDaddy] => ❌ MindfulMentor.com is NOT available
```

#### Setup
1. `pip install -r requirements.txt`
2. Copy `env.example` to `.env` and fill with your credentials

#### Commands

- `python finder.py --help` to list commands
- `python finder.py check-domain [domain]` to check whether domain is taken
- `python finder.py search [keyword]` to perform AI-based search
