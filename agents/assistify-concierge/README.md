# Assistify - Concierge

Welcome to the **Assistify Concierge**, your AI-powered guide for seamless interaction with our platform. This agent is designed to provide friendly and knowledgeable assistance, helping users navigate and utilize Assistify effectively.

## Table of Contents

- [Assistify - Concierge](#assistify---concierge)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)

## Introduction

The Assistify Concierge excels in user guidance, customer engagement, and feature navigation. It provides detailed insights, explores features with ease, and offers expert help for your inquiries. Access the Assistify Concierge for personalized support and detailed information about the platform.

## Features

- **User Guidance**: Assists users in navigating the Assistify platform.
- **Feature Exploration**: Provides information about various features and how to use them.
- **Expert Assistance**: Answers questions and resolves user queries effectively.
- **Personalized Support**: Tailors responses based on user interactions.

## Setup

### Prerequisites

- **Python** (v3.10 or higher)
- **OpenAI API Key**
- **Trello API Key and Token** (for data integration)
- **Hatch** package manager (`pip install hatch`)

### Installation


2. **Copy the environment variables template**:

   ```bash
   cp env.default .env
   ```

3. **Install dependencies and activate the virtual environment**:

   ```bash
   hatch env create
   hatch shell
   ```

### Environment Variables

Configure the following variables in your `.env` file:

#### Required

- `OPENAI_API_KEY`: Your OpenAI API key.
- `TRELLO_API_KEY`: Your Trello API key.
- `TRELLO_API_TOKEN`: Your Trello API token.

#### Project

- `ASSISTANT_NAME`: Assistify - Concierge
- `ASSISTANT_DESCRIPTION`: Your friendly assistant to help navigate Assistify
- `DATA_FILE_PREFIX`: Assistify - Concierge

#### Trello

- `TRELLO_BOARD_NAME`: The name of your Trello board (e.g., Assistify)


### Running the Assistant

1. **Extract Trello Data** (if applicable):

   ```bash
   hatch run trello-extract
   ```

2. **Summarize Code (optional)**:

   If you wish to include code summaries:

   ```bash
   hatch run summary path/to/codebase
   ```

3. **Build the Assistant**:

   ```bash
   hatch run build
   ```

4. **Start a Chat Session**:

   ```bash
   hatch run chat
   ```

   This script will:

   - Load or create a new assistant.
   - Start a chat thread with the assistant.
   - Read input from the command line.

## Testing

### End-to-End Test

Run an end-to-end test to verify the assistant's functionality:

```bash
hatch run e2e
```

This script will:

- Create a new assistant.
- Send a message to the assistant.
- Remove the assistant.

### Unit Tests

Execute unit tests:

```bash
hatch run test
```

### Coverage Gutters

To visualize code coverage in your editor:

```bash
Command + Shift + P => Coverage Gutters: Watch
```


## Contact

Assistify is developed by Justin Beall of **Dev3loper.ai**.

- **Website**: [dev3loper.ai](https://www.dev3loper.ai)

---

Happy assisting with Assistify Concierge!
