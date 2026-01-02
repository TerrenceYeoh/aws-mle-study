# Section 7: Generative AI Model Fundamentals

## Overview

This section covers the transformer architecture, self-attention mechanism, Large Language Models (LLMs), and AWS services for generative AI.

**Key Takeaways:**
- Transformers replaced RNNs using self-attention for parallelizable training
- Self-attention uses Query, Key, Value matrices to compute contextual embeddings
- GPT is decoder-only; BERT is encoder-only; T5 uses both
- LLM parameters: temperature, top-p, top-k control output randomness
- AWS Bedrock provides access to foundation models; JumpStart for notebooks

---

## Core Concepts

### Transformer-Architecture

**The Key Innovation:** "Attention is All You Need" (2017)

**Evolution:**
1. RNN/LSTM: Sequential processing, information bottleneck
2. Attention mechanism: Hidden state per token, but still sequential
3. **Transformers:** Replace RNNs with FFNNs + self-attention = parallelizable

**Why Transformers Won:**
- Process entire sequence at once (not word-by-word)
- Parallelizable → train on much more data
- Better handling of long-range dependencies
- Scales to hundreds of billions of parameters

**Related:** [[07-genai-fundamentals#Self-Attention]], [[07-genai-fundamentals/07-genai-fundamentals#RNN]], [[07-genai-fundamentals/07-genai-fundamentals#LSTM]], [[07-genai-fundamentals/07-genai-fundamentals#GPT]]

---

### Self-Attention

**Purpose:** Create contextual embeddings that capture word meaning in context

**Example:** "novel" means different things in:
- "I read a good novel" → book
- "Attention is a novel idea" → original

**The Q, K, V Mechanism:**

| Matrix | Purpose | Analogy |
|--------|---------|---------|
| **Query (Q)** | What am I looking for? | Search query |
| **Key (K)** | What do I contain? | Index/label |
| **Value (V)** | What information do I provide? | Content |

**Process:**
```
1. Compute q, k, v for each token (embedding × weight matrices)
2. Score = dot product of query with each key
3. Apply softmax to normalize scores
4. Weighted sum of values = new contextual embedding
```

**Formula:** Attention(Q,K,V) = softmax(QK^T / √d_k) × V

**Related:** Multi-Head-Attention, Masked-Attention, Positional-Encoding

---

### Masked-Self-Attention

**Purpose:** Prevent tokens from seeing future tokens during training

| Model | Approach |
|-------|----------|
| **GPT** | Masked self-attention (can't see future) |
| **BERT** | Masked language modeling (predict masked tokens) |

**Effect:** Ensures autoregressive generation (each token depends only on previous)

**Related:** [[07-genai-fundamentals/07-genai-fundamentals#GPT]], [[07-genai-fundamentals/07-genai-fundamentals#BERT]], [[07-genai-fundamentals#Self-Attention]]

---

### Multi-Head-Attention

**Concept:** Run multiple self-attention operations in parallel

**How:**
- Reshape q, k, v vectors into matrices
- Each row = one "head"
- Process heads in parallel

**Benefits:**
- Different heads learn different relationship types
- Increased parallelization
- Richer representations

**Related:** [[07-genai-fundamentals#Self-Attention]], Transformer-Architecture

---

### GPT-Architecture

**Generative Pre-Trained Transformer**

**Structure:** Decoder-only (stacks of decoder blocks)

```
Input Tokens
    ↓
Token Embedding + Positional Encoding
    ↓
┌─────────────────────┐
│   Decoder Block     │ ×N
│  ┌───────────────┐  │
│  │ Masked Self-  │  │
│  │   Attention   │  │
│  └───────────────┘  │
│  ┌───────────────┐  │
│  │ Feed-Forward  │  │
│  │      NN       │  │
│  └───────────────┘  │
└─────────────────────┘
    ↓
Token Probabilities (Logits)
```

**Key Insight:** No input/output distinction
- Learns language by predicting next token
- Prompt = initial tokens; model continues generating
- Enables training on unlabeled text

**Related:** Decoder-Only, [[07-genai-fundamentals#Foundation-Models]], LLM

---

### LLM-Processing

**Input Processing:**
| Step | Purpose |
|------|---------|
| Tokenization | Text → numerical token IDs |
| Token Embedding | Capture semantic relationships |
| Positional Encoding | Capture position in sequence |

**Output Processing:**
1. Decoder stack outputs vector
2. Multiply with token embeddings → logits
3. Apply sampling (temperature) → select next token
4. Repeat until done

**Related:** Tokenization, [[07-genai-fundamentals/07-genai-fundamentals#Embeddings]], [[07-genai-fundamentals/07-genai-fundamentals#Temperature]]

---

### LLM-Parameters

**Sampling Parameters:**

| Parameter | What It Controls | Low Value | High Value |
|-----------|-----------------|-----------|------------|
| **Temperature** | Randomness in selection | Predictable, focused | Creative, diverse |
| **Top P** | Probability threshold | Fewer options | More options |
| **Top K** | Number of candidates | Conservative | Exploratory |

**Size Parameters:**

| Parameter | Definition |
|-----------|------------|
| **Context Window** | Max tokens LLM can process at once |
| **Max Tokens** | Limit for input or output tokens |

**Related:** [[07-genai-fundamentals/07-genai-fundamentals#Temperature]], Sampling, Token-Limits

---

### Transfer-Learning-LLM

**Fine-Tuning Approaches:**

| Approach | Description | Use Case |
|----------|-------------|----------|
| Full fine-tuning | Train entire model on new data | Major domain shift |
| Freeze + retrain | Freeze base, train top layers | Specific task adaptation |
| New tokenizer | Train tokenizer for new language | Language adaptation |
| Prompt-completion | Examples of desired behavior | Personality/style |
| Classification head | Add classification layer | Sentiment, categories |

**Related:** [[07-genai-fundamentals/07-genai-fundamentals#Fine-Tuning]], [[07-genai-fundamentals#Foundation-Models]], [[07-genai-fundamentals/07-genai-fundamentals#BERT]]

---

## AWS Services

### Amazon-Bedrock

**Purpose:** Managed service to access foundation models via API

**Available Models:**

| Model | Provider | Best For |
|-------|----------|----------|
| **Claude** | Anthropic | Conversations, Q&A, reasoning |
| **Jurassic-2** | AI21 Labs | Multilingual text (6 languages) |
| **Stable Diffusion** | Stability.ai | Image generation |
| **Llama** | Meta | General text LLM |
| **Amazon Titan** | Amazon | Text, embeddings, multimodal |

**Amazon Titan Capabilities:**
- Text summarization & generation
- Question answering
- Embeddings (personalization, semantic search)

**Related:** [[07-genai-fundamentals#Foundation-Models]], [[08-bedrock-applications#SageMaker-JumpStart]]

---

### SageMaker-JumpStart

**Purpose:** Quick-start notebooks with foundation models in SageMaker Studio

**Available Models:**
| Category | Examples |
|----------|----------|
| Text Generation | Falcon, Flan, BloomZ, GPT-J |
| Image Generation | Stable Diffusion |
| Multilingual | Amazon Alexa |

**Workflow:**
1. Open SageMaker Studio
2. Navigate to JumpStart
3. Select foundation model
4. Get pre-configured notebook

**Related:** SageMaker-Studio, [[07-genai-fundamentals#Foundation-Models]], [[08-bedrock-applications#Amazon-Bedrock]]

---

### Foundation-Models

**Definition:** Large pre-trained models adapted for specific tasks

**Major Models:**

| Model | Provider | Architecture | Specialty |
|-------|----------|--------------|-----------|
| GPT-4 | OpenAI | Decoder-only | General, reasoning |
| Claude | Anthropic | Decoder-only | Safety, long context |
| BERT | Google | Encoder-only | Understanding, classification |
| T5 | Google | Encoder-Decoder | Translation, summarization |
| LLaMA | Meta | Decoder-only | Open-weight LLM |
| DALL-E | OpenAI | Diffusion | Image generation |

**Related:** [[08-bedrock-applications#Amazon-Bedrock]], [[07-genai-fundamentals#Transfer-Learning]], [[07-genai-fundamentals/07-genai-fundamentals#Fine-Tuning]]

---

## Concept Relationships

```
                        ┌───────────────────────────────────┐
                        │        TRANSFORMER EVOLUTION      │
                        └───────────────────────────────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│   RNN/LSTM    │               │   Attention   │               │  Transformer  │
│  (Sequential) │      →        │  (Per token)  │      →        │  (Parallel)   │
└───────────────┘               └───────────────┘               └───────────────┘
                                                                        │
                        ┌───────────────────────────────────────────────┤
                        │                       │                       │
                        ▼                       ▼                       ▼
                ┌───────────────┐       ┌───────────────┐       ┌───────────────┐
                │ Encoder-only  │       │ Decoder-only  │       │Encoder-Decoder│
                │    (BERT)     │       │ (GPT, Claude) │       │   (T5, BART)  │
                └───────────────┘       └───────────────┘       └───────────────┘
                        │                       │                       │
                        ▼                       ▼                       ▼
                Understanding           Generation              Translation
                Classification          Chat/Q&A                Summarization


                        ┌───────────────────────────────────┐
                        │         AWS GENAI STACK           │
                        └───────────────────────────────────┘
                                        │
                ┌───────────────────────┼───────────────────────┐
                │                       │                       │
                ▼                       ▼                       ▼
        ┌───────────────┐       ┌───────────────┐       ┌───────────────┐
        │    Bedrock    │       │   JumpStart   │       │   SageMaker   │
        │  (API Access) │       │  (Notebooks)  │       │(Full Control) │
        └───────────────┘       └───────────────┘       └───────────────┘
                │                       │                       │
                └───────────────────────┴───────────────────────┘
                                        │
                                        ▼
                                ┌───────────────┐
                                │  Foundation   │
                                │    Models     │
                                │ Claude, Titan │
                                │ Llama, SD     │
                                └───────────────┘
```

---

## Exam Tips

### Transformer Fundamentals
- Self-attention computes weighted average of all token embeddings
- Q, K, V matrices are learned through backpropagation
- Masked attention prevents seeing future tokens (GPT uses this)
- Multi-head attention = multiple attention operations in parallel

### Architecture Types
- **Encoder-only (BERT):** Understanding, classification, NER
- **Decoder-only (GPT):** Text generation, chat, completion
- **Encoder-Decoder (T5):** Translation, summarization

### LLM Parameters
- High temperature = more random/creative output
- Low temperature = more consistent/focused output
- Top P and Top K also control randomness (higher = more random)
- Context window limits how much text model can process at once

### AWS Services for GenAI
- **Bedrock:** API access to foundation models (Claude, Titan, Llama, SD)
- **SageMaker JumpStart:** Pre-configured notebooks with models
- **Amazon Titan:** AWS's own foundation model (text + embeddings)

### Fine-Tuning
- Can fine-tune by adding layers on top of pre-trained model
- Provide prompt-completion examples for behavior adaptation
- Can adapt LLMs for classification by adding classification head
