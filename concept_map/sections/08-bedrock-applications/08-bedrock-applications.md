# Section 8: Building Generative AI Applications With Bedrock

## Overview

This section covers Amazon Bedrock for building generative AI applications, including RAG with knowledge bases, LLM agents with tools, and guardrails for content safety.

**Key Takeaways:**
- Bedrock provides serverless API access to foundation models (Claude, Titan, Llama, etc.)
- RAG uses vector databases to augment LLM responses with external knowledge
- Knowledge Bases enable "chat with your document" functionality
- Agents give LLMs tools (via Lambda functions) to interact with external systems
- Guardrails provide content filtering, PII protection, and hallucination prevention

---

## Core Concepts

### Amazon-Bedrock

**What It Is:**
- Serverless API for generative AI foundation models
- Invoke chat, text, or image models
- Can integrate with SageMaker Canvas

**Model Options:**
- Pre-built foundation models
- Your own fine-tuned models
- Your own imported models

**Available Models:**
| Provider | Model |
|----------|-------|
| AI21 Labs | Jurassic-2 |
| Amazon | Titan |
| Anthropic | Claude |
| Cohere | Command |
| Meta | Llama 3 |
| Mistral AI | Mistral |
| Stability AI | Stable Diffusion |

**Related:** [[07-genai-fundamentals#Foundation-Models]], [[08-bedrock-applications#SageMaker-JumpStart]], [[08-bedrock-applications#RAG]]

---

### Bedrock-API-Endpoints

| Endpoint | Purpose | Key Operations |
|----------|---------|----------------|
| **bedrock** | Manage, deploy, train models | - |
| **bedrock-runtime** | Perform inference | Converse, ConverseStream, InvokeModel, InvokeModelWithResponseStream |
| **bedrock-agent** | Manage agents and knowledge bases | - |
| **bedrock-agent-runtime** | Inference against agents/KBs | InvokeAgent, Retrieve, RetrieveAndGenerate |

**Related:** IAM-Permissions, [[08-bedrock-applications#Agents]], [[08-bedrock-applications#Knowledge-Bases]]

---

### Fine-Tuning-Bedrock

**Purpose:** Adapt existing LLM to specific use case

**Benefits:**
- Eliminates need for extensive prompt engineering
- Saves tokens in the long run
- Can fine-tune a fine-tuned model (iterative improvement)

**Custom Models (Supervised):**
- Supported: Titan, Cohere, Meta
- Format: `{"prompt": "question", "completion": "answer"}`
- Upload training data to S3

**Continued Pre-Training (Unsupervised):**
- Feed raw text to familiarize model with domain
- Format: `{"input": "text content"}`
- Use case: Business documents, domain-specific content

**Security:** Use VPC and PrivateLink for sensitive training data

**Related:** [[07-genai-fundamentals#Transfer-Learning]], [[07-genai-fundamentals#Foundation-Models]]

---

### Retrieval-Augmented-Generation

**Definition:** "Open-book exam" for LLMs - query external database instead of relying on model's training

**How It Works:**
```
1. User asks question
2. Query external database for relevant info
3. Include retrieved info in prompt to LLM
4. LLM generates response using retrieved context
```

**Pros:**
- Faster & cheaper than fine-tuning
- Easy to update (just update database)
- Leverages semantic search
- Prevents hallucinations on unknown topics
- Not technically "training"

**Cons:**
- Can be overcomplicated search engine
- Sensitive to prompt templates
- Non-deterministic
- Can still hallucinate
- Sensitive to retrieval relevancy

**Related:** [[08-bedrock-applications/08-bedrock-applications#Vector-Database]], [[08-bedrock-applications#Knowledge-Bases]], [[07-genai-fundamentals/07-genai-fundamentals#Embeddings]]

---

### Vector-Database

**Purpose:** Store data alongside computed embedding vectors for semantic search

**How Retrieval Works:**
1. Compute embedding vector for search query
2. Query vector database for items close to that vector
3. Get back top-N most similar items (K-Nearest Neighbor)

**Database Options:**
| Type | Examples |
|------|----------|
| **Adapted existing DBs** | OpenSearch, Elasticsearch, SQL, Neptune, Redis, MongoDB, Cassandra |
| **Commercial purpose-built** | Pinecone, Weaviate |
| **Open source** | Chroma, Marqo, Vespa, Qdrant, LanceDB, Milvus |

**Related:** [[07-genai-fundamentals/07-genai-fundamentals#Embeddings]], [[08-bedrock-applications#RAG]], [[08-bedrock-applications#Knowledge-Bases]]

---

### Knowledge-Bases

**Purpose:** Managed RAG in Bedrock - "Chat with your document"

**Data Sources:**
- S3 (with optional JSON schema)
- Web crawler
- Confluence
- Salesforce
- SharePoint

**Requirements:**
- Embedding model (Cohere or Amazon Titan)
- Vector store
- Control chunking (tokens per vector)

**Vector Store Options:**
| Option | Notes |
|--------|-------|
| OpenSearch Serverless | Default for development |
| MemoryDB | Vector capabilities |
| Aurora | - |
| MongoDB Atlas | - |
| Pinecone | - |
| Redis Enterprise Cloud | - |

**Usage:**
- Direct application integration
- Incorporate into agents ("Agentic RAG")

**Related:** [[08-bedrock-applications#RAG]], [[08-bedrock-applications/08-bedrock-applications#Vector-Database]], [[08-bedrock-applications#Agents]]

---

### Bedrock-Guardrails

**Purpose:** Content filtering for prompts and responses

**Filtering Types:**
- Word filtering
- Topic filtering
- Profanities
- PII removal (or masking)

**Contextual Grounding Check:**
- Prevents hallucination
- Measures "grounding" (response similarity to context)
- Measures "relevance" (response relevance to query)

**Integration:**
- Agents
- Knowledge bases
- Custom blocked message response

**Related:** [[08-bedrock-applications#Agents]], Safety, Content-Moderation

---

### LLM-Agents

**Definition:** LLMs with tools and discretion on which to use

**Components:**
| Component | Implementation |
|-----------|----------------|
| **Memory** | Chat history + external data stores |
| **Planning Module** | Guidance on decomposing questions |
| **Tools Core** | Functions via tools API (Lambda) |

**Key Characteristics:**
- Prompts guide tool usage
- Tools access external information/services
- Can ask user for missing information

**Related:** Action-Groups, [[08-bedrock-applications#Knowledge-Bases]], [[09-mlops#AWS-Lambda]]

---

### Action-Groups

**Purpose:** Define tools for Bedrock agents

**Configuration:**
1. Select foundation model
2. Define Action Groups (tools)
   - Prompt informs FM when to use
   - Parameters: name, description, type, required
3. Associate Lambda functions
4. Use OpenAI-style schemas or Bedrock UI

**Features:**
- FM can ask user for missing information
- Knowledge bases as tools ("Agentic RAG")
- Optional Code Interpreter (write code, produce charts)

**Related:** [[08-bedrock-applications#Agents]], [[09-mlops#AWS-Lambda]], [[08-bedrock-applications#Knowledge-Bases]]

---

### Deploying-Agents

**Steps:**
1. Create an "alias" (deployed snapshot)
2. Choose throughput option
3. Invoke via bedrock-agent-runtime

**Throughput Options:**
| Type | Description |
|------|-------------|
| **On-Demand (ODT)** | Account-level quotas |
| **Provisioned (PT)** | Purchase increased rate/tokens |

**Invocation:** InvokeAgent request with alias ID

**Related:** [[08-bedrock-applications#Agents]], API-Endpoints

---

## AWS Services

### Amazon-Bedrock

**Model Evaluation:**
| Type | Methods |
|------|---------|
| Automatic | Accuracy, toxicity, robustness, BERTScore, F1 |
| Human (BYOT) | Bring your own team |
| Human (AWS) | AWS-managed team |

**Watermark Detection:**
- Detects if image was generated by Titan

**Bedrock Studio:**
- Web app workspace without AWS accounts
- Single Sign On with IAM + Identity Provider
- Project collaboration

**Related:** [[07-genai-fundamentals#Foundation-Models]], Model-Evaluation

---

## Concept Relationships

```
                        ┌───────────────────────────────────┐
                        │         AMAZON BEDROCK            │
                        └───────────────────────────────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│   Foundation  │               │  Fine-Tuning  │               │   Guardrails  │
│    Models     │               │ Custom/CPT    │               │Content Filter │
└───────────────┘               └───────────────┘               └───────────────┘
        │
        ├───────────────────────────────┬───────────────────────────────┐
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│  Direct API   │               │    Agents     │               │ Knowledge     │
│   Inference   │               │  (Tools/LLM)  │               │   Bases       │
└───────────────┘               └───────────────┘               └───────────────┘
                                        │                               │
                                        │       ┌───────────────────────┘
                                        │       │
                                        ▼       ▼
                                ┌───────────────────────┐
                                │     Agentic RAG       │
                                │  (Agent + KB + Tools) │
                                └───────────────────────┘
                                        │
                        ┌───────────────┼───────────────┐
                        │               │               │
                        ▼               ▼               ▼
                ┌───────────┐   ┌───────────┐   ┌───────────┐
                │  Lambda   │   │  Vector   │   │ Embedding │
                │ Functions │   │    DB     │   │  Models   │
                └───────────┘   └───────────┘   └───────────┘


                        ┌───────────────────────────────────┐
                        │        RAG ARCHITECTURE           │
                        └───────────────────────────────────┘

    ┌─────────┐   Embed    ┌─────────────┐   Semantic   ┌─────────────┐
    │  User   │ ────────►  │  Embedding  │ ──────────►  │  Vector DB  │
    │  Query  │            │   Model     │   Search     │ (OpenSearch)│
    └─────────┘            └─────────────┘              └─────────────┘
                                                               │
                                                               │ Top-K Results
                                                               ▼
    ┌─────────┐            ┌─────────────┐              ┌─────────────┐
    │Response │ ◄────────  │   Bedrock   │ ◄──────────  │  Augmented  │
    │         │            │    Model    │              │   Prompt    │
    └─────────┘            └─────────────┘              └─────────────┘
```

---

## Exam Tips

### Bedrock Fundamentals
- Bedrock is serverless API access to foundation models
- Four API endpoints: bedrock, bedrock-runtime, bedrock-agent, bedrock-agent-runtime
- Must request model access before using (Titan approves immediately)
- Third-party models billed through AWS

### Fine-Tuning vs RAG vs Continued Pre-Training
- **Fine-tuning:** Labeled prompt-completion pairs, adapts model behavior
- **Continued pre-training:** Unlabeled data, familiarizes model with domain
- **RAG:** No training, queries external database for context
- RAG is faster/cheaper than fine-tuning but can still hallucinate

### Knowledge Bases
- Requires embedding model (Cohere or Titan)
- Default vector store: OpenSearch Serverless
- Control chunking (tokens per vector)
- Sources: S3, web crawler, Confluence, Salesforce, SharePoint

### Agents
- Action Groups define tools (Lambda functions)
- Prompts guide when to use tools
- Parameter descriptions help LLM extract info from user queries
- "Agentic RAG" = RAG as a tool for the agent
- Code Interpreter allows agent to write code

### Guardrails
- Content filtering: word, topic, profanity, PII
- Contextual Grounding Check prevents hallucination
- Measures grounding (context similarity) and relevance (query match)

### Deployment
- Create alias for agent deployment
- On-Demand (ODT) vs Provisioned (PT) throughput
- InvokeAgent with alias ID via bedrock-agent-runtime

### Additional Features
- Model evaluation: automatic (BERTScore, F1) or human
- Watermark detection for Titan images
- Bedrock Studio: web app without AWS accounts
