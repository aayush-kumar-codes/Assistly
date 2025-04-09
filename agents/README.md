# Assistify Agents

Welcome to the **Assistify Agents** repository! This directory contains specialized AI assistants designed to provide

## Agent Structure

Each agent follows a common structure:

- **`data/`**: Stores data files used by the agent (e.g., code summaries, Trello data).
- **`prompts/`**: Includes the agent's prompt files.
- **`integration/`**: Contains integration tests for the agent.
- **`run_chat.py`**: Script to interact with the agent via the command line.
- **`run_end_to_end.py`**: Script for end-to-end testing.

## Available Agents

### Assistify Concierge

- **Purpose**: Acts as a friendly and knowledgeable assistant to help users navigate and utilize Assistify effectively.
- **Data Sources**: Trello board data, code summaries.
- **Intention**: Provide guidance, answer questions, and enhance user experience within the Assistify platform.
- **[More Details](assistify-concierge/README.md)**

### Assistify Product Owner

- **Purpose**: Provides insights into product management aspects, offering technical details and updates about the Assistify project.
- **Data Sources**: Trello boards, code summaries from Assistify API and UI.
- **Intention**: Assist in product planning, backlog management, and offer strategic insights.
- **[More Details](assistify-product-owner/README.md)**

### Warm Intro AI

- **Purpose**: Automates the creation of personalized outreach messages for busy professionals.
- **Data Sources**: Personal and professional data analysis (e.g., LinkedIn profiles, conference bios).
- **Intention**: Help users craft messages that resonate, fostering valuable connections and potential collaborations.
- **[More Details](warm-intro-ai/README.md)**

## Building a New Agent

To build a new agent, you can follow these steps:

1. **Copy an Existing Agent**: Choose an existing agent (e.g., `assistify-concierge`) and copy its directory.

   ```bash
   cp -r assistify-concierge new-agent-name
   ```

2. **Update Properties**: Modify the configuration files, prompts, and data to suit your new agent's purpose.

   - Update `env.default` with the new agent's name, description, and settings.
   - Edit prompts in the `prompts/` directory.
   - Replace or add data files in the `data/` directory.

3. **Install Dependencies**: Navigate to your new agent's directory and set up the environment.

   ```bash
   cd new-agent-name
   hatch env create
   ```

4. **Build the Agent**: Use the provided scripts to build and test your agent.

   ```bash
   hatch run build
   ```

5. **Add to Migrations**: To include your new agent in the application, add it to a migration script in the `assistify-api` repository. This ensures the agent appears in the app upon startup.

6. **Test Your Agent**: Run unit and integration tests to verify your agent behaves as expecte

By using these libraries, the agents can be more powerful and context-aware.


## Contact

Assistify is developed by Justin Beall of **Dev3loper.ai**.

- **Website**: [dev3loper.ai](https://www.dev3loper.ai)

---

Ready to enhance your productivity with AI? Explore our specialized agents and see how they can assist you today!

## Additional Note

All these agents are available when logging into the Assistify interface. Explore each agent to experience their unique capabilities tailored to enhance your professional workflows.

---

Thank you for exploring the Assistify Agents!
