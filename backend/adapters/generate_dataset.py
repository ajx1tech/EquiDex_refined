import pandas as pd
import random
from faker import Faker

fake = Faker()
ethnicities = ["Caucasian", "African American", "Hispanic", "East Asian", "South Asian", "Middle Eastern"]
age_groups = ["18-25", "26-35", "36-45", "46-55", "56+"]
candidates = []

print("Generating 10,000 candidate profiles...")

for _ in range(10000):
    eth = random.choice(ethnicities)
    age = random.choice(age_groups)
    qual_score = round(random.uniform(65.0, 99.0), 1)
    
    # Injecting intentional bias against specific groups so the AI can catch it
    decision_threshold = 80.0
    if eth in ["Hispanic", "Middle Eastern", "African American"]:
        decision_threshold = 88.0 
    if age in ["46-55", "56+"]:
        decision_threshold += 3.0 
        
    decision = "Accepted" if qual_score >= decision_threshold else "Rejected"

    candidates.append({
        "name": fake.name(),
        "age_group": age,
        "ethnicity": eth,
        "experience": round(random.uniform(1.0, 20.0), 1),
        "qualification_score": qual_score,
        "decision": decision
    })

df = pd.DataFrame(candidates)
df.to_csv("equidex_massive_dataset.csv", index=False)
print("Saved! Ready for upload.")