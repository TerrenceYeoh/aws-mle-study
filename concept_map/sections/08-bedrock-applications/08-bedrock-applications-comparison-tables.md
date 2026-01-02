# Section 8: Building Generative AI Applications With Bedrock - Comparison Tables

## Customization Approaches

### Fine-Tuning vs Continued Pre-Training vs RAG

| Aspect | Fine-Tuning | Continued Pre-Training | RAG |
|--------|-------------|------------------------|-----|
| **Data Type** | Labeled (prompt-completion) | Unlabeled (raw text) | External database |
| **Format** | `{"prompt": "...", "completion": "..."}` | `{"input": "text"}` | Documents in vector DB |
| **Training** | Yes (supervised) | Yes (unsupervised) | No training |
| **Cost** | Expensive | Moderate | Cheapest |
| **Speed to Deploy** | Slow (training time) | Slow | Fast |
| **Update Data** | Retrain model | Retrain model | Update database |
| **Use Case** | Specific behavior/style | Domain familiarity | Current/external knowledge |
| **Supported Models** | Titan, Cohere, Meta | Titan, Cohere, Meta | Any |

### When to Use Each Approach

| Scenario | Recommended Approach | Why |
|----------|---------------------|-----|
| Need model to adopt specific personality | Fine-tuning | Adapts behavior through examples |
| Domain-specific terminology | Continued Pre-Training | Familiarizes with domain vocabulary |
| Access to frequently updated data | RAG | Easy to update database |
| Customer support with knowledge base | RAG | Query existing documentation |
| Classification tasks | Fine-tuning | Train on labeled categories |
| Reduce prompt length | Fine-tuning/CPT | Behavior encoded in model |

---

## Bedrock API Endpoints

### Endpoint Purposes

| Endpoint | Purpose | Key Operations | Use Case |
|----------|---------|----------------|----------|
| **bedrock** | Management | Create, list, delete models | Admin tasks |
| **bedrock-runtime** | Inference | InvokeModel, Converse, ConverseStream | Direct model calls |
| **bedrock-agent** | Agent management | Create, update agents | Admin tasks |
| **bedrock-agent-runtime** | Agent inference | InvokeAgent, Retrieve, RetrieveAndGenerate | RAG & agent apps |

---

## Database Options for RAG

### Vector Database Comparison

| Database Type | Examples | Pros | Cons |
|---------------|----------|------|------|
| **Adapted Existing** | OpenSearch, PostgreSQL, MongoDB | Familiar, existing infrastructure | May not be optimized for vectors |
| **Commercial Purpose-Built** | Pinecone, Weaviate | Optimized, managed, scalable | Cost, vendor lock-in |
| **Open Source** | Chroma, Qdrant, Milvus | Free, customizable | Self-managed, less support |

### Knowledge Base Vector Store Options

| Vector Store | Best For | Notes |
|--------------|----------|-------|
| **OpenSearch Serverless** | Development, prototyping | Default option |
| **MemoryDB** | Low-latency requirements | Vector capabilities |
| **Aurora** | Existing PostgreSQL users | pgvector extension |
| **MongoDB Atlas** | Document-oriented data | Atlas Vector Search |
| **Pinecone** | Production scale | Purpose-built |
| **Redis Enterprise** | Caching + vectors | Combined use case |

---

## RAG Database Types

### Graph DB vs OpenSearch vs Vector DB

| Criteria | Graph DB (Neo4j) | OpenSearch | Vector DB |
|----------|------------------|------------|-----------|
| **Search Type** | Relationship traversal | TF/IDF keyword | Semantic similarity |
| **Best For** | Product recommendations | Traditional text search | RAG/semantic search |
| **Query** | Graph queries (Cypher) | Boolean queries | K-Nearest Neighbor |
| **When to Use** | Entity relationships | Exact text matching | Meaning-based search |

---

## Agent Components

### Agent Architecture

| Component | Implementation | Purpose |
|-----------|----------------|---------|
| **Memory** | Chat history + data stores | Maintain context |
| **Planning Module** | Prompt guidance | Break down questions |
| **Tools Core** | Lambda functions | Execute actions |
| **Action Groups** | Tool definitions | Define capabilities |
| **Knowledge Bases** | Vector stores | RAG functionality |

### Action Groups vs Knowledge Bases

