import json

with open('ck3wikiscraper/tenets.json', 'r', encoding='utf-8') as f:
    tenets = json.load(f)

pairs = []

for tenet in tenets:
    name = tenet['name']
    effects = tenet['effects']
    requirements = tenet['requirements']

    # Advisor-style response for effects
    if effects:
        effect_lines = []
        for e in effects:
            if e['value']:
                effect_lines.append(f"- **{e['value']}** {e['description']}")
            else:
                effect_lines.append(f"- {e['description']}")
        effect_str = "\n".join(effect_lines)
        response = (
            f"Noble ruler, the **{name}** tenet bestows the following effects upon your faith:\n"
            f"{effect_str}\n"
            f"Would you like to know the requirements to adopt this tenet, or compare it to another?"
        )
        pairs.append({
            "prompt": f"What does the {name} tenet do?",
            "response": response
        })

    # Advisor-style response for requirements
    if requirements:
        req_str = "; ".join(requirements)
        response = (
            f"To embrace the **{name}** tenet, you must meet these requirements: {req_str}.\n"
            f"Should you seek further counsel on its strategic value or synergy with other tenets, do ask."
        )
        pairs.append({
            "prompt": f"What are the requirements for the {name} tenet?",
            "response": response
        })

with open('tenet_pairs.jsonl', 'w', encoding='utf-8') as f:
    for pair in pairs:
        f.write(json.dumps(pair, ensure_ascii=False) + '\n')

print(f"Generated {len(pairs)} prompt-response pairs in advisor style.")