## Get Started with Vertex AI Studio

Vertex AI is a comprehensive machine learning development platform that provides both predictive and generative AI capabilities. It allows you to train, evaluate, and deploy predictive machine learning models for forecasting purposes. Additionally, you can utilize the platform to discover, tune, and serve generative AI models to produce content.

Vertex AI Studio lets you quickly test and customize generative AI models so you can leverage their capabilities in your applications. It provides a variety of tools and resources including both UI (user interface) and coding examples that make it easy to start with generative AI, even if you don't have a background in machine learning.

This lab guides you through Vertex AI Studio, where you'll unlock the potential of cutting-edge generative AI models. You'll explore Gemini and use it to analyze images, design prompts, and generate conversations directly on the Google Cloud console. No need for API or Python SDKs - it's all accessible through the intuitive user interface.

### Objectives

In this lab, you will learn how to:

- Analyze images with Gemini
- Explore Vertex AI Studio Freeform mode
- Design text prompts for zero-shot, one-shot, and few-shot prompting
- Generate conversations with chat prompts

### Prompt design

**Prompt design methods**

There are three main methods to design prompts:

- Zero-shot prompting - This is a method where the LLM is given only a prompt that describes the task and no additional data. For example, if you want the LLM to answer a question, you just prompt "what is prompt design?".
- One-shot prompting - This is a method where the LLM is given a single example of the task that it is being asked to perform. For example, if you want the LLM to write a poem, you might give it a single example poem.
  - input: The color of the grass is
  - output: The color of the grass is green
  - test input: The color of the sky is
- Few-shot prompting - This is a method where the LLM is given a small number of examples of the task that it is being asked to perform. For example, if you want the LLM to write a news article, you might give it a few news articles to read.
  - input | output
  - A well-made and entertaining film | positive
  - I fell asleep after 10 minutes | negative
  - The movie was ok | neutral
  - test input: It was a time well spent! | positive

**Parameters**

Temperature and Token limit are two important parameters that you can adjust to influence the model's response.

- Temperature controls the randomness in token selection. A lower temperature is good when you expect a true or correct response. A temperature of 0 means the highest probability token is always selected. A higher temperature can lead to diverse, unexpected, or potentially biased results. The `gemini-1.5-pro` model has a temperature range of 0 - 2 and a default of 1.
- Output token limit determines the maximum amount of text output from one prompt. A token is approximately four characters.

### Chat

`gemini-1.5-flash`

System instructions

```text
Your name is Roy.
You are a support technician of an IT department.
You only respond with "Have you tried turning it off and on again?" to any queries.
```

Prompt

```text
My computer is so slow! What should I do?
```

Response

```text
Have you tried turning it off and on again?
```

System instructions

```text
Your name is Roy.
You are a support technician of an IT department.
You are here to support the users with their queries.
```

Prompt

```text
My computer is so slow! What should I do?
```

Response

- more useful response

### More Resources

- [Prompting](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design)
  - [Design multimodal prompts](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/design-multimodal-prompts)
