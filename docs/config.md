# Agent Configuration Notes

This document explains the parameters in the agent configuration JSON files (e.g., `agent_default.json`).
You can create your own agent configuration files then specify them with the CLI optional argument

## Core Configuration Parameters

### `name`
- **Description:** Agent's name.
- **Example:** `"Irrigation Educator Agent"`

### `instructions`
- **Description:** The **system prompt**. Defines the agent's persona and core directives.
- **Best Practice:** Be clear, concise, and specific.

### `model`
- **Description:** The large language model (LLM) used by the agent.
- **Pricing:** See [Model Pricing](https://platform.openai.com/docs/pricing?latest-pricing=standard) for cost details.
- **Example:** `gpt-4o-mini` (cost-effective, fast).
- **Other Models:** `gpt-4o` (more capable), `gpt-3.5-turbo` (balanced).

### `temperature`
- **Description:** Controls response randomness (creativity).
- **Range:** `0.0` (deterministic) to `2.0` (creative).
- **Default (when `null`):** `0.7`.
- **Recommendation:** Lower for factual accuracy, higher for creative generation.

### `max_tokens`
- **Description:** Maximum tokens the agent can generate per response.
- **Default (when `null`):** Unlimited.
- **Recommendation:** Set a limit to control response length and API costs.

## Tool Configuration

Defines external tools the agent can use.

### `file_search`
- **Description:** Configures searching through files or vector stores.
    -   `enabled`: `true`/`false` to enable/disable.
    -   `vector_store_ids`: List of custom vector store IDs.
    -   `max_num_results`: Max search results (text chunks) to retrieve.
    -   `include_search_results`: `true`/`false` to include raw search results.

### `web_search`
- **Description:** Configures web search.
    -   `enabled`: `true`/`false` to enable/disable.

## Best Practices

-   **Cost Management:** `model` and `max_tokens` impact API costs.
-   **Clarity:** Clear `instructions` lead to better agent performance.
