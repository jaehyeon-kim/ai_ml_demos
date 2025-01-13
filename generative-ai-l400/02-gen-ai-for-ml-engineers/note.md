## Generative AI for Machine Learning Engineers

### 01 Attention Mechanism

- [Gen AI for Developers](https://www.youtube.com/playlist?list=PLBgogxgQVM9s0i9oloJwjIG-zj6Svsm20)
  - [Encoder-Decoder Architecture: Overview](https://www.youtube.com/watch?v=671xny8iows)
  - [Attention Mechanism: Overview](https://www.youtube.com/watch?v=8PmOaVYVeKY)

### 02 Encoder-Decoder Architecture

- [Text generation with an RNN](https://github.com/GoogleCloudPlatform/asl-ml-immersion/blob/master/notebooks/text_models/solutions/text_generation.ipynb)
- [Advanced Solutions Lab](https://cloud.google.com/asl)
  - [GitHub](https://github.com/GoogleCloudPlatform/asl-ml-immersion)

### 03 Transformer Models and BERT Model

- [Classify text with BERT](https://github.com/GoogleCloudPlatform/asl-ml-immersion/blob/master/notebooks/text_models/solutions/classify_text_with_bert.ipynb)

### 05 Create Image Captioning Models

- [Image Captioning with Visual Attention](https://github.com/GoogleCloudPlatform/asl-ml-immersion/blob/master/notebooks/multi_modal/solutions/image_captioning.ipynb)

### 06 Implementing Generative AI with Vertex AI

#### LLM Prompt Design Best Practices

Use cases

- Q & A
- Recommendations
- Translation (EN to FR, EN to JSON ...)
- Brainstorming
- Conversations
- ...

Unfancy prompt design

- Task description
- Examples
- Prompt

Guidelines

- Examples improve performance to a point
- Instructions improve performance beyond just examples
- Don't try to design the perfect prompt
  - An instruction with 5-7 examples is great
- For great performance, use real(istic) data!

Prompts and workflows

- Don't be tempted to create one prompt that will solve the entire user problem
- An LLM workflow comprises multiple tasks, each can be solved with an LLM prompt
- Ideally each task can be independently tested
- Workflows lead to:
  - greater user control and trust
  - better model performance
  - easier testing

Hidden best practice:

1. Minimize end-user ending of prompts
   - It makes prompts fragile, difficult to test, and hard to use prompt tuning
2. Turn a generative task into a classification may increase safety
   - I'm a high school student and mostly think computers are cool and want to program. Recommend me a programming activity...
   - I'm [[a high school student]] and [[mostly think computers are cool]]... Which of these activities do you suggest and why: a) learn Python - it's easy and fun. b) OCaml - it'll expose you to a new way to think...
   - Benefits: reducing output variability `->` easier to test, easier to control

Consider PETS (Parameter efficient fine-tuning service)

- Technique also known as Parameter Efficient Tuning (PEFT)
- Yields higher accuracy, with more examples (50-100 is usually plenty)
- A helpful (but not entirely accurate) way to think about it
  - PETS compresses your prompt with lots of examples into a short token
- Achieves state-of-the-art results in many tasks without specialized ("fine-tuned") model
- Somewhat smaller inference costs, but not as lot as distillation
- Works best for classification / narrow generation tasks
- Less well for creative generations

#### Resources

- [Generative AI for Developers](https://www.youtube.com/playlist?list=PLIivdWyY5sqLRCzKJyixrIDPQKwU6XHpn)
- [Distilling step-by-step: Outperforming larger language models with less training data and smaller model sizes](https://research.google/blog/distilling-step-by-step-outperforming-larger-language-models-with-less-training-data-and-smaller-model-sizes/)

### 07 Vector Search and Embeddings

Use cases for enterprises

- Visual Search
  - External: Find similar products through images
  - internal: Discover similar cases through medical examination images
- Natural Language Search
  - External: Search through conversations
  - Internal: Q&A document retrieval, internal "Google"
- Recommendation
  - External: Recommend products
  - Internal: Recommend SMEs across teams

Challenges of keyword search

- Follows the process: crawl `->` index `->` serve
- Saves data in tables
- Is effective to a certain extent

Drawbacks

- Search becoming more sophisticated requires search engines to be more intelligent
- The traditional search technology:
  - Can't understand query intent and context
  - Does not support multimodal search
  - Lacks domain specificity

Vector Search

- Follows the process: encode `->` index `->` search
- Converts data to vectors
- Understands the context

Benefits

- Semantic understanding (incl natural language search)
- Multimodal search capabilities
- Personalization & recommendation

Two challenges

1. How to encode data? (Embeddings)
   - How to convert multimodal data to a representation that captures semantic meanings?
2. How to index and search data? (Vector Search)
   - How to build a search space that enables fast and efficient search?

Word embeddings

- A technique to encode text into meaningful vectors
- Benefits:
  - They contain dense representation i.e. low dimension and dense vectors
  - They capture the semantic meaning of words i.e. distributed representation
- A neural network (embedding models) for word embeddings
  - Word2Vec
  - GloVe
  - FastText

Vector Search

- Measure distance: How can you measure the distance between vectors?
  - Manhattan distance (L1), Euclidean distance (L2), Cosine distance, Dot product distance
- Search vectors: How can you efficiently search similar vectors?
  - Search algorithms: Brute-force algorithm, Tree-Ah algorithm (Shallow tree + Asymmetric Hashing)

Interact with Vector Search

- UI:
  - Google Cloud Console
  - No code
- Notebooks (for example, Colab and Workbench):
  - APIs: pre-training embeddings APIs, vector search APIs
  - Code-based
- Gcloud:
  - Google Cloud command line
    - Minimum code

Typical use cases of Vector Search

- Search
  - Semantic search: Document retrieval, ranking
  - Multimedia search: Video, music, image search
- Personalization
  - Ads targeting: Keywords targeting, similar user targeting
  - Recommendation: Candidate generation, filter and diversity
- Trust and safety
  - Trust and safety: Spam, abuse content, label propagation
  - Content re-use: Copyright detection, video re-upload
- LLMs (to combat hallucinations)
  - Retrieval augmented generation: RetrievalQA, agents personal knowledge base
  - Example mining: Training private embedding models

The grounding problem (hallucinations)

- LLMs can only understand
  - The information that they were trained on
    - They do not know domain specific data
    - They do not have the real-time information
  - The information that they are explicitly given in the prompt
    - They often assume that the prompt is true
    - They don't have the capability to ask context information

Also, an LLM does not know anything outside what it was trained on, and it cannot truly know if that information is accurate.

Some native solutions are fine-tuning, human review and prompt engineering.
Vector search can provide additional real-time fact checks to LLMs.

### Resources

- [Natural Language Processing on Google Cloud](https://partner.cloudskillsboost.google/course_templates/40)
- [Embeddings](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings)
  - [Text embeddings](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings)
  - [Multimodal embeddings](https://cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-multimodal-embeddings)
- [Vertex AI Embeddings for Text: Grounding LLMs made easy](https://cloud.google.com/blog/products/ai-machine-learning/how-to-use-grounding-for-your-llms-with-text-embeddings)
- [Overview of Vertex AI Vector Search](https://cloud.google.com/vertex-ai/docs/vector-search/overview)
- [Vector Search notebook tutorials](https://cloud.google.com/vertex-ai/docs/vector-search/notebooks)
- [GoogleCloudPlatform/generative-ai/embeddings](https://github.com/GoogleCloudPlatform/generative-ai/tree/main/embeddings)
- [GoogleCloudPlatform/vertex-ai-samples/notebooks/official/vector_search](https://github.com/GoogleCloudPlatform/vertex-ai-samples/tree/main/notebooks/official/vector_search)
