import json
def load_data(dataset,topic, number):
    with open(f'G:/Python/fine_tune_improve_mathematical_reasoning/Qwen2.5-1.5B_Fine-tuning/dataset/MATH/{dataset}/{topic}/{number}.json', 'r', encoding= 'utf-8') as f:
        data = json.load(f)
    return data

