# Awesome PHP AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of awesome PHP libraries and tools for integrating AI, Machine Learning, and Natural Language Processing into your PHP applications. Contributions are welcome!

## Table of Contents

- [Libraries](#libraries)
  - [Natural Language Processing](#natural-language-processing)
  - [Machine Learning](#machine-learning)
  - [Deep Learning](#deep-learning)
  - [Computer Vision](#computer-vision)
  - [Data Manipulation](#data-manipulation)
  - [Command Line Tools](#command-line-tools)
  - [Video Processing](#video-processing)
- [API Clients](#api-clients)
- [Learning Resources](#learning-resources)
- [Contributing](#contributing)

## Libraries

### Natural Language Processing

- **[LLPhant](https://github.com/theodo-group/llphant)** - A comprehensive PHP Generative AI Framework using OpenAI GPT 4. Inspired by Langchain.
- **[EleLLM](https://github.com/wpai-inc/EleLLM)** - A PHP framework that makes working with LLMs more pleasurable and accessible.
- **[php-llms](https://github.com/alnutile/php-llms)** - A practical guide and toolkit for PHP developers integrating LLMs into existing projects.
- **[php-ml](https://github.com/jorgecasas/php-ml)** - A PHP machine learning library.
- **[php-rag](https://github.com/rzarno/php-rag)** - Application using LLM (Llama3/GPT-4) for text generation with database-backed retrieval.
- **[cocur/slugify](https://github.com/cocur/slugify)** - Converts a string into a slug (NLP utility).
- **[Prism](https://github.com/echolabsdev/prism)** - A unified interface for working with LLMs in Laravel applications.
- **[Instructor PHP](https://github.com/cognesy/instructor-php)** - Extract structured data from LLM outputs with type safety and validation.
- **[Resonance](https://github.com/distantmagic/resonance)** - High-performance PHP framework optimized for IO-intensive LLM applications.
- **[Ollama PHP](https://github.com/ArdaGnsrn/ollama-php)** - PHP client for Ollama, enabling local LLM deployment and interaction.
- **[LLM Chain Bundle](https://github.com/php-llm/llm-chain-bundle)** - Symfony bundle for seamless integration of the LLM Chain library.
- **[LLM Chain](https://github.com/php-llm/llm-chain)** - Comprehensive PHP library for building LLM-powered applications.
- **[EasyAI-PHP](https://github.com/HosonoDE/EasyAI-PHP)** - EasyAI-PHP is an open-source initiative designed to significantly simplify the entry into artificial intelligence for PHP-developers (so basically Lang-Chain for PHP). Based on PHP 8.1+, this project integrates advanced AI models and utilities, allowing developers to incorporate complex AI functionalities with minimal coding.
- **[mcp-php](https://github.com/garyblankenship/mcp-php)** - Setting Up a Model Context Protocol (MCP) Server in Laravel
- **[transformers-php](https://github.com/CodeWithKyrian/transformers-php)** - Transformers PHP is a toolkit for PHP developers to add machine learning magic to their projects easily.
- **[Elasticsearch ChatGPT PHP](https://github.com/elastic/elasticsearch-chatgpt-php)** - Use ChatGPT to search in Elasticsearch using natural language
- **[LLM Agents](https://github.com/llm-agents-php/agents)** - LLM Agents is a PHP library for building and managing Language Model (LLM) based agents. It provides a framework for creating autonomous agents that can perform complex tasks, make decisions, and interact with various tools and APIs.
- **[langchain-php](https://github.com/kambo-1st/langchain-php)** - Building applications with LLMs through composability in PHP
- **[Lugha](https://github.com/devscast/lugha)** - Lugha is a PHP Generative AI Framework to build chatbot, RAG systems and AI-powered applications
- **[laravel-llm-prompt](https://github.com/SabatinoMasala/laravel-llm-prompt)** - laravel-llm-prompt manager
- **[LLM-Port-Laravel](https://github.com/BorahLabs/LLM-Port-Laravel)** - Wrapper around the most popular LLMs that allows drop-in replacement of large language models in Laravel.
- **[ai-team](https://github.com/sarfraznawaz2005/ai-team)** - A package allowing to create team of AI members that can work and collaborate together to achieve a common goal.
- **[laravel-prompt-alchemist](https://github.com/moe-mizrak/laravel-prompt-alchemist)** - Versatile LLM Tool Use (Function Calling) package for Laravel, compatible with all LLMs, enabling LLM to execute actual code functions (unlike LLMs' built-in capabilities).
- **[mulagent](https://github.com/FunkyOz/mulagent)** - The orchestration of multiple agents involves the use of routines and handoffs. Simplifying, a routine is a series of steps to follow to achieve a goal, and a handoff is the transition from one agent to another, like a switchboard transferring a phone call.
- **[prompt-generator](https://github.com/llm-agents-php/prompt-generator)** - Prompt generator for LLM agents with interceptors
- **[instructrice](https://github.com/adrienbrault/instructrice)** - Typed LLM Outputs in PHP. Supports GPT, Claude, Gemini or any OpenAI compatible provider!
- **[llm](https://github.com/artisan-build/llm)** - Provides Laravel integrations for various LLM providers
- **[php-llm-json-adapter](https://github.com/takaaki-mizuno/php-llm-json-adapter)** - When using LLMs from the system, you often expect to get output results in JSON: OpenAPI's GPT API has a mechanism called Function Calling, which can return JSON, but Google's Gemini does not seem to have that functionality.
- **[LaravelLLMContext](https://github.com/jeremysalmon/LaravelLLMContext)** - Artisan Command to Generate LLM Context for a Laravel Project
- **[llm-magic](https://github.com/Capevace/llm-magic)** - LLM-agnostic AI toolkit for Laravel
- **[php-llm-documents](https://github.com/thojou/php-llm-documents)** - PHP LLM Documents is a powerful PHP library that brings LLM (Large Language Model) functionality into the PHP ecosystem.
- **[fireworksai-adapter](https://github.com/modelflow-ai/fireworksai-adapter)** - The adapter integrates open-source models hosted by fireworks.ai into Modelflow AI.
- **[Taskallama](https://github.com/coding-wisely/taskallama)** - Taskallama is a Laravel package that provides seamless integration with Ollama's LLM API. It simplifies generating AI-powered content, from professional task writing to conversational agents, with minimal effort. Whether you're building a task management system, an HR assistant for job posts, or blog content generation, Taskallama has you covered.
- **[fabric-pattern](https://github.com/php-llm/fabric-pattern)** - Slim PHP wrapper for Daniel Miessler's fabric pattern
- **[aipi-php](https://github.com/skito/aipi-php)** - Universal API client for common AI models
- **[Sidekick](https://github.com/PapaRascal2020/sidekick)** - Say hello to Sidekick! A Laravel package that provides a common syntax for using Claude, Mistral, Cohere and OpenAi APIs.
- **[Laravel OpenRouter](https://github.com/moe-mizrak/laravel-openrouter)** - Laravel integration for OpenRouter's unified LLM API interface.

### Machine Learning

- **[Rubix ML](https://github.com/RubixML/ML)** - Machine learning library for building algorithms and models.
- **[TensorFlow PHP](https://github.com/tensorflow/tfjs)** - PHP bindings for TensorFlow.

### Computer Vision

- **[opencv/opencv-php](https://github.com/php-opencv/php-opencv)** - OpenCV bindings for PHP for image processing and computer vision.

### Data Manipulation

- **[brick/math](https://github.com/brick/math)** - Handles arbitrary precision mathematics in PHP.
- **[php-ai/php-ds](https://github.com/php-ds)** - PHP data structures extension for performance.
- **[redis-vector-php](https://github.com/redis-applied-ai/redis-vector-php)** - Redis Vector Library (RedisVL) enables Redis as a real-time database for LLM applications, based on Predis PHP client

### Command Line Tools

- **[ai-commit](https://github.com/guanguans/ai-commit)** - Automagically generate conventional git commit messages with AI. - 使用 AI 自动生成约定式 git 提交信息。
- **[Laragenie](https://github.com/joshembling/laragenie)** - An AI bot made for the command line that can read and understand any codebase from your Laravel app.

### Video Processing

- **[Subvert](https://github.com/aschmelyun/subvert)** - Generate subtitles, summaries, and chapters from videos in seconds

### Vector Storage

- **[vector-storage](https://github.com/llm-agents-php/vector-storage)** - LLM Agents Vector Storage

## API Clients

- **[OpenAI PHP](https://github.com/openai-php/client)** - OpenAI PHP is a supercharged community-maintained PHP API client that allows you to interact with OpenAI API.
- **[OpenAI PHP SDK](https://github.com/orhanerday/open-ai)** - OpenAI PHP SDK : Most downloaded, forked, contributed, huge community supported, and used PHP (Laravel , Symfony, Yii, Cake PHP or any PHP framework) SDK for OpenAI GPT-3 and DALL-E. It also supports chatGPT-like streaming. (ChatGPT AI is supported)
- **[Google Cloud AI](https://github.com/googleapis/google-cloud-php)** - Google Cloud AI services in PHP.
- **[AWS Rekognition](https://aws.amazon.com/rekognition/)** - Amazon Rekognition API for image and video analysis.
- **[DeepL PHP](https://github.com/DeepLcom/deepl-php)** - Official PHP library for the DeepL language translation API.
- **[Deepseek PHP Client](https://github.com/deepseek-php/deepseek-php-client)** - ⚡️ supercharged community-maintained PHP API client that allows you to interact with deepseek API.

## Learning Resources
- **[Fun With OpenAI and Laravel](https://laracasts.com/series/fun-with-openai-and-laravel)** - Fun With OpenAI and Laravel
In this series, you'll get your feet wet with a variety of fun examples that demonstrate how to interact with OpenAI using PHP and Laravel. We'll begin by assuming that you know nothing, and then slowly work our way up one episode at a time!
- **[PHP LLM Examples](https://github.com/ezimuel/php-llm-examples)** - Examples demonstrating GenAI and LLM usage in PHP.
- **[PHP-ML Tutorials](https://php-ml.readthedocs.io/en/latest/tutorials/)** - Learn how to use PHP-ML for machine learning.
- **[Rubix ML Docs](https://docs.rubixml.com/)** - Comprehensive documentation for Rubix ML.

## Contributing

Have a PHP AI library, tool, or resource to share? Feel free to submit a PR!
