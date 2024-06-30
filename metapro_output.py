import json
import re

def extract_sentences(text):
    pattern = r'_\$\$PoS\[[^\]]+\]Target\[[^\]]+\]Source\[[^\]]+\]\$\$'
    return re.findall(pattern, text)

with open('company_speech_dataset_metapro.json', 'r') as file:
    data = json.load(file)

samp = {}
count=1
for entry in data:
    for key, value in entry.items():
        samp[value['id']] = extract_sentences(value['metapro_output'])
        print(str(count)+" done so far.")
        count+=1

with open('output_data.json', 'w') as outfile:
    json.dump(samp, outfile, indent=4)

print("Data saved to 'output_data.json'")
