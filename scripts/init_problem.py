import shutil
from pathlib import Path
from datetime import datetime, timedelta

def prepend_to_tracker(tracker_file, new_row, prob_id):
    path = Path(tracker_file)
    if not path.exists():
        path.write_text("| Date | Platform | Problem Name | Problem ID | Note/Trick | Resolve Date | Status |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n")
    
    lines = path.read_text().splitlines(keepends=True)
    lines.insert(2, new_row)
    path.write_text("".join(lines))
    print(f"📝 Prepended {prob_id} to tracker.md")

def init_problem():
    print(f"{'-'*11} NEW PROBLEM SETUP {'-'*11}")
    category = input("Category [cf/cp31/kenkooo/atcoder]: ").strip().lower()
    
    now_str = datetime.now().strftime('%Y-%m-%d')
    paths = {
        "cf": lambda: Path("cf") / f"{now_str}_{input('Contest Name: ')}",
        "cp31":    lambda: Path("cp31") / input("Rating: "),
        "kenkooo": lambda: Path("kenkooo") / ("bootcamp" if input("bootcamp[1]/contests[2]: ") == "1" else "contests") / input("Sub-folder/Contest: "),
        "atcoder": lambda: Path("atcoder") / "contests" / f"{now_str}_{input('Contest Name: ')}"
    }
    
    folder_path = paths.get(category, paths["cf"])()
    folder_path.mkdir(parents=True, exist_ok=True)
    
    p_id = input("Problem ID: ").strip().upper()
    slug = input("Short Name: ").strip().lower().replace(" ", "_")
    file_path = folder_path / f"{p_id}_{slug}.py"
            
    template = Path("base/template_iter.py")
    if template.exists():
        shutil.copy(template, file_path)
    else:
        file_path.write_text("# TODO: Implement solution\n")
        
    date_now = datetime.now().strftime('%b %d')
    resolve_date = (datetime.now() + timedelta(days=14)).strftime("%b %d")
    new_row = f"| {date_now} | {category.upper()} | {slug.title()} | {p_id} |  | {resolve_date} | ⏳ |\n"
    
    tracker_file = "tracker.md"
    prepend_to_tracker(tracker_file, new_row, p_id)
    print(f"✅ Created {file_path}")
    
    
if __name__ == "__main__":
    init_problem()