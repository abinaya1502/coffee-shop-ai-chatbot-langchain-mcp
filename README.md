# Coffee Shop AI Chatbot – LangChain & MCP

An AI-powered coffee shop chatbot built using **LangChain, LangGraph, Model Context Protocol (MCP), Amazon Bedrock, and PostgreSQL**.

The project demonstrates how LLM-based conversational applications can interact with external tools and backend services through an MCP client-server architecture.

## Overview

This project implements an AI chatbot designed for a coffee shop use case. It combines LLM-powered conversational workflows with tool integration to support context-aware interactions.

The application is organized into two major components:

- **MCP Client:** Handles chatbot-side application logic and communication with the MCP server.
- **MCP Server:** Exposes backend capabilities through MCP tools, resources, and prompts.

## Key Technologies

| Technology | Purpose |
|---|---|
| Python | Application development |
| LangChain | LLM application development |
| LangGraph | Agent workflows and orchestration |
| MCP | Client-server communication and tool integration |
| Amazon Bedrock | Foundation model integration |
| PostgreSQL | Database management |
| FastAPI | API development |
| UV | Python dependency management |

## Architecture

The project follows an MCP client-server architecture.

1. The user interacts with the chatbot.
2. The client processes the request through the chatbot workflow.
3. The MCP client communicates with the MCP server.
4. The MCP server exposes the required tools and resources.
5. Backend services and database operations support the requested functionality.
6. The chatbot returns a response to the user.

## Project Structure

```text
coffee-shop-ai-chatbot-langchain-mcp/
│
├── design/
│   ├── mcp_client_class.puml
│   ├── mcp_client_sequence.wsd
│   ├── mcp_server_class.puml
│   └── mcp_server_sequence.wsd
│
├── dev/
│   ├── mcp client/
│   │   ├── src/
│   │   │   ├── agents/
│   │   │   ├── models/
│   │   │   ├── routes/
│   │   │   ├── services/
│   │   │   └── utils/
│   │   ├── main.py
│   │   └── pyproject.toml
│   │
│   └── mcp server/
│       ├── src/
│       │   ├── migrations/
│       │   ├── prompts/
│       │   ├── repositories/
│       │   ├── resourses/
│       │   ├── routes/
│       │   └── tools/
│       ├── main.py
│       └── pyproject.toml
│
└── .gitignore
```

## Getting Started

### Prerequisites

- Python version compatible with the project's `.python-version` files
- UV package manager
- PostgreSQL
- AWS account and appropriate Amazon Bedrock access, if required by your configuration

### Installation

Clone the repository:

```bash
git clone https://github.com/abinaya1502/coffee-shop-ai-chatbot-langchain-mcp.git
```

Navigate to the project directory:

```bash
cd coffee-shop-ai-chatbot-langchain-mcp
```

### Install Dependencies

Install the client dependencies:

```bash
cd "dev/mcp client"
uv sync
```

Install the server dependencies in a separate terminal:

```bash
cd "dev/mcp server"
uv sync
```

### Configuration

Configure the required environment variables for the client and server based on the settings modules and project configuration.

Typical configuration areas may include:

- Database connection details
- AWS credentials and model configuration
- MCP server connection settings

Do not commit actual passwords, API keys, AWS credentials, or other secrets.

### Running the Application

Start the MCP server and MCP client separately using their respective application entry points and the commands defined in their project configuration.

Refer to the individual README files in each component for any additional execution instructions.

## Design Documentation

The `design/` directory contains architecture documentation:

- MCP Client Class Diagram
- MCP Client Sequence Diagram
- MCP Server Class Diagram
- MCP Server Sequence Diagram

These diagrams illustrate the structure and interactions between the client and server components.

## Learning Outcomes

This project demonstrates practical exposure to:

- Building LLM-powered chatbot applications
- Working with LangChain and LangGraph
- Implementing MCP client-server architecture
- Integrating tools, prompts, and resources
- Connecting AI applications with backend services
- Working with Python, PostgreSQL, and AWS services

## Security

- Credentials and sensitive configuration values should be stored locally.
- Environment files containing secrets should not be committed.
- AWS access should use appropriately configured credentials and permissions.

## Author

**Abinaya Ganesan**

