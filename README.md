# Qwen2.5-1.5B Fine-Tuned for Mathematical Reasoning

This repository contains a fine-tuned version of [Qwen2.5-1.5B](https://huggingface.co/Qwen/Qwen2.5-1.5B) specifically trained for mathematical reasoning using a step-by-step chain-of-thought approach.

### Model Overview

- **Base Model**: Qwen2.5-1.5B (Decoder-only causal language model)
- **Task**: Mathematical question answering with reasoning
- **Technique**: Chain-of-thought style fine-tuning
- **Fine-Tuning Dataset**: Custom math dataset (GM8K-style format)

### Key Features

### 8-bit Quantization
- **Library**: `bitsandbytes`
- **Purpose**: Reduces memory usage and speeds up inference
- **Benefit**: Enables fine-tuning and inference on limited GPU hardware

### Parameter-Efficient Fine-Tuning (LoRA)
- **Library**: `peft` (Hugging Face)
- **Configuration**:
  - `r=16`, `alpha=32`
  - Target Modules: `q_proj`, `v_proj`
- **Advantage**: Only a small subset of parameters are trained while freezing the original model weights

### Training Details
- Optimizer: `paged_adamw_8bit`
- Learning Rate: `2e-4`
- Epochs: `3`
- Batch Size: `4` (per device)
- Mixed Precision: `fp16`
- Evaluation: Accuracy based on final numerical prediction matching

##  Chain-of-Thought Format

Each input is formatted as:

<|user|>
Solve the following math problem step-by-step:
{question}
<|assistant|>

## Results

| Model           | Accuracy |
|----------------|----------|
| Qwen2.5-1.5B (base)   | 2.3%     |
| Fine-Tuned + LoRA | **6.4%**     |

>  Improvement of 178% over the base model on final answer accuracy

## Files

- `adapter_model.safetensors` – Fine-tuned LoRA adapter
- `adapter_config.json` – LoRA configuration
- `tokenizer.json`, `vocab.json`, etc. – Required tokenizer files



Dataset --> kagglehub.dataset_download("awsaf49/math-dataset")
                
