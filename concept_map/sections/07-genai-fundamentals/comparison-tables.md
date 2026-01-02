# Section 7: Generative AI Model Fundamentals - Comparison Tables

## Architecture Comparisons

### RNN vs Transformer

| Aspect | RNN/LSTM | Transformer |
|--------|----------|-------------|
| **Processing** | Sequential (token by token) | Parallel (all tokens at once) |
| **Context** | Hidden state (bottleneck) | Self-attention (all tokens) |
| **Training Speed** | Slow (can't parallelize) | Fast (parallelizable) |
| **Long Sequences** | Struggles (vanishing gradient) | Handles well |
| **Scalability** | Limited | Billions of parameters |
| **Memory** | Lower | Higher |

---

### Transformer Architecture Types

| Architecture | Components | Example Models | Best For |
|--------------|------------|----------------|----------|
| **Encoder-only** | Encoders only | BERT, RoBERTa, DistilBERT | Understanding, classification, NER |
| **Decoder-only** | Decoders only | GPT, Claude, LLaMA | Text generation, chat, completion |
| **Encoder-Decoder** | Both | T5, BART, mT5 | Translation, summarization |

### When to Use Each Architecture

| Task | Recommended Architecture | Why |
|------|-------------------------|-----|
| Sentiment analysis | Encoder-only (BERT) | Needs understanding, not generation |
| Text generation | Decoder-only (GPT) | Autoregressive generation |
| Chatbot | Decoder-only (GPT, Claude) | Generate responses |
| Translation | Encoder-Decoder (T5) | Understand source, generate target |
| Summarization | Encoder-Decoder (T5) | Understand document, generate summary |
| Named Entity Recognition | Encoder-only (BERT) | Token classification |
| Question Answering | Either | Depends on format |

---

## Self-Attention Components

### Q, K, V Matrices

| Matrix | Full Name | Purpose | Analogy |
|--------|-----------|---------|---------|
| **Q** | Query | What am I looking for? | Search query |
| **K** | Key | What do I contain? | Index entry |
| **V** | Value | What information do I provide? | Content |

### Self-Attention vs Masked Self-Attention

| Aspect | Self-Attention | Masked Self-Attention |
|--------|----------------|----------------------|
| **Visibility** | All tokens see all tokens | Tokens can't see future tokens |
| **Used In** | Encoders (BERT) | Decoders (GPT) |
| **Purpose** | Bi-directional understanding | Autoregressive generation |

---

## LLM Parameters

### Sampling Parameters

| Parameter | Definition | Low Value Effect | High Value Effect |
|-----------|------------|------------------|-------------------|
| **Temperature** | Randomness in token selection | Predictable, focused | Creative, diverse |
| **Top P** | Cumulative probability threshold | Conservative, fewer options | Exploratory, more options |
| **Top K** | Number of top candidates | Very focused | More variety |

### When to Use Each Setting

| Use Case | Temperature | Top P | Top K |
|----------|-------------|-------|-------|
| **Factual Q&A** | Low (0.1-0.3) | Low (0.5-0.7) | Low (10-20) |
| **Creative Writing** | High (0.7-1.0) | High (0.9-1.0) | High (50+) |
| **Code Generation** | Low-Medium (0.2-0.5) | Medium (0.7-0.9) | Medium (20-40) |
| **Chat/Conversation** | Medium (0.5-0.7) | Medium (0.8-0.95) | Medium (30-50) |

### Size Parameters

| Parameter | Definition | Impact |
|-----------|------------|--------|
| **Context Window** | Max tokens model can process | Limits input + output total |
| **Max Tokens** | Limit for output length | Controls response length |
| **Max Input Tokens** | Limit for input length | May need to truncate |

---

## Foundation Models

### Major Foundation Models

| Model | Provider | Architecture | Parameters | Specialty |
|-------|----------|--------------|------------|-----------|
| GPT-4 | OpenAI | Decoder-only | ~1.7T (est.) | Reasoning, general |
| Claude | Anthropic | Decoder-only | Large | Safety, long context |
| BERT | Google | Encoder-only | 340M | Understanding |
| T5 | Google | Enc-Dec | 11B | Multi-task |
| LLaMA 2 | Meta | Decoder-only | 7B-70B | Open weights |
| Falcon | TII | Decoder-only | 7B-180B | Open source |

### AWS Bedrock Models

| Model | Provider | Type | Best For |
|-------|----------|------|----------|
| **Claude** | Anthropic | Text LLM | Conversations, Q&A, analysis |
| **Jurassic-2** | AI21 Labs | Text LLM | Multilingual (6 languages) |
| **Stable Diffusion** | Stability.ai | Image | Art, logos, design |
| **Llama** | Meta | Text LLM | General purpose |
| **Amazon Titan** | Amazon | Text/Embedding | Summarization, search, embeddings |

### Amazon Titan Variants

| Variant | Purpose | Use Case |
|---------|---------|----------|
| Titan Text | Text generation | Summarization, Q&A |
| Titan Embeddings | Vector embeddings | Semantic search, RAG |
| Titan Multimodal | Text + Image | Image understanding |

---

## AWS GenAI Services

### Bedrock vs SageMaker JumpStart

| Aspect | Bedrock | SageMaker JumpStart |
|--------|---------|---------------------|
| **Access Type** | API | Notebook |
| **Infrastructure** | Fully managed | SageMaker managed |
| **Customization** | Limited fine-tuning | Full fine-tuning |
| **Use Case** | Quick integration | Custom development |
| **Models** | Curated set | Broader selection |
| **Pricing** | Per-token | Instance-based |

### When to Use Each Service

| Scenario | Recommended Service |
|----------|---------------------|
| Quick prototype with API | Bedrock |
| Production application with API | Bedrock |
| Custom fine-tuning needed | SageMaker JumpStart |
| Need Jupyter notebooks | SageMaker JumpStart |
| Want Hugging Face models | SageMaker JumpStart |
| Minimal infrastructure management | Bedrock |

---

## Fine-Tuning Approaches

### Transfer Learning Methods for LLMs

| Method | Description | When to Use |
|--------|-------------|-------------|
| **Full Fine-tuning** | Train entire model | Large dataset, major domain shift |
| **Freeze + Retrain** | Freeze base, train top layers | Limited data, similar domain |
| **LoRA/QLoRA** | Low-rank adaptation | Efficient fine-tuning |
| **Prompt Tuning** | Learn soft prompts | Very limited data |
| **RLHF** | Reinforcement learning from human feedback | Alignment, safety |

### Fine-Tuning Data Requirements

| Method | Data Needed | Compute Needed |
|--------|-------------|----------------|
| Full Fine-tuning | Large (10K+) | Very High |
| Freeze + Retrain | Medium (1K+) | Medium |
| LoRA | Small (100+) | Low |
| Prompt Tuning | Very Small (10+) | Very Low |

---

## Quick Decision Tables

### Which Architecture?

| Question | Answer |
|----------|--------|
| Need to understand/classify text? | Encoder-only (BERT) |
| Need to generate text? | Decoder-only (GPT) |
| Need translation/summarization? | Encoder-Decoder (T5) |
| Building a chatbot? | Decoder-only (GPT, Claude) |

### Which Temperature?

| Question | Answer |
|----------|--------|
| Need consistent, factual answers? | Low (0.1-0.3) |
| Need creative, varied output? | High (0.7-1.0) |
| Balanced for conversation? | Medium (0.5-0.7) |

### Which AWS Service?

| Question | Answer |
|----------|--------|
| Just need API access to models? | Bedrock |
| Need notebook environment? | SageMaker JumpStart |
| Need to fine-tune model? | SageMaker JumpStart |
| Want minimal setup? | Bedrock |
| Need Hugging Face models? | SageMaker JumpStart |

### Which Bedrock Model?

| Question | Answer |
|----------|--------|
| Best for conversation/reasoning? | Claude |
| Need multilingual support? | Jurassic-2 |
| Need image generation? | Stable Diffusion |
| Need embeddings for search? | Amazon Titan |
| Want open-weight model? | Llama |
