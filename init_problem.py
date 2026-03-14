import shutil
import os
import sys
from datetime import datetime, timedelta

def init_problem():
    print("----------- NEW PROBLEM SETUP -------------")
    category = input("Please enter the category: (contest/cp31): ").strip().lower()
    
    if category == "contest":
        name = input("Contest Name (e.g Div3_940): ").strip()
        folder_path = os.path.join("contests", f"{datetime.now().strftime('%Y-%m-%d')}_{name}")
    else:
        rating = input("Rating (800/900/1000...): ").strip()
        folder_path = os.path.join("cp31", rating)
            
    prob_id = input("Problem ID (e.g 1901A): ").strip().upper()
    prob_slug = input("Short Name (e.g line_trip): ").strip().lower().replace(" ", "_")
    
    filename = f"{prob_id}_{prob_slug}.py"
    
    os.makedirs(folder_path, exist_ok=True)
    full_path = os.path.join(folder_path, filename)
    
    template_path = "base/template.py"
    if os.path.exists(template_path):
        shutil.copy(template_path, full_path)
        print(f"✅ Created {full_path} from template.")
    else:
        with open(full_path, "w") as f:
            f.write("# TODO: Implement solution\n")
        print(f"⚠️ template.py not found. Created empty file at {full_path}.")
        
    date_now = datetime.now().strftime('%b %d')
    resolve_date = (datetime.now() + timedelta(days=14)).strftime("%b %d")
    new_row = f"| {date_now} | {category.upper()} | {prob_slug.title()} | {prob_id} |  | {resolve_date} | ⏳ |\n"
    
    tracker_file = "tracker.md"
    with open(tracker_file, "a") as f:
        f.write(new_row)
    print(f"📝 Appended {prob_id} to tracker.md")
    
if __name__ == "__main__":
    init_problem()