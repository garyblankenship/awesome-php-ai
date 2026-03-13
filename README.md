# Awesome PHP AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of awesome PHP libraries and tools for AI, Machine Learning, and Natural Language Processing.

Contributions welcome! Read the [contributing guidelines](#contributing) to get started.

---

## Table of Contents

- [LLM Frameworks](#llm-frameworks)
- [LLM Clients & Adapters](#llm-clients--adapters)
- [Natural Language Processing](#natural-language-processing)
- [Machine Learning](#machine-learning)
- [Computer Vision](#computer-vision)
- [Vector Storage & RAG](#vector-storage--rag)
- [Command Line Tools](#command-line-tools)
- [Video Processing](#video-processing)
- [API Clients](#api-clients)
- [Learning Resources](#learning-resources)

---

## LLM Frameworks

Full-featured frameworks for building LLM-powered applications.

| Repo | Description |
|---------|-------------|
| [Magic](https://github.com/dtyq/magic) | Open-source all-in-one AI productivity platform with agents, workflows, and collaboration. |
| [Prism](https://github.com/prism-php/prism) | Unified interface for working with LLMs in Laravel applications. |
| [Neuron AI](https://github.com/neuron-core/neuron-ai) | PHP Agentic Framework for production-ready AI applications with RAG and multi-agent workflows. |
| [LLPhant](https://github.com/theodo-group/llphant) | Comprehensive PHP Generative AI Framework using OpenAI GPT-4. Inspired by Langchain. |
| [langchain-php](https://github.com/kambo-1st/langchain-php) | Building applications with LLMs through composability in PHP. |
| [Vizra ADK](https://github.com/vizra-ai/vizra-adk) | Build, test, and deploy intelligent AI agents the Laravel way. |
| [Resonance](https://github.com/distantmagic/resonance) | High-performance PHP framework optimized for IO-intensive LLM applications. |
| [LLM Chain](https://github.com/php-llm/llm-chain) | PHP library for building LLM-based and AI-based features and applications. |
| [Lugha](https://github.com/devscast/lugha) | PHP Generative AI Framework to build chatbots, RAG systems and AI-powered applications. |
| [EasyAI-PHP](https://github.com/HosonoDE/EasyAI-PHP) | Simplifies AI entry for PHP developers (LangChain-style). Based on PHP 8.1+. |
| [EleLLM](https://github.com/wpai-inc/EleLLM) | A PHP framework that makes working with LLMs more pleasurable and accessible. |

---

## LLM Clients & Adapters

Client libraries and provider integrations.

| Repo | Description |
|---------|-------------|
| [OpenAI PHP](https://github.com/openai-php/client) | Supercharged community-maintained PHP API client for OpenAI. |
| [OpenAI PHP SDK](https://github.com/orhanerday/open-ai) | Most downloaded PHP SDK for OpenAI GPT-3, DALL-E, and ChatGPT with streaming support. |
| [Gemini PHP](https://github.com/google-gemini-php/client) | Community-maintained PHP API client for Gemini AI. |
| [WordPress PHP AI Client](https://github.com/WordPress/php-ai-client) | Provider-agnostic PHP AI client SDK for any generative AI model. |
| [Ollama PHP](https://github.com/ArdaGnsrn/ollama-php) | PHP client for Ollama, enabling local LLM deployment and interaction. |
| [grok-php/laravel](https://github.com/grok-php/laravel) | Integrate Grok AI into Laravel with an elegant, developer-friendly package. |
| [Laravel OpenRouter](https://github.com/moe-mizrak/laravel-openrouter) | Laravel integration for OpenRouter's unified LLM API interface. |
| [AI Access](https://github.com/aiaccess/ai-access) | Flexible PHP library for Gemini, OpenAI, Anthropic, DeepSeek, Grok via consistent interface. |
| [Anthropic PHP](https://github.com/mozex/anthropic-php) | Community-maintained PHP API client for Anthropic (Claude) API with streaming, tool use, and batch processing. |
| [aipi-php](https://github.com/skito/aipi-php) | Universal API client for common AI models. |
| [Sidekick](https://github.com/PapaRascal2020/sidekick) | Laravel package with common syntax for Claude, Mistral, Cohere and OpenAI APIs. |
| [LLM-Port-Laravel](https://github.com/BorahLabs/LLM-Port-Laravel) | Drop-in replacement wrapper for popular LLMs in Laravel. |

---

## Natural Language Processing

### Structured Output & Validation

| Repo | Description |
|---------|-------------|
| [Instructor PHP](https://github.com/cognesy/instructor-php) | Unified LLM API, structured data outputs with LLMs, and agent SDK - in PHP. |
| [instructrice](https://github.com/adrienbrault/instructrice) | Typed LLM outputs in PHP. Supports GPT, Claude, Gemini or any OpenAI-compatible provider. |

### AI Agents & Orchestration

| Repo | Description |
|---------|-------------|
| [LLM Agents](https://github.com/llm-agents-php/agents) | Build and manage LLM-based autonomous agents that perform complex tasks. |
| [ai-team](https://github.com/sarfraznawaz2005/ai-team) | Create teams of AI members that collaborate to achieve common goals. |
| [mulagent](https://github.com/FunkyOz/mulagent) | Multi-agent orchestration with routines and handoffs. |

### Laravel Integrations

| Repo | Description |
|---------|-------------|
| [Laravel AI](https://github.com/laravel/ai) | Official Laravel package for AI integration. |
| [Laravel MCP Server](https://github.com/opgginc/laravel-mcp-server) | Laravel package for implementing Model Context Protocol servers. |
| [Neuron Laravel](https://github.com/neuron-core/neuron-laravel) | Official Neuron AI Laravel SDK. |
| [Laravel AI Guard](https://github.com/subhashladumor1/laravel-ai-guard) | Control and optimize AI costs in Laravel - track token usage, enforce budgets. |
| [MCP Client Laravel](https://github.com/RedberryProducts/mcp-client-laravel) | Laravel-native client for MCP servers. |
| [Taskallama](https://github.com/coding-wisely/taskallama) | Laravel integration with Ollama's LLM API for content generation. |
| [ai-translations-for-laravel](https://github.com/Capevace/ai-translations-for-laravel) | Automatically translate Laravel language files using LLMs. |
| [laravel-prompt-manager](https://github.com/prismaticoder/laravel-prompt-manager) | Simplify prompt management for AI engineers using Laravel. |
| [llm-magic](https://github.com/Capevace/llm-magic) | LLM-agnostic AI toolkit for Laravel. |
| [laravel-llm-prompt](https://github.com/SabatinoMasala/laravel-llm-prompt) | Laravel LLM prompt manager. |
| [laravel-prompt-alchemist](https://github.com/moe-mizrak/laravel-prompt-alchemist) | Versatile LLM Tool Use (Function Calling) for Laravel, compatible with all LLMs. |
| [LaravelLLMContext](https://github.com/jeremysalmon/LaravelLLMContext) | Artisan command to generate LLM context for a Laravel project. |
| [llm](https://github.com/artisan-build/llm) | Laravel integrations for various LLM providers. |

### Symfony Integrations

| Repo | Description |
|---------|-------------|
| [Symfony AI Platform](https://github.com/symfony/ai-platform) | PHP library for interacting with AI platform providers. |
| [Symfony MCP SDK](https://github.com/symfony/mcp-sdk) | Model Context Protocol SDK for Client and Server applications in PHP. |
| [LLM Chain Bundle](https://github.com/php-llm/llm-chain-bundle) | Symfony bundle for seamless integration of the LLM Chain library. |
| [Symfony MCP Bundle](https://github.com/symfony/mcp-bundle) | Official Symfony integration bundle for Model Context Protocol. |
| [Symfony AI Agent](https://github.com/symfony/ai-agent) | PHP library for building agentic applications. |
| [Symfony AI Bundle](https://github.com/symfony/ai-bundle) | Integration bundle for Symfony AI components. |

### Utilities & Tools

| Repo | Description |
|---------|-------------|
| [cocur/slugify](https://github.com/cocur/slugify) | Converts strings into slugs. |
| [NlpTools](https://github.com/angeloskath/php-nlp-tools) | Collection of NLP tools and APIs for working with text. |
| [transformers-php](https://github.com/CodeWithKyrian/transformers-php) | Toolkit for PHP developers to add machine learning magic easily. |
| [CTX Generator](https://github.com/context-hub/generator) | Tool that solves context management when working with LLMs - organizes codebase info for AI assistants. |
| [TOON PHP](https://github.com/HelgeSverre/toon-php) | Token-Oriented Object Notation - compact data format for reducing token consumption with LLMs. |
| [php-ai-tool-bridge](https://github.com/manuelkiessling/php-ai-tool-bridge) | AI integration to interact with your own code and services. |
| [single-file-php-ai](https://github.com/mariorazo97/single-file-php-ai) | Drop-in, single-file PHP chat interface for Ollama/OpenAI. No Node.js, no Docker. |
| [mcp-php](https://github.com/garyblankenship/mcp-php) | Setting up a Model Context Protocol (MCP) Server in Laravel. |
| [prompt-generator](https://github.com/llm-agents-php/prompt-generator) | Prompt generator for LLM agents with interceptors. |
| [php-llm-documents](https://github.com/thojou/php-llm-documents) | Brings LLM functionality for document processing. |
| [fabric-pattern](https://github.com/php-llm/fabric-pattern) | Slim PHP wrapper for Daniel Miessler's fabric pattern. |
| [php-llm-json-adapter](https://github.com/takaaki-mizuno/php-llm-json-adapter) | JSON output adapter for LLMs that lack native function calling. |
| [fireworksai-adapter](https://github.com/modelflow-ai/fireworksai-adapter) | Adapter for open-source models hosted by fireworks.ai. |

---

## Machine Learning

| Repo | Description |
|---------|-------------|
| [Rubix ML](https://github.com/RubixML/ML) | Machine learning library for building algorithms and models. |
| [php-ml](https://github.com/jorgecasas/php-ml) | A PHP machine learning library. |

---

## Computer Vision

| Repo | Description |
|---------|-------------|
| [opencv/opencv-php](https://github.com/php-opencv/php-opencv) | OpenCV bindings for PHP for image processing and computer vision. |

---

## Vector Storage & RAG

| Repo | Description |
|---------|-------------|
| [php-rag](https://github.com/rzarno/php-rag) | LLM-powered text generation with database-backed retrieval. |
| [redis-vector-php](https://github.com/redis-applied-ai/redis-vector-php) | Redis Vector Library for LLM applications, based on Predis. |
| [vector-storage](https://github.com/llm-agents-php/vector-storage) | LLM Agents Vector Storage. |

---

## Command Line Tools

| Repo | Description |
|---------|-------------|
| [ai-commit](https://github.com/guanguans/ai-commit) | Automagically generate conventional git commit messages with AI. |
| [Laragenie](https://github.com/joshembling/laragenie) | AI bot for the command line that reads and understands Laravel codebases. |

---

## Video Processing

| Repo | Description |
|---------|-------------|
| [Subvert](https://github.com/aschmelyun/subvert) | Generate subtitles, summaries, and chapters from videos in seconds. |

---

## API Clients

| Repo | Description |
|---------|-------------|
| [Google Cloud AI](https://github.com/googleapis/google-cloud-php) | Google Cloud AI services in PHP. |
| [DeepL PHP](https://github.com/DeepLcom/deepl-php) | Official PHP library for the DeepL language translation API. |
| [AWS Rekognition](https://aws.amazon.com/rekognition/) | Amazon Rekognition API for image and video analysis. |

---

## Learning Resources

| Repo | Description |
|---------|-------------|
| [onnxruntime-php](https://github.com/ankane/onnxruntime-php) | ONNX Runtime - high performance scoring engine for ML models - for PHP. |
| [Elasticsearch ChatGPT PHP](https://github.com/elastic/elasticsearch-chatgpt-php) | Use ChatGPT to search in Elasticsearch using natural language. |
| [YouTube AI Agent](https://github.com/neuron-core/youtube-ai-agent) | AI agents for YouTube video summarization (Neuron framework example). |
| [PHP LLMs Book](https://github.com/alnutile/php-llms) | Practical guide for PHP developers on integrating LLMs into projects. |
| [Deep Research Agent](https://github.com/neuron-core/deep-research-agent) | Deep research agent built with Neuron PHP AI framework. |
| [PHP LLM Examples](https://github.com/ezimuel/php-llm-examples) | Examples demonstrating GenAI and LLM usage in PHP. |
| [SearchAugmentedLLM](https://github.com/EliasPereirah/SearchAugmentedLLM) | Empowers LLMs with information from the web. |
| [neuranotes-api](https://github.com/waponix/neuranotes-api) | Note-taking app showcasing LLM, RAG integration, and scalable architecture. |

### Tutorials & Documentation

- [Fun With OpenAI and Laravel](https://laracasts.com/series/fun-with-openai-and-laravel) - Laracasts series on OpenAI with PHP and Laravel.
- [PHP-ML Tutorials](https://php-ml.readthedocs.io/en/latest/tutorials/) - Learn how to use PHP-ML for machine learning.
- [Rubix ML Docs](https://docs.rubixml.com/) - Comprehensive documentation for Rubix ML.

---

## Data Manipulation

| Repo | Description |
|---------|-------------|
| [brick/math](https://github.com/brick/math) | Arbitrary precision mathematics in PHP. |
| [php-ai/php-ds](https://github.com/php-ds) | PHP data structures extension for performance. |

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Add your library/tool to the appropriate section
3. Include the library name, GitHub link, and a brief description
4. Submit a pull request

Please ensure your submission is relevant to PHP and AI/ML/NLP.

---

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