| Aspect | Action Groups | Knowledge Bases |
|--------|---------------|-----------------|
| **Purpose** | Execute actions via Lambda | Query documents via RAG |
| **Implementation** | Lambda functions | Vector DB + embedding model |
| **Use Case** | API calls, calculations, external systems | "Chat with your document" |
| **Configuration** | Parameters, prompts | Data sources, chunking |

---

## Throughput Options

### On-Demand vs Provisioned

| Aspect | On-Demand (ODT) | Provisioned (PT) |
|--------|-----------------|------------------|
| **Quotas** | Account-level | Purchased |
| **Cost** | Pay per use | Reserved capacity |
| **Best For** | Variable workloads | Consistent high volume |
| **Rate Limits** | Default limits | Increased limits |

---

## Guardrail Features

### Filtering Types

| Filter Type | What It Blocks | Configuration |
|-------------|----------------|---------------|
| **Word Filtering** | Specific words/phrases | Custom word lists |
| **Topic Filtering** | Entire topics | Topic definitions |
| **Profanity** | Offensive language | Built-in |
| **PII** | Personal data | Remove or mask |

### Contextual Grounding Check

| Metric | What It Measures | Purpose |
|--------|------------------|---------|
| **Grounding** | Response similarity to context | Prevent hallucination |
| **Relevance** | Response relevance to query | Ensure on-topic answers |

---

## Model Evaluation Options

### Automatic vs Human Evaluation

| Aspect | Automatic | Human (BYOT) | Human (AWS) |
|--------|-----------|--------------|-------------|
| **Metrics** | BERTScore, F1, toxicity, robustness | Custom criteria | Custom criteria |
| **Speed** | Fast | Slow | Slow |
| **Cost** | Low | Team cost | AWS charges |
| **Objectivity** | Consistent | Variable | Managed |
| **Best For** | Initial screening | Domain expertise | No internal team |

---

## Quick Decision Tables

### Which Customization Approach?

| Question | Answer |
|----------|--------|
| Need specific personality/style? | Fine-tuning |
| Need domain vocabulary? | Continued Pre-Training |
| Need current/external data? | RAG |
| Need fast deployment? | RAG |
| Budget is limited? | RAG |
| Need consistent behavior patterns? | Fine-tuning |

### Which Vector Store?

| Question | Answer |
|----------|--------|
| Just prototyping? | OpenSearch Serverless |
| Already using PostgreSQL? | Aurora (pgvector) |
| Need enterprise scale? | Pinecone |
| Low-latency required? | MemoryDB |
| Document-oriented? | MongoDB Atlas |

### Which API Endpoint?

| Question | Answer |
|----------|--------|
| Direct model inference? | bedrock-runtime |
| Manage models/agents? | bedrock or bedrock-agent |
| Call agent with tools? | bedrock-agent-runtime |
| RAG query? | bedrock-agent-runtime |

### Which Agent Feature?

| Question | Answer |
|----------|--------|
| Need to call external APIs? | Action Groups (Lambda) |
| Need document Q&A? | Knowledge Bases |
| Need both? | Agentic RAG |
| Need code generation? | Code Interpreter |

### Which Guardrail Feature?

| Question | Answer |
|----------|--------|
| Block specific words? | Word filtering |
| Prevent topic drift? | Topic filtering |
| Protect user privacy? | PII removal/masking |
| Prevent hallucination? | Contextual Grounding Check |

---

## Bedrock Models Comparison

### Available Foundation Models

| Provider | Model | Type | Best For |
|----------|-------|------|----------|
| **Amazon** | Titan | Text, Embeddings, Multimodal | General purpose, embeddings |
| **Anthropic** | Claude | Text | Reasoning, long context, safety |
| **AI21 Labs** | Jurassic-2 | Text | Multilingual (6 languages) |
| **Cohere** | Command | Text | Enterprise, embeddings |
| **Meta** | Llama 3 | Text | Open-weight, general |
| **Mistral AI** | Mistral | Text | Efficient, general |
| **Stability AI** | Stable Diffusion | Image | Image generation |

### Embedding Models for Knowledge Bases

| Model | Provider | Notes |
|-------|----------|-------|
| **Titan Embeddings** | Amazon | Default option |
| **Cohere Embed** | Cohere | Alternative |
